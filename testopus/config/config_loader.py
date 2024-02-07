import json
from testopus.config.config import Config
from testopus.report.report_type import ReportType
from testopus.logger.logger import logger

_DEFAULT_CONFIG_PATH = "testopus/default_config.json"


class ConfigLoader:
    """
    Loads configuration settings from a JSON file.
    """

    @staticmethod
    def load(path=None):
        """
        Loads configuration settings from the specified JSON file path.
        """

        if path is None:
            path = _DEFAULT_CONFIG_PATH

        try:
            with open(path, 'r') as file:
                json_data = json.load(file)

            cfg = Config(
                search_path=json_data.get('search_path', ''),
                test_case_name_rules=json_data.get('test_case_name_rules', ["*"]),
                unit_test_name_rules=json_data.get('unit_test_name_rules', ["test"]),
                should_report=json_data.get('should_report', True),
                report_format=ReportType(value=json_data.get('report_format', 'json')),
                should_save_report=json_data.get('should_save_report', False),
                report_path=json_data.get('report_path', '')
            )

            return cfg

        except FileNotFoundError:
            logger.error(f"File not found: {path}")
            return None

        except json.JSONDecodeError:
            logger.error(f"Error decoding JSON in file: {path}")
            return None

        except Exception as e:
            logger.error(f"An unexpected error occurred: {str(e)}")
            return None
