
# -*- coding: utf-8 -*-

"""Console script for nyuki geotiff files compressor."""
import sys
import os
import click
import rasterio
from rasterio.warp import calculate_default_transform, reproject, Resampling

@click.command()
@click.option('--sourcetiff', required=True, type=click.Path(exists=True),
              prompt="Source file path",
              help="Enter the path to the original GEOTIFF raster image")
@click.option('--target_compression', default='LZW', show_default=True,
              type=click.Choice(['LZW', 'LZMA', 'LERC', 'JPEG', 'JPEG2000',
                                 'DEFLATE', 'WEBP', 'ZSTD', 'NONE'], case_sensitive=True),
              prompt="Target compression method",
              help="Enter the compression standard to apply to the raster.")
def main(sourcetiff, target_compression='LZW'):
    """Compress Geotiff raster files to shrink file size.

       This tool will compress a Geotiff raster image using the specified compression
       method. The supported methods are LZW, LZMA, JPEG, and JPEG2000 standards.
       JPEG and JPEG2000 compression usually produce the smallest files and are good
       for most users, even though the method is "lossy." Alternatively, LZW and LZMA
       are "lossless" methods, but they produce larger file sizes.

       The link provides a good overview of preferred compression methods for different
       use cases.
       https://doc.arcgis.com/en/imagery/workflows/best-practices/imagery-formats-and-performance.htm

       Note that in some cases, compression can make the file size larger. Hence it could
       take a few attempts to find the right compression scheme. 

    
        Commandline app:\n
        >>> nyuki raster compressor --sourcetiff file1.tif --target_compression 'lzw'

        Invoke interactive mode:\n
        >>> nyuki raster compressor
        """

    compressor(sourcetiff, target_compression)
    return 0

def compressor(sourcefile, target_compression='LZW'):

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
    click.echo(f"source current compression: {profile.get('compress', 'Uncompressed')}")
    click.echo(f"target epsg: {target_compression}\n")


    # check if new compression is same as old compression
    
    
    click.confirm('[INFO] File compression takes a while.\nDo you want to continue?',
                  abort=True)

    click.echo('\n[INFO] Good time to get a cup of coffee.\n[INFO] This task can take 15-30 minutes or longer depending on file size.\n')

    with rasterio.Env():

    # Write an array as a raster band to a new 8-bit file. For
    # the new file's profile, we start with the profile of the source

    # specify compression standard
        profile.update(
            compress=target_compression,
            BIGTIFF = "IF_SAFER")
        
        with rasterio.open(targetfile, 'w', **profile) as dst:
            for ji, window in dat.block_windows(1):
                dst.write(dat.read(window=window), window=window)



    click.echo('[INFO] Task complete.')

if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
