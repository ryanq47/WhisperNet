from DataEngine.SimpleC2DbHandler import SimpleC2DbHandler

import os

''' Imports
Go ahead and define any other imports you may need here.

'''
import logging
import inspect
from flask import request
#from flask_login import LoginManager, login_required
import requests
import json

## API stuff
from functools import wraps
from flask import request, jsonify, make_response
from flask_jwt_extended import get_jwt_identity, jwt_required
from Utils.ApiHelper import api_response
from werkzeug.exceptions import BadRequest
from DataEngine.Neo4jHandler import Neo4jConnection
from Utils.Logger import LoggingSingleton
from PluginEngine.ControlPlugins.SimpleC2Plugin.Utils.ListenerHandler import HttpListenerHandler
from Utils.DataSingleton import Data
from PluginEngine.ControlPlugins.SyncPlugin.Modules.SyncHandler import SyncHandler
from Utils.ApiHelper import api_response
################################################
# Info clas
################################################
'''Info class
Fill in your info for the plugin here. This is defined near the top, so it's accessible
by anything that may need it.

'''
class Info:
    name    = "Sync"
    author  = "ryanq47"
    endpoint = "/sync"
    classname = "Sync"
    plugin_type = "Builtin"
    #dashboard = True

class Sync():
    def __init__(self, app):
        self.logger = LoggingSingleton.get_logger()
        self.data = Data()
        self.app = app

################################################
# Main Stuff
################################################

    def main(self):
        '''
        Main function/entry point for the plugin.
        '''
        self.logger.debug(f"{inspect.stack()[0][3]}")
        self.logger.debug(f"Loading {Info.name}")
        self.register_routes()

    ## Put all the routes here.
    def register_routes(self):
        self.logger.debug(f"{inspect.stack()[0][3]}")
        self.app.route(f'/api/{Info.endpoint}', methods = ["POST"])(self.handle_sync_request)


    def handle_sync_request(self):
        """
        Handle a synchronous JSON request by parsing it and processing through SyncHandler.
        """

        ## Check if the request is JSON
        if not request.is_json:
            return "Request data is not JSON", 400

        ## Get JSON data from the request
        try:
            response = request.get_json()
        except Exception as e:
            return f"Error parsing JSON: {e}", 400

        ## Parse JSON using SyncHandler
        synchandler = SyncHandler()
        synchandler.parse_response(response=response)

        #return make_response("success", 200)
        # replace with typical make response
        #return api_response(status_code=400)
        return api_response(status_code=200, status="success")
        #return "Request processed successfully", 200

