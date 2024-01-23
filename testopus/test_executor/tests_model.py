from dataclasses import dataclass


@dataclass(frozen=True)
class TOTestItem:
    test_name: str
    duration: float
    succeeded: bool
    error: str


@dataclass(frozen=True)
class TOTestsModel:
    tests: [TOTestItem]
