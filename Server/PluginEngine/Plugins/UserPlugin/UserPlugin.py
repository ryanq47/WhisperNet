'''
Hey! This is the plugin template. You can create your own plugins with this template. Said plugins can either
live directly on this server, or have an external component. See the FlaskAPIListenerPlugin for an example 
of an external component.

The first section is plugin options, aimed at making some harder settings a bit easier to configure.

Throw a description of your plugin here as well:
################################################
<desc> Plugin makes the world go around.
################################################


Last but not least, fill in the "Info" class with the proper fields. 
'''
## Don't remove me. This is the base plugin class, parent to all classes for plugins.
from PluginEngine.Plugins.BasePlugin import BasePlugin

''' Imports
Go ahead and define any other imports you may need here.

'''
import logging
import inspect
from flask import request
from werkzeug.exceptions import BadRequest

import SecurityEngine.AuthenticationHandler
from Utils.LoggingBaseClass import BaseLogging
from Utils.UtilsHandler import api_response
from SecurityEngine.AuthenticationHandler import AccessManagement

################################################
# Info class
################################################
'''Info class
Fill in your info for the plugin here. This is defined near the top, so it's accessible
by anything that may need it.

'''
class Info:
    name    = "UserHandler"
    author  = "ryanq.47"
    endpoint = "/user"
    classname = "UserHandler"
    plugin_type = "Builtin"

################################################
# Authenitcation settings
################################################
'''
## If you want JWT tokens on your endpoint, uncomment the lines below

Then, add '@jwt_required' decorator to your functions you want protected. 

Boom, you now need an account/authorization to access this endpoint.

Roles Notes:
This plugin has X roles:
    iam_admin: Admin role
    iam_user: Not sure if this will be needed, will there ever be a case of a "iam_user" needed?

'''
from flask_jwt_extended import jwt_required

################################################
# Logging & Debugging
################################################
''' ## Logging & Debugging ##
I highly recommend you to use the logging module, it makes life a lot easier

Debugging:

    The first instruction in each function is "logging.debug(f"{function_debug_symbol} {inspect.stack()[0][3]}")"
    This will print the function name and the line number of the function call. It makes it easier to debug. Set the 
    logging level to something other than "DEBUG" to shut this off. It can get quite noisy.


Options:

    If global_debug is True, the plugin will log to console.
    function_debug_symbol is the symbol to put before each log entry for this plugin. 
'''


## Inherets BasePlugin
## Is a class instance, the __init__ is from BasePlugin.
class UserHandler(BasePlugin, BaseLogging):
    def __init__(self, app, DataStruct):
        BasePlugin.__init__(self, app, DataStruct)
        BaseLogging.__init__(self)  

    def main(self):
        '''
        Main function/entry point for the plugin.
        '''
        self.logger.debug(f"{self.function_debug_symbol} {inspect.stack()[0][3]}")
        self.logger.debug(f"{self.logging_debug_symbol} Loading {Info.name}")
        self.register_routes()

    ## Put all the routes here.
    def register_routes(self):
        self.logger.debug(f"{self.function_debug_symbol} {inspect.stack()[0][3]}")
        self.app.route(f'/{Info.endpoint}', methods=["GET"])(self.userhandler_base)

        self.app.route(f"/api/{Info.endpoint}/create", methods=["POST"])(self.create_user)
        self.app.route(f"/api/{Info.endpoint}/delete", methods=["POST"])(self.delete_user)

        #self.app.route(f"/{self.UrlSc.CREATE_USER}", methods=["POST"])(self.create_user)
        #self.app.route(f"/{self.UrlSc.DELETE_USER}", methods=["POST"])(self.delete_user)

    ## Define your plugin functions here.
    def userhandler_base(self):
        self.logger.debug(f"{self.function_debug_symbol} {inspect.stack()[0][3]}")
        startup_message = (f"Plugin is up!<br>Plugin Name: {Info.name}<br> \
        Plugin Author: {Info.author}<br> \
        Plugin Endpoint: {Info.endpoint}<br>")

        return startup_message
    
    ## Create users
    @jwt_required()
    @AccessManagement.role_required('iam_admin')
    def create_user(self):
        try:
            username = request.json.get('username')
            password = request.json.get('password')

            # Early exit if user creation is not successful
            if not SecurityEngine.AuthenticationHandler.UserManagement.create_user(
                username=username,
                password=password,
                path_struct=self.DataStruct.path_struct
            ):
                return api_response(status_code=403)

            # Main logic after early exit check
            self.logger.info(f"{self.logging_info_symbol} Created user '{username}'")
            return api_response(status_code=200, message=f"User '{username}' created")

        except BadRequest:
            return api_response(status_code=400)
        except Exception as e:
            return api_response(status_code=500)

    ## Delete users
    @jwt_required()
    @AccessManagement.role_required('iam_admin')
    def delete_user(self):
        try:
            username = request.json.get('username')

            # Early exit if user deletion is not successful
            if not SecurityEngine.AuthenticationHandler.UserManagement.delete_user(
                username=username,
                path_struct=self.DataStruct.path_struct
            ):
                return api_response(status_code=403)

            # Main logic after early exit check
            self.logger.info(f"{self.logging_info_symbol} Deleted user '{username}'")
            return api_response(status_code=200, message=f"User {username} deleted")

        except BadRequest:
            return api_response(status_code=400)
        except Exception as e:
            return api_response(status_code=500)

