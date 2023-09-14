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


## Error name...... Inherets...
class GENERAL_ERROR(Exception):
    def __init__(self):
        exc_type, exc_value, exc_traceback = sys.exc_info() ## getting error stuff
        calling_function = inspect.stack()[1][3]            # Get the name of the calling function
        original_error = exc_value
        logging.debug(f"{calling_function}: {original_error}") # dropping error in log
        super().__init__(f"{calling_function}: {original_error}") # printing to screen

class FILE_LOAD_ERROR(Exception):
    def __init__(self):
        exc_type, exc_value, exc_traceback = sys.exc_info() ## getting error stuff
        calling_function = inspect.stack()[1][3]            # Get the name of the calling function
        original_error = exc_value
        logging.debug(f"{calling_function}: {original_error}") # dropping error in log
        super().__init__(f"{calling_function}: {original_error}") # printing to screen

class PROCESS_SPAWN_ERROR(Exception):
    def __init__(self):
        exc_type, exc_value, exc_traceback = sys.exc_info() ## getting error stuff
        calling_function = inspect.stack()[1][3]            # Get the name of the calling function
        original_error = exc_value
        logging.debug(f"{calling_function}: {original_error}") # dropping error in log
        super().__init__(f"{calling_function}: {original_error}") # printing to screen