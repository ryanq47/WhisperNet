import random
import Utils.UtilsHandler
import logging
import inspect
import SecurityEngine.EncryptionHandler
import DataEngine.AuthenticationDBHandler
import os
import Utils.ErrorDefinitions
import bcrypt
import Utils.GuardClauses
from Utils.LoggingBaseClass import BaseLogging
## For role_required
from flask_jwt_extended import get_jwt_identity, jwt_required
from functools import wraps
from flask import jsonify
from Utils.UtilsHandler import api_response

## This is super hacky. My Dumbass made this a static method, so to properly use the BaseLogging class, I need to to 
## init the instance, and then call the logging function
base_logging = BaseLogging()
function_debug_symbol = base_logging.function_debug_symbol


class Authentication(BaseLogging):
    '''
    The authentication interface for the whole platform. Pulls from the user.db database, and can be used to authentcation
    with whatever wild methods I come up with in the future. Flexible on purpose
    
    '''
    @staticmethod
    def authentication_eval(username = None, password = None, path_struct = None) -> bool:
        '''
        Checks if user is authorized for access

        Checks:
            - Username
            - Password

            
        Dev notes, this is not perfect. Might need some work. It just feels weird
        '''

        base_logging.logger.debug(f"{function_debug_symbol} {inspect.stack()[0][3]}")

        print(f"User: {username}")

        #server_absolute_path = path_struct.sys_path
        db_relative_path = "DataBases/users.db"
        db_absolute_path = db_relative_path
        #db_absolute_path = os.path.join(server_absolute_path, db_relative_path)

        try:
            db_instance = DataEngine.AuthenticationDBHandler.AuthenticationSQLDBHandler(
                db_path=db_absolute_path
            )

            if db_instance.get_username(username=username):
                if Authentication._validate_password(db_instance=db_instance, username=username, password=password):
                    #base_logging.logger.warning(f"{base_logging.logging_warning_symbol} User {username} authenticated")
                    return True
            
        except Exception as e:
            # dosen't return anything, could be an issue?
            ## This could also be show stopper
            #raise Utils.ErrorDefinitions.GENERAL_ERROR
            base_logging.logger.debug(f"Authentication Error: {e}")
        
        return False

    @staticmethod
    def api_authentication_eval(username = None, password = None, path_struct = None) -> bool:
        '''
        Checks if api user is authorized for access

        Checks:
            - Username
            - Password

            
        Dev notes, this is not perfect. Might need some work. It just feels weird
        '''

        base_logging.logger.debug(f"{function_debug_symbol} {inspect.stack()[0][3]}")

        print(f"User: {username}")

        #server_absolute_path = path_struct.sys_path
        db_relative_path = "DataBases/users.db"
        db_absolute_path = db_relative_path
        #db_absolute_path = os.path.join(server_absolute_path, db_relative_path)

        try:
            db_instance = DataEngine.AuthenticationDBHandler.AuthenticationSQLDBHandler(
                db_path=db_absolute_path
            )

            if db_instance.get_api_username(username=username):
                if Authentication._validate_api_password(db_instance=db_instance, username=username, password=password):
                    #base_logging.logger.warning(f"{base_logging.logging_warning_symbol} User {username} authenticated")
                    return True
            
        except Exception as e:
            # dosen't return anything, could be an issue?
            ## This could also be show stopper
            #raise Utils.ErrorDefinitions.GENERAL_ERROR
            base_logging.logger.debug(f"Authentication Error: {e}")
        
        return False

    @staticmethod
    def api_get_user_role(username = None) -> bool:
        '''
        Gets API user role
            
        '''
        base_logging.logger.debug(f"{function_debug_symbol} {inspect.stack()[0][3]}")

        print(f"User: {username}")

        #server_absolute_path = path_struct.sys_path
        db_relative_path = "DataBases/users.db"
        db_absolute_path = db_relative_path
        #db_absolute_path = os.path.join(server_absolute_path, db_relative_path)

        try:
            db_instance = DataEngine.AuthenticationDBHandler.AuthenticationSQLDBHandler(
                db_path=db_absolute_path
            )

            role = db_instance.get_api_user_roll(username=username)

            if role:
                ## Role is a tuple in a list due to SQLite, so we are just retruning the tuple & stripping the list
                # role: [(admin, filehost_admin)]
    
                role = role[0]
                # role converted to (admin, filehost_admin)

                ## turning into list for jwt
                role_dict = []
                ## Split on "," remove spaces, and lowercase
                for i in role.split(","):
                    i = i.replace(" ", "")
                    i = i.lower()
                    role_dict.append(i)

                ## role_dict = [admin, filehost_admin]
                return role_dict
            
            else:
                base_logging.logger.warning(f"{base_logging.logging_warning_symbol} User {username} seemingly does not have any roles")
                    
        except Exception as e:
            # dosen't return anything, could be an issue?
            ## This could also be show stopper
            #raise Utils.ErrorDefinitions.GENERAL_ERROR
            base_logging.logger.warning(f"{base_logging.logging_warning_symbol} Error: {e}")
        
        return False


    @staticmethod
    def _validate_password(db_instance=None, password=None, username=None) -> bool:
        '''
        Validates a username. Private Func,Should not be called from outside this class.

        '''
        base_logging.logger.debug(f"{function_debug_symbol} {inspect.stack()[0][3]}")

        try:
            if Utils.GuardClauses.guard_t_f_check(username is None, "[*] Username argument is 'None'! Authentication will fail!"):
                return False

            ## 
            pass_blob_tuple = db_instance.get_password_blob(username=username)
            ## blob is first item in tuple
            pass_blob = pass_blob_tuple[0]

            print(f"PassBlob: {pass_blob}")
            print(f"PassWord: {password}")


            if pass_blob == False:
                base_logging.logger.debug(f"[*] Could not get password hash for user '{username}' from users.db")
                return False

            ## get username's password blob
            ## [func dep, beign weird
            '''
            if SecurityEngine.EncryptionHandler.Hashing.bcrypt_hash_and_compare(
                #entered_data=password,
                #stored_data=pass_blob
                entered_data=username,
                stored_data=pass_blob
            ):
                print(f"Successful Login: '{username}':'{password}'")'''

            #if bcrypt.checkpw("1234".encode(), "$2b$12$6l17I4n6BUqF3C43ldlg4u8kzCdDCLU/AJBTa44Yi.PGNon5hv3Mu".encode()):
            
            if bcrypt.checkpw(password.encode(), pass_blob.encode()):
                base_logging.logger.info(f"Successful Login: '{username}':'{password}'")
                return True
            
            else:
                base_logging.logger.warning(f"Bad Login: '{username}':'{password}'")
        
        except Exception as e:
            base_logging.logger.debug(f"[*] Error: {e}")

        return False

    @staticmethod
    def _validate_api_password(db_instance=None, password=None, username=None) -> bool:
        '''
        Validates an api pass. Exact same as _validate_password, save for the function it calls. Made more sense to implement
        a dedicated method, rather than add an argument to _validate_password, potentially breaking existing code

        ## This is what changed
        pass_blob_tuple = db_instance.get_api_password_blob(username=username)

        from

        pass_blob_tuple = db_instance.get_password_blob(username=username)

        '''
        base_logging.logger.debug(f"{function_debug_symbol} {inspect.stack()[0][3]}")

        try:
            if Utils.GuardClauses.guard_t_f_check(username is None, "[*] Username argument is 'None'! Authentication will fail!"):
                return False

            ## 
            pass_blob_tuple = db_instance.get_api_password_blob(username=username)
            ## blob is first item in tuple
            pass_blob = pass_blob_tuple[0]

            print(f"PassBlob: {pass_blob}")
            print(f"PassWord: {password}")


            if pass_blob == False:
                base_logging.logger.debug(f"[*] Could not get password hash for user '{username}' from users.db")
                return False

            ## get username's password blob
            ## [func dep, beign weird
            '''
            if SecurityEngine.EncryptionHandler.Hashing.bcrypt_hash_and_compare(
                #entered_data=password,
                #stored_data=pass_blob
                entered_data=username,
                stored_data=pass_blob
            ):
                print(f"Successful Login: '{username}':'{password}'")'''

            #if bcrypt.checkpw("1234".encode(), "$2b$12$6l17I4n6BUqF3C43ldlg4u8kzCdDCLU/AJBTa44Yi.PGNon5hv3Mu".encode()):
            
            if bcrypt.checkpw(password.encode(), pass_blob.encode()):
                base_logging.logger.info(f"Successful Login: '{username}':'{password}'")
                return True
            
            else:
                base_logging.logger.warning(f"Bad Login: '{username}':'{password}'")
        
        except Exception as e:
            base_logging.logger.debug(f"[*] Error: {e}")

        return False

