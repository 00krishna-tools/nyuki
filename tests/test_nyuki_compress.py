#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `nyuki` package."""

import pytest
import nyuki
from nyuki.geotiff_compressor import compressor
import dhash


@pytest.mark.usefixtures('small_image')


def test_compress():
    print('hello')
    assert 1 == 1

def test_lzw_compression(small_image):
    compressor(small_image, 'LZW')
    assert nyuki.utilities.dhash_distance(small_image, 'sample_image_small_compress_LZW.tif') < 0.20

def test_lzma_compression():
    pass

def test_deflate_compression():
    pass

def test_jpeg_compression():
    pass

def test_jpeg2000_compression():
    pass

def test_webp_compression():
    pass

def test_zstd_compression():
    pass

def test_none_compression():
    pass

