from legitimail.filters.domain import Domain
from legitimail.utilities.candidate import Candidate
import pytest


@pytest.fixture
def domain():
    return Domain()


@pytest.fixture
def good_candidate():
    return Candidate(entry="lovering810@gmail.com")


def test_happy_candidate_domain(domain, good_candidate):
    assert domain.filter(candidate=good_candidate)
