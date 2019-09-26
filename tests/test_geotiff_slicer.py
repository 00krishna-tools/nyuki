#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `src` package."""

import pytest
from click.testing import CliRunner
from src import geotiff_chopper


def test_demo():
    print('hello')
    assert 1 == 1


def test_run_geotiff_slicer():
    geotiff_chopper.chopper('grid_022.tif', 'grid_022.geojson', 512)

