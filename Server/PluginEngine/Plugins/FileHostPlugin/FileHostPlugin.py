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
import os

''' Imports
Go ahead and define any other imports you may need here.

'''
import logging
import inspect
#from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity, exceptions
#from flask import Flask, jsonify, request, send_from_directory, render_template, Response
from flask import jsonify, send_from_directory, render_template


################################################
# Info class
################################################
'''Info class
Fill in your info for the plugin here. This is defined near the top, so it's accessible
by anything that may need it.

'''
class Info:
    name    = "FileHost"
    author  = "ryanq47"
    endpoint = "/filehost"
    classname = "FileHost"
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
class FileHost(BasePlugin, BaseLogging):
    def __init__(self, app, DataStruct):
        #super().__init__(app, DataStruct)  # Problem with this was that it was trying to stuff app, 
        # and Datastruct into both, and both parent classes take different args, thus causing problems.

        ## Initialize BasePlugin and BaseLogging parent classes. Can't use one super call as stated above
        BasePlugin.__init__(self, app, DataStruct)
        BaseLogging.__init__(self)  
        # Just in case you need to test logging/it breaks...
        #self.logger.warning("LOGGING IS WORKING - <PLUGINNAME>")

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
        self.app.route(f'/{Info.endpoint}', methods = ["GET"])(self.filehost_base_directory)
        self.app.route(f'/{Info.endpoint}/command', methods=["GET"])(self.command_endpoint)
        self.app.route(f'/{Info.endpoint}/<path:filename>', methods = ["GET"])(self.filehost_download_file)
        self.app.route(f'/{Info.endpoint}/upload', methods = ["GET"])(self.filehost_upload_file)


    # for controlling ext plugin
    def command_endpoint(self):
        json = {
            "command": "stuff"
        }

        return jsonify(json)
    
    def filehost_download_file(self, filename):
        print(f"Filename; {filename}")
        return send_from_directory(
            "PluginEngine/Plugins/FileHostPlugin/Files",
            filename,
            as_attachment=True)


    def filehost_upload_file(self):
        return "not implemented."

    def filehost_base_directory(self):
        '''
        eventually.. if not auth then re-auth
        '''

        servername = "FileHost Plugin"

        list_of_files = []

        ## populate the list of plugins from the database
        for file in os.listdir("PluginEngine/Plugins/FileHostPlugin/Files/"):
            '''
            Data comes back in a tuple:
            [('FlaskAPIListnener', '/flasklistener', 'ryanq.47', 'Builtin', 0), (more data)]
            This makes it slightly less readable for creating the dict below. Also,
            should prolly make a dedicated function for this.
            '''
            try:
                ## chagne to join
                with open(f"PluginEngine/Plugins/FileHostPlugin/Files/{file}", "rb") as f:
                    data = f.read(40)

                dict_ = {
                    'name': file,
                    'contents': data,
                }

            except Exception as e: 
                dict_ = {
                    'name': f"ERROR: {e}",
                    'contents': '',
                }
            finally:
                list_of_files.append(dict_)

        return render_template('filehost-dashboard.html', 
                            files=list_of_files,
                            servername = servername)