import unittest
import time
from testopus.test_executor.tests_model import TOTestItem, TOTestsModel


class TOTestResult(unittest.TextTestResult):
    def __init__(self, stream, descriptions, verbosity):
        super().__init__(stream, descriptions, verbosity)
        self.test_models = []
        self.start_time = None

    def startTestRun(self):
        self.start_time = time.time()

    def addSuccess(self, test):
        super().addSuccess(test)
        self._add_test_item(test, succeeded=True)

    def addFailure(self, test, err):
        super().addFailure(test, err)
        exception_type, exception_instance, _ = err
        error_string = f"{exception_type.__name__}: {exception_instance}"
        self._add_test_item(test, succeeded=False, error=error_string)

    def addError(self, test, err):
        super().addError(test, err)
        exception_type, exception_instance, _ = err
        error_string = f"{exception_type.__name__}: {exception_instance}"
        self._add_test_item(test, succeeded=False, error=error_string)

    def printErrors(self):
        return

    def printErrorList(self, flavour, errors):
        return

    def get_tests_model(self):
        return TOTestsModel(self.test_models)

    def _add_test_item(self, test, succeeded, error=None):
        duration = time.time() - self.start_time
        test_name = self.getDescription(test)
        test_item = TOTestItem(test_name, duration, succeeded, error or "")
        self.test_models.append(test_item)
