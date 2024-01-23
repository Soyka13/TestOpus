from testopus.test_opus_runner import TestOpusRunner
from testopus.config.config import Config

if __name__ == "__main__":
    cfg = Config(search_path="/Users/olenastepaniuk/Desktop/Python/TestOpus/unit_tests/",
                 test_case_name_rules=["*_tests.py", "test_*.py"],
                 unit_test_name_rules=["test", "different"],
                 should_report=True,
                 report_format="json",
                 should_save_report=True,
                 report_path="/Users/olenastepaniuk/Desktop/Python/TestOpus/reports/json/")
    runner = TestOpusRunner(config=cfg)
    runner.run()

    # test_directory = "/Users/olenastepaniuk/Desktop/Python/TestOpus/unit_tests/"
    # test_result = run_tests(test_directory)
    # report = test_result.get_report()
    #
    # json_report_creator = JSONReportCreator(report)
    # json_report_creator.display()
