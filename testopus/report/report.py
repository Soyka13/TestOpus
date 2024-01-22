from dataclasses import dataclass


@dataclass(frozen=True)
class ReportItem:
    test_name: str
    duration: float
    succeeded: bool
    error: str


@dataclass(frozen=True)
class Report:
    tests: [ReportItem]
