import sqlite3
import logging
import inspect
import Utils.UtilsHandler
import Utils.ErrorDefinitions
import Utils.GuardClauses
from Utils.LoggingBaseClass import BaseLogging

function_debug_symbol = "[^]"


class AuthenticationSQLDBHandler(BaseLogging):
    '''
    This DB handler is for Authentication

    DB is connected to on initilization of this class.
    
    '''

    def __init__(self, db_path):
        super().__init__()
        self.dbconn = None
        self.cursor = None
        self.connect_to_db(db_path)
        self.logger.debug(f"[*] Successful DB connection to {db_path}")

    def connect_to_db(self, db_path):
        '''
        Initiates the connection to the database

        sets self.dbconn to the connection
        sets self.curson to the cursor of self.dbconn
        
        '''
        self.logger.debug(f"{function_debug_symbol} {inspect.stack()[0][3]}")

        try:
            self.dbconn = sqlite3.connect(db_path)
            self.cursor = self.dbconn.cursor()
            self.logger.debug(f"[DBHandler.connect_to_db()] Successful connection to: {db_path}")


        except Exception as e:
            raise DataEngine.ErrorDefinitions.GENERAL_ERROR
        

    def get_username(self, username = None) -> bool:
        '''
        Get a username
        
        '''

        self.logger.debug(f"{function_debug_symbol} {inspect.stack()[0][3]}")

        # guard clause to check if username is none.
        if Utils.GuardClauses.guard_t_f_check(username is None, "[*] Username argument is 'None'!"):
            return False

        # check if user exists
        self.cursor.execute(f"SELECT 1 FROM users WHERE username = ?", (username,))

        result = self.cursor.fetchone()

        if result:
            return True
        
        else:
            return False

        # if exist, return true

    def get_api_username(self, username = None) -> bool:
        '''
        Get a username
        
        '''

        self.logger.debug(f"{function_debug_symbol} {inspect.stack()[0][3]}")

        # guard clause to check if username is none.
        if Utils.GuardClauses.guard_t_f_check(username is None, "[*] Username argument is 'None'!"):
            return False

        # check if user exists
        self.cursor.execute(f"SELECT 1 FROM api_users WHERE username = ?", (username,))

        result = self.cursor.fetchone()

        if result:
            return True
        
        else:
            return False

        # if exist, return true

    def get_api_password_blob(self, username = None):
        '''
        Get a password blob for API users. Exact copy of get_password_blob save for the table being accessed
        
        Note, may need to add a check for if more than one result is returned -- hey dipshit, fixed with primary keys
        '''
        self.logger.debug(f"{function_debug_symbol} {inspect.stack()[0][3]}")

        print(username)

        # guard clause to check if username is none.
        if Utils.GuardClauses.guard_t_f_check(username is None, "[*] Username argument is 'None'! Authentication will fail!"):
            return False

        try:
            self.cursor.execute(f"SELECT password_hash FROM api_users WHERE username = ?", (username,))

            password_hash = self.cursor.fetchone()

            if password_hash:
                return password_hash
            
            else:
                return False
        except Exception as e:
            print(f"[*] Error: {e}")

    def get_api_user_roll(self, username = None):
        '''
        Gets the role of the API user provided.

        returns a list of tupels

        [(admin, user)]        
        
        '''
        self.logger.debug(f"{function_debug_symbol} {inspect.stack()[0][3]}")

        print(username)

        # guard clause to check if username is none.
        if Utils.GuardClauses.guard_t_f_check(username is None, "[*] Username argument is 'None'! Authentication will fail!"):
            return False

        try:
            self.cursor.execute(f"SELECT role FROM api_users WHERE username = ?", (username,))

            role = self.cursor.fetchone()

            if role:
                return role
            
            else:
                return False
        except Exception as e:
            print(f"[*] Error: {e}")

    def create_api_user(self, username = None, password_blob = None) -> bool:
        '''
        The DB implementation of create_user. This directly accesses, and modifies the DB. Apart of the 
        AuthenticationSQLDBHandler class
        '''
        self.logger.debug(f"{function_debug_symbol} {inspect.stack()[0][3]}")
        
        try:
            insert_query = f'INSERT OR IGNORE INTO api_users (username, password_hash) VALUES (?, ?)'
            values = (username,password_blob)
            self.cursor.execute(insert_query, values)
            self.dbconn.commit()
            return True
        except sqlite3.IntegrityError:
            self.logger.warning(f"[*] User {username} already exists!")

        except:
            raise DataEngine.ErrorDefinitions.GENERAL_ERROR

        return False

    def delete_api_user(self, username = None) -> bool:
        '''
        The DB implementation of delete_user. This directly accesses, and modifies the DB. 
        Apart of the AuthenticationSQLDBHandler
        '''
        self.logger.debug(f"{function_debug_symbol} {inspect.stack()[0][3]}")

        try:
            delete_query = f'DELETE FROM api_users WHERE username = ?'
            values = (username,)
            self.cursor.execute(delete_query, values)
            self.dbconn.commit()
            return True
        
        except Exception as e:
            raise DataEngine.ErrorDefinitions.GENERAL_ERROR

    def create_table(self):
        """
        Creates table if needed

        user: blob
        pass: blob
        id: BLOB (not sure if needed)
        """
        self.logger.debug(f"{function_debug_symbol} {inspect.stack()[0][3]}")

        self.cursor.execute(f'''
        CREATE TABLE IF NOT EXISTS stats (
        username BLOB UNIQUE,
        password_hash BLOB,
        id BLOB UNIQUE
        )
        ''')
        self.cursor.commit()