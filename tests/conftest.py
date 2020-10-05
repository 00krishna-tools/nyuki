import sys
import pytest
import os
import shutil
import requests


collect_ignore = ['setup.py']


@pytest.fixture(scope="function")
def small_image(tmpdir):
    url = 'https://github.com/00krishna-tools/nyuki/releases/download/v0.0.1/sample_image_small.tif'

    r = requests.get(url)

    with open(os.path.join(str(tmpdir), 'sample_image_small.tif'), 'wb') as f:
        f.write(r.content)

    return os.path.join(str(tmpdir), 'sample_image_small.tif')


@pytest.fixture(scope="function")
def big_image(tmpdir):
    url = 'https://github.com/00krishna-tools/nyuki/releases/download/v0.0.1/sample_image_big.tif'

    r = requests.get(url)

    with open(os.path.join(str(tmpdir), 'sample_image_big.tif'), 'wb') as f:
        f.write(r.content)

    return os.path.join(str(tmpdir), 'sample_image_big.tif')


@pytest.fixture(scope="function")
def small_vector_file(tmpdir):
    url = 'https://github.com/00krishna-tools/nyuki/releases/download/v0.0.1/sample_vector_file.geojson'

    r = requests.get(url)

    with open(os.path.join(str(tmpdir), 'sample_vector_file.geojson'), 'wb') as f:
        f.write(r.content)

    return os.path.join(str(tmpdir), 'sample_vector_file.geojson')
