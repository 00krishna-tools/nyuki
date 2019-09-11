# -*- coding: utf-8 -*-

"""Console script for geotiff_reprojector."""
import sys
import os
import click
import numpy as np
import rasterio
from rasterio.warp import calculate_default_transform, reproject, Resampling

@click.command()
@click.argument('sourcefile', type=click.Path(exists=True))
@click.argument('target_epsg', type=str)
def main(sourcefile, target_epsg='EPSG:4326'):
    """Application: Geotiff Reprojector.

        This tool will reproject a raster image to a different EPSG coordinate projection.
        The user enters the source GEOTIFF filename, the target GEOTIFF filename,
        and a target EPSG projection.

        Arguments: \n
            SOURCEFILE (path): Path to the original GEOTIFF raster image \n
            TARGETFILE (path): the path and name of the new resampled raster image written by this application. \n
            TARGET_EPSG (string): The coordinate projection to apply to the raster image. For examples 'EPSG:4326' \n
        """

    reprojector(sourcefile, target_epsg)
    return 0

def reprojector(sourcefile, target_epsg='EPSG:4326'):

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
            'height': height
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

if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
