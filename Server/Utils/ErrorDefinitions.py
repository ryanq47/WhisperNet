import logging
import inspect
import sys
'''

Error Template: 

class GENERAL_ERROR(Exception):
    def __init__(self):
        exc_type, exc_value, exc_traceback = sys.exc_info() ## getting error stuff
        calling_function = inspect.stack()[1][3]            # Get the name of the calling function
        original_error = exc_value
        logging.debug(f"{calling_function}: {original_error}") # dropping error in log
        super().__init__(f"{calling_function}: {original_error}") # printing to screen

'''

'''
NOTE!! These DO NOT inheret anything save for Exception (a python built in - if that fails you have bigger issues). 
This is so that no matter what fails (even the Inhereted classes), this error handler will still run. 
'''

debug_symbol = " -- "

## Error name...... Inherets...
class GENERAL_ERROR(Exception):
    def __init__(self):
        exc_type, exc_value, exc_traceback = sys.exc_info() ## getting error stuff
        calling_function = inspect.stack()[1][3]            # Get the name of the calling function
        original_error = exc_value
        logging.debug(f"\n{debug_symbol}Uh Oh - General Error{debug_symbol}")
        logging.debug(f"{calling_function}: {original_error}") # dropping error in log
        super().__init__(f"{calling_function}: {original_error}") # printing to screen

class FILE_LOAD_ERROR(Exception):
    def __init__(self):
        exc_type, exc_value, exc_traceback = sys.exc_info() ## getting error stuff
        calling_function = inspect.stack()[1][3]            # Get the name of the calling function
        original_error = exc_value
        logging.debug(f"\n{debug_symbol}Uh Oh - A File failed to load{debug_symbol}")
        logging.debug(f"{calling_function}: {original_error}") # dropping error in log
        super().__init__(f"{calling_function}: {original_error}") # printing to screen

class PROCESS_SPAWN_ERROR(Exception):
    def __init__(self):
        exc_type, exc_value, exc_traceback = sys.exc_info() ## getting error stuff
        calling_function = inspect.stack()[1][3]            # Get the name of the calling function
        original_error = exc_value
        logging.debug(f"\n{debug_symbol}Uh Oh - A Process failed to spawn{debug_symbol}")
        logging.debug(f"{calling_function}: {original_error}") # dropping error in log
        super().__init__(f"{calling_function}: {original_error}") # printing to screen

class INIT_ERROR(Exception):
    def __init__(self):
        exc_type, exc_value, exc_traceback = sys.exc_info() ## getting error stuff
        calling_function = inspect.stack()[1][3]            # Get the name of the calling function
        original_error = exc_value
        logging.debug(f"\n{debug_symbol}Uh Oh - An initialization error has occurred{debug_symbol}")
        logging.debug(f"{calling_function}: {original_error}") # dropping error in log
        super().__init__(f"{calling_function}: {original_error}") # printing to screen

class YAML_LOAD_ERROR(Exception):
    def __init__(self):
        exc_type, exc_value, exc_traceback = sys.exc_info() ## getting error stuff
        calling_function = inspect.stack()[1][3]            # Get the name of the calling function
        original_error = exc_value
        logging.debug(f"\n{debug_symbol}Uh Oh - YAML loading failed{debug_symbol}")
        logging.debug(f"{calling_function}: {original_error}") # dropping error in log
        super().__init__(f"{calling_function}: {original_error}") # printing to screen