class SkipException(Exception):
    def __init__(self, message: str = "Function execution has been skipped."):
        self.message = message
        super().__init__(self.message)


class FailureExpectedException(Exception):
    def __init__(self, message: str = "Failure expected during function execution."):
        self.message = message
        super().__init__(self.message)


def skip(func):
    def wrapper(*args, **kwargs):
        raise SkipException()
    return wrapper


def failure_expected(func):
    def wrapper(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except Exception as e:
            error_string = f"{type(e).__name__}: {e}"
            raise FailureExpectedException(message=error_string)
    return wrapper
