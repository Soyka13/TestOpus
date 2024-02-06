class SkipException(Exception):
    def __init__(self, message: str = "Function execution has been skipped."):
        self.message = message
        super().__init__(self.message)

def skip(func):
    def wrapper(*args, **kwargs):
        raise SkipException()
    return wrapper
