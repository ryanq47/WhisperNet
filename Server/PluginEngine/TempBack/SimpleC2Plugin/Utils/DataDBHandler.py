import sqlite3


class FilehostDataDBHandler:
    '''
    FileHost DB handler for the FileHostDB.db
    
    '''
    def __init__(self):
        pass


    def update_plugin_checkin_data(self):
        '''
        Updates, (or creates if row doesnt exist)
        a row in the plugin_checkin_data table.

        This table is used for getting the current "nodes" or external plugins
        
        '''
        ...

    def get_plugin_checkin_data(self):
        '''
        retrieves data from the plugin_checkin_data table, for use by
        the webserver
        
        '''
        ...