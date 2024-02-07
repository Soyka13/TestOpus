from dataclasses import dataclass
from testopus.report.report_type import ReportType


@dataclass(frozen=True)
class Config:
    """
    Configuration class for test case, unit test and report settings.

    Parameters:
        search_path (str): The path to search for test cases.
        test_case_name_rules ([str]): A list of rules to filter test case names.
        unit_test_name_rules ([str]): A list of rules to filter unit test names.
        should_report (bool): A flag indicating whether to generate a report.
        report_format (ReportType): The type of report to generate.
        should_save_report (bool): A flag indicating whether to save the report.
        report_path (str): The path to save the report.
    """
    search_path: str
    test_case_name_rules: [str]
    unit_test_name_rules: [str]
    should_report: bool
    report_format: ReportType
    should_save_report: bool
    report_path: str
