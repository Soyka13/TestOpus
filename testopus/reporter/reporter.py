from testopus.config.config import Config
from testopus.report.report_type import ReportType
from testopus.report.report_model import TOReportModel
from testopus.report.json_report_creator import JSONReportCreator


class TestReporter:
    """
    Generates and manages test reports based on the provided configuration and result.
    """
    def __init__(self, config: Config, result: TOReportModel):
        self.config = config
        self.report_creator = None

        match config.report_format:
            case ReportType.json:
                self.reportCreator = JSONReportCreator(result)
            case _:
                # By default, JSON report is created
                self.reportCreator = JSONReportCreator(result)

    def report(self):
        """
        Generates and manages the test report based on the configuration settings.
        """
        if not self.config.should_report:
            return

        self.reportCreator.display()

        if self.config.should_save_report:
            self.reportCreator.save(self.config.report_path)
