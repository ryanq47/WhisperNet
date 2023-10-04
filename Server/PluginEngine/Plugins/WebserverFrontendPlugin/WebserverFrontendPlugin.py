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
import sqlite3
#from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity, exceptions
from flask import render_template, request, redirect

import DataEngine.ServerDataDbHandler
import SecurityEngine.AuthenticationHandler



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
        self.datadb_instance = DataEngine.ServerDataDbHandler.ServerDataDbHandler()
        self.dbconn = None
        self.cursor = None

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
        list_of_plugins = []

        ## if self.dbconn is none, then connect
        if not self.guard_db_connection():
            self.connect_to_db()

        plugin_data = self.datadb_instance.retrieve_plugins_from_table(cursor = self.cursor)
        #print(plugin_data)

        ## populate the list of plugins from the database
        for plugin in plugin_data:
            '''
            Data comes back in a tuple:
            [('FlaskAPIListnener', '/flasklistener', 'ryanq.47', 'Builtin', 0), (more data)]
            This makes it slightly less readable for creating the dict below. Also,
            should prolly make a dedicated function for this.
            '''
            dict_ = {
                'name': plugin[0],
                'endpoint': plugin[1],
                'author': plugin[2],
            }
            list_of_plugins.append(dict_)

        return render_template('webserverfrontendplugin-dashboard.html', 
                            plugins=list_of_plugins,
                            servername = servername)

    def login(self):
        username = request.form['username']
        password = request.form['password']

        ## LOGIN LOGIC HERE

        if SecurityEngine.AuthenticationHandler.Authentication.authentication_eval(
            username = username,
            password = password
        ):
            
            ## need to issue JWT tokens here too

            return redirect(f'{Info.endpoint}/dashboard')
        else:
            return render_template('webserverfrontendplugin-index.html')
    
    def connect_to_db(self):
        db_name = "DataBases/ServerData.db"
        try:
            self.dbconn = sqlite3.connect(db_name)
            self.cursor = self.dbconn.cursor()
            self.logger.info(f"{self.logging_info_symbol} Successful connection to: {db_name}")

        except Exception as e:
            self.logger.warning(f"{self.logging_warning_symbol} Error: {e}")


    def guard_db_connection(self) -> bool:
        '''
        A guard against the self.dbconn being None.
        '''
        self.logger.debug(f"{self.function_debug_symbol} {inspect.stack()[0][3]}")

        if self.dbconn is None:
            self.logger.warning(f"{self.logging_info_symbol} Connection to DB is None. Reconnecting")
            return False

        return True

    