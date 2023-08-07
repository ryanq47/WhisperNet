import os
import logging
from datetime import datetime
import yaml

################
## QOL Functions
################

"""
Desc: A custom encode/decoder for things, with a format try/except block built in.
Some clients send odd characters sometimes so this is a failsafe
"""

## str -> bytes
def str_encode(input, formats=["utf-8", "iso-8859-1", "windows-1252", "ascii"]) -> bytes:
    for format in formats:
        try:
            return input.encode(format)
        except UnicodeEncodeError:
            logging.debug(f"Could not encode bytes to {format}")
        except Exception as e:
            logging.warning(f"ERRMSG: {e}\n")


## bytes -> str
def bytes_decode(input, formats=["utf-8", "iso-8859-1", "windows-1252", "ascii"]) -> str:
    for format in formats:
        try:
            return input.decode(format)
            logging.debug(f"Succesfully decoded bytes to {format}")
        except UnicodeEncodeError:
            logging.debug(f"Could not decode bytes to {format}")
        except Exception as e:
            logging.warning(f"ERRMSG: {e}\n")


def file_check(filepath):
    '''
    Checks for an existance of a file. if it does not exist, it prints a warning to screen
    
    '''
    if not os.path.isfile(filepath):
        logging.warning(f"UtilsHandler.pt (file_check) File not found: {filepath}\n")

def continue_anyways():
    '''
    A little function that propmts the user to continue anyway. Returns true/false. 
    '''
    if input("Enter 'y' to continue execution (high chance of failure), or any other key to exit: ").lower() == "y":
        return True
    else:
        return False


def timestamp() -> str:
    try:
        time = datetime.utcnow()
        return str(time)
    except Exception as e:
        logging.debug(f"[UtilsHandler.timestamp()]: Error with timestamp: {e}")
        return "timestamperr"
    
def yaml_load(yaml_file = None):

    '''Loads yaml. Also allows for "hot" reloads as this loads the yaml file each call
    
    <ignore> geenrate_random_cookie each time a new client joins. AKA edit your yaml code, 
     and at next auth, you'll have new settings applied </ingore>
    '''
    try:
        with open(yaml_file, 'r') as yaml_file:
            yaml_dict_object = yaml.safe_load(yaml_file)
            
    except Exception as e:
        print(f"[Utils.UtilsHandler.yaml_load()] Error loading YAML: {e}")

    return yaml_dict_object