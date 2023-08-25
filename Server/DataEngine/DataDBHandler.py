import sqlite3
import logging
import inspect
import Utils.UtilsHandler

function_debug_symbol = "[^]"

'''
Note, this handler is a little different than the other one. (save for DataSQLDBHandler) This one uses static classes to interact with the db, and the respective values are passed.
This allows for easier sectioning of commands for the DB & easier error checking (i.e. check the cursor & connection exist before each op).
This may come back to bite me, but I wanted to try it

'''


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
            logging.debug(f"{function_debug_symbol} {inspect.stack()[0][3]}: {e}")
    
    def connection_check(self):
        if self.dbconn == None:
            print("self.dbconn == None")
        if self.cursor == None:
            print("self.cursor == None")
    def wipe_db(self):
        """
        Initializes ALL TABLES in the DB.

        AKA wipes them & redoes them.

        ## DevNote: This is meant as a 'oh fuck nuke the DB' backup.
        """
        logging.debug(f"{function_debug_symbol} {inspect.stack()[0][3]}")
        pass

    def init_db(self):
        """
        Uses each classes' _create_table function to create tables if they do not exist.

        Note, this will NOT overwrite data, as each of the _create_table methods uses the 'CREATE TABLE IF NOT EXISTS' command
        """
        logging.debug(f"{function_debug_symbol} {inspect.stack()[0][3]}")
        self.stats_create_table()

    def stats_create_table(self):
        logging.debug(f"{function_debug_symbol} {inspect.stack()[0][3]}")
        self.connection_check()
        StatsHandlerDB._create_table(dbconn=self.dbconn, cursor=self.cursor)
    
    def stats_set_start_time(self):
        logging.debug(f"{function_debug_symbol} {inspect.stack()[0][3]}")
        self.connection_check()
        StatsHandlerDB._set_start_time(dbconn=self.dbconn, cursor=self.cursor)

    def stats_get_stats(self) -> str:
        logging.debug(f"{function_debug_symbol} {inspect.stack()[0][3]}")
        self.connection_check()
        return GeneralHandlerDB._get_data_in_table(dbconn=self.dbconn, cursor=self.cursor, table = "stats")



## All the logic is handled in these subclasses. Much cleaner that way
# set to "private" functinos as these should not be called directly, and instead use the above classes methods to call them

class GeneralHandlerDB:
    '''
    This class is for more generic DB actions, like getting all the data from a table. This is to
    prevent repeat functions
    
    '''
    def _get_data_in_table(dbconn = None, cursor = None, table = None):
        table_results = f'SELECT * FROM {table};'
        return table_results
        #print(table_results)

class StatsHandlerDB:

    def _create_table(dbconn = None, cursor = None):
        '''
        Creates stats table
        '''
        logging.debug(f"{function_debug_symbol} {inspect.stack()[0][3]}")

        cursor.execute(f'''
        CREATE TABLE IF NOT EXISTS stats (
        stat_name BLOB,
        stat_value BLOB
        )
        ''')
        dbconn.commit()

    def _set_start_time(dbconn = None, cursor = None):
        '''
        sets the server start time in the DataDB
        
        Get key... update start time... etc
        
        '''
        logging.debug(f"{function_debug_symbol} {inspect.stack()[0][3]}")

        time = Utils.UtilsHandler.timestamp()

        insert_query = f'INSERT INTO stats (stat_name, stat_value) VALUES (?, ?)'
        values = ("start_time",time)
        cursor.execute(insert_query, values)
        dbconn.commit()




