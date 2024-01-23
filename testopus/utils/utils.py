import os
from testopus.logger.logger import logger


class NullWriter:
    def write(self, *args, **kwargs):
        pass

    def writeln(self, *args, **kwargs):
        pass

    def flush(self, *args, **kwargs):
        pass


def dir_exists(path):
    exists = os.path.exists(path) and os.path.isdir(path)

    if exists:
        logger.info(f"The directory '{path}' exists.")
    else:
        logger.error(f"The directory '{path}' does not exist. Aborting...")

    return exists


def absolute_path(raw_path):
    if os.path.isabs(raw_path):
        # Path is absolute
        return raw_path
    else:
        return os.getcwd() + '/' + raw_path
