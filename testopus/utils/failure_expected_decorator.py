class FailureExpectedException(Exception):
    def __init__(self, message: str = "Failure expected during function execution."):
        self.message = message
        super().__init__(self.message)


def failure_expected(func):
    def wrapper(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except Exception as e:
            error_string = f"{type(e).__name__}: {e}"
            raise FailureExpectedException(message=error_string)
    return wrapper
