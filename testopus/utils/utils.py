from pathlib import Path
from testopus.logger.logger import logger


def dir_exists(path: Path):
    exists = path.exists() and path.is_dir()

    if exists:
        logger.info(f"The directory '{path}' exists.")
    else:
        logger.error(f"The directory '{path}' does not exist. Aborting...")

    return exists