class UserManagement:
    '''
    The class for handling user shit. I.e. creating, deleting, modifying
    '''
    @staticmethod
    def create_user(path_struct = None, username = None, password = None):
        '''
        Creates users. Is an abstraction over the AuthenticationSQLDBHandler.create_user

        path_struct: The class instance containing path data
        username: username of user to create
        pass: pass of user to create
        '''
        base_logging.logger.debug(f"{function_debug_symbol} {inspect.stack()[0][3]}")
        try:
            server_absolute_path = path_struct.sys_path
            db_relative_path = "DataBases/users.db"
            db_absolute_path = os.path.join(server_absolute_path, db_relative_path)


            db_instance = DataEngine.AuthenticationDBHandler.AuthenticationSQLDBHandler(
                db_path=db_absolute_path
            )

            password_blob =  SecurityEngine.EncryptionHandler.Hashing.bcrypt_hash(
                data = password
            )

            if Utils.GuardClauses.guard_t_f_check(password_blob is None, "[*] password_blob is none, error occured during hashing"):
                return False

            if db_instance.create_user(
                username = username,
                password_blob = password_blob,
            ):
                return True
        
        except Exception as e:
            base_logging.logger.debug(f"Could not connect to DB: {e}")
        
        return False
    
    @staticmethod
    def delete_user(path_struct = None, username = None):
        '''
        For deleting users. Is an abstraction over the AuthenticationSQLDBHandler.delete_user

        path_struct: The class instance containing path data
        username: The username to delete
        '''
        base_logging.logger.debug(f"{function_debug_symbol} {inspect.stack()[0][3]}")
        try:
            server_absolute_path = path_struct.sys_path
            db_relative_path = "DataBases/users.db"
            db_absolute_path = os.path.join(server_absolute_path, db_relative_path)

            db_instance = DataEngine.AuthenticationDBHandler.AuthenticationSQLDBHandler(
                db_path=db_absolute_path
            )

            if db_instance.delete_user(
                username = username
            ):
                return True
        
        except Exception as e:
            base_logging.logger.debug(f"Could not connect to DB: {e}")
        
        return False

