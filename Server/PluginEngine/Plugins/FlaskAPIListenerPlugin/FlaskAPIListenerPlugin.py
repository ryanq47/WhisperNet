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
from Utils.LoggingBaseClass import BaseLogging

''' Imports
Go ahead and define any other imports you may need here.

'''
import logging
import inspect


################################################
# Info class
################################################
'''Info class
Fill in your info for the plugin here. This is defined near the top, so it's accessible
by anything that may need it.

'''
class Info:
    name    = "FlaskAPIListnener"
    author  = "ryanq.47"
    endpoint = "/flasklistener"
    classname = "FlaskAPIListener"
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


Options:

    If global_debug is True, the plugin will log to console.
    function_debug_symbol is the symbol to put before each log entry for this plugin. 
'''

################################################
# The actual code
################################################

## Inherets BasePlugin
class FlaskAPIListener(BasePlugin, BaseLogging):
    def __init__(self, app, DataStruct):
        BasePlugin.__init__(self, app, DataStruct)
        BaseLogging.__init__(self)  
    def main(self):
        '''
        Main function/entry point for the plugin.
        '''
        logging.debug(f"{self.function_debug_symbol} {inspect.stack()[0][3]}")
        self.logger.debug(f"{self.logging_debug_symbol} Loading {Info.name}")
        self.register_routes()

        ## does stuff

    ## Put all the routes here.
    def register_routes(self):
        logging.debug(f"{self.function_debug_symbol} {inspect.stack()[0][3]}")
        ## Base Endpoint
        self.app.route(f"/{Info.endpoint}", methods=["POST", "GET"])(self._plugin_function)
    

    ## Define your plugin functions here.

    def _plugin_function(self):
        logging.debug(f"{self.function_debug_symbol} {inspect.stack()[0][3]}")
        startup_message = (f"Plugin is up!<br>Plugin Name: {Info.name}<br> \
        Plugin Author: {Info.author}<br> \
        Plugin Endpoint: {Info.endpoint}<br>")

        return startup_message
    