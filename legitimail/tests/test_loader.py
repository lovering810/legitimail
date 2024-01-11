from legitimail.utilities import loader
import pytest


DEFINED_FILTERS = ["domain"]


@pytest.fixture
def good_list():
    return ["domain"]


def test_load_all():
    successful_filters = loader.load_all_filters()
    assert successful_filters == DEFINED_FILTERS
