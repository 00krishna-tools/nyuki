
#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `src` package."""

import pytest
import nyuki
from nyuki.geotiff_resampler import resampler
import dhash
import os

@pytest.mark.usefixtures('small_image')


@pytest.mark.parametrize("resolution", [0.12, 0.24])
def test_image_resampler(small_image, resolution):

    newfile = resampler(small_image, resolution, yes=True)
    res = nyuki.utilities.dhash_distance(small_image, newfile)
    os.remove(newfile)
    assert  res < 0.20

