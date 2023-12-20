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
import getpass

## This is super hacky. My Dumbass made this a static method, so to properly use the BaseLogging class, I need to to 
## init the instance, and then call the logging function
base_logging = BaseLogging()
function_debug_symbol = base_logging.function_debug_symbol


class Authentication(BaseLogging):
    '''
    The authentication interface for the whole platform. Pulls from the user.db database, and can be used to authentcation
    with whatever wild methods I come up with in the future. Flexible on purpose
    
    '''

    # [? test me]
    @staticmethod
    def api_authentication_eval(username=None, password=None, path_struct=None) -> bool:
        '''
        Checks if API user is authorized for access.

        Checks:
            - Username
            - Password
        '''

        base_logging.logger.debug(f"{function_debug_symbol} {inspect.stack()[0][3]}")

        # Validate input parameters
        if not username or not password:
            base_logging.logger.warning("Username or password not provided for authentication")
            return False

        # Path setup
        db_relative_path = "DataBases/users.db"
        db_absolute_path = db_relative_path  # or os.path.join(server_absolute_path, db_relative_path)

        try:
            db_instance = DataEngine.AuthenticationDBHandler.AuthenticationSQLDBHandler(
                db_path=db_absolute_path
            )

            # Check if the username exists
            if not db_instance.get_api_username(username=username):
                base_logging.logger.debug(f"Username {username} not found")
                return False

            # Validate the password
            if Authentication._validate_api_password(db_instance=db_instance, username=username, password=password):
                return True
            else:
                base_logging.logger.debug(f"Incorrect password for user {username}")
                return False

        except Exception as e:
            base_logging.logger.error(f"Authentication Error: {e}")
            return False

    # [X]
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
            #print(f"PassWord: {password}")


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

            ## pass_blob is seemingly coming back from the db as a bytes object. Might get funky somewhere later
            if bcrypt.checkpw(password.encode(), pass_blob):
                base_logging.logger.info(f"Successful Login: '{username}'")
                return True
            
            else:
                base_logging.logger.warning(f"Bad Login: '{username}'")

        except Exception as e:
            base_logging.logger.debug(f"[*] Error: {e}")

        return False

    
    # [X]
    @staticmethod
    def api_get_user_role(username=None) -> list:
        '''
        Gets API user role, returns a list of roles

        username: Username to query for its roles

        ex: ['iam_admin', 'iam_user']
        '''
        base_logging.logger.debug(f"{function_debug_symbol} {inspect.stack()[0][3]}")

        # Path setup
        db_relative_path = "DataBases/users.db"
        db_absolute_path = db_relative_path  # or os.path.join(server_absolute_path, db_relative_path)

        if not username:
            base_logging.logger.warning(f"{base_logging.logging_warning_symbol} No username provided")
            return []

        try:
            # Initialize DB instance and fetch roles
            db_instance = DataEngine.AuthenticationDBHandler.AuthenticationSQLDBHandler(db_path=db_absolute_path)
            roles = db_instance.get_all_api_user_roles(username=username)

            if not roles:
                base_logging.logger.warning(f"{base_logging.logging_warning_symbol} User {username} does not have any roles")
                return []

            # Extract and return roles -- data look slike [(user,role)]
            return [role[1] for role in roles]

        except Exception as e:
            base_logging.logger.error(f"{base_logging.logging_warning_symbol} Error fetching roles for user {username}: {e}")
            # Depending on requirements, you might raise an error or return an empty list
            return []

