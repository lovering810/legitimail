from legitimail.filters.domain import Domain
from legitimail.utilities.candidate import Candidate
import pytest
from requests.exceptions import ConnectionError


@pytest.fixture
def domain():
    return Domain()


@pytest.fixture
def good_candidate():
    return Candidate(entry="fakeyMcfakerson@gmail.com")


@pytest.fixture
def nonesuch_domain():
    return Candidate(entry="fakeyMcfakerson@fake.realbad")


def test_happy_domain(domain, good_candidate):
    assert domain.filter(candidate=good_candidate)


def test_bad_domain(domain, nonesuch_domain):

    with pytest.raises(ConnectionError):
        domain.filter(candidate=nonesuch_domain)
