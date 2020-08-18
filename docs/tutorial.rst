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

==============================================
Nyuki Compress: Compressing images
==============================================

Geospatial data files can be very large, so compressing those files into




