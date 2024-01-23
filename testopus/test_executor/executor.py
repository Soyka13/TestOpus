import unittest
from datetime import datetime
from itertools import product

from testopus.logger.logger import logger
from testopus.test_executor.test_result import TOTestResult
from testopus.config.config import Config
from testopus.utils.utils import NullWriter


class TestExecutor:

    @staticmethod
    def run(test_suite):
        if test_suite.countTestCases() == 0:
            logger.info("No tests found, aborting...")
            return

        runner = unittest.TextTestRunner(resultclass=TOTestResult)
        # Silence original logs
        runner.stream = NullWriter()

        logger.info(f"Test execution started at {datetime.now()}.")
        result = runner.run(test_suite)
        logger.info(f"Test execution ended at {datetime.now()}.")

        return result.get_tests_model()
