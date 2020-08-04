#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.md') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = []

setup_requirements = [ ]

test_requirements = [ ]

setup(
    author="krishna bhogaonker",
    author_email='cyclotomiq@gmail.com',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    description="This command line tool will reproject, resample, and perform other manipulations on geotiff raster and vector files. ",
    entry_points={
        'console_scripts': [
            'nyuki=src.nyuki:nyuki',
            'geotiff-slicer=src.geotiff_chopper:main'
        ],
    },
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='src, nyuki',
    name='nyuki',
    packages=find_packages(include=['nyuki']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/00krishna-tools/nyuki',
    version='0.5.0',
    zip_safe=False,
)
