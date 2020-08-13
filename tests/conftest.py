import sys
import pytest
import os
import shutil

collect_ignore = ['setup.py']

test_files = [os.path.join(os.path.dirname(__file__), p) for p in [
    'test_data/sample_image_small.tif']]

@pytest.fixture(scope='function')
def data(tmpdir):
    """A temporary directory containing a copy of the files in data."""
    for filename in test_files:
        shutil.copy(filename, str(tmpdir))

    return tmpdir


@pytest.fixture(scope="function")
def small_image(data):
    return os.path.join(str(data), 'sample_image_small.tif')


