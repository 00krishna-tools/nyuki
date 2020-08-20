Command Line Tutorial
=====================

Nyuki tries to simplify a number of common geospatial operations 
on both raster and vector data. The tutorial below walks users through
the command line tools that are part of the package. A subsequent tutorial
will show how to import and use nyuki as a programming library.

================
Installing Nyuki
================

Nyuki must be installed using the free Anaconda/Miniconda python distribution from
Anaconda.com. Follow the instructions in the Installation section of documentation.

================================
Obtaining the sample image files
================================

The sample image files are located on the Github repository for the `nyuki`
package. Click on the following links to download the files.

- `sample image small`_
- `sample vector file`_

The user may also download a medium sized sample image to experiment with, if he/she wishes. 

- `sample image medium`_

.. _sample image small: https://github.com/00krishna-tools/nyuki/releases/download/v0.0.1/sample_image_small.tif
.. _sample vector file: https://github.com/00krishna-tools/nyuki/releases/download/v0.0.1/sample_vector_file.geojson
.. _sample image medium: https://github.com/00krishna-tools/nyuki/releases/download/v0.0.1/sample_image_medium.tif
==============================================
Nyuki Info: Obtaining metadata about your file
==============================================

.. raw:: html

    <div style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; height: auto;">
        <iframe src="https://www.youtube.com/embed/dQw4w9WgXcQ" frameborder="0" allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe>
    </div>

