import random
import Utils.UtilsHandler
import logging
import inspect
import SecurityEngine.EncryptionHandler

class Authentication:
    '''
    The authentication interface for the whole platform. Pulls from the user.db database, and can be used to authentcation
    with whatever wild methods I come up with in the future. Flexible on purpose
    
    '''
    def authentication_eval():
        '''
        Checks if user is authorized for access

        Checks:
            - Username
            - Password

        '''

        ## Check username

        ## Check pass

    def _validate_username() -> bool:
        '''
        Validates a username
        '''

        ## conenct to db
            ## see if user exists

    def _validate_password(password=None, username=None) -> bool:
        '''
        Validates a username
        '''

        ## connect to db

        ## get username's password blob

        if SecurityEngine.EncryptionHandler.Hashing.bcrypt_hash_and_compare(

        ):
            return True
        
        return False


class UserManagement:
    '''
    The class for handling user shit. I.e. creating, deleting, modifying lol
    '''