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

## stupid way to change this easy
GLOBAL_LEVEL = logging.DEBUG

class SymbolFormatter(logging.Formatter):
    symbols = {
        logging.DEBUG: "[D]",
        logging.INFO: "[*]",
        logging.WARNING: "[!]",
        logging.ERROR: "[!!]",
        logging.CRITICAL: "[!!]"
    }

    def format(self, record):
        record.msg = f"{self.symbols.get(record.levelno, '')} {record.msg}"
        return super().format(record)

class BaseLogging:
    def __init__(self, name=None):

        ## Moving these to nothing until they get cleaned up accross the project
        self.function_debug_symbol = ""
        #for each debugging level...
        self.logging_warning_symbol = ""
        self.logging_critical_symbol = ""
        self.logging_error_symbol = ""
        self.logging_info_symbol = ""
        self.logging_debug_symbol = ""

        # Use the class name as the logger name if not provided
        logger_name = name if name else self.__class__.__name__

        self.logger = logging.getLogger(logger_name)
        self.logger.setLevel(GLOBAL_LEVEL)

        # Check if handlers are already set to avoid duplicates, prevents some weird bugs
        if not self.logger.hasHandlers():
            # Stream Handler
            stream_handler = logging.StreamHandler()
            stream_handler.setFormatter(SymbolFormatter('%(asctime)s - %(message)s', '%Y-%m-%d %H:%M:%S'))
            self.logger.addHandler(stream_handler)

            # File Handler
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