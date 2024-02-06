from testopus.arguments_parser.argument_parser_builder import ArgumentParserBuilder
from testopus.test_opus_runner import TestOpusRunner
from testopus.config.config_loader import ConfigLoader

from testopus.loader.test_loader import TestLoader
from testopus.loader.test_case_loader import TestCaseLoader


if __name__ == "__main__":
    # Setup argument parser
    parser = ArgumentParserBuilder.build()
    args = parser.parse_args()

    # Load configuration
    cfg = ConfigLoader.load(args.config)

    # Run
    runner = TestOpusRunner(config=cfg)
    runner.run()
