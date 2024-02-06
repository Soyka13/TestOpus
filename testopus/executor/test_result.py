import time
from testopus.report.report_model import TOReportItem, TOReportModel


class TOTestResultHandler:

    def __init__(self):
        self.test_models = []
        self.start_time = None

    def start_test_run(self):
        self.start_time = time.time()

    def add_success(self, test: str):
        self._add_test_item(test, succeeded=True)

    def add_error(self, test: str, err: Exception):
        error_string = f"{type(err).__name__}: {err}"
        self._add_test_item(test, succeeded=False, error=error_string)

    def add_skip(self, test: str):
        self._add_test_item(test, succeeded=False, skipped=True)

    def add_expected_failure(self, test: str, err: Exception):
        error_string = f"{err}"
        self._add_test_item(test, succeeded=False, is_failure_expected=True, error=error_string)

    def get_report_model(self) -> TOReportModel:
        return TOReportModel(self.test_models)

    def _add_test_item(self, test: str, succeeded: bool, skipped: bool = False, is_failure_expected: bool = False,
                       error: str = None):
        duration = time.time() - self.start_time
        test_item = TOReportItem(test, duration, succeeded, skipped, is_failure_expected, error or "")
        self.test_models.append(test_item)
