class FailureExpectedException(Exception):
    """
    Exception raised when failure is expected during function execution.
    """
    def __init__(self, message: str = "Failure expected during function execution."):
        self.message = message
        super().__init__(self.message)


def failure_expected(func):
    """
    Decorator that raises a FailureExpectedException with error message if any occurred else empty string.
    Use this decorator when you expect failure in your test.
    """
    def wrapper(*args, **kwargs):
        error_string = ""
        try:
            func(*args, **kwargs)
        except Exception as e:
            error_string = f"{type(e).__name__}: {e}"

        raise FailureExpectedException(message=error_string)
    return wrapper
