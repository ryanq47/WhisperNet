'''
A collection of singeltons/"structs" for different items taht may need to be globally access

'''


class PathStruct:
    _instance = None  # Private class variable to store the single instance
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(PathStruct, cls).__new__(cls)
            # Initialize your singleton object here
        return cls._instance
    
    def __init__(self):
        ## Holds the sys path to the server.py 
        self.sys_path = None