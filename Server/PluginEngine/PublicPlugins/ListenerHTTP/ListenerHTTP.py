# HTTP listener. Meant to be standalone, most things must be done throgh API calls to it. (ex: no direct neo4j interaction, call the main server api for that.)

import sys
import os
import logging
from types import SimpleNamespace
from flask import jsonify, make_response, Flask, request, redirect, url_for
import inspect
# Scraping one file standalone for now. Public Plugins will still comm over http. 
# Can just adjust imports for standalone mode in a diff file.
#from Utils.Logger import LoggingSingleton
from PluginEngine.PublicPlugins.ListenerHTTP.Utils.Logger import LoggingSingleton
from PluginEngine.PublicPlugins.ListenerHTTP.Utils.DataSingleton import Data
from PluginEngine.PublicPlugins.ListenerHTTP.Utils.ActionLogger import ActionLogger
from PluginEngine.PublicPlugins.ListenerHTTP.Modules.Client import Client
#from PluginEngine.PublicPlugins.ListenerHTTP.Utils.Utils import Standalone
from PluginEngine.PublicPlugins.ListenerHTTP.Modules.SyncHandler import SyncHandler
from PluginEngine.PublicPlugins.ListenerHTTP.Utils.MessageBuilder import api_response, VesselBuilder

class Info:
    name    = "ListenerHTTP"
    author  = "ryanq47"
    endpoint = "/http"
    classname = "ListenerHTTP"
    plugin_type = "Portable"

