
# -*- coding: utf-8 -*-

"""Console script for Raster information tool"""
import sys
import os
import click
import numpy as np
import rasterio
from rasterio import Affine, MemoryFile
from rasterio.enums import Resampling


@click.command()
@click.option('--sourcetiff', type=click.Path(exists=True), required=True,
              prompt="Enter the path and filename of the source file",
              help="Path to the original GEOTIFF raster image")
def info(sourcetiff):
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

    information(sourcetiff)
    return 0


def information(sourcefile):

    dat = rasterio.open(sourcefile)

    click.echo(f"\n \t File info for: {sourcefile}: \n")
    click.echo(f"\t Coordinate projection: {dat.crs}")
    click.echo(f"\t File type: {dat.profile['driver']}")
    click.echo(f"\t File size: {dat.shape}")
    click.echo(f"\t Pixel Units: {dat.crs.linear_units}")
    click.echo(f"\t Pixel size: {(round(dat.res[0], 3), round(dat.res[1], 3))}")
    click.echo(f"\t Number of Bands: {dat.profile['count']}")
    click.echo(f"\t Data type per band: {dat.dtypes}")
    click.echo(f"\t Compression: {dat.profile['compress']}")
    click.echo(f"\t Nodata character: {dat.profile['nodata']}")
