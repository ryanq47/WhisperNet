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
# WHY U NO WORK
from PluginEngine.PublicPlugins.ListenerHTTP.Utils.Logger import LoggingSingleton
from PluginEngine.PublicPlugins.ListenerHTTP.Utils.DataSingleton import Data
from PluginEngine.PublicPlugins.ListenerHTTP.Utils.ActionLogger import ActionLogger
from PluginEngine.PublicPlugins.ListenerHTTP.Modules.Client import Client
from PluginEngine.PublicPlugins.ListenerHTTP.Modules.HTTPJsonRequest import HTTPJsonRequest
from PluginEngine.PublicPlugins.ListenerHTTP.Utils.Utils import Standalone
from PluginEngine.PublicPlugins.ListenerHTTP.Modules.SyncHandler import SyncHandler
from PluginEngine.PublicPlugins.ListenerHTTP.Utils.ApiHelper import api_response


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

        self.app = app
        self.bind_address = bind_address
        self.bind_port = bind_port
        self.nickname = nickname
        self.data_singleton = Data()
        self.client_class_dict = {}

    def main(self):
        '''
        Main function/entry point for the plugin.
        '''
        try:
            ## OKAY rework this chain/put in functions?
            self.logger.debug(f"{inspect.stack()[0][3]}")
            self.logger.debug(f"Loading & starting {Info.name}")


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
        self.app.route(f'{Info.endpoint}/get', methods = ["GET"])(self.listener_http_get_endpoint)
        self.app.route(f'{Info.endpoint}/post', methods = ["POST"])(self.listener_http_post_endpoint)
        self.app.route(f'{Info.endpoint}/sync', methods = ["POST"])(self.listener_http_sync_endpoint)


    def listener_http_base_endpoint(self):
        return "base_endpoint"

    def listener_http_get_endpoint(self):
        '''
            Init post endpoint. will be used for something
        '''

        # for now, just returning the mock JSON format
        dummy_request = HTTPJsonRequest()

        dummy_request.callback.server.hostname = "callbackserver" # pull this from the singleton somehwere

        dummy_request_json = dummy_request.generate_json()

        return make_response(dummy_request_json, 200)

        # steps;
            # pop next command for client from client name

    def listener_http_post_endpoint(self):
        '''
            Initial checkin endpoint. Registers client if new ~~, and gives URL for client to use going forward~~

            ONLY used for checking in, and client getting next command. All exfil/responses are sent to the SYNC endpoint. 
        
        '''
        #####
            ## New Chain
            # Recieve request
            # Parse request. 
            # Get new item in listener queue (from client class)
            # return response to client.

            ##Still need some form of client verification.


        #####

        data = request.json

        if data is None:
            return jsonify({"error": "Invalid or no JSON received"}), 400

        data_dict = dict(data)
        print(data_dict)

        # fast handling for the ClientInfo type in the vessel
        client_nickname = data_dict["data"]["ClientInfo"]["nickname"]
        self.logger.info(f"Client connected: {client_nickname}")

        if not self.data_singleton.Clients.check_if_client_exists(client_name=client_nickname):
            self.logger.debug(f"New client: {client_nickname}")
            client_instance = Client(client_nickname)

        client_instance.set_response(response=data_dict)
        # get next command
        client_command = client_instance.dequeue_command()
        # return command to client
        self.logger.debug(f"Responding to client {client_nickname}")
        return make_response(jsonify(client_command), 200)

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
            return "Request data is not JSON", 400

        ## Get JSON data from the request
        try:
            response = request.get_json()
        except Exception as e:
            self.logger.error(f"Error parsing JSON from {client_address}: {e}")
            return f"Error parsing JSON from {client_address}: {e}", 400

        ## Parse JSON using SyncHandler
        synchandler = SyncHandler()
        synchandler.parse_response(response=response)

        # return ok 
        return api_response(status_code=200, status="success")
    


def create_flask_instance():
    '''
    Creates a flask instance. Used when the plugin is NOT in standalone mode
    
    '''
    app = Flask("http_listener")
    return app



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
