import re
import logging


class Candidate:

    def __init__(self, entry: str):
        if not self.validate_string(entry=entry):
            raise AttributeError()
        self.entry = entry
        self.name, self.domain = self.entry.split("@")
        self.results = []

    @classmethod
    def from_string(cls, entry: str):
        try:
            return Candidate(entry=entry)
        except AttributeError:
            logging.debug(f"Submitted entry ({entry}) invalid")

    @staticmethod
    def validate_string(entry: str):
        # regex for syntax - ganked, not generated, probably very rudimentary
        email_regex = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b"
        return re.fullmatch(email_regex, entry)

    def assess(self):
        # this is where we look at what the filters have given us back and
        # determine if this is a Real Person
        raise NotImplementedError()