class UserManagement:
    '''
    The class for handling user shit. I.e. creating, deleting, modifying

    Note... there is nothing stopping a user from nuking the DB/deleting all the users and locking everyone out. 
    '''
    #[x] - probably good.
    @staticmethod
    def create_user(path_struct=None, username=None, password=None, roles=None):
        '''
        Creates users. Is an abstraction over the AuthenticationSQLDBHandler.create_user

        path_struct: The class instance containing path data
        username: username of user to create
        password: password of user to create
        roles: List of roles. Ex: ["filehost_admin", "iam_admin"]
        '''
        base_logging.logger.debug(f"{function_debug_symbol} {inspect.stack()[0][3]}")

        # Validate input parameters
        if not all([username, password, roles]):
            base_logging.logger.warning("Invalid input parameters for creating user")
            return False

        try:
            # Construct database path
            #db_absolute_path = os.path.join(path_struct.sys_path, "DataBases/users.db")

            # Initialize database handler
            db_instance = DataEngine.AuthenticationDBHandler.AuthenticationSQLDBHandler(
                db_path="DataBases/users.db"#db_absolute_path
            )

            # Hash the password
            password_blob = SecurityEngine.EncryptionHandler.Hashing.bcrypt_hash(data=password)
            if password_blob is None:
                base_logging.logger.warning("[*] password_blob is none, error occurred during hashing")
                return False

            # Create user in the database
            if not db_instance.create_api_user(username=username, password_blob=password_blob):
                base_logging.logger.warning("Failed to create user in the database")
                return False

            # Add roles to the user
            if not db_instance.add_api_role(username=username, roles=roles):
                base_logging.logger.warning("Failed to add roles to the user")
                return False

            return True

        except Exception as e:
            base_logging.logger.warning(f"Could not create user: {e}")
            return False

    
    @staticmethod
    def delete_user(path_struct=None, username=None):
        '''
        For deleting users. Is an abstraction over the AuthenticationSQLDBHandler.delete_user

        path_struct: The class instance containing path data
        username: The username to delete
        '''
        base_logging.logger.debug(f"{function_debug_symbol} {inspect.stack()[0][3]}")

        # Validate input parameters
        if not all([path_struct, username]):
            base_logging.logger.debug("Invalid input parameters for deleting user")
            return False

        try:
            # Construct database path
            db_absolute_path = os.path.join(path_struct.sys_path, "DataBases/users.db")

            # Initialize database handler
            db_instance = DataEngine.AuthenticationDBHandler.AuthenticationSQLDBHandler(
                db_path=db_absolute_path
            )

            # Delete user from the database
            if db_instance.delete_api_user(username=username):
                base_logging.logger.debug(f"Successfully deleted user '{username}'")
                return True
            else:
                base_logging.logger.debug(f"Failed to delete user '{username}'")
                return False

        except Exception as e:
            base_logging.logger.debug(f"Could not delete user: {e}")
            return False

    @staticmethod
    def change_user_password(username=None, password=None):
        '''
        For changing a users password

        username: username of user
        password: password of user
        
        '''
        base_logging.logger.debug(f"{function_debug_symbol} {inspect.stack()[0][3]}")

        # Validate input parameters
        if not all([username, password]):
            base_logging.logger.debug("Invalid input parameters for changing password")
            return False
        
        try:
            # Construct database path

            # Initialize database handler
            db_instance = DataEngine.AuthenticationDBHandler.AuthenticationSQLDBHandler(
                db_path="DataBases/users.db"
            )

            ## Check if user exists
            if not db_instance.get_api_username(username=username):
                base_logging.logger.warning("[*] User does not exist, cannot change password")
                return False


            ## Hash new password
            password_blob = SecurityEngine.EncryptionHandler.Hashing.bcrypt_hash(data=password)
            if password_blob is None:
                base_logging.logger.warning("[*] password_blob is none, error occurred during hashing")
                return False


            # Change user password
            if db_instance.change_api_user_password(username=username, password_hash=password_blob):
                base_logging.logger.debug(f"Successfully changed password for '{username}'")
                return True
            else:
                base_logging.logger.debug(f"Failed to change password for '{username}'")
                return False

        except Exception as e:
            base_logging.logger.debug(f"Could not change user password: {e}")
            return False


    @staticmethod
    def default_role_check_and_setup():
        '''
        A method to prompt, and create default roles if they *do not* exist. 

        Connects to DB, checks for the 'administrator' user with get_api_username, and 
        if it does not exists, calls UserManagement.create_user to create it.

        This is meant purely for the server first time startup.
        
        '''
        try:
            db_instance = DataEngine.AuthenticationDBHandler.AuthenticationSQLDBHandler(
                db_path="DataBases/users.db"#db_absolute_path
            )
        
            ## if Administrator user does not exist, create it.
            if not db_instance.get_api_username(username="administrator"):

                user_list = ["administrator"]

                for user in user_list:
                    print("=Init User Setup===============================")
                    print("No users detected by the server, creating users: ")
                    print("Note, the password will not be visible on screen")

                    password_1 = getpass.getpass(f"[>] Input password for {user}:")
                    password_2 = getpass.getpass(f"[>] Input password again for {user}:")

                    if password_1 != password_2: 
                        base_logging.logger.warning(f"{base_logging.logging_info_symbol} Passwords do not match!")
                        exit("Exiting, restart server & try again")
                        #return 
                    if UserManagement.create_user(username=user, password = password_1, roles=["iam_admin"]):
                        base_logging.logger.info(f"{base_logging.logging_info_symbol} User '{user}' created successfully")
                    else:
                        base_logging.logger.warning(f"{base_logging.logging_info_symbol} User '{user}' was not created")
        except Exception as e:
            base_logging.logger.critical(f"{base_logging.logging_critical_symbol} Could not create user")


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
