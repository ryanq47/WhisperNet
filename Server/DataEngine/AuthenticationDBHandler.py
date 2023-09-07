import sqlite3
import logging
import inspect
import Utils.UtilsHandler
import DataEngine.ErrorDefinitions
import Utils.GuardClauses

function_debug_symbol = "[^]"


class AuthenticationSQLDBHandler:
    '''
    This DB handler is for Authentication

    DB is connected to on initilization of this class
    
    '''

    def __init__(self, db_path):
        self.dbconn = None
        self.cursor = None
        self.connect_to_db(db_path)
        logging.debug(f"[*] Successful DB connection to {db_path}")

    def connect_to_db(self, db_path):
        '''
        Initiates the connection to the database

        sets self.dbconn to the connection
        sets self.curson to the cursor of self.dbconn
        
        '''
        logging.debug(f"{function_debug_symbol} {inspect.stack()[0][3]}")

        try:
            self.dbconn = sqlite3.connect(db_path)
            self.cursor = self.dbconn.cursor()
            logging.debug(f"[DBHandler.connect_to_db()] Successful connection to: {db_path}")


        except Exception as e:
            raise DataEngine.ErrorDefinitions.GENERAL_ERROR
        

    def get_username(self, username = None) -> bool:
        '''
        Get a username
        
        '''

        logging.debug(f"{function_debug_symbol} {inspect.stack()[0][3]}")

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

    def get_password_blob(self, username = None):
        '''
        Get a password blob
        

        Note, may need to add a check for if more than one result is returned
        '''
        logging.debug(f"{function_debug_symbol} {inspect.stack()[0][3]}")

        print(username)

        # guard clause to check if username is none.
        if Utils.GuardClauses.guard_t_f_check(username is None, "[*] Username argument is 'None'! Authentication will fail!"):
            return False

        try:
            self.cursor.execute(f"SELECT password_hash FROM users WHERE username = ?", (username,))

            password_hash = self.cursor.fetchone()

            if password_hash:
                return password_hash
            
            else:
                return False
        except Exception as e:
            print(f"[*] Error: {e}")

        #return pass blob

    def create_user(self, username = None, password_blob = None) -> bool:
        '''
        Creating a new user. Returns True if successful
        '''
        logging.debug(f"{function_debug_symbol} {inspect.stack()[0][3]}")
        
        try:
            insert_query = f'INSERT OR IGNORE INTO users (username, password_hash) VALUES (?, ?)'
            values = (username,password_blob)
            self.cursor.execute(insert_query, values)
            self.dbconn.commit()
            return True
        except sqlite3.IntegrityError:
            logging.warning(f"[*] User {username} already exists!")
        return False

    def delete_user(self, username = None) -> bool:
        '''
        Deleting a user. Returns True if successful
        '''
        logging.debug(f"{function_debug_symbol} {inspect.stack()[0][3]}")

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
        logging.debug(f"{function_debug_symbol} {inspect.stack()[0][3]}")

        self.cursor.execute(f'''
        CREATE TABLE IF NOT EXISTS stats (
        username BLOB UNIQUE,
        password_hash BLOB,
        id BLOB UNIQUE
        )
        ''')
        self.cursor.commit()