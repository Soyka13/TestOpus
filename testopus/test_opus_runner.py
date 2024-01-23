from testopus.test_loader.loader import TestLoader
from testopus.test_executor.executor import TestExecutor
from testopus.test_reporter.reporter import TestReporter
from testopus.config.config import Config


class TestOpusRunner:

    def __init__(self, config: Config):
        self.config = config

    def run(self):
        # Load
        loader = TestLoader(self.config)
        suit = loader.load()

        # Execute
        if suit is None:
            return
        executor = TestExecutor()
        result = executor.run(suit)

        # Report
        if result is None:
            return
        reporter = TestReporter(self.config, result)
        reporter.report()
