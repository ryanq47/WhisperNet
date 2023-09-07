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

function_debug_symbol = "[^]"

class Authentication:
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
        logging.debug(f"{function_debug_symbol} {inspect.stack()[0][3]}")

        print(f"User: {username}")

        server_absolute_path = path_struct.sys_path
        db_relative_path = "DataBases/users.db"
        db_absolute_path = os.path.join(server_absolute_path, db_relative_path)

        try:
            db_instance = DataEngine.AuthenticationDBHandler.AuthenticationSQLDBHandler(
                db_path=db_absolute_path
            )

            if db_instance.get_username(username=username):
                if Authentication._validate_password(db_instance=db_instance, username=username, password=password):
                    return True
            
        except Exception as e:
            # dosen't return anything, could be an issue?
            ## This could also be show stopper
            #raise Utils.ErrorDefinitions.GENERAL_ERROR
            logging.debug(f"Authentication Error: {e}")
        
        return False



    @staticmethod
    def _validate_password(db_instance=None, password=None, username=None) -> bool:
        '''
        Validates a username. Private Func,Should not be called from outside this class.

        '''
        logging.debug(f"{function_debug_symbol} {inspect.stack()[0][3]}")

        try:
            if Utils.GuardClauses.guard_t_f_check(username is None, "[*] Username argument is 'None'! Authentication will fail!"):
                return False

            pass_blob_tuple = db_instance.get_password_blob(username=username)
            ## blob is first item in tuple
            pass_blob = pass_blob_tuple[0]

            print(f"PassBlob: {pass_blob}")
            print(f"PassWord: {password}")


            if pass_blob == False:
                logging.debug(f"[*] Could not get password hash for user '{username}' from users.db")
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
                logging.info(f"Successful Login: '{username}':'{password}'")
                return True
            
            else:
                logging.warning(f"Bad Login: '{username}':'{password}'")
        
        except Exception as e:
            logging.debug(f"[*] Error: {e}")

        return False


class UserManagement:
    '''
    The class for handling user shit. I.e. creating, deleting, modifying lol
    '''
    @staticmethod
    def create_user(path_struct = None, username = None, password = None):
        logging.debug(f"{function_debug_symbol} {inspect.stack()[0][3]}")
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
            logging.debug(f"Could not connect to DB: {e}")
        
        return False
  