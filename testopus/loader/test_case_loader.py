import os
import glob

from testopus.config.config import Config
from testopus.logger.logger import logger


class TestCaseLoader:

    def __init__(self, config: Config):
        self.config = config

    def load(self):
        logger.info(f"Discovering test cases at {os.path.abspath(self.config.search_path)}.")

        matching_files = []

        for rule in self.config.test_case_name_rules:
            path = self.__full_path(rule)
            matching_files.extend(glob.glob(path, recursive=True))

        return matching_files

    def __full_path(self, rule):
        directory_path = os.path.abspath(self.config.search_path)
        return os.path.join(directory_path, '**', rule)
