import argparse


class ArgumentParserBuilder:
    """
    A utility class for building argument parsers with common configuration.
    """

    @staticmethod
    def build() -> argparse.ArgumentParser:
        """
        Creates and returns an argument parser with common configurations.
        """
        argument_parser = argparse.ArgumentParser(description="TOTestOpus")

        config_group = argument_parser.add_argument_group()
        config_group.add_argument("--config", type=str, help="Path to configuration file")

        return argument_parser
