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
from Utils.UtilsHandler import api_response
''' Imports
Go ahead and define any other imports you may need here.

'''
import logging
import inspect
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity, exceptions
from flask import Flask, jsonify, request, send_from_directory, render_template, Response

import SecurityEngine.AuthenticationHandler
from datetime import timedelta


################################################
# Info class
################################################
'''Info class
Fill in your info for the plugin here. This is defined near the top, so it's accessible
by anything that may need it.

'''
class Info:
    name    = "AuthenticationPlugin"
    author  = "ryanq47"
    endpoint = "/authentication" ## might not be applicable here
    classname = "AuthenticationPlugin"
    plugin_type = "Builtin"

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
#from flask_login import login_required

################################################
# Input Validation
################################################
'''
Hey. You. PUT FUCKING INPUT VALIDATION ON ALL THE FORMS (if applicable...). 
It's not hard, plus it keeps your stuff safe. Please.

'''

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
class AuthenticationPlugin(BasePlugin, BaseLogging):
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
        self.logger.critical("WOAH TEST 123")
        self.register_routes()

    ## Put all the routes here.
    def register_routes(self):
        #self.app.route("/", methods=["GET"])(self.login_page)
        #self.app.route('/login', methods=["POST"])(self.web_user_login)
        #self.app.route('/logout')(self.web_user_logout)
        self.app.route('/api/login', methods=["POST"])(self.api_user_login)
        #self.app.route('/api/logout', methods=["POST"])(...)


    def api_user_login(self):
        '''
        API login

        Have not tested sec with this.
        '''
        data = request.get_json()
    
        # for consistency
        failed_login_string = "Login has failed"
        succesful_login_string = "Succesful login"

        try:
            username = data.get('username')
            password = data.get('password')
        except Exception as e:
            return api_response(
                    status_code=401,
                    message=failed_login_string,
                    data=None,
                )

        ## Check user against DB
        if SecurityEngine.AuthenticationHandler.Authentication.api_authentication_eval(
            username = username,
            password = password
        ):
            ## Get role

            ## Dict
            user_role = SecurityEngine.AuthenticationHandler.Authentication.api_get_user_role(
                username = username
            )

            if user_role:
                # Create a dictionary with user identity and any claims (e.g., role)
                # Curious if a user can have multiple roles here
                identity_dict = {'username': username, 'role': user_role}

                token_expire = timedelta(hours=1)

                # Create a JWT token with the user's identity and claims
                access_token = create_access_token(
                    identity=identity_dict,
                    expires_delta=token_expire ## Token expire in X time
                    )

                #print(user_role)
                return api_response(
                    status_code=200,
                    message=succesful_login_string,
                    data=None,
                    access_token=access_token
                )
            #jsonify({"access_token": access_token}), 200


        else:
            print(f"{username} failed to authenticate as api user")
            return api_response(
                    status_code=401,
                    message=failed_login_string,
                    data=None,
                )



''' Old funcs related to Web

    ## login for something
    def server_login(self):
        username = request.json.get('username')
        password = request.json.get('password')

        ## need a guard statement here to make sure user & pass actually equal something

        if SecurityEngine.AuthenticationHandler.Authentication.authentication_eval(
            username=username,
            password=password,
            path_struct=Data.path_struct
        ):
            access_token = create_access_token(identity="username")
            return {'access_token': access_token}, 200
        else:
            return self.page_not_found()
    
    def web_user_login(self):

        username = request.form['username']
        password = request.form['password']

        ## Check user against DB
        if SecurityEngine.AuthenticationHandler.Authentication.authentication_eval(
            username = username,
            password = password
        ):
            ## Might be prone to injection
            user = User(username)
            login_user(user)
            #return 'Logged in successfully'
            return redirect("/filehost")
        else:
            return render_template('builtin-login.html')


                ## User login stuff for the WEB interface
    def login_page(self):
        return render_template('builtin-login.html')
    


    def web_user_logout(self):
        logout_user()
        return 'Logged out successfully'

    def page_not_found(self, e=None):

        #Handles all 40X & any try/except errors. Basically it returns a 200
        #with a "page not found"

        #This is done for security/scraping/URL discovery reasons
            
        try:
            err_404_path = random.choice(self.UrlSc.NOT_FOUND_LIST_404)
            self.logger.debug(f"Error: {e}")

            html = Utils.UtilsHandler.load_file(
                current_path=sys_path, 
                file_path=err_404_path, 
                return_path=False
            )
            
            resp = Response(html)

            # Set the 'err' cookie with the value of 'e'
            resp.set_cookie('err', str(e))

            return resp, 200
        ## Fallback for if something breaks
        except:
            return "", 200        
## no idea what these did. 
@login_manager.user_loader
def load_user(user_id):
    ## User Logic here?
    user = User(user_id)
    return user

class User(UserMixin):
    def __init__(self, id):
        self.id = id

'''