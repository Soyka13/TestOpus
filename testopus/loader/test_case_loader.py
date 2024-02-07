from pathlib import Path
import glob

from testopus.config.config import Config
from testopus.logger.logger import logger
from testopus.utils.utils import dir_exists


class TestCaseLoader:
    """
    Loads test case files based on configuration settings.
    """
    def __init__(self, config: Config):
        self.config = config

    def load(self) -> [str]:
        """
        Discovers and returns the paths of test case files based on the configuration.
        """
        directory_path = Path(self.config.search_path).resolve()
        logger.info(f"Discovering test cases at {directory_path}/")

        if not dir_exists(directory_path):
            return

        matching_files = []

        for rule in self.config.test_case_name_rules:
            path = self.__full_path(directory_path, rule)
            matching_files.extend(glob.glob(str(path), recursive=True))

        return matching_files

    @staticmethod
    def __full_path(directory_path: Path, rule: str) -> Path:
        """
        Constructs the full path for a given rule within the specified directory path.
        """
        return directory_path.joinpath('**', rule).absolute()
