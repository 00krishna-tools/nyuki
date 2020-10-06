
# -*- coding: utf-8 -*-

"""Console script for nyuki geotiff files compressor."""
import sys
import os
import click
import rasterio
from rasterio.warp import calculate_default_transform, reproject, Resampling


def compressor(sourcefile, target_compression='LZW', yes=False):

    # load file to get info.
    dat = rasterio.open(sourcefile)
    profile = dat.profile.copy()

    # create new target filename
    targetfile = os.path.basename(sourcefile).split('.')[0] \
                + '_compress_' \
                + str(target_compression) \
                + '.tif'

    click.echo("Application Settings:\n")
    click.echo(f"source filename: {sourcefile}")
    click.echo(f"target filename: {targetfile}")
    click.echo(f"source datatype: {dat.dtypes}")
    click.echo(f"source current compression: {dat.profile.get('compress', 'Uncompressed')}")
    click.echo(f"target epsg: {target_compression}\n")


    # check if new compression is same as old compression

    if not yes:
        click.confirm('[INFO] File compression takes a while.\nDo you want to continue?',
                  abort=True)

        click.echo('\n[INFO] Good time to get a cup of coffee.\n[INFO] This task can take 15-30 minutes or longer depending on file size.\n')

    with rasterio.Env():

    # Write an array as a raster band to a new 8-bit file. For
    # the new file's profile, we start with the profile of the source

    # specify compression standard
        profile.update(
            compress=target_compression,
            BIGTIFF = "YES")

        with rasterio.open(targetfile, 'w', **profile) as dst:
            for ji, window in dat.block_windows(1):
                dst.write(dat.read(window=window), window=window)

    click.echo('[INFO] Task complete.')

    return targetfile
