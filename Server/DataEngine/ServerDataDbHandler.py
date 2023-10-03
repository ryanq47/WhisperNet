import sqlite3
import logging
import inspect

'''
This DB Handler handles the core quieries for the ServerData.db database.

'''

function_debug_symbol = "[*]"

class ServerDataDbHandler:
    def __init__(self):
        self.dbconn = None
        self.cursor = None
        # hardecoded as this module is not meant to be used for anything else
        self.connect_to_db("DataBases/ServerData.db")
        
    ## DB obs
    def connect_to_db(self, db_name):
        logging.debug(f"{function_debug_symbol} {inspect.stack()[0][3]}")

        try:
            self.dbconn = sqlite3.connect(db_name)
            self.cursor = self.dbconn.cursor()
            logging.debug(f"[DBHandler.connect_to_db()] Successful connection to: {db_name}")

        except Exception as e:
            logging.debug(f"[DBHandler.connect_to_db()] Error: {e}")

    def write_to_plugins_table(self, name, endpoint, author, type, loaded) -> bool:
        '''
        A method to write data to the plugins table.

        name (str): The name of the plugin
        endpoint (str): The endpoint of the plugin
        author (str): The author of the plugin
        type (str): The type of the plugin
        loaded (bool): Whether or not the plugin is loaded or not
        '''
        logging.debug(f"{function_debug_symbol} {inspect.stack()[0][3]}")

        if not self.guard_db_connection():
            return False
        
        ''' Note, this is currently handled by the DB primary key settign, which is the "name" column in the Plugins table
        if row_exists:
            self.update_plugin_row(name, endpoint, author, type, loaded)
        '''

        try:
            sql = "INSERT INTO Plugins (name, endpoint, author, type, loaded) VALUES (?, ?, ?, ?, ?)"
            values = (name, endpoint, author, type, loaded)
            self.cursor.execute(sql, values)
            self.dbconn.commit()
            return True
        
        except Exception as e:
            logging.warning(f"[*] {inspect.stack()[0][3]}: {e}")
            return False

    ######
    # Guard clauses
    ######
    def guard_db_connection(self) -> bool:
        '''
        A guard against the self.dbconn being None.
        '''
        logging.debug(f"{function_debug_symbol} {inspect.stack()[0][3]}")

        if self.dbconn is None:
            return False

        return True