class ListenerHTTP:
    def __init__(self, app = None, bind_address = None, bind_port = None, nickname = None):
        if __name__ == "__main__":
            self.logger = LoggingSingleton.get_logger(log_level=logging.DEBUG)

        else:
            # needed as the singleton is initialized on the standalone, but is not when run as a plugin. Init takes an extra arg, 
                #as seen above.
            self.logger = LoggingSingleton.get_logger(log_level=logging.DEBUG)

        self.app = app                      # Flask instance for interfacing with flask
        self.bind_address = bind_address    # Listener bind address
        self.bind_port = bind_port          # Listener Bind Port
        self.data_singleton = Data()        # Data Singleton
        self.nickname = nickname            # nickaname of listener
        self.uuid = None                    # UUID of listener - not implemented yet


        #self.client_class_dict = {}

    def main(self):
        '''
        Main function/entry point for the plugin.
        '''
        try:
            #print("INIT FREAKING LIST")
            ## OKAY rework this chain/put in functions?
            self.logger.debug(f"{inspect.stack()[0][3]}")
            self.logger.debug(f"Loading & starting {Info.name}")

            # Load config
            #print("loadign listenre config")
            self.data_singleton.Config.load_config("listener_http_config.yaml")

            # if no flask instance, create one - prolly don't need a sep func for this.
            if self.app == None:
                self.logger.debug(f"App is none, initializing")
                self.app = create_flask_instance()

            # register routes
            self.register_routes()

            # actually start the app
            self.app.run(
                host = self.bind_address,
                port=self.bind_port,
                debug=False
            )

        except Exception as e:
            self.logger.warning(e)

    def register_routes(self):
        self.app.route(f'/', methods = ["GET"])(self.listener_http_base_endpoint)
        self.app.route(f'{Info.endpoint}/post', methods = ["POST"])(self.listener_http_post_endpoint)
        self.app.route(f'{Info.endpoint}/sync', methods = ["POST"])(self.listener_http_sync_endpoint)


    def listener_http_base_endpoint(self):
        return api_response()

    def listener_http_post_endpoint(self):
        '''
            Initial checkin endpoint. Registers client if new ~~, and gives URL for client to use going forward~~

            ONLY used for checking in, and client getting next command. All exfil/responses are sent to the SYNC endpoint. 
        
        '''
        #####
            # New Chain
            # Recieve request
            # Parse request. 
            # Get new item in listener queue (from client class)
            # return response to client.

            # Still need some form of client verification.
        #####

        try:
            data = request.json

            if data is None:
                return jsonify({"error": "Invalid or no JSON received"}), 400

            data_dict = dict(data)

            # move me to UUID
            self.logger.warning("Still Using nickname here, switch to UUID/CID")
            # Fast handling for the ClientInfo type in the vessel
            client_nickname = data_dict["data"]["ClientInfo"]["nickname"]
            #client_uuid = data_dict
            self.logger.info(f"Client connected: {client_nickname}")

            # If client does not exist
            if not self.data_singleton.Clients.check_if_client_exists(client_name=client_nickname):
                self.logger.debug(f"New client: {client_nickname}")
                client_instance = Client(client_nickname)
                #dipshit you're not adding it to current dict
                self.data_singleton.Clients.add_new_client(
                    client_object=client_instance,
                    client_name=client_nickname
                )
            else:
                self.logger.debug(f"Retrieving client instance for: {client_nickname}")
                client_instance = self.data_singleton.Clients.get_client_object(client_name=client_nickname)

            # stores response based on response ID - probably should change to store response?
            client_instance.set_response(response=data_dict)

            # Get next command
            client_command = client_instance.dequeue_command()

            if client_command == None:
                self.logger.debug(f"Client command is None for {client_nickname}")
                # set command as sleep
                #return VesselBuilder.build_prepared_sleep_request(cid=client_nickname)
        

            # Return command to client
            self.logger.debug(f"Responding to client {client_nickname}")

            # move to new build_prepared_request() method
            # Wrap in Vessel key/actions
            data = VesselBuilder.build_vessel(
                actions=[client_command]
            )
            # Add that data to response
            print(f"data > client: {data}")
            return api_response(data=data)
        
        # Error handling - move to config file.

        except KeyError as e:
            
            self.logger.error(f"KeyError: Missing key in data - {str(e)}")
            return api_response(
                status_code=self.data_singleton.Config.get_value("responses.error.status_code"),
                status=self.data_singleton.Config.get_value("responses.error.status"),
                error_message=f"KeyError: Missing key in data - {str(e)}"
            )

            #return jsonify({"error": f"Missing key in data: {str(e)}"}), 400
        
        except Exception as e:
            self.logger.error(f"An error occurred: {str(e)}")
            return api_response(
                status_code=self.data_singleton.Config.get_value("responses.internal_server_error.status_code"),
                status=self.data_singleton.Config.get_value("responses.internal_server_error.status"),
                error_message=f"An error occurred: {str(e)}"
            )
    
    ## sync DOES NOT return any response besides okay/bad.
    def listener_http_sync_endpoint(self):
        """
            End point where server can queue commands for listener/clients. Sync/Ingest endpoint. 

            Uses a modified SyncHandler

        """
        client_address = request.remote_addr
        self.logger.info(f"Received SYNC request from {client_address}")

        ## Check if the request is JSON
        if not request.is_json:
            self.logger.error(f"Request data from {client_address} is not JSON")
            return api_response(
                status_code=self.data_singleton.Config.get_value("responses.error.status_code"),
                status=self.data_singleton.Config.get_value("responses.error.status"),
                error_message=f"Request data from {client_address} is not JSON"
            )

        ## Get JSON data from the request
        try:
            response = request.get_json()

        # 400 error as it's the users problem (probably)
        except Exception as e:
            self.logger.error(f"Error parsing JSON from {client_address}: {e}")
            
            return api_response(
                status_code=self.data_singleton.Config.get_value("responses.error.status_code"),
                status=self.data_singleton.Config.get_value("responses.error.status"),
                error_message=f"Error parsing JSON from {client_address}: {e}"
            )

        ## Parse JSON using SyncHandler
        print(f"================== RESPONSE: {response}")
        synchandler = SyncHandler()
        synchandler.parse_response(response=response)

        # return ok 
        return api_response(
            status_code=self.data_singleton.Config.get_value("responses.success.status_code"),
            status=self.data_singleton.Config.get_value("responses.success.status")
        )
    

def create_flask_instance():
    '''
    Creates a flask instance. Used when the plugin is NOT in standalone mode
    
    '''
    app = Flask("http_listener")
    return app

""" For standalone mode. 
## Standalone mode options
if __name__ == "__main__":
    print(f"Starting {Info.name} in standalone mode.")

    # Do with args later
    app = Flask("http_listener")

    print(f"Hosting on: http://0.0.0.0:1000, ControlServer: 127.0.0.1")
    ## Create flask info

    plugin_instance = ListenerHTTP(
        app = app,
        bind_port=1000,
        bind_address="0.0.0.0"
    )
    plugin_instance.main()
    #plugin_instance.main()
    #app.run(host="0.0.0.0", port="1000", debug=False)
"""