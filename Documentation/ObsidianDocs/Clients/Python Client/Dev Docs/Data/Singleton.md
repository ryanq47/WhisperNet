
There is some data that needs to be accessed across the program, and that's where the singleton 'DataManager' class comes in handy

	## singleton test
	
	class DataManager:
	    '''
	    Singleton to hold data the progam needs.
	    current objects:
	
	        loaded_plugins_directory = Holds all the paths/directories of the loaded plugins
	    Currently using multiple attributes instead of one dict. That may come back to bite me later
	    '''
	    _instance = None
	    def __new__(cls):
	
	        if cls._instance is None:
	
	            cls._instance = super(DataManager, cls).__new__(cls)
	
	            #cls._instance.data = {}  # Store your shared data here -- may utilize in future
	
	            ## Holds loaded plugins
	
	            cls._instance.loaded_plugins_directory = []
	
	        return cls._instance

Currently, each data item is an attribute. 


| Attribute         | Desc     |
|--------------|-----------|
| loaded_plugins_directory | Holds the currently loaded plugins directories   | 
| Bananas      | **1.89**  |

