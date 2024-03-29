from Utils.Logger import LoggingSingleton

class Data:
    _instance = None

    def __new__(cls):
        if not cls._instance:
            # print("==== INIT =====")
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        if hasattr(self, '_initialized'):
            return
        self.Paths = Paths()
        self.Listeners = Listeners()
        self._initialized = True


# Info about the models/where they are at, etc
class Paths:
    def __init__(self):
        self.logger = LoggingSingleton.get_logger()
        self._users_db_path = None
        self._sys_path = None

    # Getter and setter for users_db_path
    @property
    def users_db_path(self):
        self.logger.debug("Accessing users_db_path: %s", self._users_db_path)
        return self._users_db_path

    @users_db_path.setter
    def users_db_path(self, value):
        self._users_db_path = value
        self.logger.debug(f"users_db_path set to: {value}")

    # Getter and setter for sys_path
    @property
    def sys_path(self):
        self.logger.debug("Accessing sys_path: %s", self._sys_path)
        return self._sys_path

    @sys_path.setter
    def sys_path(self, value):
        self._sys_path = value
        self.logger.debug(f"sys_path set to: {value}")

    def load_data(self):
        try:
            self.Data = Data()

            ## Set data items
            self.Data.Paths.users_db_path = "DataBases/users.db"
        except Exception as e:
            self.logger.critical(f"Error loading Data: {e}")



# not currently used.
class Config:
    def __init__(self):
        self.logger = LoggingSingleton.get_logger()


class Properties:
    def __init__(self):
        self.logger = LoggingSingleton.get_logger()


## Quick Docs, using nested dics for fast lookups instead a list of dicts
        
## add to dict with #dict["user3"] = {"name": "Alice Doe", "email": "alicedoe@example.com"}

# NOTE, all protocol object names, suhc as HTTP, or SMB, etc are capatalized in the data singletonton casue I think it looks nicer

class Listeners:
    def __init__(self):
        self.logger = LoggingSingleton.get_logger()
        self.HTTP = Http()


class Http:
    def __init__(self):
        self.logger = LoggingSingleton.get_logger()
        #add a getter
        self.http_listeners = {}

    def add_listener(self, process = None, info = None):
        """Add an HTTP listener to the http_listeners dict in the Data singleton. 

        Args:
            class_object: The class object of the listener. 
            nickname: The nickanme of the listener
        """

        # QUick docs:
            #class_object: object of the http listener class. Can be used to pull other data like bind addr
            #nickname: A nickname for faster/quicker lookups. Not sure how much faster, but def faster than going 
                #through each class intance & pulling the nickname attribute.
        self.logger.debug("Adding http listener to data singleton")
        listener_dict = {
            # process object
            "process":process,
            # Data about the listener.
            # ex listener_dict["info"]["nickname"]
            "info":info
        }

        ## Adding to http_listeners dict
        nickname = info["nickname"]
        self.http_listeners[nickname] = listener_dict

        self.logger.debug(self.http_listeners)

    def get_listener_by_nickname(self, nickname = None):
        listener_info = self.http_listeners.get(nickname, None)
        if listener_info is not None:
            return listener_info
        else:
            self.logger.warning(f"Listener with nickname {nickname} not found.")
            return None

    def get_listeners(self):
        """
        Quick and dirty getter. 

        Returns:
            dict: The dictionary of HTTP listeners
        """
        return self.http_listeners

'''
        listener_dict = {
            "class_object":"classobjectofspawnedlistener",
            "nickname":nickname
        }
'''

    


