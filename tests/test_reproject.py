
#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `nyuki` package."""

import pytest
import nyuki
from nyuki.geotiff_reprojector import reprojector
from nyuki.vector_reprojector import vreprojector
import os

@pytest.mark.usefixtures('small_image')


@pytest.mark.parametrize("projection", ['LZW'])
def test_raster_reprojector(small_image, projection):

    newfile = reprojector(small_image, projection, yes=True)
    res = nyuki.utilities.dhash_distance(small_image, newfile)
    os.remove(newfile)
    assert  res < 0.20
