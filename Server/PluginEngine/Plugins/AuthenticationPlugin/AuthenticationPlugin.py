#from PluginEngine.Plugins.BasePlugin import BasePlugin
from Utils.ApiHelper import api_response

import logging
import inspect
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity, exceptions
from flask import Flask, jsonify, request, send_from_directory, render_template, Response
from datetime import timedelta
#import SecurityEngine.AuthenticationHandler
from SecurityEngine.AuthenticationHandler import Authentication
from Utils.Logger import LoggingSingleton
from Utils.DataSingleton import Data

class Info:
    name    = "AuthenticationPlugin"
    author  = "ryanq47"
    endpoint = "/authentication" ## might not be applicable here
    classname = "AuthenticationPlugin"
    plugin_type = "Builtin"


class AuthenticationPlugin():
    def __init__(self, app):
        self.logger = LoggingSingleton.get_logger()
        self.app = app
        self.Data = Data()

    def main(self):
        '''
        Main function/entry point for the plugin.
        '''
        self.logger.debug(f"Loading {Info.name}")
        self.register_routes()

    ## Put all the routes here.
    def register_routes(self):
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

        authentication = Authentication(db_path=self.Data.Paths.users_db_path)

        ## Check user against DB
        if authentication.api_authentication_eval(
            username = username,
            password = password
        ):
            ## Get role

            ## Dict
            user_role = authentication.api_get_user_role(
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


