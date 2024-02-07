from dataclasses import dataclass


@dataclass(frozen=True)
class TOReportItem:
    """
    Represents a report item.

    Parameters:
        test_name (str): The name of the test.
        duration (float): The duration of the test execution.
        succeeded (bool): Indicates whether the test succeeded.
        skipped (bool): Indicates whether the test was skipped.
        is_failure_expected (bool): Indicates whether the test failure was expected.
        error (str): The error message associated with the test, if any.
    """
    test_name: str
    duration: float
    succeeded: bool
    skipped: bool
    is_failure_expected: bool
    error: str


@dataclass(frozen=True)
class TOReportModel:
    """
    Represents a test report model.

    Parameters:
    tests ([TOReportItem]): The list of test report items.
    """
    tests: [TOReportItem]
