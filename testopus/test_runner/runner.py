import sys
import unittest
from datetime import datetime

from testopus.logger.logger import logger
from testopus.test_runner.test_result import TOTestResult


class TestRunner:

    def run_tests(self, test_path=".", test_pattern="test", test_case_pattern="*_tests.py"):
        test_suite = self._discover_tests(test_path, test_pattern, test_case_pattern)

        if test_suite.countTestCases() == 0:
            logger.info("No tests found, aborting...")
            return

        runner = unittest.TextTestRunner(resultclass=TOTestResult)
        logger.info(f"Test execution started at {datetime.now()}.")
        result = runner.run(test_suite)
        logger.info(f"Test execution ended at {datetime.now()}.")
        return result

    @staticmethod
    def _discover_tests(test_path: str, test_pattern: str, test_case_pattern: str):
        logger.info(f"Discovering tests at {test_path}.")
        loader = unittest.TestLoader()
        loader.testMethodPrefix = test_pattern
        suite = loader.discover(test_path, pattern=test_case_pattern)
        number_of_test_cases = suite.countTestCases()
        logger.info(
            f"There {'is' if number_of_test_cases == 1 else 'are'} {number_of_test_cases} "
            f"test {'case' if number_of_test_cases == 1 else 'cases'} in the given directory.")
        return suite






