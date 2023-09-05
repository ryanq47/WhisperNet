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
        

    def get_username(self, username = None) -> bool:
        '''
        Get a username
        
        '''
        # check if user exists
        self.cursor.execute(f"SELECT 1 FROM users WHERE username = ?", (username,))

        result = self.cursor.fetchone()

        if result:
            return True
        
        else:
            return False

        # if exist, return true

    def get_password_blob(self, username = None):
        '''
        Get a password blob
        

        Note, may need to add a check for if more than one result is returned
        '''
        self.cursor.execute(f"SELECT password_hash FROM users WHERE username = ?", (username,))

        password_hash = self.cursor.fetchone()

        if password_hash:
            return password_hash
        
        else:
            return False

        #return pass blob

    def create_user(self, username = None, password_blob = None):
        '''
        Creating a new user
        '''
        insert_query = f'INSERT INTO users (username, password_hash) VALUES (?, ?)'
        values = (username,password_blob)
        self.cursor.execute(insert_query, values)

    def delete_user(self, username = None):
        '''
        Deleting a new user
        '''
    
        delete_query = f'DELETE FROM users WHERE username = ?'
        values = (username)
        self.cursor.execute(delete_query, values)

    def create_table(self):
        """
        Creates table if needed

        user: blob
        pass: blob
        id: BLOB (not sure if needed)
        """
        self.cursor.execute(f'''
        CREATE TABLE IF NOT EXISTS stats (
        username BLOB,
        password_hash BLOB,
        id BLOB
        )
        ''')
        self.cursor.commit()