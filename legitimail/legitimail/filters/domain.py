from legitimail.utilities.filter import Filter
from legitimail.utilities.candidate import Candidate
import requests


class Domain(Filter):

    def __init__(self) -> None:
        super().__init__()

    @staticmethod
    def filter(candidate: Candidate):
        legit = False
        schemata = ["https://", "https://www.", "http://", "http://www."]
        for schema in schemata:
            url = f"{schema}{candidate.domain}"
            if requests.head(url).ok:
                legit = True
        return legit
