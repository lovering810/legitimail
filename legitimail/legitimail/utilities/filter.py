from .candidate import Candidate


class Filter:

    def __init__(self) -> None:

        pass

    def filter(self, candidate: Candidate):
        raise NotImplementedError()
