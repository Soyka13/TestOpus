class SkipException(Exception):
    """
    Exception raised when function execution is skipped.
    """
    def __init__(self, message: str = "Function execution has been skipped."):
        self.message = message
        super().__init__(self.message)


def skip(func):
    """
    Decorator that raises a SkipException to indicate that function execution has been skipped.
    Use this decorator when you don't want to run a test.
    """
    def wrapper(*args, **kwargs):
        raise SkipException()

    return wrapper
