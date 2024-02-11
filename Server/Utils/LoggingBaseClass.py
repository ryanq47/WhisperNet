'''

A base class for handling errors


Shitty docs time:

This is meant to be inhereted:

class AuthenticationPlugin(BasePlugin, BaseLogging):
    def __init__(self, app, DataStruct):

        ## Initialize BasePlugin and BaseLogging parent classes. Can't use one super call as stuff gets fucked up
        BasePlugin.__init__(self, app, DataStruct)
        BaseLogging.__init__(self)  


From here, call self.logger.whatever to log. DO NOT call logging.whatever as that will create a NEW LOGGER that is NOT correctly formatted. Shitty docs over

'''

import logging
from colorama import init, Fore, Style

# Initialize colorama
init(autoreset=True)

GLOBAL_LEVEL = logging.DEBUG

## lower than debug
PLUGIN_LEVEL = 30
logging.addLevelName(PLUGIN_LEVEL, "FUNCTION")

def plugin(self, message, *args, **kws):
    if self.isEnabledFor(PLUGIN_LEVEL):
        self._log(PLUGIN_LEVEL, message, args, **kws)

# Add the function method to logging.Logger class
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
    def __init__(self, name=None):
        logger_name = name if name else self.__class__.__name__
        self.logger = logging.getLogger(logger_name)
        self.logger.setLevel(GLOBAL_LEVEL)

        setattr(self.logger, 'function', lambda message, *args: self.logger._log(PLUGIN_LEVEL, message, args))

        #unused, here until I clean up old log statements
        self.function_debug_symbol = ""
        #for each debugging level...
        self.logging_warning_symbol = ""
        self.logging_critical_symbol = ""
        self.logging_error_symbol = ""
        self.logging_info_symbol = ""
        self.logging_debug_symbol = ""

        if not self.logger.hasHandlers():
            # Stream Handler with color
            stream_handler = logging.StreamHandler()
            stream_handler.setFormatter(ColoredSymbolFormatter('%(asctime)s - %(message)s', '%Y-%m-%d %H:%M:%S'))
            self.logger.addHandler(stream_handler)

            # File Handler without color
            file_handler = logging.FileHandler('server.log', 'a')
            file_handler.setFormatter(SymbolFormatter('%(asctime)s - %(message)s', '%Y-%m-%d %H:%M:%S'))
            self.logger.addHandler(file_handler)




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