'''

A base class for handling errors
'''
import logging

class BaseLogging():
    # child classes will have to call super().__init__() to access/run this correctly
    def __init__(self, level = "INFO"):
        # The symbol used directly after calling functions, immensely helpful for dev
        self.function_debug_symbol = "[^]"
        #for each debugging level...
        self.logging_warning_symbol = "[!]"
        self.logging_info_symbol = "[*]"
        self.logging_debug_symbol = "[D]"
        self.quiet = False

        print('init')
        ## Exists so this can be changed if necessary
        self.log_file_name = "plugin.log"
        ## This will need to be adjusted on all modules/code that inheretes this
        self.logger = logging.getLogger()
        ## Change me to logging.DEBUG for a shitload of DEBUG messages
        #logging.basicConfig(level=logging.DEBUG)
        logging.basicConfig(level=logging.DEBUG)
        logging.basicConfig(filename=self.log_file_name, filemode='a', 
                            format='%(asctime)s - %(levelname)s - %(message)s', 
                            force=True, datefmt='%Y-%m-%d %H:%M:%S')
        

        logging.debug("BASELOGGING INIT")
