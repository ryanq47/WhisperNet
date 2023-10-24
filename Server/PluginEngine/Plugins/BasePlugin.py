'''
The base plugin. Required at the moment, and adds extra methods to sub classes that
could be useful.

'''
import inspect
from Utils.LoggingBaseClass import BaseLogging
import Utils.ErrorDefinitions
import threading
import concurrent.futures

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
    
    def cache_data(self, func) -> list:
        '''
        A decorator made to optimize "expensive" fucntions, and return the 
        results. Ideally, these results will be assigned to a varaible, so they can be 
        cached. Each function will run in a thread, so it won't be blocking

        args: func: The function you want to run. it MUST return ~something~
        
        Example problem I had:
            Each time a node tried to get file data from the server, it would run 'os.listdir()'. With one node this
            was doable, but crank it up to 5+ checking every 5 seconds, and you have a ton of uneccesary calculation going on. 
            This is meant to fix this, and not block the execution flow.
        
        '''
        def wrapper(*args, **kwargs):
            self.logger.debug(f"Starting cache")
            #print("Before the method is called.")

            ## Using concurrent in order to get data back from the function
            with concurrent.futures.ThreadPoolExecutor(max_workers=1) as executor:
                future = executor.submit(func, *args, **kwargs)
                
                # Wait for the thread to complete and retrieve the result
                result = future.result()

                return result

        # returning restul
        return wrapper
    

    

    