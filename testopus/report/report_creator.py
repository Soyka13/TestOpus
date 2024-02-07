from abc import ABC, abstractmethod
from testopus.report.report_model import TOReportModel


class ReportCreator(ABC):
    """
    Abstract base class for report creators.
    """
    @abstractmethod
    def __init__(self, model: TOReportModel):
        pass

    @abstractmethod
    def get_formatted_report(self) -> str:
        """
        Abstract method to be implemented by subclasses for getting the formatted report.
        """
        pass

    @abstractmethod
    def display(self):
        """
        Abstract method to be implemented by subclasses for displaying the report.
        """
        pass

    @abstractmethod
    def save(self, path: str):
        """
        Abstract method to be implemented by subclasses for saving the report at the given path.

        :param path: The path where the report will be saved.
        :type path: str
        """
        pass
