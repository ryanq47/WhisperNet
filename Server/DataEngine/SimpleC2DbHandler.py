import sqlite3
import inspect
from Utils.LoggingBaseClass import BaseLogging
import time
'''
This DB Handler handles the core quieries for the ServerData.db database.

'''

function_debug_symbol = "[*]"

class SimpleC2DbHandler(BaseLogging):
    def __init__(self):
        super().__init__()
        self.dbconn = None
        self.cursor = None
        # hardecoded as this module is not meant to be used for anything else
        self.connect_to_db("DataBases/SimpleC2Data.db")
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

    def create_db_if_not_exist():
        '''
        If for some reason the DB does not exist, create it. 
        '''
        pass

    def write_client_data_to_table(self, client_name, data):
        '''
        Writes JSON posted by node to table in DB. 

        client_name (str): The client name. Used as the table name. 
        data: data from the posted request. 
        
        '''
        table_creation_sql = f"""CREATE TABLE IF NOT EXISTS {client_name} (
                                Data TEXT NOT NULL,
                                Timestamp INTEGER NOT NULL
                                );"""

        try:
            unix_timestamp = int(time.time())

            self.cursor.execute(table_creation_sql)

            ## dangerous, open to injection
            insert_sql = f"INSERT INTO {client_name} (Data, Timestamp) VALUES (?, ?);"

            self.cursor.execute(insert_sql, (data,unix_timestamp,))
            self.dbconn.commit()

        except Exception as e:
            self.logger.warning(f"{self.logging_warning_symbol} {inspect.stack()[0][3]}: {e}")
            self.dbconn.rollback()
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