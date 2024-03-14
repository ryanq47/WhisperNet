# HTTP listener. Meant to be standalone, most things must be done throgh API calls to it. (ex: no direct neo4j interaction, call the main server api for that.)
from Utils.Logger import LoggingSingleton
from PluginEngine.Plugins.ListenerHTTP.Modules.Client import Client
from flask import jsonify, make_response
import inspect

class Info:
    name    = "ListenerHTTP"
    author  = "ryanq47"
    endpoint = "/http"
    classname = "ListenerHTTP"
    plugin_type = "Portable"


class ListenerHTTP():
    def __init__(self, app):
        self.logger = LoggingSingleton.get_logger()
        self.app = app
        self.client_class_dict = {}

    def main(self):
        '''
        Main function/entry point for the plugin.
        '''
        self.logger.debug(f"{inspect.stack()[0][3]}")
        self.logger.debug(f"Loading {Info.name}")
        self.register_routes()

    def register_routes(self):
        self.app.route(f'{Info.endpoint}/get', methods = ["GET"])(self.listener_http_get_endpoint)
        self.app.route(f'{Info.endpoint}/post', methods = ["POST"])(self.listener_http_post_endpoint)


    def listener_http_get_endpoint(self):
        '''
            Init post endpoint. will be sued for something
        '''

        return make_response("GET ENDPOINT - JSON HERE", 200)


    def listener_http_post_endpoint(self):
        '''
            Initial checkin endpoint. Registers client if new, and gives URL for client to use going forward
        
        '''



        self.client_checkin_validation("data")

        return make_response("POST ENDPOINT - JSON HERE", 200)


    def client_checkin_validation(self):
        pass
        # check if client exists, via query to main server DB

        # if not exists, create in main Server db

        # create class instance
        #new_client = Client(data)

        # add to dict of current clients. key is name