
.. figure:: docs/assets/animated-bee-illustration-png-clip-art.png 
   :height: 455
   :width: 249
   :align: center

======================================
Nyuki: A Geospatial Toolkit for Humans
======================================
.. image:: https://ci.appveyor.com/api/projects/status/akr8yxfous98dlrl?svg=true
   :target: https://ci.appveyor.com/api/projects/status/akr8yxfous98dlrl/branch/master?svg=true
   
"Nyuki" translates to "bee" in Swahili, but is also the word used to refer to
aerial drones. While working on a project using aerial drone imagery for
flood damage assessment with  `DataKind <https://www.datakind.org/>`_
and `WeRobotics <https://werobotics.org/>`_ we found that using many common
python geospatial libraries had a steep learning curve and were confusing
to use. So we developed some simple command line tools and library
functions to simplify common tasks and dramatically accelerate our
development.

The other challenge with processing large aerial drone images was that most
GIS software such as QGIS or ArcGIS often crashed while processing large images.
Aerial drones can easily produce 50,000 x 50,000 pixel images or more.
Because processing such large images is memory and processor intensive,
some common GIS software can often fail during processing. With nyuki
we rely on the command line which has a much lighter memory footprint and is
easier to kill if something is taking too long. 

Nyuki is developed for python 3.6 or greater and runs on Windows, MacOS, and Linux
operating systems.

We also wanted to thank all of the developers who built the libraries that we
use in nyuki. Writing geospatial libraries is hard work, and 



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
into those environments. ``Conda`` packages are stored in different public or
private channels, depending on whether the developer intends a package for
public use, or for a limited group of users. Nyuki is currently located in ``krishnab75`` Anaconda
channel but will soon be added to the widely ``conda-forge`` channel. 


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

The user should now be in the ``nyuki-env`` python environment. To access nyuki's
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


⛏️ Built Using 
--------------

-  ``Click <https://click.palletsprojects.com/en/7.x/>``_ - Command Line Interface
-  ``Rasterio<https://rasterio.readthedocs.io/en/latest/>``_ - Geospatial Library for Rasters
-  ``Geopandas<https://geopandas.org/>``_ Geospatial Library for Vector data  

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
