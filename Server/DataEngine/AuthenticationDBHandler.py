import sqlite3
import logging
import inspect
import Utils.UtilsHandler
import DataEngine.ErrorDefinitions

function_debug_symbol = "[^]"


class AuthenticationSQLDBHandler:
    '''
    This DB handler is for Authentication

    DB is connected to on initilization of this class
    
    '''

    def __init__(self, db_name):
        self.dbconn = None
        self.cursor = None
        self.connect_to_db(db_name)
        logging.debug(f"[*] Successful DB connection to {db_name}")

    def connect_to_db(self, db_name):
        '''
        Initiates the connection to the database

        sets self.dbconn to the connection
        sets self.curson to the cursor of self.dbconn
        
        '''
        logging.debug(f"{function_debug_symbol} {inspect.stack()[0][3]}")

        try:
            self.dbconn = sqlite3.connect(db_name)
            self.cursor = self.dbconn.cursor()
            logging.debug(f"[DBHandler.connect_to_db()] Successful connection to: {db_name}")

        except Exception as e:
            raise DataEngine.ErrorDefinitions.GENERAL_ERROR
        

    def get_username(username = None) -> bool:
        '''
        Get a username
        
        '''

        # if exist, return true

    def get_password_blob(username = None):
        '''
        Get a password blob
        
        '''

        #return pass blob

    def create_user(username = None, password_blob = None):
        '''
        Creating a new user
        '''

    def delete_user(username = None):
        '''
        Deleting a new user
        '''

    def create_table():
        """
        Creates table if needed

        user: blob
        pass: blob
        id: int (not sure if needed)
        """