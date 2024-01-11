from ..utilities.filter import Filter
from ..utilities.candidate import Candidate
import requests


class Domain(Filter):

    def __init__(self) -> None:
        super().__init__()

    @staticmethod
    def filter(candidate: Candidate):
        return requests.head(candidate.domain).ok
