'''
Handles all encrpytion realted items needed
'''

import bcrypt
import Utils.ErrorDefinitions

class Hashing:
    def bcrypt_hash(data=None) -> bytes:
        '''
        Hashes the input item with bcrypt

        returns a byte representation of the hashed pw
        '''
        try:
            ## Convert to bytes
            byte_data = data.encode('utf-8')
            hashed_password = bcrypt.hashpw(byte_data, bcrypt.gensalt())

            return hashed_password
        except:
            raise Utils.ErrorDefinitions.GENERAL_ERROR
        
    # depracated, being weird
    def bcrypt_hash_and_compare(entered_data=None, stored_data=None) -> bool:
        '''
        compares entered_data to stored_data. 
        Used primarily for password hash checking

        entered_data: A raw string with data
        stored_data: The Bcrypt encrypted blob

        returns a bool, true == Success/they match
        '''
        try:
            ## Convert to bytes
            entered_data = entered_data.encode()
            stored_data = stored_data.encode()

            if bcrypt.checkpw(entered_data, stored_data):
                return True
            
            else:
                return False

        except:
            raise Utils.ErrorDefinitions.GENERAL_ERROR
