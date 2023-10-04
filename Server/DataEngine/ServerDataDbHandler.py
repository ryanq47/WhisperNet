import sqlite3
import inspect
from Utils.LoggingBaseClass import BaseLogging

'''
This DB Handler handles the core quieries for the ServerData.db database.

'''

function_debug_symbol = "[*]"

class ServerDataDbHandler(BaseLogging):
    def __init__(self):
        super().__init__()
        self.dbconn = None
        self.cursor = None
        # hardecoded as this module is not meant to be used for anything else
        self.connect_to_db("DataBases/ServerData.db")
        #self.logger = super().logger

    ## DB obs
    def connect_to_db(self, db_name):
        self.logger.debug(f"{self.function_debug_symbol} {inspect.stack()[0][3]}")

        try:
            self.dbconn = sqlite3.connect(db_name)
            self.cursor = self.dbconn.cursor()
            self.logger.info(f"{self.logging_info_symbol} Successful connection to: {db_name}")

        except Exception as e:
            self.logger.warning(f"{self.logging_warning_symbol} Error: {e}")

    def write_to_plugins_table(self, name, endpoint, author, type, loaded) -> bool:
        '''
        A method to write data to the plugins table.

        name (str): The name of the plugin
        endpoint (str): The endpoint of the plugin
        author (str): The author of the plugin
        type (str): The type of the plugin
        loaded (bool): Whether or not the plugin is loaded or not
        '''
        self.logger.debug(f"{self.function_debug_symbol} {inspect.stack()[0][3]}")

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
            #self.dbconn.close()
            return True
        
        except Exception as e:
            self.logger.warning(f"{self.logging_warning_symbol} {inspect.stack()[0][3]}: {e}")
            self.dbconn.rollback()
            return False
    

    def retrieve_plugins_from_table(self, cursor = None):
        '''
        A method to retirieve plugins from the Plugins table

        REturn a string (actaully I think it's a tuple... need to check) on success, or a bool (false) on failure

        '''
        self.logger.debug(f"{self.function_debug_symbol} {inspect.stack()[0][3]}")

        #if not self.guard_db_connection():
            #return False
        
        ''' Note, this is currently handled by the DB primary key settign, which is the "name" column in the Plugins table
        if row_exists:
            self.update_plugin_row(name, endpoint, author, type, loaded)
        '''

        try:
            sql = "SELECT name, endpoint, author, type, loaded FROM Plugins"
            cursor.execute(sql)
            data = cursor.fetchall()
            return data
        
        except Exception as e:
            self.logger.warning(f"{self.logging_warning_symbol} {inspect.stack()[0][3]}: {e}")
            return False


    ######
    # Guard clauses
    ######
    def guard_db_connection(self) -> bool:
        '''
        A guard against the self.dbconn being None.
        '''
        self.logger.debug(f"{self.function_debug_symbol} {inspect.stack()[0][3]}")

        if self.dbconn is None:
            self.logger.warning(f"{self.logging_info_symbol} Connection to DB is None.")
            return False

        return True