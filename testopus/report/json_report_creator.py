import json
from datetime import datetime
from pathlib import Path

from testopus.report.report_model import TOReportModel
from testopus.report.report_creator import ReportCreator
from testopus.logger.logger import logger
from testopus.utils.utils import dir_exists


class ReportJSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, TOReportModel):
            return {"tests": [
                {
                    "test": test.test_name,
                    "duration": test.duration,
                    "succeeded": test.succeeded,
                    "skipped": test.skipped,
                    "is_failure_expected": test.is_failure_expected,
                    "error": test.error
                } for test in o.tests
            ]}
        return super().default(o)


class JSONReportCreator(ReportCreator):

    def __init__(self, model: TOReportModel):
        self.model = model

    def get_formatted_report(self):
        return json.dumps(self.model, cls=ReportJSONEncoder, indent=4)

    def display(self):
        logger.info(self.get_formatted_report())

    def save(self, path=None):
        if path is None:
            current_directory = Path.cwd()
            path = current_directory / '/reports' / 'json'

        full_path = Path(path).resolve()

        if not dir_exists(full_path):
            return

        logger.info(f"Saving report at {full_path}.")

        file_name = f"Report-{datetime.now().strftime('%Y-%m-%d-%H:%M:%S')}.json"

        report_path = full_path / file_name

        with open(report_path, 'w') as json_file:
            json_file.write(self.get_formatted_report())

        logger.info(f"Report saved to {report_path}")
