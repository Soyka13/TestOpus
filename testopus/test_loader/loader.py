import unittest
from itertools import product

from testopus.config.config import Config
from testopus.logger.logger import logger
from testopus.utils.utils import dir_exists, absolute_path


class TestLoader:

    def __init__(self, config: Config):
        self.config = config

    def load(self):
        full_search_path = absolute_path(self.config.search_path)

        logger.info(f"Discovering tests at {full_search_path}.")

        if not dir_exists(full_search_path):
            return

        loader = unittest.TestLoader()
        suite = unittest.TestSuite()

        for test_case_rule, unit_test_rule \
                in product(self.config.test_case_name_rules, self.config.unit_test_name_rules):
            loader.testMethodPrefix = unit_test_rule
            tests = loader.discover(full_search_path, pattern=test_case_rule)
            suite.addTests(tests)

        number_of_test_cases = suite.countTestCases()

        logger.info(
            f"There {'is' if number_of_test_cases == 1 else 'are'} {number_of_test_cases} "
            f"test {'case' if number_of_test_cases == 1 else 'cases'} in the given directory.")
        return suite
