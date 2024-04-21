from DataEngine.SimpleC2DbHandler import SimpleC2DbHandler

import os

''' Imports
Go ahead and define any other imports you may need here.

'''
import logging
import inspect
from flask import jsonify, send_from_directory, redirect, make_response
#from flask_login import LoginManager, login_required
import requests
import json

## API stuff
from functools import wraps
from flask import request, jsonify
from flask_jwt_extended import get_jwt_identity, jwt_required
from Utils.ApiHelper import api_response
from werkzeug.exceptions import BadRequest
from DataEngine.Neo4jHandler import Neo4jConnection
from Utils.Logger import LoggingSingleton
from PluginEngine.ControlPlugins.SimpleC2Plugin.Utils.ListenerHandler import HttpListenerHandler
from Utils.DataSingleton import Data
################################################
# Info class
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
        """_summary_


        """

        ## Get request

        ## Parse JSON

        ## Get specific keys in data key, do actions based on that. 
            # Link to parsing module or something
            #module.sort_data() or something

        ...
