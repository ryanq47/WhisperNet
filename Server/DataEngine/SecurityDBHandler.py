import sqlite3
import logging
import inspect
import Utils.UtilsHandler

class DataSQLDBHandler:
    '''
    This DB handler is for Data. The other is for handling the agents & their commands.

    DB is connected to on initilization of this class
    
    '''

    def __init__(self, db_name):
        self.dbconn = None
        self.cursor = None
        self.connect_to_db(db_name)
        logging.debug(f"[*] Successful DB connection to {db_name}")