# -*- coding: utf-8 -*-

"""Console script for geotiff_reprojector."""
import sys
import os
import click
import rasterio
from rasterio.warp import calculate_default_transform, reproject, Resampling

def reprojector(sourcefile, target_epsg='EPSG:4326', yes=False):

    # load file to get epsg info.
    dat = rasterio.open(sourcefile)

    # create new target filename
    targetfile = os.path.basename(sourcefile).split('.')[0] \
                + '_proj_' \
                + str(target_epsg).split(':')[1] \
                + '.tif'

    click.echo("Application Settings:\n")
    click.echo(f"source filename: {sourcefile}")
    click.echo(f"target filename: {targetfile}")
    click.echo(f"source epsg: {dat.crs}")
    click.echo(f"target epsg: {target_epsg}\n")
    dat.close()

    if not yes:
        click.confirm('[INFO] File reprojection takes a while.\nDo you want to continue?',
                  abort=True)

        click.echo('\n[INFO] Good time to get a cup of coffee.\n[INFO] This task can take 15-30 minutes or longer depending on file size.\n')

    with rasterio.open(sourcefile) as src:
        transform, width, height = calculate_default_transform(
            src.crs, target_epsg, src.width, src.height, *src.bounds)
        kwargs = src.meta.copy()
        kwargs.update({
            'crs': target_epsg,
            'transform': transform,
            'width': width,
            'height': height,
            'compress': 'LZW',
            'BIGTIFF' : 'IF_SAFER'
        })



        with rasterio.open(targetfile, 'w', **kwargs) as dst:
            for i in range(1, src.count + 1):
                reproject(
                    source=rasterio.band(src, i),
                    destination=rasterio.band(dst, i),
                    src_transform=src.transform,
                    src_crs=src.crs,
                    dst_transform=transform,
                    dst_crs=target_epsg,
                    resampling=Resampling.nearest)

    click.echo('[INFO] Task complete.')
    return targetfile
