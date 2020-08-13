
# -*- coding: utf-8 -*-

"""Utilities file for Nyuki package.

These are some miscellaneous helper functions to facilitate some
of Nyuki's operations. The functions include

1. get_file_type(): Function to determine if a file is a vector or raster file.

"""
import sys
import os
import numpy as np
import rasterio
from rasterio import Affine, MemoryFile
from rasterio.enums import Resampling
from PIL import Image
import dhash
from osgeo import gdal


Image.MAX_IMAGE_PIXELS = None

def get_file_type(filename):
    """
    This function will determine whether a file is a raster or vector
    geospatial file. For example, a Geotiff file is a raster file, while
    a shapefile or geojson file is a vector file.  
    """

    ds = gdal.OpenEx(filename)
    try:
        metadata = ds.GetDriver().GetMetadata()
    except:
        print(filename, 'File invalid, please specify either a vector or raster file.')
    else:
        raster_capable = 'DCAP_RASTER' in metadata
        vector_capable = 'DCAP_VECTOR' in metadata


    if raster_capable:
        return('raster')
    else:
        return('vector')


def dhash_distance(left, right, hash_size=8):
        left = Image.open(left)
        right = Image.open(right)
        hash1 = dhash.dhash_int(left, size=hash_size)
        hash2 = dhash.dhash_int(right, size=hash_size)
        num_bits_different = dhash.get_num_bits_different(hash1, hash2)
        return 100 * num_bits_different / (hash_size * hash_size * 2)
