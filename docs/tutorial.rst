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

The first think that most users want to do is check the metadata about their
raster or vector files. Metadata includes the spatial coordinate system used
to encode the data, or the size of the image, whether there is compression
applied to the image, among other things. ``Nyuki` had designed a metadata
tool that compares to 


*****
 





