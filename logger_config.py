
import logging
import os

# Get the current directory
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))

# Create logs directory if it doesn't exist
LOGS_DIR = os.path.join(CURRENT_DIR, "logs")
if not os.path.exists(LOGS_DIR):
    os.makedirs(LOGS_DIR)

# Configure logging format
LOG_FORMAT = '%(asctime)s | %(levelname)s | %(filename)s | %(funcName)s | %(message)s'
LOG_FILE = os.path.join(LOGS_DIR, 'testlogging.log')

# Setup logging configuration
logging.basicConfig(
    level=logging.DEBUG,
    format=LOG_FORMAT,
    handlers=[
        logging.FileHandler(LOG_FILE),
        logging.StreamHandler()  # Also print to console
    ]
)


class LoggerWrapper:
    """
    Wrapper class around logging.Logger that supports multiple arguments
    Allows passing multiple arguments which will be concatenated as strings
    """

    def __init__(self, logger):
        self.logger = logger

    def _format_message(self, *args):
        """
        Format multiple arguments into a single message string

        Args:
            *args: Variable number of arguments to concatenate

        Returns:
            str: Concatenated message
        """
        return ' '.join(str(arg) for arg in args)

    def debug(self, *args):
        """Log a debug message with support for multiple arguments"""
        message = self._format_message(*args)
        self.logger.debug(message, stacklevel=2)

    def info(self, *args):
        """Log an info message with support for multiple arguments"""
        message = self._format_message(*args)
        self.logger.info(message, stacklevel=2)

    def warning(self, *args):
        """Log a warning message with support for multiple arguments"""
        message = self._format_message(*args)
        self.logger.warning(message, stacklevel=2)

    def error(self, *args):
        """Log an error message with support for multiple arguments"""
        message = self._format_message(*args)
        self.logger.error(message, stacklevel=2)

    def critical(self, *args):
        """Log a critical message with support for multiple arguments"""
        message = self._format_message(*args)
        self.logger.critical(message, stacklevel=2)

    # Aliases
    def warn(self, *args):
        """Alias for warning()"""
        self.warning(*args)

    def exception(self, *args):
        """Log an exception with support for multiple arguments"""
        message = self._format_message(*args)
        self.logger.exception(message, stacklevel=2)


def get_logger(module_name):
    """
    Get a logger instance for a specific module with support for multiple arguments

    Args:
        module_name (str): The name of the module using the logger

    Returns:
        LoggerWrapper: Logger wrapper instance configured for the module

    Example:
        logger = get_logger(__name__)
        logger.info("Message", "with", "multiple", "arguments")
        # Output: "Message with multiple arguments"

        logger.info(f"Square of 5 is - ", 25)
        # Output: "Square of 5 is -  25"
    """
    base_logger = logging.getLogger(module_name)
    return LoggerWrapper(base_logger)
