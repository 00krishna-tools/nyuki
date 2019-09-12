#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = ['Click>=6.0', ]

setup_requirements = ['pytest-runner', ]

test_requirements = ['pytest', ]

setup(
    author="krishna bhogaonker",
    author_email='cyclotomiq@gmail.com',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    description="This package takes a geotiff file and resamples it to a new resolution. The user enters the path to the file and the resampling factor, and the package outputs the new file. ",
    entry_points={
        'console_scripts': [
            'geotiff-resampler=src.geotiff_resampler:main',
            'geotiff-reprojector=src.geotiff_reprojector:main',
            'geotiff-slicer=src.geotiff_chopper:main',
        ],
    },
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='src, geotiff_reprojector',
    name='src',
    packages=find_packages(include=['src']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/00krishna/geotiff_resampler',
    version='0.1.0',
    zip_safe=False,
)
