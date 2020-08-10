======================================
Nyuki: A Geospatial Toolkit for Humans
======================================

"Nyuki" translates to "bee" in Swahili, but is also the word used to refer to
aerial drones. While working on a collaboration between `DataKind <https://www.datakind.org/>`_
and `WeRobotics <https://werobotics.org/>`_ using drone imagery for flood damage
assessment, we found it really hard to do simple manipulations to large geotiff image and vector
files. Something as simple as resizing an image took 15-20 lines complicated
code. Hence we designed Nyuki to help turn these cumbersome tasks into one-line
commands. We started with a few common operations but hope to expand.
Contributions are always welcome. Also please give us a star if you like our tool.

📝 Table of Contents
-------------------

-  `About`_
-  `Getting Started`_
-  `Deployment`_
-  `Usage`_
-  `Built Using`_
-  `TODO`_
-  `Contributing`_
-  `Authors`_
-  `Acknowledgments`_

🧐 About 
-------

Nyuki is a command line tool that simplifies common and easy image
processing tasks. The tools implemented so far include:

-  Reprojecting geotiff and vector files
-  Resampling geotiff files to higher or lower resolution
-  Compressing geotiff files to save space

🏁 Getting Started 
-----------------

These instructions will get you a copy of the project up and running on
your local machine for development and testing purposes. See
`deployment`_ for notes on how to deploy the project on a live system.

Prerequisites
~~~~~~~~~~~~~

Nyuki relies on the open source Anaconda/Miniconda python distribution for scientific
computing. Many of the python and C++ libraries that nyuki depends upon are
difficult to install due to complicated dependencies between package or the
need to compile C++ files. Hence we chose to use a more robust package
manager: ``conda``. 

Once conda is installed from the following `link <https://www.anaconda.com/products/individual>`_ ,
the user can create new virtual environments and install packages like nyuki
into those environments. `Conda` package are stored in different public or
private channels, depending on whether the developer intends a package for
public use, or for a limited group of users. Nyuki is currently located in `krishnab75` Anaconda
channel but will soon be added to the widely `conda-forge` channel. 


Installing
~~~~~~~~~~

Assuming that the user has successfully installed the Anaconda/miniconda
python distribution on their computer, the user may install nyuki in a stand-alone
environment using

::

   conda create -n nyuki-env -c krishnab75 nyuki

This will create a new environment named ``nyuki-env`` into which the nyuki
application will be installed. Follow the prompts for the install and answer
"yes" at the install prompt. Nyuki will install a number of dependencies, so
it may take a few minutes to complete the installation. 

Once installation is complete, you can activate the environment and begin
to use nyuki

::

   conda activate nyuki-env

The user should now be in the `nyuki-env` python environment. To access nyuki's
commands and tools, type

::

   nyuki --help


🔧 Running the tests 
-------------------

Explain how to run the automated tests for this system.

Break down into end to end tests
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Explain what these tests test and why

::

   Give an example

And coding style tests
~~~~~~~~~~~~~~~~~~~~~~

Explain what these tests test and why

::

   Give an example

🎈 Usage 
-------

Add notes about how to use the system.

🚀 Deployment 
------------

Add additional notes about how to deploy this on a live system.

⛏️ Built Using 
--------------

-  `Click`_ - Command Line Interface
-  `Rasterio`_ - Geospatial Library for Rasters
-  `Geopandas`_ Geospatial Library for Vector data  

✍️ Authors 
----------

-  `@00krishna <https://github.com/00krishna>`_ - krishna bhogaonker

See also the list of

.. _About: #about
.. _Getting Started: #getting_started
.. _Deployment: #deployment
.. _Usage: #usage
.. _Built Using: #built_using
.. _TODO: ../TODO.md
.. _Contributing: ../CONTRIBUTING.md
.. _Authors: #authors
.. _Acknowledgments: #acknowledgement
.. _deployment: #deployment
