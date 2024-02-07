from dataclasses import dataclass


@dataclass(frozen=True)
class TOTest:
    """
    Represents a test object.

    Parameters:
        name (str): The name of the test.
        module_name (str): The name of the module containing the test.
        class_name (str): The name of the class containing the test.
    """
    name: str
    module_name: str
    class_name: str

    def is_member_of_class(self):
        """
        Checks if the test is a member of a class.
        """
        return self.class_name != ""

    """
    Returns the str description of the test.
    """
    def get_description(self):
        return f"{self.name} ({self.module_name}.{self.class_name})"

    def __repr__(self):
        return f"{self.name} ({self.module_name}.{self.class_name})"

    def __str__(self):
        return f"{self.name} ({self.module_name}.{self.class_name})"


@dataclass
class TOTestCase:
    """
    Represents a test case.

    Parameters:
        path (str): The path of the test case.
        tests ([TOTest]): The list of tests in the test case.
    """
    path: str
    tests: list = None

    def __init__(self, path: str, tests: list = None):
        if tests is None:
            tests = []

        if self.tests is None:
            self.tests = tests

        self.path = path
