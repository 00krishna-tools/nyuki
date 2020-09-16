# -*- coding: utf-8 -*-

import sys
import os
import click
import numpy as np
from contextlib import contextmanager
from .geotiff_resampler import resampler
from .geotiff_reprojector import reprojector
from .vector_reprojector import vreprojector
from .geotiff_compressor import compressor
from .geotiff_info import information
from .utilities import get_file_type


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


@nyuki.command()
@click.option('--sourcefile', type=click.Path(exists=True), required=True,
              prompt="Enter the path and filename of the source file",
              help="Path to the original GEOTIFF raster image")
def info(sourcefile):
    """Raster metadata and information tool.

    This tool provides metadata about a raster image, including the file's
    coordinate project, resolution, pixel size, number of bands, data types,
    etc. The tool provides the same information found in `gdalinfo` but in
    a friendlier form for reading.

    Commandline app:\n
    >>> geotiff_info --sourcetiff file1.tif

    Invoke interactive mode:\n
    >>> geotiff_info
    """

    information(sourcefile)
    return 0

@raster.command()
@click.option('--sourcetiff', type=click.Path(exists=True), required=True,
              prompt="Enter the path and filename of the source file",
              help="Path to the original GEOTIFF raster image")
@click.option('--target_resolution', type=np.float, required=True,
              prompt="Enter the target resolution in appropriate units for the projection",
              help="The resolution desired for the resampled image, in the units of that image's projection, eg., meters, degrees, etc.")
@click.option('--yes', '-y', is_flag=True, default=False, help="Execute command without prompting for user confirmation.")
def resample(sourcetiff, target_resolution, yes):
    """Upsample or Downsample a Geotiff to a different resolution.

    This tool will resample a raster image to a different resolution.
    The user enters the source GEOTIFF filename, and a target resolution.
    The tool will then resample the image to a new resolution and output the
    new GEOTIFF file to the source directory.

    This tool will preserve the original projection of the image.

    Commandline app:\n
    >>> nyuki resample --sourcetiff file1.tif --target_resolution 0.15 -y

    Invoke interactive mode:\n
    >>> nyuki resample
    """

    resampler(sourcetiff, target_resolution, yes)
    return 0


@raster.command()
@click.option('--sourcetiff', required=True, type=click.Path(exists=True),
              prompt="Source file path",
              help="Enter the path to the original GEOTIFF raster image")
@click.option('--target_epsg', default='EPSG:4326', show_default=True, type=str,
              prompt="Target coordinate EPSG",
              help="Enter the coordinate projection to apply to the raster image.")
@click.option('--yes', '-y', is_flag=True, default=False, help="Execute command without prompting for user confirmation.")
def reproject(sourcetiff, target_epsg='EPSG:4326', yes=False):
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

    reprojector(sourcetiff, target_epsg, yes)
    return 0


@raster.command()
@click.option('--sourcetiff', required=True, type=click.Path(exists=True),
              prompt="Source file path",
              help="Enter the path to the original GEOTIFF raster image")
@click.option('--target_compression', default='LZW', show_default=True,
              type=click.Choice(['LZW','JPEG','JPEG2000',
                                 'DEFLATE', 'NONE'], case_sensitive=True),
              prompt="Target compression method",
              help="Enter the compression standard to apply to the raster.")
@click.option('--yes', '-y', is_flag=True, default=False, help="Execute command without prompting for user confirmation.")
def compress(sourcetiff, target_compression, yes):
    """ Compress Geotiff raster files to shrink file size.

       This tool will compress a Geotiff raster image using the specified compression
       method. The supported methods are LZW, JPEG, DEFLATE, and JPEG2000 standards.
       JPEG and JPEG2000 compression usually produce the smallest files and are good
       for most users, even though the method is "lossy." Alternatively, LZW
       is "lossless" methods, but they produce larger file sizes.

       The link provides a good overview of preferred compression methods for different
       use cases.
       https://doc.arcgis.com/en/imagery/workflows/best-practices/imagery-formats-and-performance.htm

       Note that in some cases, compression can make the file size larger. Hence it could
       take a few attempts to find the right compression scheme.


        Commandline app:\n
        >>> nyuki raster compress --sourcetiff file1.tif --target_compression 'LZW' -y

        Invoke interactive mode:\n
        >>> nyuki raster compress
        """

    compressor(sourcetiff, target_compression, yes)
    return 0




@vector.command()
@click.option('--sourcefile', required=True, type=click.Path(exists=True),
              prompt="Source file path",
              help="Enter the path to the original GEOJSON or vector file")
@click.option('--target_epsg', default='EPSG:4326', show_default=True, type=str,
              prompt="Target coordinate EPSG",
              help="Enter the coordinate projection to apply to the raster image.")
@click.option('--yes', '-y', is_flag=True, default=False, help="Execute command without prompting for user confirmation.")
def reproject(sourcefile, target_epsg='EPSG:4326', yes=False):
    """Reproject a vector file to a new coordinate system.

        This tool will reproject a vector file to a different EPSG coordinate projection.
        The user enters the source vector filename, and a valid target EPSG projection.
        The file is output to the same directory as the source file.

        Commandline app:\n
        >>> nyuki vector reproject --sourcefile file1.geojson --target_epsg 'EPSG:4326'

        Invoke interactive mode:\n
        >>> nyuki vector reproject
        """
    vreprojector(sourcefile, target_epsg, yes)
    return 0















if __name__ == '__main__':
    nyuki()
