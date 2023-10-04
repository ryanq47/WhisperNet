'''

A base class for handling errors
'''
import logging

class BaseLogging():

    # child classes will have to call super().__init__() to access/run this correctly
    def __init__(self):
        self.function_debug_symbol = "[*]"
        ## Exists so this can be changed if necessary
        self.log_file_name = "server.log"
        ## This will need to be adjusted on all modules/code that inheretes this
        self.logger = logging.getLogger()

        logging.basicConfig(level=logging.DEBUG)
        logging.basicConfig(filename=self.log_file_name, filemode='a', 
                            format='%(asctime)s - %(levelname)s - %(message)s', 
                            force=True, datefmt='%Y-%m-%d %H:%M:%S')
        
        self.logger.addHandler(logging.StreamHandler())
        logging.debug("BASELOGGING INIT")

