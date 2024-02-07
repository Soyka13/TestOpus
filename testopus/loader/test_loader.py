import ast
import inspect

from testopus.config.config import Config
from testopus.loader.test_case_loader import TestCaseLoader
from testopus.loader.test_case_model import *
from testopus.logger.logger import logger


class TestLoader:
    """
    Loads test cases and their associated tests based on configuration settings.
    """
    def __init__(self, config: Config, test_case_loader: TestCaseLoader):
        self.config = config
        self.test_case_loader = test_case_loader

    def load(self) -> [TOTestCase]:
        """
        Discovers and returns the test cases and their associated tests based on the configuration.
        """

        # Load file paths
        files = self.test_case_loader.load()
        test_cases = []

        for file_path in files:
            logger.info(f"Discovering tests at {file_path}")

            test_case = TOTestCase(path=file_path)

            with open(file_path, 'r') as file:
                code = file.read()
                # Parse the code into an abstract syntax tree (AST)
                tree = ast.parse(code, filename=file_path)

                # Traverse the AST nodes
                for node in ast.walk(tree):
                    for rule in self.config.unit_test_name_rules:
                        if isinstance(node, ast.ClassDef):
                            class_name = node.name
                        # Create a test object if the node matches the rule
                        elif isinstance(node, ast.FunctionDef) and node.name.startswith(rule):
                            test = TOTest(name=node.name, module_name=inspect.getmodulename(file_path) or "",
                                          class_name=class_name or "")
                            test_case.tests.append(test)
            test_cases.append(test_case)
        return test_cases
