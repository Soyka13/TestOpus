from pathlib import Path
from testopus.logger.logger import logger


def dir_exists(path: Path) -> bool:
    """
    Checks if the directory specified by the given path exists and logs the result.

    :param path: The path to the directory.
    :type path: Path
    :return: True if the directory exists, False otherwise.
    :rtype: bool
    """
    exists = path.exists() and path.is_dir()

    if exists:
        logger.info(f"The directory '{path}' exists.")
    else:
        logger.error(f"The directory '{path}' does not exist. Aborting...")

    return exists
