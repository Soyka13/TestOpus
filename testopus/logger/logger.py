import logging
from enum import Enum, auto


class Colors(Enum):
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD_RED = '\033[91;1m'
    RESET = '\033[0m'


class DefaultFormatter(logging.Formatter):
    """
    Custom log formatter with default formatting and colorized output.
    """

    LOG_COLORS = {
        'DEBUG': Colors.BLUE.value,
        'INFO': Colors.GREEN.value,
        'WARNING': Colors.YELLOW.value,
        'ERROR': Colors.RED.value,
        'CRITICAL': Colors.BOLD_RED.value
    }

    def __init__(self):
        super().__init__(fmt='%(asctime)s [%(levelname)s] [%(filename)s:%(lineno)d] %(message)s',
                         datefmt='%Y-%m-%d %H:%M:%S')

    def format(self, record):
        """
        Formats the log record, applying color based on log level.
        """
        log_message = super().format(record)

        log_level = record.levelname
        color = self.LOG_COLORS.get(log_level, Colors.RESET.value)

        formatted_message = f'{color}{log_message}{Colors.RESET.value}'
        return formatted_message


class TOLogger(logging.Logger):
    """
    Custom logger with a default formatter.
    """
    def __init__(self, name, level=logging.NOTSET, formatter=None):
        super().__init__(name, level)

        if formatter is None:
            formatter = DefaultFormatter()

        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        self.addHandler(console_handler)


# Global instance of a TOLogger
logger = TOLogger('com.TestOpus.TOLogger')
