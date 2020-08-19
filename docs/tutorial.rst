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

 nyuki info --sourcefile sample_image_small.tif 

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
is the 










=======================================================================
Nyuki Resample: Upsampling/Downsampling images to different resolutions
=======================================================================
























