'''
Hey! This is the External plugin template. You can create the external part of your plugins with this.

The first section is plugin options, aimed at making some harder settings a bit easier to configure.

Throw a description of your plugin here as well:
################################################
<desc> Plugin makes the world go around.
################################################


Last but not least, fill in the "Info" class with the proper fields. 
'''
## Don't remove me. This is the base plugin class, parent to all classes for plugins.
from ExternalBaseClass import ExternalBasePlugin
from Utils.LoggingBaseClass import BaseLogging

''' Imports
Go ahead and define any other imports you may need here.

'''
import logging
import inspect
from time import sleep
#from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity, exceptions
#from flask import Flask, jsonify, request, send_from_directory, render_template, Response

from flask import Flask, send_from_directory
import threading

################################################
# Info class
################################################
'''Info class
Fill in your info for the plugin here. This is defined near the top, so it's accessible
by anything that may need it.

'''
class Info:
    name    = "FH01_Ext"
    author  = "Plugin Author"
    plugin_type = "External"


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
class ExternalPluginClass(ExternalBasePlugin, BaseLogging):
    def __init__(self, app):
        #super().__init__(app, DataStruct)  # Problem with this was that it was trying to stuff app, 
        # and Datastruct into both, and both parent classes take different args, thus causing problems.

        ## Initialize BasePlugin and BaseLogging parent classes. Can't use one super call as stated above
        ExternalBasePlugin.__init__(self)
        BaseLogging.__init__(self)
          
        # Just in case you need to test logging/it breaks...
        #self.logger.warning("LOGGING IS WORKING - <PLUGINNAME>")
        self.app = app
        self.control_server_ip      = "127.0.0.1"
        self.control_server_port    = "5000"
        self.authorization_header   = None

    def main(self):
        '''
        Main function/entry point for the plugin.
        '''
        self.logger.debug(f"{self.function_debug_symbol} {inspect.stack()[0][3]}")
        self.logger.debug(f"{self.logging_debug_symbol} Loading {Info.name}")

        self.control_server_url = "http://127.0.0.1:5000/external"
        self.control_server_command_endpoint = "/api/command"

        while True:
            self.get_command_loop()
            sleep(30)
            ## using super here to access the functions in the parent. Could call it by name, 
            ## buy would hav to do ExternalBasePlugin.get_command(self) instead

    def register_routes(self):
        self.logger.debug(f"{self.function_debug_symbol} {inspect.stack()[0][3]}")
        self.app.route(f'/', methods = ["GET"])(self.plugin_function)
        self.app.route(f'/<path:filename>', methods = ["GET"])(self.serve_file)


    ## Define your plugin functions here.
    def plugin_function(self):
        self.logger.debug(f"{self.function_debug_symbol} {inspect.stack()[0][3]}")
        startup_message = (f"Plugin is up!<br>Plugin Name: {Info.name}<br> \
        Plugin Author: {Info.author}<br> ")

        return startup_message


    def get_command_loop(self):
        command = super().get_command()
        logging.debug(f"{self.logging_debug_symbol}: {command}")
        ## do stuff with command - build out command tree?


    def serve_file(self, filename):
        print(f"Filename; {filename}")
        return send_from_directory(
            "Files/",
            filename,
            ## Important to have as_attachment=True here.
            as_attachment=True)


if __name__ == "__main__":
    app = Flask(__name__)

    exteral_plugin = ExternalPluginClass(app)
    exteral_plugin.register_routes()

    ## Setup Daemon for heartbeat in background
    ## Note, this daemon method is inhereted from BasePlugin
    heartbeat_daemon = threading.Thread(
        target=exteral_plugin.heartbeat_daemon
    )


    heartbeat_daemon.daemon = True
    heartbeat_daemon.start()

    app.run(host="0.0.0.0", port=5001, debug=True)
