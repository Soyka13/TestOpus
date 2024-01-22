from abc import ABC, abstractmethod
from testopus.report.report import Report


class ReportCreator(ABC):
    @abstractmethod
    def __init__(self, report: Report):
        pass

    @abstractmethod
    def get_formatted_report(self):
        pass

    @abstractmethod
    def display(self):
        pass

    @abstractmethod
    def save(self, path):
        pass
