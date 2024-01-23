from testopus.config.config import Config
from testopus.report.report_type import ReportType
from testopus.test_executor.tests_model import TOTestsModel
from testopus.report.json_report_creator import JSONReportCreator


class TestReporter:

    def __init__(self, config: Config, result: TOTestsModel):
        self.config = config
        self.report_creator = None

        match config.report_format:
            case ReportType.json:
                self.reportCreator = JSONReportCreator(result)
            case _:
                # By default, JSON report is created
                self.reportCreator = JSONReportCreator(result)

    def report(self):
        if not self.config.should_report:
            return

        self.reportCreator.display()

        if self.config.should_save_report:
            self.reportCreator.save()
