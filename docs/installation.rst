.. highlight:: shell

============
Installation
============


Stable release
--------------
Because nyuki relies on a number of geospatial python packages, the usual
``pip`` package manager does not work very well. ``Pip`` works very well for
python-only packages, but when there are ``C`` and ``C++`` libraries involved,
then we rely on a more robust package manager such as ``conda`` and the
`Miniconda <https://docs.conda.io/en/latest/miniconda.html>`_ python distribution.
`Anaconda.com <https://www.anaconda.com/>`_, the company, provides the Miniconda
distribution for free to users. 

To use nyuki, users must:

1. Install the ``miniconda`` python distribution.

2. Set the Anaconda channels from which to download nyuki and its python
package dependencies.

3. Download and install nyuki.

4. Activate nyuki for usage.

We will walk the use through each of these four steps. 

Step 1: Download the ``miniconda`` python distribution.
*******************************************************

The Anaconda python distribution saves data scientists a lot of time by bundling
the most commonly used python package for scientific computing. `Anaconda.com <https://www.anaconda.com/products/individual>`_
provides and maintains this distribution for users to download free of charge.
Users on Windows, Macos, or Linux can find their appropriate installer by following
the link above. Once Miniconda is installed, the user can move on to step 2. The
video shows how to install Miniconda on a linux machine. 

Step 2: Setting up the Anaconda channels to install ``nyuki``
*************************************************************

Before installing ``nyuki`` we need to tell the ``conda`` package installer
where to look for both ``nyuki`` and its dependencies. `Anaconda Cloud <https://anaconda.org>`_
is a package repository that stores pre-built packages in the same way that
the Python Package Index (PyPI) stores most python packages. 



To install nyuki, run this command in your terminal:

.. code-block:: console

    $ conda install nyuki

This is the preferred method to install nyuki, as it will always install the most recent stable release.

If you don't have `pip`_ installed, this `Python installation guide`_ can guide
you through the process.

.. _pip: https://pip.pypa.io
.. _Python installation guide: http://docs.python-guide.org/en/latest/starting/installation/


From sources
------------

The sources for nyuki can be downloaded from the `Github repo`_.

You can either clone the public repository:

.. code-block:: console

    $ git clone git://github.com/00krishna-tools/nyuki

Or download the `tarball`_:

.. code-block:: console

    $ curl  -OL https://github.com/00krishna-tools/nyuki/tarball/master

Once you have a copy of the source, you can install it with:

.. code-block:: console

    $ python setup.py install


.. _Github repo: https://github.com/00krishna-tools/nyuki
.. _tarball: https://github.com/00krishna/nyuki/tarball/master
