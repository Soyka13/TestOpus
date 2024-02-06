from dataclasses import dataclass


@dataclass(frozen=True)
class TOTest:
    name: str
    module_name: str
    class_name: str

    def is_member_of_class(self):
        return self.class_name != ""

    def get_description(self):
        return f"{self.name} ({self.module_name}.{self.class_name})"

    def __repr__(self):
        return f"{self.name} ({self.module_name}.{self.class_name})"

    def __str__(self):
        return f"{self.name} ({self.module_name}.{self.class_name})"


@dataclass
class TOTestCase:
    path: str
    tests: list = None

    def __init__(self, path: str, tests=None):
        if tests is None:
            tests = []

        if self.tests is None:
            self.tests = tests

        self.path = path
