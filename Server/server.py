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
    from flask import Flask#, jsonify, request, send_from_directory, render_template, Response, redirect
    from flask_jwt_extended import JWTManager#, create_access_token, jwt_required, get_jwt_identity, exceptions
    #from flask_wtf.csrf import CSRFProtect  # Import CSRFProtect
    from flask_login import LoginManager#, UserMixin, login_user, login_required, logout_user, current_user

    # My Modules
    from Utils.Logger import LoggingSingleton
    from Utils.Startup import StartupBanner
    from Utils.DataSingleton import Data
    #import SecurityEngine.AuthenticationHandler
    #import Utils.UtilsHandler
    #import ApiEngine.ConfigHandler
    #import Utils.DataObjects
    #import DataEngine.ServerDataDbHandler
    import DataEngine.Neo4jHandler

    ## Error modules
    #import Utils.ErrorDefinitions
    #from Utils.LoggingBaseClass import BaseLogging

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

## Globals bad. I know
args                = parser.parse_args()
ip                  = args.ip
port                = int(args.port)
quiet               = args.quiet
fileserverport      = args.fileserverport
generate_keys       = args.generatekeys
sys_path = os.path.dirname(os.path.realpath(__file__))
function_debug_symbol = "[^]"


class ControlServer():
    def __init__(self, app):
        super().__init__()
        self.app = app
        self.logger = LoggingSingleton.get_logger(log_level=logging.DEBUG)
        self.load_data()
        self.load_plugins(self.app)
        self.init_routes()
        self.startup_tasks()

    def init_routes(self):
        pass
        #self.app.route("/", methods=["GET"])(self.<FUNC>)

    def load_data(self):
        try:
            self.Data = Data()

            ## Set data items
            self.Data.Paths.users_db_path = "DataBases/users.db"
        except Exception as e:
            self.logger.critical(f"Error loading Data: {e}")

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
                    self.logger.info(f"Loading: {plugin_file}")

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
                            plugin_instance = class_obj(app)

                            # Calling main on the class
                            plugin_instance.main()

                            ## Write to Plugins table
                            
                            ## Need to find way to access said path, somethings fucky wucky
                            p_name = module.Info.name
                            endpoint = module.Info.endpoint
                            author = module.Info.author
                            type = module.Info.plugin_type
                            loaded = 0

                            ## not being used currently. Keeps track of the plugins. Need towipe table b4 doing a load plugins tho
                            ## otherwise you get some annoyign unique constaints for the sqlite db
                            #Data.server_data_db_handler.write_to_plugins_table(p_name, endpoint, author, type, loaded)
                            
                    except ImportError as e:
                        self.logger.warning(f"Error importing module {module_path}: {e}. Plugin has NOT loaded successfully")
                    except AttributeError as e:
                        self.logger.warning(f"AttributeError: {e}")
        self.logger.info("Done Loading Plugins")

    def startup_tasks(self):
        '''
        Any other startup tasks
        '''
        # setup JWT
        self.jwt = JWTManager(self.app)
        ## Try to connect to db (add logic later)
        
        #self.logger.warning("Neo4j disbaled during rebuild - make sure to re-enablle")
        # Temp disabled during rebuild
        neo4j = DataEngine.Neo4jHandler.Neo4jConnection()
        neo4j.test()

        # GOES LAST
        #SecurityEngine.AuthenticationHandler.UserManagement.default_role_check_and_setup()
        StartupBanner.successful_startup_banner(ip=ip, port=port)



if __name__ == "__main__":
    ## Init data structures
    
    ## Debug mode on windows is broken.
    #ControlServer.app.run(host="0.0.0.0", port=5000, debug=False)
        
    # try/except commented out so it will fail & give a stack trace if an exception is not caught elsewhere by the code. 
    #try:
        from waitress import serve
        ## These vars are defined at the top, and in relation to argparse
        print(StartupBanner.startup_banner(ip = ip, port = port, version="??"))


        app = Flask(__name__)

        control_server = ControlServer(app)

        ## JWT stuff
        app.config['JWT_SECRET_KEY'] = 'PLEASECHANGEME'  # Change this to your secret key - also move to a config file

        ## Telling flask to SHYUT UP
        log = logging.getLogger('werkzeug')
        log.setLevel(logging.WARNING)

        app.run(host=ip, port=port, debug=False)

    #except OSError as oe:
    #    print(f"OS Error: {oe}")
    #except Exception as e:
    #    print(f"Server Unknown error: {e}")