from dataclasses import dataclass


@dataclass(frozen=True)
class TOReportItem:
    test_name: str
    duration: float
    succeeded: bool
    skipped: bool
    is_failure_expected: bool
    error: str


@dataclass(frozen=True)
class TOReportModel:
    tests: [TOReportItem]
