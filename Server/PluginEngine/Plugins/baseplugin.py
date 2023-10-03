'''
The base plugin. Required at the moment, and adds extra methods to sub classes that
could be useful.


'''


class BasePlugin:
    def __init__(self, app, DataStruct):
        self.app = app
        self.print_symbol = "[*]"
        ## A class with data that might be handy
        self.DataStruct = DataStruct
        print("BaseClass init")
        self.db = None


    def register_routes(self):
        # Define common route registration logic here.
        pass

    def database_connect(self) -> bool:
        '''
        Connect to DB
        '''
        ...

        #self.db = connected_db_instance

    def database_interact(self, query) -> str:
        '''
        Interact with DB. 

        Warning/Coding note: This needs to be secure. 
        
        '''

        ## Guard: If self.db is None, then throw/return error or something.
        ## Need to figure out if that error will end up on screen or silently fail

        pass
        return "results"
    

    