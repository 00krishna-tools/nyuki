
#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `nyuki` package."""

import pytest
import nyuki
from nyuki.geotiff_reprojector import reprojector
from nyuki.vector_reprojector import vreprojector
import os
import rasterio

@pytest.mark.usefixtures('small_image')


@pytest.mark.parametrize("projection", ['EPSG:4326', 'EPSG:3857'])
@pytest.mark.skip(reason="no way of currently testing this")
def test_raster_reprojector(small_image, projection):
    dat = rasterio.open(small_image)
    crs = dat.crs
#    import pdb; pdb.set_trace()
    newfile = reprojector(small_image, projection, yes=True)
    newfile2 = reprojector(newfile, str(crs), yes=True)
    res = nyuki.utilities.dhash_distance(small_image, newfile2, hash_size=16)
    os.remove(newfile)
    assert  res < 0.20
