import argparse


class ArgumentParserBuilder:

    @staticmethod
    def build():
        argument_parser = argparse.ArgumentParser(description="TOTestOpus")

        config_group = argument_parser.add_mutually_exclusive_group(required=False)
        config_group.add_argument("--config", type=str, help="Path to configuration file")

        return argument_parser
