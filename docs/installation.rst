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

Note, ``nyuki`` is not provided through the Python Package Index, and hence
users may not install the package using ``pip install nyuki.`` This code will
certainly not work.

Step 2: Setting up the Anaconda channels to install ``nyuki``
*************************************************************

Before installing ``nyuki`` we need to tell the ``conda`` package installer
where to look for both ``nyuki`` and its dependencies. `Anaconda Cloud <https://anaconda.org>`_
is a package repository that stores pre-built packages in the same way that
the Python Package Index (PyPI) stores most python package source files. Anaconda cloud
organizes packages by groupings known as "channels," hence when installing
packages we generally like to specify the channel from which we are installing
the package. This point is especially true when installing geospatial packages,
because different channels may have subtly different versions of common
python packages. If users obtain packages from the wrong Anaconda channels,
then some software dependencies for ``nyuki` may be improperly installed and
``nyuki`` will not function as expected--and understandably frustrating dilemma.

To specify the correct channel installation, we us the following code. 


.. code-block:: console

    $ conda config --add channels conda-forge 

The command will set the ``conda`` package manager to look in the ``conda-forge``
channel first, which is exactly what we would like. ``Nyuki`` will also eventually
reside in the ``conda-forge`` channel. Now we are ready for the next step. 


Step 3: Creating a ``conda`` environment and installing ``nyuki``
*****************************************************************

The Miniconda/Anaconda distribution allow users to create virtual environments
for their software project. A virtual environment creates small encapsulated
python installations that are completely independent and isolated from the main
python packages installed on the user's computer. For example a user may create
one virtual ``conda`` environment to test some legacy Python 2.7 code while
creating another ``conda`` environment to develop some new Python 3.8 code. The
advantage of virtual environments is that they allow multiple versions of python
to reside on the same computer without interfering with each other.

To install ``nyuki`` we will create our own ``conda``virtual environment. Enter
the following code at the command prompt:

.. code-block:: console

    $ conda create --yes -n proj_nyuki python=3.7 -c krishnab75 nyuki

This code will create a new ``conda`` environment--named ``proj_nyuki``--and then install the ``nyuki``
package. If the use chooses, he/she can change ``proj_nyuki`` to any python compliant name that he/she
desires. Currenty ``nyuki`` is stored in my personal Anaconda cloud channel, but
that will soon change to ``conda-forge.``

Congratulations, you have successfully installed the ``nyuki`` package.


Step 4: Activating the ``conda`` environment and using ``nyuki``
****************************************************************

Now that ``nyuki`` is installed, we can begin to use it. First we need to
activate the new project environment and then we can test whether ``nyuki``
was properly installed.

To activate the new environment, use the following command at the terminal prompt.

.. code-block:: console

    $ conda activate proj_nyuki

Most users will now see their prompt change to reference the new virtual environment
(proj_nyuki). To test whether ``nyuki`` was successfully installed, the user can
check whether the help functionality work on the package.


.. code-block:: console

    $ nyuki --help

If the ``nyuki`` help text fills the terminal, then the package is ready to use.

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
