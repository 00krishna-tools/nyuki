# -*- coding: utf-8 -*-

import sys
import os
import click
import numpy as np
from contextlib import contextmanager
from .geotiff_resampler import resampler
from .geotiff_reprojector import reprojector
from .vector_reprojector import vreprojector


@click.group()
def nyuki():
    """Application: Nyuki toolkit

    Nyuki makes it easy to process raster and vector images using python.
    Use one of the commands listed below to reproject, upsample, downsample,
    or compress your Geotiff or Geojson files. Nyuki was developed in
    collaboration with DataKind and WeRobotics. 
    """
    pass


@nyuki.group()
def vector():
    """Nyuki vector tools


    These tools process geojson vector files.
    """
    pass


@nyuki.group()
def raster():
    """Nyuki raster toolkit


    These tools process Geotiff raster files.
    """
    pass

@raster.command()
@click.option('--sourcetiff', type=click.Path(exists=True), required=True,
              prompt="Enter the path and filename of the source file",
              help="Path to the original GEOTIFF raster image")
@click.option('--target_resolution', type=np.float, required=True,
              prompt="Enter the target resolution in appropriate units for the projection",
              help="The resolution desired for the resampled image, in the units of that image's projection, eg., meters, degrees, etc.")
def resample(sourcetiff, target_resolution):
    """Upsample or Downsample a Geotiff to a different resolution.

    This tool will resample a raster image to a different resolution.
    The user enters the source GEOTIFF filename, and a target resolution.
    The tool will then resample the image to a new resolution and output the
    new GEOTIFF file to the source directory.

    This tool will preserve the original projection of the image.

    Commandline app:\n
    >>> nyuki resample --sourcetiff file1.tif --target_resolution 0.15

    Invoke interactive mode:\n
    >>> nyuki resample
    """

    resampler(sourcetiff, target_resolution)
    return 0


@raster.command()
@click.option('--sourcetiff', required=True, type=click.Path(exists=True),
              prompt="Source file path",
              help="Enter the path to the original GEOTIFF raster image")
@click.option('--target_epsg', default='EPSG:4326', show_default=True, type=str,
              prompt="Target coordinate EPSG",
              help="Enter the coordinate projection to apply to the raster image.")
def reproject(sourcetiff, target_epsg='EPSG:4326'):
    """Reproject a Geotiff file to a new coordinate projection.

        This tool will reproject a raster image to a different EPSG coordinate projection.
        The user enters the source GEOTIFF filename, and a valid target EPSG projection.
        The file is output to the same directory as the source file. The new file is
        also compressed with JPEG compression to keep the file size manageable.

        Commandline app:\n
        >>> nyuki reproject --sourcetiff file1.tif --target_epsg 'EPSG:4326'

        Invoke interactive mode:\n
        >>> nyuki reproject
        """

    reprojector(sourcetiff, target_epsg)
    return 0


@vector.command()
@click.option('--sourcefile', required=True, type=click.Path(exists=True),
              prompt="Source file path",
              help="Enter the path to the original GEOJSON or vector file")
@click.option('--target_epsg', default='EPSG:4326', show_default=True, type=str,
              prompt="Target coordinate EPSG",
              help="Enter the coordinate projection to apply to the raster image.")
def reproject(sourcefile, target_epsg='EPSG:4326'):
    """Reproject a vector file to a new coordinate system.

        This tool will reproject a vector file to a different EPSG coordinate projection.
        The user enters the source vector filename, and a valid target EPSG projection.
        The file is output to the same directory as the source file.

        Commandline app:\n
        >>> nyuki vector reproject --sourcefile file1.geojson --target_epsg 'EPSG:4326'

        Invoke interactive mode:\n
        >>> nyuki vector reproject
        """

    vector_reprojector(sourcefile, target_epsg)
    return 0















if __name__ == '__main__':
    nyuki()








