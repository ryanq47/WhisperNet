'''

A (kinda shitty/complicated) logging class. Meant to be a singleton

Implement (in __init__)

self.logger = LoggingSingleton.get_logger()
logger.debug("This is a debug message.")

## Messages/Logs look like:
    2024-02-20 18:51:55 - [D] randomclass.__init__ - This is a debug message.
    2024-02-20 18:51:55 - [PLGN] randomclass.my_method - This is a warning message.

## Log Levels: (in order from least, to most severe)
    debug
    info
    error
    warning
    critical

'''

import logging
from colorama import init, Fore, Style
import threading
import inspect

# Initialize colorama
init(autoreset=True)


class LoggingSingleton():
    _logger_instance = None
    # making thread safe if ever needed
    _lock = threading.Lock()

    @classmethod
    def get_logger(cls, name="ApplicationLogger", log_level=logging.DEBUG):
        if cls._logger_instance is None:
            with cls._lock:
                if cls._logger_instance is None:  # Double check locking
                    # If log_level is specified, update the class attribute
                    if log_level is not None:
                        cls._log_level = log_level
                    cls._initialize_logger(name)
        return cls._logger_instance

    @classmethod
    def _initialize_logger(cls, name):
        logger = logging.getLogger(name)
        logger.setLevel(cls._log_level)
        logger.propagate = False

        # Stream Handler with color
        if not logger.hasHandlers():
            stream_handler = logging.StreamHandler()
            stream_handler.setFormatter(
                ColoredSymbolFormatter(
                    '%(asctime)s - %(message)s',
                    '%Y-%m-%d %H:%M:%S'))
            logger.addHandler(stream_handler)

            # File Handler without color
            file_handler = logging.FileHandler('WhisperNetServer.log', 'a')
            file_handler.setFormatter(
                SymbolFormatter(
                    '%(asctime)s - %(message)s',
                    '%Y-%m-%d %H:%M:%S'))
            logger.addHandler(file_handler)

        cls._logger_instance = logger


class ColoredSymbolFormatter(logging.Formatter):
    symbols = {
        logging.DEBUG: Fore.LIGHTBLUE_EX + "[D]",
        logging.INFO: Fore.GREEN + "[*]",
        logging.WARNING: Fore.YELLOW + "[!]",
        logging.ERROR: Fore.LIGHTRED_EX + "[!!]",
        logging.CRITICAL: Fore.MAGENTA + "[! WOAH !]"
    }

    def format(self, record):
        symbol = self.symbols.get(record.levelno, '')

        # Inspect the stack to find the caller's class and function
        stack = inspect.stack()

        # get info from stack frame in inspect module, makes logging easier.
        caller_frame = stack[8]
        frame = caller_frame[0]
        info = inspect.getframeinfo(frame)

        # Extracting class name from the frame
        args, _, _, value_dict = inspect.getargvalues(frame)
        if len(args) and args[0] == 'self':
            class_name = value_dict['self'].__class__.__name__
        else:
            class_name = 'N/A'

        # Updating the message to include class and function name
        record.msg = f"{symbol} {class_name}.{info.function} - {record.msg}{Style.RESET_ALL}"
        return super().format(record)


class SymbolFormatter(logging.Formatter):
    symbols = {
        logging.DEBUG: "[D]",
        logging.INFO: "[*]",
        logging.WARNING: "[!]",
        logging.ERROR: "[!!]",
        logging.CRITICAL: "[! WOAH !]"
    }

    def format(self, record):
        record.msg = f"{self.symbols.get(record.levelno, '')} {record.msg}"
        return super().format(record)
