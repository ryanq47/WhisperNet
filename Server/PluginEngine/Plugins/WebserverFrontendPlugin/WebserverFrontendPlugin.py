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
#from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity, exceptions
from flask import render_template, request, redirect



################################################
# Info class
################################################
'''Info class
Fill in your info for the plugin here. This is defined near the top, so it's accessible
by anything that may need it.

'''
class Info:
    name    = "WebserverFrontendPlugin"
    author  = "ryanq.47"
    endpoint = "/stats"
    classname = "WebserverFrontend"
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

    The first instruction in each function is "logging.debug(f"{self.function_debug_symbol} {inspect.stack()[0][3]}")"
    This will print the function name and the line number of the function call. It makes it easier to debug. Set the 
    logging level to something other than "DEBUG" to shut this off. It can get quite noisy.


Options:

    If global_debug is True, the plugin will log to console.
    self.function_debug_symbol is the symbol to put before each log entry for this plugin. 
'''


## Inherets BasePlugin
class WebserverFrontend(BasePlugin, BaseLogging):
    ## Weird setup, this takes in app, DataStruct, passes it to baseclass, which then init's and sets it to self.app, and self.DataStruct
    def __init__(self, app, DataStruct):
        BasePlugin.__init__(self, app, DataStruct)
        BaseLogging.__init__(self)  
        #self.logger.warning("LOGGING IS WORKING - WebServerFrontendPlugin")

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
        self.app.route(f'/stats', methods=['GET'])(self.login_page)
        self.app.route(f'/{Info.endpoint}/dashboard', methods=['GET'])(self.dashboard)
        self.app.route(f'/{Info.endpoint}/login', methods=['POST'])(self.login)

    def login_page(self):
        return render_template('webserverfrontendplugin-index.html')

    def dashboard(self):
        servername = "DevServer"
        list_of_plugins = [
            {'name':'pluginname', 'author':'author', 'endpoint':'endpoint',},
            {'name':'pluginname', 'author':'author', 'endpoint':'endpoint',},
            {'name':'pluginname', 'author':'author', 'endpoint':'endpoint',},
            ]

        return render_template('webserverfrontendplugin-dashboard.html', 
                            plugins=list_of_plugins,
                            servername = servername)

    def login(self):
        username = request.form['username']
        password = request.form['password']

        # Add your authentication logic here (e.g., checking credentials)
        # For this example, we'll simply print the received data.
        #print(f'Username: {username}, Password: {password}')

        ## LOGIN LOGIC HERE

        # You can redirect the user to a different page after login, for example:
        return redirect(f'{Info.endpoint}/dashboard')