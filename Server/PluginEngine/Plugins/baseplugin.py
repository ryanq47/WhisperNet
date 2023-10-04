'''
The base plugin. Required at the moment, and adds extra methods to sub classes that
could be useful.


'''
import inspect
from Utils.LoggingBaseClass import BaseLogging
import Utils.ErrorDefinitions

class BasePlugin(BaseLogging):
    def __init__(self, app, DataStruct):
        # breaks stuff, cause it's using the instance that calls it and that doesn't have logging implemented when called 
        ## as BasePlugin is called first. Design flaw for sure
        #self.logger.debug(f"{self.function_debug_symbol} {inspect.stack()[0][3]}")
        try:
            self.app = app
            self.print_symbol = "[*]"
            ## A class with data that might be handy
            self.DataStruct = DataStruct
            #print("BaseClass init")
            self.db = None
        except Exception as e:
            raise Utils.ErrorDefinitions.INIT_ERROR()


    def register_routes(self):
        # Define common route registration logic here.
        self.logger.debug(f"{self.function_debug_symbol} {inspect.stack()[0][3]}")

        pass

    def database_connect(self) -> bool:
        '''
        Connect to DB
        '''
        self.logger.debug(f"{self.function_debug_symbol} {inspect.stack()[0][3]}")
        ...

        #self.db = connected_db_instance

    def database_interact(self, query) -> str:
        '''
        Interact with DB. 

        Warning/Coding note: This needs to be secure. 
        
        '''
        self.logger.debug(f"{self.function_debug_symbol} {inspect.stack()[0][3]}")

        ## Guard: If self.db is None, then throw/return error or something.
        ## Need to figure out if that error will end up on screen or silently fail

        pass
        return "results"
    

    

    