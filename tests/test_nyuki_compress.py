#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `nyuki` package."""

import pytest
import nyuki
from nyuki.geotiff_compressor import compressor
import os


@pytest.mark.usefixtures('small_image')
@pytest.mark.usefixtures('big_image')


@pytest.mark.parametrize("compression", ['LZW',
                                         'JPEG',
                                         'JPEG2000',
                                         'DEFLATE',
                                         'NONE'])
def test_small_compression(small_image, compression):
    newfile = compressor(small_image, compression, yes=True)
    res = nyuki.utilities.dhash_distance(small_image, newfile, hash_size=8)
    os.remove(newfile)
    assert res < 0.20


@pytest.mark.parametrize("compression", ['JPEG'])
def test_bigtiff_compression(big_image, compression):
    newfile = compressor(big_image, compression, yes=True)
    os.remove(newfile)
    assert True
