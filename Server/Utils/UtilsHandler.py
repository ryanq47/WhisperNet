import os
import logging
from datetime import datetime
import yaml
#import DataEngine.JsonHandler
import Utils.ErrorDefinitions
import subprocess
import threading
from flask import jsonify
################
## QOL Functions
################

"""
Desc: A custom encode/decoder for things, with a format try/except block built in.
Some clients send odd characters sometimes so this is a failsafe
"""

import logging
import inspect

function_debug_symbol = "[^]"

## str -> bytes
def str_encode(input, formats=["utf-8", "iso-8859-1", "windows-1252", "ascii"]) -> bytes:
    logging.debug(f"{function_debug_symbol} {inspect.stack()[0][3]}")

    for format in formats:
        try:
            return input.encode(format)
        except UnicodeEncodeError:
            logging.debug(f"Could not encode bytes to {format}")
        except Exception as e:
            logging.warning(f"ERRMSG: {e}\n")


## bytes -> str
def bytes_decode(input, formats=["utf-8", "iso-8859-1", "windows-1252", "ascii"]) -> str:
    logging.debug(f"{function_debug_symbol} {inspect.stack()[0][3]}")

    for format in formats:
        try:
            return input.decode(format)
            logging.debug(f"Succesfully decoded bytes to {format}")
        except UnicodeEncodeError:
            logging.debug(f"Could not decode bytes to {format}")
        except Exception as e:
            logging.warning(f"ERRMSG: {e}\n")


def file_check(filepath):
    logging.debug(f"{function_debug_symbol} {inspect.stack()[0][3]}")

    '''
    Checks for an existance of a file. if it does not exist, it prints a warning to screen
    
    '''
    if not os.path.isfile(filepath):
        logging.warning(f"UtilsHandler.pt (file_check) File not found: {filepath}\n")

def continue_anyways():
    logging.debug(f"{function_debug_symbol} {inspect.stack()[0][3]}")

    '''
    A little function that propmts the user to continue anyway. Returns true/false. 
    '''
    if input("Enter 'y' to continue execution (high chance of failure), or any other key to exit: ").lower() == "y":
        return True
    else:
        return False


def timestamp() -> str:
    logging.debug(f"{function_debug_symbol} {inspect.stack()[0][3]}")

    try:
        time = datetime.utcnow()
        return str(time)
    except Exception as e:
        logging.debug(f"[UtilsHandler.timestamp()]: Error with timestamp: {e}")
        return "timestamperr"
    
def yaml_load(yaml_file = None):
    logging.debug(f"{function_debug_symbol} {inspect.stack()[0][3]}")


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


def load_file(current_path, file_path, return_path = True):
    '''
    Used to load files, having one function keeps this consistent

    current_path = the sys_path, or path to the .py files directory where it is being called from.
    Ex:  C:\\Users\\USER\\Documents\\GitHub\\WhisperNet\\Server>

    file_path (str) = The relative path to the file 
    Ex:  Config/ApiSchemas/default.yaml

    return_path (bool): if True, the absolute path of the file will be returned.
    If false, the contents of the file will be returned, Defaults to 'True'

    returns:
        File contents, or An absolute path based on the return_path arg

    '''
    logging.debug(f"{function_debug_symbol} {inspect.stack()[0][3]}")

    ## Replacing \ with / -- not needed
    #current_path = current_path.replace("\\", "/")
    #file_path = file_path.replace("\\", "/")
    # removeing / or \\ from file path if added to make it relative, otehrwise os.path.join thinks its an absolute path
    file_path = file_path.lstrip('/')
    file_path = file_path.lstrip('\\')


    try:
        logging.debug(f"current_path: {current_path}, file_path={file_path}")
        # Combine the current path and file path using os.path.join
        absolute_path = os.path.join(current_path, file_path)
        logging.debug(f"Loading {absolute_path}")

        # Check if the resulting path is within the current directory
        #if not os.path.abspath(absolute_path).startswith(os.path.abspath(current_path)):
            #raise ValueError("File path is outside the current directory.")

        # Check if the file exists
        if not os.path.isfile(absolute_path):
            raise FileNotFoundError(f"File not found at {absolute_path}")

        if return_path:
            return absolute_path

        else:
            # Open and read the file
            with open(absolute_path, 'r') as file:
                file_contents = file.read()
            return file_contents

    except (ValueError, FileNotFoundError):
        raise Utils.ErrorDefinitions.FILE_LOAD_ERROR
    except Exception:
        raise Utils.ErrorDefinitions.GENERAL_ERROR
    
