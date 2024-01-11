from legitimail.utilities.candidate import Candidate
import pytest


@pytest.fixture
def good_candidate():
    return Candidate(entry="fakeyMcfakerson@gmail.com")


def test_entry_split(good_candidate):

    assert good_candidate.name == "fakeyMcfakerson"
    assert good_candidate.domain == "gmail.com"


def test_bad_entry():

    with pytest.raises(AttributeError):
        Candidate("fakeyMcfakerson@fakeurl")
