#!/bin/python3
try:
    import subprocess
    import socket
    import threading
    import os
    import random
    import atexit
    from datetime import datetime, timezone
    import logging
    import argparse
    import threading
    import traceback
    import ssl
    import inspect
    import random
    import importlib
    from flask import Flask, jsonify, request, send_from_directory, render_template, Response, redirect
    from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity, exceptions
    #from flask_wtf.csrf import CSRFProtect  # Import CSRFProtect
    from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user

    # My Modules
    import SecurityEngine.AuthenticationHandler
    import Utils.UtilsHandler
    import ApiEngine.ConfigHandler
    import Utils.DataObjects
    import DataEngine.ServerDataDbHandler
    import DataEngine.Neo4jHandler

    ## Error modules
    import Utils.ErrorDefinitions
    from Utils.LoggingBaseClass import BaseLogging

except Exception as e:
    print(f"[server.py] Import Error: {e}")
    exit()


login_manager = LoginManager()

"""
Argparse settings first in order to be able to change anything
"""
parser = argparse.ArgumentParser()
parser.add_argument('--ip', help="The IP to listen on (0.0.0.0 is a good default", required=True)
parser.add_argument('--port', help="The port to listen on", required=True)
parser.add_argument('--quiet', help="No output to console", action='store_true')
parser.add_argument('--fileserverport', help="what port for the file server", default=80)
parser.add_argument('-c', '--generatekeys', help="ReGen Certs & Keys", action="store_true")
#parser.add_argument('--evasionprofile', help="The evasion profile", default="/EvasionProfiles/default.yaml")
#parser.add_argument('--apiconfigprofile', help="The API config profile", default="Config/ApiSchemas/default.yaml")

## Globals bad. I know
args                = parser.parse_args()
ip                  = args.ip
port                = int(args.port)
quiet               = args.quiet
fileserverport      = args.fileserverport
generate_keys       = args.generatekeys
#evasion_profile     = args.evasionprofile
#api_config_profile  = args.apiconfigprofile
sys_path = os.path.dirname(os.path.realpath(__file__))
function_debug_symbol = "[^]"


class Data(BaseLogging):
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
    #self.logger.debug(f'[*] PathStruct.sys_path: {path_struct.sys_path}')

class ControlServer(BaseLogging):
    def __init__(self, app):
        super().__init__()
        self.app = app
        ## this could use a refactor
        self.load_plugins(self.app)
        self.jwt = JWTManager(self.app)
        #self.config_file_path = Utils.UtilsHandler.load_file(current_path=sys_path, file_path=api_config_profile)
        #self.UrlSc = ApiEngine.ConfigHandler.UrlSchema(api_config_profile=self.config_file_path)
        #self.UrlSc.load()
        self.init_routes()
        self.startup_tasks()

    def init_routes(self):
        pass
        #self.app.route("/", methods=["GET"])(self.<FUNC>)

    ## ugly af
    def load_plugins(self, app):
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
                    self.logger.info(f"{self.logging_info_symbol} Discovered: {plugin_file}")

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
                        self.logger.warning(f"{self.logging_warning_symbol} Error importing module {module_path}: {e}")
                    except AttributeError as e:
                        self.logger.warning(f"{self.logging_warning_symbol} AttributeError: {e}")

    def startup_tasks(self):
        '''
        Any other startup tasks
        '''

        ## Try to connect to db (add logic later)
        neo4j = DataEngine.Neo4jHandler.Neo4jConnection()
        neo4j.test()

        # GOES LAST
        SecurityEngine.AuthenticationHandler.UserManagement.default_role_check_and_setup()

        successful_startup_banner()
def startup_banner(ip = None, port = None, version = None):
    #version = "version"
    #ip = "127.0.0.1"
    #port = 5000

    demonsay_list = [
        "~~~shh... blueteam is watching~~~",
        "0x41414141414141414141...",
        "There is no right or wrong, only fun and boring",
        "No place like 127.0.0.1",
        "For legal reasons, this software does not exist"
    ]

    demonsay = random.choice(demonsay_list)

    a = f"""
 __      __.__    .__                             _______          __      _________                                
/  \    /  \  |__ |__| ____________   ___________ \      \   _____/  |_   /   _____/ ______________  __ ___________ 
\   \/\/   /  |  \|  |/  ___/\____ \_/ __ \_  __ \/   |   \_/ __ \   __\  \_____  \_/ __ \_  __ \  \/ // __ \_  __ \\
 \        /|   Y  \  |\___ \ |  |_> >  ___/|  | \/    |    \  ___/|  |    /        \  ___/|  | \/\   /\  ___/|  | \/
  \__/\  / |___|  /__/____  >|   __/ \___  >__|  \____|__  /\___  >__|   /_______  /\___  >__|    \_/  \___  >__|   
       \/       \/        \/ |__|        \/              \/     \/               \/     \/                 \/    

  =================================================================================================================
  <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    V: {version} -- github.com/ryanq47/whispernet
    Author: Ryanq.47                                         |_|      {demonsay}
                                                            ('.') ///   
                                                            <(_)`-/'    
                                                        <-._/J L /  -bf-
    IP: {ip} Port: {port}
    WebInt: http://{ip}:{port}/
  >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
  =================================================================================================================

"""
    
    return a

def successful_startup_banner():
    '''
    Prints if the server successfuly starts. Using global ip & port vars. 
    Yes it's bad. I know
    '''
    banner = f"""
===============================================
Server has successfuly started on: {ip}:{port}
===============================================
"""
    print(banner)

if __name__ == "__main__":
    ## Init data structures

    Data()
    
    ## Debug mode on windows is broken.
    #ControlServer.app.run(host="0.0.0.0", port=5000, debug=False)
    try:
        ## These vars are defined at the top, and in relation to argparse
        print(startup_banner(ip = ip, port = port, version="??"))

        from waitress import serve

        app = Flask(__name__)

        control_server = ControlServer(app)
        #serve(app, host=ip, port=port)
        app.secret_key = 'notasecretkey'

        ## Web Based login

        login_manager.init_app(app)

        ## JWT stuff
        app.config['JWT_SECRET_KEY'] = 'PLEASECHANGEME'  # Change this to your secret key - also move to a config file

        ## Telling flask to SHYUT UP
        log = logging.getLogger('werkzeug')
        log.setLevel(logging.WARNING)

        app.run(host="0.0.0.0", port=5000, debug=False)

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