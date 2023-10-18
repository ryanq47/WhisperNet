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
from flask import jsonify, send_from_directory, render_template, flash, redirect
from flask_login import LoginManager, login_required

#from flask_wtf import FlaskForm
#from wtforms import StringField, SubmitField, FileField
#from wtforms.validators import DataRequired, Length

## API stuff
from functools import wraps
from flask import request, jsonify
from flask_jwt_extended import get_jwt_identity, jwt_required

import hashlib

################################################
# Info class
################################################
'''Info class
Fill in your info for the plugin here. This is defined near the top, so it's accessible
by anything that may need it.

'''
class Info:
    name    = "SimpleC2"
    author  = "ryanq47"
    endpoint = "/simplec2"
    classname = "SimpleC2"
    plugin_type = "Builtin"
    #dashboard = True

################################################
# Authenitcation settings
################################################
'''
## To lock endpoints behind a login, do this:

Add '@login_required' decorator to your functions you want protected. 

Boom, you now need an account/authorization to access this endpoint.
These users are the same throughout the entire program, so all you have to do 
is add that decorator, and the following imports, and you are good to go. 

'''
#from flask_login import LoginManager, login_required

################################################
# Input Validation
################################################
'''
Hey. You. PUT FUCKING INPUT VALIDATION ON ALL THE FORMS (if applicable...). 
It's not hard, plus it keeps your stuff safe. Please.

'''

'''
class FileUploadForm(FlaskForm):
    file_upload = FileField('File Upload')  # Add a FileField for file uploads
    submit = SubmitField('Submit')

## Globally accessible forms.
class Forms:
    file_upload_form = FileUploadForm()'''

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

## RoleCheck Decorator - move to BasePlugin after testing
def role_required(required_role):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            current_user = get_jwt_identity()
            user_role = current_user.get('role') if current_user else None

            if user_role != required_role:
                return jsonify({"message": "Access denied"}), 403

            return func(*args, **kwargs)

        return wrapper

    return decorator


## Inherets BasePlugin
## Is a class instance, the __init__ is from BasePlugin.
class SimpleC2(BasePlugin, BaseLogging):
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
        self.app.route(f'/{Info.endpoint}', methods = ["GET"])(self.simplec2_dashboard)
        self.app.route(f'/api/{Info.endpoint}/', methods=["GET"])(self.simplec2_api_placeholder)

    def simplec2_dashboard(self):
        '''
        Dashaboards
        
        '''

        return "dashboard"
    
    def simplec2_api_placeholder(self):
        '''
        api
        '''
        return "api"
