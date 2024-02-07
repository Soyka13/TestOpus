from testopus.arguments_parser.argument_parser_builder import ArgumentParserBuilder
from testopus.test_opus_runner import TestOpusRunner
from testopus.config.config_loader import ConfigLoader

if __name__ == "__main__":
    # Setup argument parser
    parser = ArgumentParserBuilder.build()
    args = parser.parse_args()

    # Load configuration
    cfg = ConfigLoader.load(args.config)

    # Run
    runner = TestOpusRunner(config=cfg)
    runner.run()
