import os
from pathlib import Path


def get_path_current_working_directory() -> Path:
    """
    Gets the current working directory using pathlib.
    :return:
    """
    return Path.cwd()

def get_path(path: str) -> Path:
    """
    Gets the path of the given path.
    :param path:
    :return:
    """
    return Path(os.path.abspath(path))

def get_current_working_directory() -> Path:
    """
    Gets the current working directory using os.path.abspath.
    :return:
    """
    return Path(os.path.abspath(''))