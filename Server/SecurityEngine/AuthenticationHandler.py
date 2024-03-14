import logging
import bcrypt
from DataEngine.AuthenticationSQLDBHandler import AuthenticationSQLDBHandler
from SecurityEngine.EncryptionHandler import PasswordManager
from flask_jwt_extended import get_jwt_identity
from functools import wraps
from flask import jsonify
from Utils.ApiHelper import api_response
import getpass
from Utils.Logger import LoggingSingleton

logger = LoggingSingleton.get_logger()

class Authentication():
    def __init__(self, db_path="DataBases/users.db"):
        self.db_instance = AuthenticationSQLDBHandler(db_path=db_path)

    def api_authentication_eval(self, username, password) -> bool:
        logger.debug(f"Starting API authentication evaluation for user {username}")
        
        if not username or not password:
            logger.warning("Username or password not provided for authentication")
            return False

        try:
            if not self.db_instance.get_api_username(username=username):
                logger.debug(f"Username {username} not found during authentication evaluation")
                return False

            if self._validate_api_password(username=username, password=password):
                logger.info(f"User {username} authenticated successfully")
                return True
            else:
                logger.debug(f"Incorrect password for user {username}")
                return False
        except Exception as e:
            logger.error(f"Authentication error for user {username}: {e}")
            raise

    def _validate_api_password(self, username, password) -> bool:
        logger.debug(f"Validating API password for user {username}")

        try:
            pass_blob_tuple = self.db_instance.get_api_password_blob(username=username)
            pass_blob = pass_blob_tuple[0]

            if not pass_blob:
                logger.debug(f"Could not get password hash for user '{username}' from users.db")
                return False

            if PasswordManager.verify_password(password, pass_blob):
                logger.info(f"Successful Login for user '{username}'")
                return True
            else:
                logger.warning(f"Bad Login attempt for user '{username}'")
                return False
        except Exception as e:
            logger.error(f"Error validating API password for user {username}: {e}")
            raise

    def api_get_user_role(self, username) -> list:
        logger.debug(f"Getting API user role for {username}")

        if not username:
            logger.warning("No username provided for role fetching")
            return []

        try:
            roles = self.db_instance.get_all_api_user_roles(username=username)

            if not roles:
                logger.warning(f"User {username} does not have any roles")
                return []

            return [role[1] for role in roles]
        except Exception as e:
            logger.error(f"Error fetching roles for user {username}: {e}")
            raise

class UserManagement(Authentication):
    def create_user(self, username, password, roles):
        logger.debug(f"Creating user {username} with roles {roles}")

        if not all([username, password, roles]):
            logger.warning("Invalid input parameters for creating user")
            return False

        try:
            password_blob = PasswordManager.hash_password(password)
            if not self.db_instance.create_api_user(username=username, password_blob=password_blob):
                logger.warning("Failed to create user in the database")
                return False

            if not self.db_instance.add_api_role(username=username, roles=roles):
                logger.warning("Failed to add roles to the user")
                return False

            logger.info(f"User {username} created successfully")
            return True
        except Exception as e:
            logger.error(f"Could not create user {username}: {e}")
            raise

    def delete_user(self, username):
        logger.debug(f"Deleting user {username}")

        if not username:
            logger.warning("Invalid input parameters for deleting user")
            return False

        try:
            if self.db_instance.delete_api_user(username=username):
                logger.info(f"Successfully deleted user '{username}'")
                return True
            else:
                logger.warning(f"Failed to delete user '{username}'")
                return False
        except Exception as e:
            logger.error(f"Could not delete user {username}: {e}")
            raise

    def change_user_password(self, username, password):
        logger.debug(f"Changing password for user {username}")

        if not all([username, password]):
            logger.warning("Invalid input parameters for changing password")
            return False

        try:
            password_blob = PasswordManager.hash_password(password)
            if self.db_instance.change_api_user_password(username=username, password_hash=password_blob):
                logger.info(f"Successfully changed password for '{username}'")
                return True
            else:
                logger.warning(f"Failed to change password for '{username}'")
                return False
        except Exception as e:
            logger.error(f"Could not change password for user {username}: {e}")
            raise

    def add_user_role(self, username, roles):
        logger.debug(f"Adding roles {roles} to user {username}")

        if not all([username, roles]):
            logger.warning("Invalid input parameters for adding user role")
            return False
        
        try:
            if not self.db_instance.add_api_role(username=username, roles=roles):
                logger.warning(f"Could not add roles to '{username}'")
                return False

            logger.info(f"Roles {roles} added to user '{username}' successfully")
            return True
        except Exception as e:
            logger.error(f"Could not add role to user {username}: {e}")
            raise

    def delete_user_role(self, username, roles):
        logger.debug(f"Deleting roles {roles} from user {username}")

        if not all([username, roles]):
            logger.warning("Invalid input parameters for deleting user role")
            return False

        try:
            if not self.db_instance.delete_api_role(username=username, roles=roles):
                logger.warning(f"Could not delete roles from '{username}'")
                return False

            logger.info(f"Roles {roles} deleted from user '{username}' successfully")
            return True
        except Exception as e:
            logger.error(f"Could not delete role from user {username}: {e}")
            raise

    def default_role_check_and_setup(self):
        logger.debug("Checking and setting up default roles")
        
        try:
            if not self.db_instance.get_api_username(username="administrator"):
                logger.info("No administrator user found, creating default administrator user")

                for user in ["administrator"]:
                    password_1 = getpass.getpass(f"Input password for {user}:")
                    password_2 = getpass.getpass(f"Input password again for {user}:")

                    if password_1 != password_2: 
                        logger.warning("Passwords do not match")
                        exit("Exiting, restart server & try again")
                    
                    if UserManagement.create_user(username=user, password=password_1, roles=["iam_admin"]):
                        logger.info(f"User '{user}' created successfully")
                    else:
                        logger.warning(f"User '{user}' was not created")
        except Exception as e:
            logger.critical(f"Critical error during default role setup: {e}")
            raise

class AccessManagement:
    @staticmethod
    def role_required(*required_roles):
        logger.debug(f"Role required decorator invoked with roles: {required_roles}")

        def decorator(func):
            @wraps(func)
            def wrapper(*args, **kwargs):
                try:
                    current_user = get_jwt_identity()
                    user_roles = current_user.get('role')

                    if not any(role in required_roles for role in user_roles):
                        logger.warning("Access denied due to insufficient roles")
                        return api_response(status_code=403)
                
                except Exception as e:
                    logger.error(f"Error in role_required decorator: {e}")
                    raise

                return func(*args, **kwargs)
            return wrapper
        return decorator