class AccessManagement:
    '''
    A class to handle access stuff. 
    '''
    ## RoleCheck Decorator - move to BasePlugin after testing
    @staticmethod
    def role_required(*required_roles):
        '''
        
        A (static) wrapper to allow/deny based on roles

        required_roles: Roles required. I think it's a tuple. See 
            below code exaple on how to properly call this func
        
        Ex Usage: 

        With this, either 'admin' or 'editor' can access this function
            
            @role_required('admin', 'editor')
            def sensitive_function():
                # Your sensitive function code here
                return "Sensitive data accessed"

        '''

        def decorator(func):
            @wraps(func)
            def wrapper(*args, **kwargs):
                try:
                    current_user = get_jwt_identity()

                    # This is a list
                    user_roles = current_user.get('role')

                    # Check if any of the user's roles match the required roles
                    if not any(role in required_roles for role in user_roles):
                        return api_response(
                            status_code=403,
                        )
                
                except Exception as e:
                    ## This is here so I can handle the errors instead of letting
                    # flask spit out whatever it wants.
                    return api_response(
                        status_code=500
                        #message=str(e) ## Dumb & stupid remove once done debugging
                    )
                #jsonify({"message": "Access denied"}), 403

                return func(*args, **kwargs)
            return wrapper
        return decorator