The first thing that most users want to do is check the metadata about their
raster or vector files. Metadata includes the spatial coordinate system used
to encode the data, or the size of the image, whether there is compression
applied to the image, among other things. ``Nyuki` had designed a metadata
tool that compares to the standard ``gdalinfo`` tool; however whereas ``gdalinfo``
can be a bit confusing to navigate, ``nyuki info`` is meant to be a little
easier to interpret.

To start the tutorial, navigate via the command line to the directory in which
the small test files were downloaded. Next we activate the ``proj_nyuki``
environment to access our ``nyuki`` application.

.. code-block:: console

    $ conda activate proj_nyuki

We will usually see the ``(proj_nyuki)`` indicator appear next to the command
prompt in the terminal. Next we can test that ``nyuki`` is installed using the
Help command.

.. code-block:: console

    $ nyuki --help

If the help screen appears, then ``nyuki`` is installed. If otherwise, then
check the Installation instructions located in this documentation website.

To obtain the metadata information for the raster file, type:

.. code-block:: console

    $ nyuki info --sourcefile sample_image_small.tif

The output should resemble

.. code-block:: console

 	 File info for: sample_image_small.tif: 

	 Coordinate projection: EPSG:32737
	 File type: GTiff
	 File size: (1312, 2170)
	 Pixel Units: metre
	 Pixel size: (0.068, 0.068)
	 Number of Bands: 3
	 Data type per band: ('uint8', 'uint8', 'uint8')
	 Compression: Uncompressed
	 Nodata character: None

The output shows the coordinate projection for the file, the file size in
pixels, the length units for each pixel--in this case meters, the length
corresponding to each pixel(6.8 centimeters), the number of raster bands and
their datatypes, as well as the compression format used for the image.

For the sake of comparison, the user might try obtaining the same information
for the file using ``gdalinfo``. The command below will produce a similar output
to ``nyuki info``, but we leave it to the user to decide which is easier to
read.

.. code-block:: console

    $ gdalinfo sample_image_small.tif

To see the metadata for a vector file, we use the same command, but with
a reference to a vector file. Note that the vector information tool is still
a work in process and currently shows only limited information. 

.. code-block:: console

    $ nyuki info --sourcefile sample_vector_file.geojson

 	 File info for: sample_vector_file.geojson: 

	 Coordinate projection: epsg:4326

Thus ``nyuki info`` provide an easy to read summary of file metadata for raster
and vector files. 

==================================
Nyuki Compress: Compressing images
==================================

Geospatial data files can be very large, so compressing those files before
storing or transmitting them is important. ``Nyuki`` supports the following common
compression standards:

- LZW
- LZMA
- JPEG
- JPEG2000
- DEFLATE
- ZSTD
- NONE (removes compression from file)

If you have never heard of some or most of these standards, that is fine. These
are common methods that give reliable results across Windows, Mac, and Linux
platforms. Note that the "NONE" standard will actually uncompress a file, or
save a file with no compression. 

To try out the compression features, let's start by looking at information on
the small tif file and confirming that it really is uncompressed.

.. code-block:: console

   (proj_nyuki)$ nyuki info --sourcefile sample_image_small.tif

 	 File info for: sample_image_small.tif: 

	 Coordinate projection: EPSG:32737
	 File type: GTiff
	 File size: (1312, 2170)
	 Pixel Units: metre
	 Pixel size: (0.068, 0.068)
	 Number of Bands: 3
	 Data type per band: ('uint8', 'uint8', 'uint8')
	 Compression: Uncompressed
	 Nodata character: None

The compression setting shows "Uncompressed."

Next we can apply LZMA compression to the file using the following command.

.. code-block:: console

   (proj_nyuki)$ nyuki raster compress --sourcetif sample_image_small.tif --target_compression LZMA -y

After a minute, ``nyuki`` will indicate that the operation is complete. Now we
can check that the file was actually compressed. We can confirm this in two
ways: check the file information and check the file size.

To check the file information we can use the same command we originally used:

.. code-block:: console

   (proj_nyuki)$ nyuki info --sourcefile sample_image_small_compress_LZMA.tif

 	 File info for: sample_image_small_compress_LZMA.tif: 

	 Coordinate projection: EPSG:32737
	 File type: GTiff
	 File size: (1312, 2170)
	 Pixel Units: metre
	 Pixel size: (0.068, 0.068)
	 Number of Bands: 3
	 Data type per band: ('uint8', 'uint8', 'uint8')
	 Compression: lzma
	 Nodata character: None

So now we can see that the compression standard is set to "LZMA."

Further, if we want to see the different in file size, we could use a command
like:

.. code-block:: console

   (proj_nyuki)$ ls -lh

   -rw-rw-r-- 1 demo demo 282M Aug 11 14:07 sample_image_medium.tif
   -rw-rw-r-- 1 demo demo 3.5M Aug 18 12:09 sample_image_small_compress_LZMA.tif
   -rw-rw-r-- 1 demo demo 8.2M Aug 11 14:37 sample_image_small.tif
   -rw-rw-r-- 1 demo demo 318K Aug 13 16:28 sample_vector_file.geojson

So again we can see that the uncompressed file is 8.2 MB while the compressed
file is 3.5 MB. Not that in some cases--and for confusing reasons--compressed
files may actually be larger than their uncompressed originals. The circumstances
under which this happens have to do with the compression algorithms used and how
those algorithms represent the compressed form of the data.

====================================================================
Nyuki Reproject: Reprojecting images to different coordinate systems
====================================================================

The next tool to investigate is the reproject tool. One common operation in
geospatial analysis is to convert from one system of coordinates to another.
Sometimes a user has an image with coordinates in latitude/longitude, and they
prefer to work in some coordinate system that is more attuned to a local
geographic region. Further, different coordinate systems use different units
of length. Switching coordinate systems may sometimes make analysis easier
because the units of length are easier to interpret. A good example of this
is the common latitude/longitude EPSG:4326 coordinate system which uses the hard to
interpret unit length of "degrees, hours, minutes." Reprojecting this image to
a coordinate system that uses meters or feet may be easier to interpret. So
let's work through an example.

Let's look at our original small image and determine its coordinate system and
units.

.. code-block:: console

   (proj_nyuki)$ nyuki info --sourcefile sample_image_small.tif

 	 File info for: sample_image_small.tif: 

	 Coordinate projection: EPSG:32737
	 File type: GTiff
	 File size: (1312, 2170)
	 Pixel Units: metre
	 Pixel size: (0.068, 0.068)
	 Number of Bands: 3
	 Data type per band: ('uint8', 'uint8', 'uint8')
	 Compression: Uncompressed
	 Nodata character: None

So the coordinate system is EPSG:32732 with units in "meters". The EPSG: 32737
coordinate system is local to Tanzania and hence users of Tanzanian imagery
prefer to keep their images in the EPSG:32737 coordinate system.

However, if for some reason the user needs to display his/her image with
images from other parts of the world, then it is common to reproject that image
to a common coordinate system. The EPSG:4326 coordinate system, based on
Latitude/Longitude is often the default coordinate system and works well all
over the world.

Let's reproject our image to this new coordinate system.

.. code-block:: console

   (proj_nyuki)$ nyuki raster reproject --sourcetiff sample_image_small.tif --target_epsg EPSG:4326 -y

After the code runs, the user can see the output file as ``sample_image_small_proj_4326.tif.``
To check that the projection operation completed successfully we can use the
``nyuki info`` tool as such 

.. code-block:: console

   (proj_nyuki)$ nyuki info --sourcefile sample_image_small_proj_4326.tif

 	 File info for: sample_image_small_proj_4326.tif: 

	 Coordinate projection: EPSG:4326
	 File type: GTiff
	 File size: (1315, 2170)
	 Pixel Units: unknown, likely degrees
	 Pixel size: (0.0, 0.0)
	 Number of Bands: 3
	 Data type per band: ('uint8', 'uint8', 'uint8')
	 Compression: lzw
	 Nodata character: None

Which show that the projection was applied. Alternatively we could load the
file into QGIS or ArcGIS and check that the file is accurately reprojected,
but otherwise unchanged. 


=======================================================================
Nyuki Resample: Upsampling/Downsampling images to different resolutions
=======================================================================

Next we can look at the resampling tool in ``nyuki.`` The resampling tool
will either downsample or upsample an image to reduce or increase its resolution, respectively.
Often large geospatial images are taken with very high resolution which also
leads to high file sizes. For a website or publication format, image resolution
is often downsampled/reduced to shrink the file size while preserving most
of the detail.

When we examine a file in ``nyuki``, we can see the resolution of each pixel
as 0.067 meters. In other words, given that each pixel is square shaped, the
height and width of each pixel corresponds to 6.7 centimeters.

.. code-block:: console

   (proj_nyuki)$ nyuki info --sourcefile sample_image_small.tif

 	 File info for: sample_image_small.tif: 

	 Coordinate projection: EPSG:32737
	 File type: GTiff
	 File size: (1312, 2170)
	 Pixel Units: metre
	 Pixel size: (0.068, 0.068)
	 Number of Bands: 3
	 Data type per band: ('uint8', 'uint8', 'uint8')
	 Compression: Uncompressed
	 Nodata character: None

By resampling the image we will reduce the image resolution so that each
pixel corresponds to 22 centimeters. The choice of 22 centimeters is arbitrary,
and users are free to resample to any size they wish.

.. code-block:: console

   (proj_nyuki)$ nyuki raster resample --sourcetiff sample_image_small.tif --target_resolution 0.22 -y

Once the process is complete we can import the image into QGIS or ArcGIS to
check the result. Or we can simply check the information on the image. 

.. code-block:: console

   (proj_nyuki)$ nyuki info --sourcefile sample_image_small_resampled_0_22metre.tif

   File info for: sample_image_small_resampled_0_22metre.tif:

	 Coordinate projection: EPSG:32737
	 File type: GTiff
	 File size: (405, 670)
	 Pixel Units: metre
	 Pixel size: (0.22, 0.22)
	 Number of Bands: 3
	 Data type per band: ('uint8', 'uint8', 'uint8')
	 Compression: Uncompressed
	 Nodata character: None

The new pixel size indicates that each pixel is now 22 centimeters square and
that the image has been successfully resampled. 
















