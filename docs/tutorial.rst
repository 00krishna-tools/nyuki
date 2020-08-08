Tutorial
========

Nyuki tries to simplify a number of common geospatial operations 
on both raster and vector data. The tutorial below walks through 
the installation of the tool as well as practice demos of 
each tool. So let's get started. 

================
Installing Nyuki
================

Nyuki must be installed using the Anaconda python distribution from Anaconda.com. Download and install the 
free individual version of Miniconda from the following `website <https://docs.conda.io/en/latest/miniconda.html>`_
. To install Miniconda go to the command prompt on follow the instructions for Linux, Windows, or Mac.

Linux
*****

First install miniconda

.. code-block:: bash

     bash minconda

Follow the prompts to install miniconda. Then close and restart the terminal in order to ensure that Miniconda is installed. 
At the prompt type

.. code-block:: bash

     conda init <shellname>

You can use replace `<shellname>` with the name of your current shell software, such as `conda init bash` or `conda init zsh`, etc. 

Once miniconda is installed, we must create a new virtual environment to contain the software that we install. 