def write_file(current_path, file_path, data):
    '''
    Writes files

    current_path = the sys_path, or path to the .py files directory where it is being called from.
    Ex:  C:\\Users\\USER\\Documents\\GitHub\\WhisperNet\\Server>

    file_path (str) = The relative path to the file 
    Ex:  Config/ApiSchemas/default.yaml

    return_path (bool): if True, the absolute path of the file will be returned.
    If false, the contents of the file will be returned, Defaults to 'True'

    returns:
        File contents, or An absolute path based on the return_path arg

    '''
    logging.debug(f"{function_debug_symbol} {inspect.stack()[0][3]}")

    ## Replacing \ with / -- not needed
    #current_path = current_path.replace("\\", "/")
    #file_path = file_path.replace("\\", "/")
    # removeing / or \\ from file path if added to make it relative, otehrwise os.path.join thinks its an absolute path
    file_path = file_path.lstrip('/')
    file_path = file_path.lstrip('\\')


    try:
        logging.debug(f"current_path: {current_path}, file_path={file_path}")
        # Combine the current path and file path using os.path.join
        absolute_path = os.path.join(current_path, file_path)
        logging.debug(f"Loading {absolute_path}")

        # Check if the resulting path is within the current directory
        #if not os.path.abspath(absolute_path).startswith(os.path.abspath(current_path)):
            #raise ValueError("File path is outside the current directory.")

        # Check if the file exists
        #if not os.path.isfile(absolute_path):
            #raise FileNotFoundError(f"File not found at {absolute_path}")

        # Open and read the file
        with open(absolute_path, 'wb') as file:
            file.write(data)

    except (ValueError, FileNotFoundError):
        raise Utils.ErrorDefinitions.FILE_LOAD_ERROR
    except Exception:
        raise Utils.ErrorDefinitions.GENERAL_ERROR


def process_spawner(path=None, command=None):
    '''
    A dedicated process spawner for the project. This is mainly used for creating listener processes.

    Returns a bool (true on success), but may be expanded to return a dict of the results. 
    
    path: Path of file/executable
        ex: C:\\myshell.exe

    command: Command to run
        ex: myshell.exe --ip 127.0.0.1

    thread: Run said process in a thread

    '''

    try:
        # Run the command and capture stdout and stderr
        completed_process = subprocess.run(
            command,
            shell=False,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            universal_newlines=True  # Use text mode for string output (Python 3.7+)
        )

            # Print stdout and stderr
        #print(completed_process.stdout)
        #print(completed_process.stderr)

        # Check the return code to see if the command was successful
        if completed_process.returncode == 0:
            return True
            #return "spawned successfully"
            #print("Command executed successfully.")
        else:
            return False
            #return "spawned failed"
            #print(f"Command failed with return code {completed_process.returncode}")

    except Exception:
        raise Utils.ErrorDefinitions.PROCESS_SPAWN_ERROR

def threaded_process_spawner(path=None, command=None) -> bool:
    '''
    Spawns a process, in its own thread, and in daemon mode so it closes nicely. This exists for consistency accross the project

    path: Path of file/executable
        ex: C:\\myshell.exe

    command: Command to run
        ex: myshell.exe --ip 127.0.0.1


    returns bool (true for success)

    '''

    try:
        process_thread = threading.Thread(target=process_spawner, args=(path, command,))
        process_thread.daemon = True
        process_thread.start()
        logging.debug(f"[*] Process Started: {command}")
        return True
    
    ## change me to raise
    except Exception:
        raise Utils.ErrorDefinitions.PROCESS_SPAWN_ERROR
    
def api_response(status_code=None, message=None, **kwargs):
    '''
    Helper function to create a response json_str to send back to the user. 
    
    status_code(int): Status code
    message(str): Message to send along with the response
    data(Any): Data to be sent back 
    
    Note! You can include custom keys with kwargs:
    ex:

    return api_response(
        code=200, 
        message="Login successful", 
        data=None,
        access_token=access_token,  ## Kwarg
        error_code="AUTH_FAILURE"## Kwarg
    )

    '''
    response = {
        'status': status_code,
        'message': message
        ## kwargs will get added here, see next line
    }
    # Update the response with any additional keyword arguments
    response.update(kwargs)
    return jsonify(response), status_code