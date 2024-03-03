import logging
import inspect
from flask import request
from werkzeug.exceptions import BadRequest

import SecurityEngine.AuthenticationHandler
from Utils.LoggingBaseClass import BaseLogging
from Utils.UtilsHandler import api_response
from SecurityEngine.AuthenticationHandler import AccessManagement
from Utils.Logger import LoggingSingleton

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
Roles Notes:
This plugin has X roles:
    iam_admin: Admin role
    iam_user: Not sure if this will be needed, will there ever be a case of a "iam_user" needed?

'''
from flask_jwt_extended import jwt_required

class UserHandler():
    def __init__(self, app):
        self.logger = LoggingSingleton.get_logger()

    def main(self):
        '''
        Main function/entry point for the plugin.
        '''
        self.logger.debug(f"Loading {Info.name}")
        self.register_routes()

    ## Put all the routes here.
    def register_routes(self):
        self.app.route(f'/{Info.endpoint}', methods=["GET"])(self.userhandler_base)

        self.app.route(f"/api/{Info.endpoint}/create", methods=["POST"])(self.create_user)
        self.app.route(f"/api/{Info.endpoint}/delete", methods=["POST"])(self.delete_user)
        self.app.route(f"/api/{Info.endpoint}/changepass", methods=["POST"])(self.change_user_password)
        self.app.route(f"/api/{Info.endpoint}/role/add", methods=["POST"])(self.add_user_role)
        self.app.route(f"/api/{Info.endpoint}/role/delete", methods=["POST"])(self.remove_user_role)

        #self.app.route(f"/{self.UrlSc.CREATE_USER}", methods=["POST"])(self.create_user)
        #self.app.route(f"/{self.UrlSc.DELETE_USER}", methods=["POST"])(self.delete_user)

    ## Define your plugin functions here.
    def userhandler_base(self):
        startup_message = (f"Plugin is up!<br>Plugin Name: {Info.name}<br> \
        Plugin Author: {Info.author}<br> \
        Plugin Endpoint: {Info.endpoint}<br>")

        return startup_message
    
    #[X]
    ## Create users
    @jwt_required()
    @AccessManagement.role_required('iam_admin')
    def create_user(self):
        try:
            username = request.json.get('username')
            password = request.json.get('password')
            roles = request.json.get('roles')
            print(roles)

            # Early exit if user creation is not successful
            if not SecurityEngine.AuthenticationHandler.UserManagement.create_user(
                username=username,
                password=password,
                path_struct=self.DataStruct.path_struct,
                roles=roles
            ):
                return api_response(status_code=403)

            # Main logic after early exit check
            self.logger.info(f"Created user '{username}'")
            return api_response(status_code=200, message=f"User '{username}' created")

        except BadRequest:
            return api_response(status_code=400)
        except Exception as e:
            return api_response(status_code=500)

    #[X]
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
            self.logger.info(f"Deleted user '{username}'")
            return api_response(status_code=200, message=f"User {username} deleted")

        except BadRequest:
            return api_response(status_code=400)
        except Exception as e:
            return api_response(status_code=500)

    #[X]
    @jwt_required()
    @AccessManagement.role_required('iam_admin')
    def change_user_password(self):
        try:
            username = request.json.get('username')
            password = request.json.get('password')

            # Early exit if user deletion is not successful
            if not SecurityEngine.AuthenticationHandler.UserManagement.change_user_password(
                username=username,
                password=password
            ):
                return api_response(status_code=403)

            # Main logic after early exit check
            self.logger.info(f"Changed password for '{username}'")
            return api_response(status_code=200, message=f"Changed password for '{username}'")

        except BadRequest:
            return api_response(status_code=400)
        except Exception as e:
            return api_response(status_code=500)

    #[X]  
    @jwt_required()
    @AccessManagement.role_required('iam_admin')
    def add_user_role(self):
        '''
        Adds a user role
        
        '''
        try:
            username = request.json.get('username')
            roles = request.json.get('roles')
            ## Roles is a list: ['role1','role2']

            # Early exit if user deletion is not successful
            if not SecurityEngine.AuthenticationHandler.UserManagement.add_user_role(
                username=username,
                roles=roles
            ):
                return api_response(status_code=403)

            # Main logic after early exit check
            self.logger.info(f"Added {roles} roles for '{username}'")
            return api_response(status_code=200, message=f"Added {roles} roles for '{username}'")

        except BadRequest:
            return api_response(status_code=400)
        except Exception as e:
            return api_response(status_code=500)
        
    @jwt_required()
    @AccessManagement.role_required('iam_admin')
    def remove_user_role(self):
        '''
        Removes a user role
        
        '''
        try:
            username = request.json.get('username')
            roles = request.json.get('roles')

            # Early exit if user deletion is not successful
            if not SecurityEngine.AuthenticationHandler.UserManagement.delete_user_role(
                username=username,
                roles=roles
            ):
                return api_response(status_code=403)

            # Main logic after early exit check
            self.logger.info(f"Removed {roles} roles for '{username}'")
            return api_response(status_code=200, message=f"Removed {roles} roles for '{username}'")

        except BadRequest:
            return api_response(status_code=400)
        except Exception as e:
            return api_response(status_code=500)