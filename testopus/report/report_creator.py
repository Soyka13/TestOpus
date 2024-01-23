from abc import ABC, abstractmethod
from testopus.test_executor.tests_model import TOTestsModel


class ReportCreator(ABC):
    @abstractmethod
    def __init__(self, model: TOTestsModel):
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
