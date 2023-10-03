#!/bin/python3
try:
    import subprocess
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
    import importlib
    from flask import Flask, jsonify, request, send_from_directory, render_template, Response
    from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity, exceptions


    # My Modules
    #import tcp_listener
    #import DataEngine.JsonHandler as json_parser
    #import DataEngine.JsonHandler
    #import DataEngine.DataDBHandler
    #from DataEngine.RSAEncryptionHandler import Encryptor ##  Not needed, switching to SSL
    #import ClientEngine.ClientHandler
    #import ClientEngine.MaliciousClientHandler
    import SecurityEngine.AuthenticationHandler
    #import Comms.CommsHandler
    import Utils.UtilsHandler
    #import Utils.KeyGen
    import ApiEngine.ConfigHandler
    import Utils.DataObjects
    import DataEngine.ServerDataDbHandler

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
    path_struct.os_type = os.name

    ## DB instance of the ServerData.db
    server_data_db_handler =  DataEngine.ServerDataDbHandler.ServerDataDbHandler()

    ## DataLake?
    '''
    Maybe a db for purely server based stuff. 
    Usecase would be for the stats plugin/having a data pool available for plugins to use

    ## One DB for user/security related items

    ## One DB for Data/Non critical data, so:
        - Plugins loaded
        - Other

    ## Addtitonally, each plugin should/can have its own DB.
    Ideally, this would be stored in the plugin subfolder. BaseClass will need a 
    DB implementation/interface method as well for easy db access.
        
    
    '''

    ## Getting all the paths in the log just in case something fails/is off
    logging.debug(f'[*] PathStruct.sys_path: {path_struct.sys_path}')


def load_plugins(app):
    plugins_root_dir = os.path.join(sys_path, "PluginEngine/Plugins")

    # Iterate over subdirectories (one for each plugin)
    for plugin_folder in os.listdir(plugins_root_dir):
        #print(plugin_folder)
        plugin_folder_path = os.path.join(plugins_root_dir, plugin_folder)

        # Check if it's a directory
        if not os.path.isdir(plugin_folder_path):
            continue

        # Inside each plugin folder, look for Python files with the same name as the folder
        for plugin_file in os.listdir(plugin_folder_path):
            if plugin_file.endswith('.py'):
                print(f"[*] Discovered {plugin_file}")

                plugin_name = plugin_file[:-3]  # Remove the '.py' extension
                module_path = f"PluginEngine.Plugins.{plugin_folder}.{plugin_name}"

                try:
                    module = importlib.import_module(module_path)

                    # Find classes defined in the module
                    classes = inspect.getmembers(module, inspect.isclass)

                    # Look for a class that you want to instantiate
                    for name, class_obj in classes:
                        if name != module.Info.classname:
                            continue

                        # Instantiate the class with 'app' as an argument
                        plugin_instance = class_obj(app, Data)

                        # Calling main on the class
                        plugin_instance.main()

                        ## Write to Plugins table
                        
                        ## Need to find way to access said path, somethings fucky wucky
                        p_name = module.Info.name
                        endpoint = module.Info.endpoint
                        author = module.Info.author
                        type = module.Info.plugin_type
                        loaded = 0

                        Data.server_data_db_handler.write_to_plugins_table(p_name, endpoint, author, type, loaded)
                        

                except ImportError as e:
                    print(f"Error importing module {module_path}: {e}")
                except AttributeError as e:
                    print(f"AttributeError: {e}")

            
