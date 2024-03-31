'''

A base class for handling errors

self.logger = LoggingSingleton.get_logger()
logger.debug("This is a debug message.")

'''

import logging
from colorama import init, Fore, Style
import threading

# Initialize colorama
init(autoreset=True)

GLOBAL_LEVEL = logging.DEBUG

# Define a new logging level
PLUGIN_LEVEL = 30
logging.addLevelName(PLUGIN_LEVEL, "FUNCTION")

def plugin(self, message, *args, **kws):
    if self.isEnabledFor(PLUGIN_LEVEL):
        self._log(PLUGIN_LEVEL, message, args, **kws)

# Extend the Logger class with a custom method
logging.Logger.plugin = plugin

class ColoredSymbolFormatter(logging.Formatter):
    symbols = {
        logging.DEBUG: Fore.LIGHTBLUE_EX + "[D]",
        logging.INFO: Fore.GREEN + "[*]",
        logging.WARNING: Fore.YELLOW + "[!]",
        logging.ERROR: Fore.LIGHTRED_EX + "[!!]",
        logging.CRITICAL: Fore.MAGENTA + "[! WOAH !]",
        PLUGIN_LEVEL: Fore.LIGHTCYAN_EX + "[PLGN]"
    }

    def format(self, record):
        symbol = self.symbols.get(record.levelno, '')
        record.msg = f"{symbol} {record.msg}{Style.RESET_ALL}"
        return super().format(record)

class SymbolFormatter(logging.Formatter):
    symbols = {
        logging.DEBUG: "[D]",
        logging.INFO: "[*]",
        logging.WARNING: "[!]",
        logging.ERROR: "[!!]",
        logging.CRITICAL: "[! WOAH !]",
        PLUGIN_LEVEL: "[PLGN]"
    }

    def format(self, record):
        record.msg = f"{self.symbols.get(record.levelno, '')} {record.msg}"
        return super().format(record)

class BaseLogging:
    _logger_instance = None
    ## making thread safe if ever needed
    _lock = threading.Lock()

    @classmethod
    def get_logger(cls, name="ApplicationLogger"):
        if cls._logger_instance is None:
            with cls._lock:
                if cls._logger_instance is None:  # Double check locking
                    cls._initialize_logger(name)
        return cls._logger_instance

    @classmethod
    def _initialize_logger(cls, name):
        logger = logging.getLogger(name)
        logger.setLevel(GLOBAL_LEVEL)
        logger.propagate = False

        # Add custom logging levels as methods to the logger
        setattr(logger, 'function', lambda message, *args: logger._log(PLUGIN_LEVEL, message, args))

        # Stream Handler with color
        if not logger.hasHandlers():
            stream_handler = logging.StreamHandler()
            stream_handler.setFormatter(ColoredSymbolFormatter('%(asctime)s - %(message)s', '%Y-%m-%d %H:%M:%S'))
            logger.addHandler(stream_handler)

            # File Handler without color
            file_handler = logging.FileHandler('server.log', 'a')
            file_handler.setFormatter(SymbolFormatter('%(asctime)s - %(message)s', '%Y-%m-%d %H:%M:%S'))
            logger.addHandler(file_handler)

        cls._logger_instance = logger




''' OLD
import logging

class BaseLogging():
    # child classes will have to call super().__init__() to access/run this correctly
    def __init__(self):
        # The symbol used directly after calling functions, immensely helpful for dev
        self.function_debug_symbol = "[^]"
        #for each debugging level...
        self.logging_warning_symbol = "[!]"
        self.logging_critical_symbol = "[!!]"
        self.logging_error_symbol = "[!!]"
        self.logging_info_symbol = "[*]"
        self.logging_debug_symbol = "[D]"

        ## Exists so this can be changed if necessary
        self.log_file_name = "server.log"
        ## This will need to be adjusted on all modules/code that inheretes this
        self.logger = logging.getLogger()
        ## Change me to logging.DEBUG for a shitload of DEBUG messages
        logging.basicConfig(level=logging.DEBUG)
        logging.basicConfig(filename=self.log_file_name, filemode='a',
                            format='%(asctime)s - %(levelname)s - %(message)s',
                            force=True, datefmt='%Y-%m-%d %H:%M:%S')

        self.logger.addHandler(logging.StreamHandler())
        #logging.debug("BASELOGGING INIT")

'''
