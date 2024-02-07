import time
from testopus.report.report_model import TOReportItem, TOReportModel


class TOTestResultHandler:
    """
     Handles the results of test execution and generates a report model.
    """

    def __init__(self):
        self.test_models = []
        self.start_time = None

    def start_test_run(self):
        """
        Sets the start time of the test run.
        """
        self.start_time = time.time()

    def add_success(self, test: str):
        """
        Adds a successful test result.

        :param test: The name of the test.
        :type test: str
        """
        self._add_test_item(test, succeeded=True)

    def add_error(self, test: str, err: Exception):
        """
        Adds an error test result.

        :param test: The name of the test.
        :type test: str

        :param err: The exception occurred during the test.
        :type err: Exception
        """
        error_string = f"{type(err).__name__}: {err}"
        self._add_test_item(test, succeeded=False, error=error_string)

    def add_skip(self, test: str):
        """
        Adds a skipped test result.

        :param test: The name of the test.
        :type test: str
        """
        self._add_test_item(test, succeeded=False, skipped=True)

    def add_expected_failure(self, test: str, err: Exception):
        """
        Adds an expected failure test result.

        :param test: The name of the test.
        :type test: str

        :param err: The exception occurred during the test.
        :type err: Exception
        """
        error_string = f"{err}"
        self._add_test_item(test, succeeded=False, is_failure_expected=True, error=error_string)

    def get_report_model(self) -> TOReportModel:
        """
        Generates and returns the report model.

        :return: The generated report model.
        :rtype: TOReportModel
        """
        return TOReportModel(self.test_models)

    def _add_test_item(self, test: str, succeeded: bool, skipped: bool = False, is_failure_expected: bool = False,
                       error: str = None):
        """
        Adds a test item to the report model.

        :param test: The name of the test.
        :type test: str

        :param succeeded: Flag indicating whether the test succeeded.
        :type succeeded: bool

        :param skipped: Flag indicating whether the test was skipped.
        :type skipped: bool, optional

        :param is_failure_expected: Flag indicating whether the test's failure was expected.
        :type is_failure_expected: bool, optional

        :param error: The error message if the test failed.
        :type error: str, optional
        """
        duration = time.time() - self.start_time
        test_item = TOReportItem(test, duration, succeeded, skipped, is_failure_expected, error or "")
        self.test_models.append(test_item)
