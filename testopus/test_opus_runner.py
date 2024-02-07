from testopus.loader.test_case_loader import TestCaseLoader
from testopus.loader.test_loader import TestLoader
from testopus.executor.executor import TestExecutor
from testopus.reporter.reporter import TestReporter
from testopus.config.config import Config


class TestOpusRunner:
    """
    Orchestrates the loading, execution and reporting of test cases.
    """

    def __init__(self, config: Config):
        self.config = config

    def run(self):
        # Load
        loader = TestLoader(self.config, test_case_loader=TestCaseLoader(config=self.config))
        suit = loader.load()

        # Execute
        executor = TestExecutor()
        result = executor.run(suit)

        # Report
        reporter = TestReporter(self.config, result)
        reporter.report()
