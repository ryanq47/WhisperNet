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
#from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity, exceptions
#from flask import Flask, jsonify, request, send_from_directory, render_template, Response



################################################
# Info class
################################################
'''Info class
Fill in your info for the plugin here. This is defined near the top, so it's accessible
by anything that may need it.

'''
class Info:
    name    = "PluginTemplate"
    author  = "Plugin Author"
    endpoint = "/template"
    classname = "PluginClass"
    plugin_type = "Builtin"

################################################
# Authenitcation settings
################################################
'''
## If you want JWT tokens on your endpoint, uncomment the lines below

Then, add '@jwt_required' decorator to your functions you want protected. 

Boom, you now need an account/authorization to access this endpoint.

'''
#from flask_jwt_extended import jwt_required

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
class PluginClass(BasePlugin):
    def __init__(self, app, DataStruct):
        ## Weird setup, this takes in app, DataStruct, passes it to baseclass, which then init's and sets it to self.app, and self.DataStruct
        super().__init__(app, DataStruct)
        ## Getting the logger instance here
        self.logger = super().logger

    def main(self):
        '''
        Main function/entry point for the plugin.
        '''
        self.logger.debug(f"{self.function_debug_symbol} {inspect.stack()[0][3]}")
        print(f"{self.print_symbol} Loading {Info.name}")
        self.register_routes()

    ## Put all the routes here.
    def register_routes(self):
        self.logger.debug(f"{self.function_debug_symbol} {inspect.stack()[0][3]}")
        self.app.route(f'/{Info.endpoint}', methods=["GET"])(self.plugin_function)
    

    ## Define your plugin functions here.
    def plugin_function(self):
        self.logger.debug(f"{self.function_debug_symbol} {inspect.stack()[0][3]}")
        startup_message = (f"Plugin is up!<br>Plugin Name: {Info.name}<br> \
        Plugin Author: {Info.author}<br> \
        Plugin Endpoint: {Info.endpoint}<br>")

        return startup_message
