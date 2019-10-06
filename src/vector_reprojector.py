# -*- coding: utf-8 -*-

"""Console script for geotiff_reprojector."""
import sys
import os
import click
import geopandas as gpd

@click.command()
@click.option('--sourcefile', required=True, type=click.Path(exists=True),
              prompt="Source file path",
              help="Enter the path to the original GEOJSON or vector file")
@click.option('--target_epsg', default='EPSG:4326', show_default=True, type=str,
              prompt="Target coordinate EPSG",
              help="Enter the coordinate projection to apply to the raster image.")
def main(sourcefile, target_epsg='EPSG:4326'):
    """Application: Vector Reprojector.

        This tool will reproject a vector file to a different EPSG coordinate projection.
        The user enters the source vector filename, and a valid target EPSG projection.
        The file is output to the same directory as the source file.

        Commandline app:\n
        >>> vector-reprojector --sourcefile file1.geojson --target_epsg 'EPSG:4326'

        Invoke interactive mode:\n
        >>> vector-reprojector
        """

    reprojector(sourcefile, target_epsg)
    return 0

def reprojector(sourcefile, target_epsg='EPSG:4326'):

    # load file to get epsg info.
    buildings = gpd.read_file(sourcefile)
    buildings = buildings[buildings.geometry.notnull()]
    buildings = buildings[~buildings.is_empty]
    # create new target filename
    targetfile = os.path.basename(sourcefile).split('.')[0] \
                + '_proj_' \
                + str(target_epsg).split(':')[1] \
                + '.geojson'

    click.echo("Application Settings:\n")
    click.echo(f"source filename: {sourcefile}")
    click.echo(f"target filename: {targetfile}")
    click.echo(f"source epsg: {buildings.crs['init']}")
    click.echo(f"target epsg: {target_epsg}\n")

    click.confirm('Are you ready to proceed?',
                  abort=True)

    click.echo('\n[INFO] Executing reprojection.\n')

    buildings_reprojected = buildings.to_crs(target_epsg)
    buildings_reprojected.to_file(targetfile, driver='GeoJSON')

    click.echo('[INFO] Task complete.')

if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
