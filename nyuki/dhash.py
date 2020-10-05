
"""
NOTE THAT THIS ENTIRE MODULE IS TAKEN FROM Jetsetter https://github.com/Jetsetter/dhash .
I am using the conda package manager to install this package, and that does not allow
me to install packages from outside of conda defaults or conda-forge. Since the
dhash package is not in either of these channels, I just copied the code into this module.
I wanted to make sure that Jetsetter received the credit for developing this module,
and that I am simply copying the module from him/her while giving him/her appropriate attribution.


Calculate difference hash (perceptual hash) for a given image, useful for detecting duplicates.

For example usage, see README.rst.

This code is licensed under a permissive MIT license -- see LICENSE.txt.

The dhash project lives on GitHub here:
https://github.com/Jetsetter/dhash
"""

from __future__ import division
import numpy as np
import sys

# Allow library to be imported even if neither wand or PIL are installed
try:
    import wand.image
except ImportError:
    wand = None

try:
    import PIL.Image
except ImportError:
    PIL = None


__version__ = '1.3'

IS_PY3 = sys.version_info.major >= 3


def get_grays(image, width, height):
    """Convert image to grayscale, downsize to width*height, and return list
    of grayscale integer pixel values (for example, 0 to 255).

    >>> get_grays([0,0,1,1,1, 0,1,1,3,4, 0,1,6,6,7, 7,7,7,7,9, 8,7,7,8,9], 5, 5)
    [0, 0, 1, 1, 1, 0, 1, 1, 3, 4, 0, 1, 6, 6, 7, 7, 7, 7, 7, 9, 8, 7, 7, 8, 9]

    >>> import os
    >>> test_filename = os.path.join(os.path.dirname(__file__), 'dhash-test.jpg')
    >>> with wand.image.Image(filename=test_filename) as image:
    ...     get_grays(image, 9, 9)[:18]
    [95, 157, 211, 123, 94, 79, 75, 75, 78, 96, 116, 122, 113, 93, 75, 82, 81, 79]
    """
    if isinstance(image, (tuple, list)):
        if len(image) != width * height:
            raise ValueError('image sequence length ({}) not equal to width*height ({})'.format(
                    len(image), width * height))
        return image

    if wand is None and PIL is None:
        raise ImportError('must have wand or Pillow/PIL installed to use dhash on images')

    if wand is not None and isinstance(image, wand.image.Image):
        with image.clone() as small_image:
            small_image.type = 'grayscale'
            small_image.resize(width, height)
            blob = small_image.make_blob(format='RGB')
            if IS_PY3:
                return list(blob[::3])
            else:
                return [ord(c) for c in blob[::3]]

    elif PIL is not None and isinstance(image, PIL.Image.Image):
        gray_image = image.convert('L')
        small_image = gray_image.resize((width, height), PIL.Image.ANTIALIAS)
        return list(small_image.getdata())

    else:
        raise ValueError('image must be a wand.image.Image or PIL.Image instance')


def dhash_row_col(image, size=8):
    """Calculate row and column difference hash for given image and return
    hashes as (row_hash, col_hash) where each value is a size*size bit
    integer.

    >>> row, col = dhash_row_col([0,0,1,1,1, 0,1,1,3,4, 0,1,6,6,7, 7,7,7,7,9, 8,7,7,8,9], size=4)
    >>> format(row, '016b')
    '0100101111010001'
    >>> format(col, '016b')
    '0101001111111001'

    >>> import os
    >>> test_filename = os.path.join(os.path.dirname(__file__), 'dhash-test.jpg')
    >>> with wand.image.Image(filename=test_filename) as image:
    ...     row, col = dhash_row_col(image)
    >>> (row, col) == (13962536140006260880, 9510476289765573406)
    True
    """
    width = size + 1
    grays = get_grays(image, width, width)

    row_hash = 0
    col_hash = 0
    for y in range(size):
        for x in range(size):
            offset = y * width + x
            row_bit = grays[offset] < grays[offset + 1]
            row_hash = row_hash << 1 | row_bit

            col_bit = grays[offset] < grays[offset + width]
            col_hash = col_hash << 1 | col_bit

    return (row_hash, col_hash)


