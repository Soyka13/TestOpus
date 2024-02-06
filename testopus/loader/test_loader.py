import ast
import inspect

from testopus.config.config import Config
from testopus.loader.test_case_loader import TestCaseLoader
from testopus.loader.test_case_model import *
from testopus.logger.logger import logger


class TestLoader:

    def __init__(self, config: Config, test_case_loader: TestCaseLoader):
        self.config = config
        self.test_case_loader = test_case_loader

    def load(self):
        files = self.test_case_loader.load()
        test_cases = []

        for file_path in files:
            logger.info(f"Discovering tests at {file_path}")

            test_case = TOTestCase(path=file_path)

            with open(file_path, 'r') as file:
                code = file.read()
                tree = ast.parse(code, filename=file_path)

                for node in ast.walk(tree):
                    for rule in self.config.unit_test_name_rules:
                        if isinstance(node, ast.ClassDef):
                            class_name = node.name
                        elif isinstance(node, ast.FunctionDef) and node.name.startswith(rule):
                            test = TOTest(name=node.name, module_name=inspect.getmodulename(file_path) or "",
                                          class_name=class_name or "")
                            test_case.tests.append(test)

            test_cases.append(test_case)
        return test_cases
