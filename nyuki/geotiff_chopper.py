# -*- coding: utf-8 -*-

"""Console script for geotiff_reprojector."""
import sys
import os
import click
import numpy as np
import rasterio
import rasterio.features
from PIL import Image
import PIL
from osgeo import gdal
from tqdm import trange, tqdm
import geopandas as gpd
import pandas as pd

# disable pixel size checks
PIL.Image.MAX_IMAGE_PIXELS = None

@click.command()
@click.option('--sourcetiff', type=click.Path(exists=True), required=True,
              prompt="Enter the path for the source tiff image",
              help="Path to the GEOTIFF raster image")
@click.option('--sourcemask', type=click.Path(), required=True,
              prompt="Enter the path for the source mask file",
              help="Path to the labels geojson file that corresponds to the GEOTIFF file")
@click.option('--size', type=int, required=True, default=512,
              prompt="Enter the size of the sliced images in pixels",
              help="The size in pixels of the chopped images, such as 512 for 512x512 images")
def main(sourcetiff, sourcemask, size):
    """Application: Geotiff Chopper.

        This tool will slice a raster GEOTIFF image into size x size PNG images with
        corresponding labels.
        The user enters the source GEOTIFF filename, the mask filename, and the sliced
        image size. Output files are saved to 'images' and 'labels' folders in the
        working directory.

        This tool is used as follows. The User should first use a cool like QGIS or
        similar to clip the raster layer using the vector (mask) layer--or alternatively
        clipping the vector layer using the raster layer. Then these two equally sized
        layers are exported as a GEOTIFF and geojson layer. It is critical that both
        files respect the same exact geographical boundaries, otherwise there will be
        misalignments when the images are sliced.

        Note that the mask and source tiff file do not need to be in the same EPSG or
        coordinate projection. Because both files are converted to PNG files for slicing,
        the projection does not matter.

        Examples:

        Commandline app:\n
        >>> geotiff-slicer --sourcetiff file1.tif --sourcemask file1.geojson --size 512

        Invoke interactive mode:\n
        >>> geotiff-slicer

        """

    chopper(sourcetiff, sourcemask, size)

    return 0

def chopper(sourcetiff, sourcemask, size):

    raster = rasterio.open(sourcetiff)
    buildings = gpd.read_file(sourcemask)

    click.echo("Application Settings:\n")
    click.echo(f"source image: {sourcetiff}")
    click.echo(f"source mask: {sourcemask}")
    click.echo(f"output image size: {size} x {size} ")
    click.echo(f"source epsg: {raster.crs}")
    click.echo(f"masks epsg: {buildings.crs['init'].upper()}")

    click.confirm(f'The image and masks files must be in the same coordinate projection. \n Please convert the files so that the coordinate projections match.\n', abort=True)

    # filenames for temporary files
    tmp_imagefilename = 'tmp_sourceimage.png'
    tmp_masksfilename = 'tmp_masks.png'
    img_master_directory = os.getcwd()
    img_prefix = os.path.basename(sourcetiff).split('.')[0]

    # read masks and remove empty geometries
    buildings = buildings[~buildings.is_empty]

    # rasterize the
    print('[INFO] Rasterizing the masks')
    tfl_raster = rasterize_masks(buildings, raster)

    # write masks to new png file.
    img = Image.fromarray(tfl_raster)
    img.save(tmp_masksfilename)

    options_list = [
        '-ot Byte',
        '-of PNG',
        '-scale'
    ]
    options_string = " ".join(options_list)

    print('[INFO] Converting image from TIFF to PNG format for chopping.\n This might take some time depending upon compression of the original TIFF file.')

    gdal.Translate(tmp_imagefilename,
                   sourcetiff,
                   options=options_string)

    print('[INFO] Beginning the image slicing process.')
    max_height, max_width = img_chopper(tmp_imagefilename,
                                        tmp_masksfilename,
                                        img_master_directory,
                                        prefix=img_prefix,
                                        height=size,
                                        width=size)
    print(f"max height slices: {max_height}, max width slices: {max_width}")

    print('[INFO] Complete slicing image.')
    print('[INFO] Cleaning up files.')
    os.remove(tmp_imagefilename)
    os.remove(tmp_masksfilename)
    print('[INFO] Done.')

def rasterize_masks(masks, raster):
    tfl_raster = rasterio.features.rasterize(
        [(x.geometry, 255) for i, x in masks.iterrows()],
        out_shape=raster.shape,
        transform=raster.transform,
        fill=0,
        all_touched=True,
        dtype=rasterio.uint8)
    return tfl_raster

def check_empty_pixels_below_threshold(image_array, threshold=0.50):
    status = True
    empty_pixels = np.sum(image_array==0)/image_array.size
    white_pixels = np.sum(image_array==255)/image_array.size
    if empty_pixels >= threshold:
        status = False
    if white_pixels >= threshold:
        status = False
    return status


def img_chopper(img, label,
                images_master_directory,
                prefix=None,
                height=512,
                width=512,
                image_directory_name='images',
                label_directory_name='labels'):
    img_dir = os.path.join(images_master_directory, image_directory_name)
    label_dir = os.path.join(images_master_directory, label_directory_name)
    csv_dir = images_master_directory
    os.makedirs(img_dir, exist_ok=True)
    os.makedirs(label_dir, exist_ok=True)

    counter = 1
    im = Image.open(img)
    lb = Image.open(label)
    imgwidth, imgheight = im.size
    lbwidth, lbheight = lb.size
    print(f'image size {im.size}')
    print(f'label size {lb.size}')
    assert (im.size == lb.size), "image and label sizes don't match"

    # setup csv export
    image_max_height = len(range(0, imgheight, height))
    image_max_width = len(range(0, imgwidth, width))
    csv_export = pd.DataFrame(np.zeros([image_max_height * image_max_width, 3]))
    csv_export.columns = ['image', 'label', 'naive_test_train_split90_10']

    for i in tqdm(range(0, imgheight, height), desc='height_dimension'):
        for j in tqdm(range(0, imgwidth, width), desc='width_dimension', leave=False):
            box = (j, i, j + width, i + height)
            a = im.crop(box)
            b = lb.crop(box)
            if check_empty_pixels_below_threshold(np.asarray(a)):
                try:
                    a.save(os.path.join(img_dir, f"{prefix}_{counter}.png"))
                    b.save(os.path.join(label_dir, f"{prefix}_{counter}.png"))
                    csv_export.loc[counter - 1, 'image'] = os.path.join(prefix + '/' + image_directory_name,
                                                                        f"{prefix}_{counter}.png")
                    csv_export.loc[counter - 1, 'label'] = os.path.join(prefix + '/' + label_directory_name,
                                                                        f"{prefix}_{counter}.png")
                    csv_export.loc[
                        counter - 1, 'naive_test_train_split90_10'] = "Train" if np.random.uniform() <= 0.90 else "Test"
                    counter += 1
                except:
                    pass
    csv_export.to_csv(os.path.join(csv_dir, f'{prefix}' + '_data_index.csv'), header=True)
    return (image_max_height, image_max_width)

if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
