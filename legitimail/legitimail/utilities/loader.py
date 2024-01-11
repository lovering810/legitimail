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
    filter_name = filter_path.stem()
    if not filter_path.exists():
        raise FileNotFoundError(
            f"No module for filter {filter_name} (Looked at {filter_path})"
        )
    try:
        module_spec = importlib.util.spec_from_file_location(
            filter_name, filter_path
        )
        module = importlib.util.module_from_spec(spec=module_spec)
        sys.modules[filter_name] = module
        module_spec.loader.exec_module(module)
    except Exception as e:
        raise ImportError(
            f"Could not import {filter_name} from file {filter_path}: {e}"
        )
    return module


def load_all_filters():
    # get all filters (non-__init__ .py files)
    filterfiles = filter(
        lambda x: not x.startswith("__"), list(FILTER_DIR.glob('*.py'))
        )
    successful_filters = []
    for ff in filterfiles:
        logging.debug(f"Trying to load {ff.name}")
        try:
            load_filter_module(ff)
            successful_filters.append(ff.stem())
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
