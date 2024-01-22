import datetime
import unittest
import time
from testopus.report.report import ReportItem, Report


class TOTestResult(unittest.TextTestResult):
    def __init__(self, stream, descriptions, verbosity):
        super().__init__(stream, descriptions, verbosity)
        self.report_items = []
        self.start_time = None

    def startTestRun(self):
        self.start_time = time.time()

    def addSuccess(self, test):
        super().addSuccess(test)
        self._add_report_item(test, succeeded=True)

    def addFailure(self, test, err):
        super().addFailure(test, err)
        exception_type, exception_instance, _ = err
        error_string = f"{exception_type.__name__}: {exception_instance}"
        self._add_report_item(test, succeeded=False, error=error_string)

    def addError(self, test, err):
        super().addError(test, err)
        exception_type, exception_instance, _ = err
        error_string = f"{exception_type.__name__}: {exception_instance}"
        self._add_report_item(test, succeeded=False, error=error_string)

    def printErrors(self):
        return

    def printErrorList(self, flavour, errors):
        return

    def get_report(self):
        return Report(self.report_items)

    def _add_report_item(self, test, succeeded, error=None):
        duration = time.time() - self.start_time
        test_name = self.getDescription(test)
        report_item = ReportItem(test_name, duration, succeeded, error or "")
        self.report_items.append(report_item)
