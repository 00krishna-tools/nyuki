#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `nyuki` package."""

import pytest
import nyuki
from nyuki.geotiff_compressor import compressor
import dhash
import os

@pytest.mark.usefixtures('small_image')


def test_compress():
    print('hello')
    assert 1 == 1

@pytest.mark.parametrize("compression", ['LZW', 'LZMA','JPEG', 'JPEG2000','DEFLATE', 'WEBP', 'ZSTD', 'NONE'])
def test_lzw_compression(small_image, compression):

    newfile = compressor(small_image, compression, yes=True)
    res = nyuki.utilities.dhash_distance(small_image, newfile)
    os.remove(newfile)
    assert  res < 0.20


def teardown_function():
    print('tearing down')
