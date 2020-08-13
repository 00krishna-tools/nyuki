import sys
import pytest

collect_ignore = ['setup.py']

FIXTURE_DIR = os.path.join(
    os.path.dirname(os.path.realpath(__file__)),
    'test_data',
    )

@pytest.fixture(scope="module")
@pytest.mark.datafiles(os.path.join(FIXTURE_DIR, 'sample_image_small.tif'))
def small_image(datafiles):
    return datafiles
