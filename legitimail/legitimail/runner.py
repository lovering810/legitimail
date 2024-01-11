from .utilities.candidate import Candidate
from .utilities.loader import load_all_filters, load_listed_filters
from pathlib import Path


def ingest_file(file_loc: Path) -> list[Candidate]:

    raise NotImplementedError("Haven't made this yet")


def assemble_filters(filter_list: list[str] = None) -> list[str]:

    if not filter_list:
        available_filters = load_all_filters()
    else:
        available_filters = load_listed_filters(filter_list=filter_list)
    
    return available_filters


def run(file_loc: str, filter_list: list[str] = None):

    file_loc = Path(file_loc)
    candidates = ingest_file(file_loc=file_loc)
    filters = assemble_filters(filter_list=filter_list)

    # TODO: parallelize, order, consider
    # applying filtration differently - ordered by type of
    # candidate, e.g.
    for candidate in candidates:
        for filt in filters:
            filt.filter(candidate)

    # candidates contain the results of the various filters
    # so we can parse the results post hoc
    return candidates