def dhash_int(image, size=8):
    """Calculate row and column difference hash for given image and return
    hashes combined as a single 2*size*size bit integer (row_hash in most
    significant bits, col_hash in least).

    >>> dhash_int([0,0,1,1,1, 0,1,1,3,4, 0,1,6,6,7, 7,7,7,7,9, 8,7,7,8,9], size=4)
    1272009721
    """
    row_hash, col_hash = dhash_row_col(image, size=size)
    return row_hash << (size * size) | col_hash


def get_num_bits_different(hash1, hash2):
    """Calculate number of bits different between two hashes.

    >>> get_num_bits_different(0x4bd1, 0x4bd1)
    0
    >>> get_num_bits_different(0x4bd1, 0x5bd2)
    3
    >>> get_num_bits_different(0x0000, 0xffff)
    16
    """
    return bin(hash1 ^ hash2).count('1')


def format_bytes(row_hash, col_hash, size=8):
    """Format dhash integers as binary string of size*size//8 bytes (row_hash
    and col_hash concatenated, big endian).

    >>> hash_bytes = format_bytes(19409, 14959, size=4)
    >>> type(hash_bytes) is bytes
    True
    >>> [hex(b) for b in hash_bytes] if IS_PY3 else [hex(ord(b)) for b in hash_bytes]
    ['0x4b', '0xd1', '0x3a', '0x6f']

    >>> hash_bytes = format_bytes(1, 2, size=4)
    >>> type(hash_bytes) is bytes
    True
    >>> [hex(b) for b in hash_bytes] if IS_PY3 else [hex(ord(b)) for b in hash_bytes]
    ['0x0', '0x1', '0x0', '0x2']
    """
    bits_per_hash = size * size
    full_hash = row_hash << bits_per_hash | col_hash
    if IS_PY3:
        return full_hash.to_bytes(bits_per_hash // 4, 'big')
    else:
        return '{0:0{1}x}'.format(full_hash, bits_per_hash // 2).decode('hex')


def format_hex(row_hash, col_hash, size=8):
    """Format dhash integers as hex string of size*size//2 total hex digits
    (row_hash and col_hash concatenated).

    >>> format_hex(19409, 14959, size=4)
    '4bd13a6f'
    >>> format_hex(1, 2, size=4)
    '00010002'
    """
    hex_length = size * size // 4
    return '{0:0{2}x}{1:0{2}x}'.format(row_hash, col_hash, hex_length)


def format_matrix(hash_int, bits='01', size=8):
    """Format dhash integer as matrix of bits.

    >>> row, col = dhash_row_col([0,0,1,1,1, 0,1,1,3,4, 0,1,6,6,7, 7,7,7,7,9, 8,7,7,8,9], size=4)
    >>> print(format_matrix(row, bits='.*', size=4))
    .*..
    *.**
    **.*
    ...*
    >>> print(format_matrix(col, size=4))
    0101
    0011
    1111
    1001
    """
    output = '{:0{}b}'.format(hash_int, size * size)
    if IS_PY3:
        output = output.translate({ord('0'): bits[0], ord('1'): bits[1]})
    else:
        output = unicode(output).translate({ord('0'): unicode(bits[0]), ord('1'): unicode(bits[1])})
        output = type(bits[0])(output)
    width = size * len(bits[0])
    lines = [output[i:i + width] for i in range(0, size * width, width)]
    return '\n'.join(lines)


def format_grays(grays, size=8):
    r"""Format grays list as matrix of gray values.

    >>> out = format_grays([0,0,1,1,1, 0,1,1,3,4, 0,1,6,6,7, 7,7,7,7,9, 8,7,7,8,9], size=4)
    >>> print('\n'.join(line.strip() for line in out.splitlines()))
    0   0   1   1   1
    0   1   1   3   4
    0   1   6   6   7
    7   7   7   7   9
    8   7   7   8   9
    """
    width = size + 1
    lines = []
    for y in range(width):
        line = []
        for x in range(width):
            gray = grays[y * width + x]
            line.append(format(gray, '4'))
        lines.append(''.join(line))
    return '\n'.join(lines)


def force_pil():
    """If both wand and Pillow/PIL are installed, force the use of Pillow/PIL."""
    global wand
    if PIL is None:
        raise ValueError('Pillow/PIL library must be installed to use force_pil()')
    wand = None
