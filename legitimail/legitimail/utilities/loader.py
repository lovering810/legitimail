import importlib.util
import logging
import sys
from pathlib import Path

FILTER_DIR = Path(__file__).parents[1] / "filters"


def load_filter_module(
    filter_path: Path
):
    """Given filter name try to retrieve and load a module from file.

    Args:
    filter_name: string name of filter to be loaded

    Raises:
    FileNotFoundError: if the module cannot be found on the path
    ImportError: if the module is found on the path, but suffers some kind of
    import error due to malformation.

    Returns:
    module: if a module exists for this field, returns it.
    """
    assert isinstance(filter_path, Path)
    filter_name = filter_path.stem
    logging.debug(f"Filter name: {filter_name}")
    if not filter_path.exists():
        raise FileNotFoundError(
            f"No module for filter {filter_name} (Looked at {filter_path})"
        )
    try:
        logging.debug(f"Trying to import spec from loc {filter_path}")
        module_spec = importlib.util.spec_from_file_location(
            filter_name, filter_path
        )
        logging.debug(f"Found module spec {module_spec}, trying to import")
        module = importlib.util.module_from_spec(spec=module_spec)
        logging.debug(f"Imported module from spec {module}")
        sys.modules[filter_name] = module
        logging.debug(f"Assigned module to sys path at {filter_name}")
        module_spec.loader.exec_module(module)
        logging.debug("Loaded module!")
    except Exception as e:
        raise ImportError(
            f"Could not import {filter_name} from file {filter_path}: {e}"
        )
    return module


def load_all_filters():
    # get all filters (non-__init__ .py files)
    filterfiles = [f for f in filter(
        lambda x: not x.stem.startswith("__"), list(FILTER_DIR.glob('*.py'))
        )]
    logging.debug(f"filterfiles: {filterfiles}")
    successful_filters = []

    for ff in filterfiles:
        logging.debug(f"Trying to load {ff}")
        try:
            load_filter_module(ff)
            successful_filters.append(ff.stem)
        except Exception as e:
            logging.warning(f"Could not load filter: {e}")

    return successful_filters


def load_listed_filters(filter_list):
    successful_filters = []
    for fil in filter_list:
        filter_path = FILTER_DIR / f"{fil}.py"
        try:
            load_filter_module(filter_path)
            successful_filters.append(fil)
        except Exception as e:
            logging.warning(f"Could not load filter: {e}")

    return successful_filters
