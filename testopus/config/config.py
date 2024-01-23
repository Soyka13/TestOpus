from dataclasses import dataclass
from testopus.report.report_type import ReportType


@dataclass(frozen=True)
class Config:
    search_path: str
    test_case_name_rules: [str]
    unit_test_name_rules: [str]
    should_report: bool
    report_format: ReportType
    should_save_report: bool
    report_path: str
