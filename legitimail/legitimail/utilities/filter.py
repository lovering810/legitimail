from .candidate import Candidate


class Filter:

    def __init__(self, filter_fn: callable) -> None:
        self.filter = filter_fn

    def filter(self, candidate: Candidate):
        raise NotImplementedError()
