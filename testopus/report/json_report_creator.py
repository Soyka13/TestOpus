import json
import os
from datetime import datetime

from testopus.report.report import Report
from testopus.report.report_creator import ReportCreator
from testopus.logger.logger import logger


class ReportEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, Report):
            return {"report_items": [
                {
                    "test": test.test_name,
                    "duration": test.duration,
                    "succeeded": test.succeeded,
                    "error": test.error
                } for test in o.tests
            ]}
        return super().default(o)


class JSONReportCreator(ReportCreator):

    def __init__(self, report: Report):
        self.report = report

    def get_formatted_report(self):
        return json.dumps(self.report, cls=ReportEncoder, indent=4)

    def display(self):
        logger.info(self.get_formatted_report())

    def save(self, path=None):
        if path is None:
            current_directory = os.getcwd()
            path = current_directory + '/reports/json/'

        if not os.path.exists(path):
            os.makedirs(path)

        file_name = f"Report-{datetime.now().strftime("%Y-%m-%d-%H:%M:%S")}.json"

        report_path = path + file_name

        with open(report_path, 'w') as json_file:
            json_file.write(self.get_formatted_report())
        logger.info(f"Report saved to {report_path}")
