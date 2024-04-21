# HTTP listener. Meant to be standalone, most things must be done throgh API calls to it. (ex: no direct neo4j interaction, call the main server api for that.)

import sys
import os
import logging
from types import SimpleNamespace
from flask import jsonify, make_response, Flask, request
import inspect

## This section exists to import only specific modules etiher the standalone OR the integrated
## may need. Goal is to minimize imports, and only have it set the import dir.

## Standalone
if __name__ == "__main__":
    print("Standalone Mode")
## Integrated
else:
    ## Hacky little method to keep one import section, but just tell the 
    ## interpreter where to look for these plugins
    current_directory = os.path.dirname(os.path.abspath(__file__))
    print("Integrated mode")
    #("Current directory:", current_directory)

    # Insert this path at the start of the sys.path
    # This ensures that it is the first location Python looks for modules to import
    sys.path.insert(0, current_directory)


from Utils.ActionLogger import ActionLogger
from Utils.Logger import LoggingSingleton
from Modules.Client import Client
from Modules.HTTPJsonRequest import HTTPJsonRequest
from Utils.Utils import Standalone
from Utils.DataSingleton import Data

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
            self.logger = LoggingSingleton.get_logger()

        self.app = app

        self.bind_address = bind_address
        self.bind_port = bind_port
        self.nickname = nickname

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


    def listener_http_post_endpoint(self):
        '''
            Initial checkin endpoint. Registers client if new, and gives URL for client to use going forward

            this function needs to be broken up, into generating a dynamic URL for hte clietns to go to (maybe redirect them - need to think that out) - or just emit this entirely to start
            and get the next command queued for them. 

            For now using a dummy_request
        
        '''

        #####
            ## New Chain
            # Recieve request
            # Parse request. 
            # store request - somewhere
            # Get new item in listener queue (from client class)
            # return response to client.


        #####

        data = request.json

        if data is None:
            return jsonify({"error": "Invalid or no JSON received"}), 400

        data_dict = dict(data)

        ## Check if client exist, 

        ## if not:
            # add to singleton or somewhere with client name
        client_instance = Client(app=self.app, action_logger=ActionLogger())

        client_instance.set_response(response=data_dict)

        # get next command
        client_command = client_instance.dequeue_command()

        # return command to client
        return make_response(jsonify(client_command), 200)
    

        '''

        # Get JSON data
        data = request.json

        if data is None:
            return jsonify({"error": "Invalid or no JSON received"}), 400

        # Convert JSON data to a dictionary
        data_dict = dict(data)
        
        # Optionally, convert to SimpleNamespace for attribute-style access
        data_ns = SimpleNamespace(**data_dict)

        print(data_ns)

        # Example usage of the namespace
        print(data_ns.response_id)  # Access attributes directly
        #print(data_ns.result.data)  # Nested data access

        # Temp here, create response back to client
        dummy_request = HTTPJsonRequest()
        dummy_request.callback.server.hostname = "callbackserver" # pull this from the singleton somehwere
        dummy_request_json = dummy_request.generate_json()

        # send response back
        return make_response(dummy_request_json, 200)
        ## Handling Data - Temp here, move to diff function once the dynamic URL is set/thought about.

        #self.client_checkin_validation("data")
        #return make_response("POST ENDPOINT - JSON HERE", 200)
        '''

    def client_checkin_validation(self):
        pass
        # check if client exists, via query to main server DB

        # if not exists, create in main Server db

        # create class instance
        #new_client = Client(data)

        # add to dict of current clients. key is name
    
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