## Move to own file eventually
class ControlServer:
    def __init__(self):
        self.app = Flask(__name__)
        load_plugins(self.app)
        self.app.config['JWT_SECRET_KEY'] = 'PLEASECHANGEME'  # Change this to your secret key - also move to a config file
        self.jwt = JWTManager(self.app)
        self.config_file_path = Utils.UtilsHandler.load_file(current_path=sys_path, file_path=api_config_profile)
        self.UrlSc = ApiEngine.ConfigHandler.UrlSchema(api_config_profile=self.config_file_path)
        self.UrlSc.load()
        self.init_routes()


    def init_routes(self):
        self.app.route("/", methods=["GET"])(self.no_subdir)
        self.app.route("/home_base", methods=["GET"])(self.no_subdir)
        self.app.route(f"/{self.UrlSc.AGENT_BASE_ENDPOINT}", methods=["GET"])(self.agent_base)
        self.app.route(f"/{self.UrlSc.SERVER_LOGIN_ENDPOINT}", methods=["POST"])(self.server_login)
        self.app.route(f"/{self.UrlSc.SERVER_BASE_ENDPOINT}", methods=["GET"])(self.server_base)
        self.app.route(f"/{self.UrlSc.UPLOAD_BASE_ENDPOINT}/<path:path>", methods=["GET"])(self.download_file)
        self.app.route(f"/{self.UrlSc.UPLOAD_BASE_ENDPOINT}/<filename>", methods=["POST"])(self.post_file)
        self.app.route(f"/status/listeners", methods=["POST"])(self.status)
        self.app.route('/status')(self.index)

    def no_subdir(self):
        try:
            # Yaml load code here
            ## load random choice from list
            html_file_path = random.choice(self.UrlSc.HOMEPAGE_LIST)

            # open file
            html = Utils.UtilsHandler.load_file(
                current_path = sys_path, 
                file_path = html_file_path, 
                return_path = False )
            # return HTML
            return html
            ## oh my god it worked on the first time

        except Exception:
            self.page_not_found()
    
    ## for agents checking in
    def agent_base(self):
        return "agent_base"
    
    ## login
    def server_login(self):
        username = request.json.get('username')
        password = request.json.get('password')

        ## need a guard statement here to make sure user & pass actually equal something

        if SecurityEngine.AuthenticationHandler.Authentication.authentication_eval(
            username=username,
            password=password,
            path_struct=Data.path_struct
        ):
            access_token = create_access_token(identity="username")
            return {'access_token': access_token}, 200
        else:
            return self.page_not_found()


    # commands to control the server
    @jwt_required()
    def server_base(self):
        try:
            return "server_base"
        except:
            self.page_not_found()
    

    ## File Section
    # https://docs.faculty.ai/user-guide/apis/flask_apis/flask_file_upload_download.html
    # by default, http://ip/files/FILENAME
    def download_file(self, path):
        try:
            ## as attachment downloads it, instead of displaying in browser
            return send_from_directory(self.UrlSc.UPLOAD_FOLDER, path, as_attachment=True)
        except Exception as e:
            #print(e)
            return self.page_not_found()

    @jwt_required()
    def post_file(self, filename):
        """Upload a file."""

        if "/" in filename:
            # Return 400 BAD REQUEST
            return "No Subdirectories allowed", 400
        
        Utils.UtilsHandler.write_file(
            current_path=sys_path,
            file_path=self.UrlSc.UPLOAD_FOLDER + "/" + filename,
            data = request.data
        )

        # Return 201 CREATED
        return "", 201
    def status(self):
        pass
    
    def index(self):
        dummy_json_data = {
            "status": "up",
            "message": "Website is up and running!",
        }

        #path = os.path.join(sys_path, "ApiEngine\html\statuspage\statuspage.html")

        # Render the HTML template with initial JSON data
        return render_template('index.html', json_data=dummy_json_data)

    '''
    ## any bad auth returns this
    @self.app.errorhandler(exceptions.NoAuthorizationError)
    @self.app.errorhandler(401)
    @self.app.errorhandler(403)
    @self.app.errorhandler(404)
    @self.app.errorhandler(405) # Method not allowed'''
    def page_not_found(self, e=None):
        '''
        Handles all 40X & any try/except errors. Basically it returns a 200
        with a "page not found"

        This is done for security/scraping/URL discovery reasons
            
        '''
        try:
            err_404_path = random.choice(self.UrlSc.NOT_FOUND_LIST_404)
            logging.debug(f"Error: {e}")

            html = Utils.UtilsHandler.load_file(
                current_path=sys_path, 
                file_path=err_404_path, 
                return_path=False
            )
            
            resp = Response(html)

            # Set the 'err' cookie with the value of 'e'
            resp.set_cookie('err', str(e))

            return resp, 200
        ## Fallback for if something breaks
        except:
            return "", 200


if __name__ == "__main__":
    ## Init data structures

    Data()
    
    ## Debug mode on windows is broken.
    #ControlServer.app.run(host="0.0.0.0", port=5000, debug=False)
    try:
        from waitress import serve
        control_server = ControlServer()
        #serve(control_server.app, host=ip, port=port)
        control_server.app.run(host="0.0.0.0", port=5000, debug=True)
    except OSError as oe:
        print(f"OS Error: {oe}")
    except Exception as e:
        print(f"Unknown error: {e}")

        


'''
Daemon notes. It runs threads in the background, as long as the program is still executing, i.e. in a loop of some sorts.


Some things to think about.
    - Should the client connect here? This would give it control over each listener, vs controlling one at a time
    - Should I jsut bite the bullet and switch to an API based control scheme?
'''