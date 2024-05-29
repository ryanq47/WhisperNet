from Utils.Logger import LoggingSingleton
import yaml

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
        self.Config = Config()
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
        self._config_file_path = None  # config_file_path
        self._config = None

    # Getter for config_file_path
    @property
    def config_file_path(self):
        return self._config_file_path

    # Setter for config_file_path
    @config_file_path.setter
    def config_file_path(self, value):
        self._config_file_path = value

    # Getter for config
    @property
    def config(self):
        return self._config

    # Setter for config
    @config.setter
    def config(self, value):
        self._config = value

    # load the config
    def load_config(self, config_file_path = None):
        self.logger.info(f"Loading listener config: {self.config_file_path}")

        #if a path is passed in, use it.
        if config_file_path:
            self.config_file_path = config_file_path

        try:
            with open(self._config_file_path, 'r') as config_file:
                self._config = yaml.safe_load(config_file)
                #print(self._config)
                if self._config is None:
                    self.logger.info(f"Config file could not be loaded!")

                else:
                    self.logger.info(f"Config loaded successfully!: {self.config_file_path}")

        except Exception as e:
            # this is bad
            self.logger.critical(f"Error loading configuration from {self._config_file_path}: {e}")
            exit()

    def get_value(self, key, default=None):
        """
        Retrieve a value from the loaded configuration.
        
        :param key: The key to look up in the configuration.
        :param default: The default value to return if the key is not found.
        :return: The value from the configuration or the default value.
        """
        if not self._config:
            self.logger.error("Configuration not loaded. Call load_config() first.")
            return default

        keys = key.split('.')
        value = self._config
        try:
            for k in keys:
                value = value[k]
            return value
        except KeyError:
            self.logger.error(f"Key '{key}' not found in configuration.")
            return default


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
        self.HTTPProcess = HttpProcess()

class HttpProcess:
    """For managing listeners local processess.
    """
    def __init__(self):
        self.logger = LoggingSingleton.get_logger()
        #add a getter
        self.http_listeners = {}

    def add_listener_process(self, process=None, info=None):
        """For managing listener processes spun up locally.

        Args:
            process (_type_): Process of lsitener
            info (_type_): Info dict of listener
        """
        self.logger.debug("Adding http listener to data singleton")
        listener_dict = {
            #  object
            "process":process,
            # address of listener
            "info":info
        }

        # for the switch to lpid
        #lpid = info["lpid"]
        #self.http_listeners[lpid] = listener_dict

        nickname = info["nickname"]
        self.http_listeners[nickname] = listener_dict

    def get_listener_process_by_lpid(self, lpid = None):
        listener_info = self.http_listeners.get(lpid, None)
        if listener_info is not None:
            return listener_info
        else:
            self.logger.warning(f"Listener with nickname {lpid} not found.")
            return None
        
    def get_listener_process_by_nickname(self, nickname = None):
        listener_info = self.http_listeners.get(nickname, None)
        if listener_info is not None:
            return listener_info

        else:
            self.logger.warning(f"Listener process {nickname} has no info.")
            return None

    def get_listeners(self):
        """
        Quick and dirty getter. 

        Returns:
            dict: The dictionary of HTTP listeners
        """
        return self.http_listeners

class Http:
    """For managing listeners over HTTP
    """
    def __init__(self):
        self.logger = LoggingSingleton.get_logger()
        #add a getter
        self.http_listeners = {}
        ## Synced data. uhhh can prolly call this somethign diff.
        self.synced_data_store = [] # Dictionary to hold other dictionaries

    ## Process Based Functions - shuold probably split into 2 classes. 


    ## Class based fucntions

    def add_listener(self, class_object = None, lid=None):
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
            #  object
            "class_object":class_object,
            # address of listener
            "lid":lid
        }
        # any other data is stored in the lsitener class

        ## Adding to http_listeners dict
        self.http_listeners[lid] = listener_dict

        self.logger.debug(self.http_listeners)

    def get_listener_class_object_by_lid(self, lid=None):
        """
        Retrieve a listener class object by its listener ID (lid).

        Args:
            lid: The listener ID.

        Returns:
            dict or None: The dictionary containing listener information if found, otherwise None.
        """
        listener_info = self.http_listeners.get(lid, None)
        if listener_info is not None:
            if listener_info["class_object"] is not None:
                return listener_info["class_object"]
            else:
                self.logger.warning(f"Listener {lid} class object is empty!")
            #return listener_info[]
        else:
            self.logger.warning(f"Lookup for Listener with ID {lid} not found.")
            return None

    def get_listener_by_lid(self, lid=None):
        """
        Retrieve a listener dict by its listener ID (lid).

        Args:
            lid: The listener ID.

        Returns:
            dict or None: The dictionary containing listener information if found, otherwise None.

        listener_dict = {
            #  object
            "class_object":class_object,
            # listener ID
            "lid":lid
        }
        """
        listener_info = self.http_listeners.get(lid, None)
        if listener_info is not None:

            return listener_info
            #return listener_info[]
        else:
            self.logger.warning(f"Lookup for Listener with ID {lid} not found.")
            return None

    def get_listeners(self):
        """
        Quick and dirty getter. 

        Returns:
            dict: The dictionary of HTTP listeners
        """
        return self.http_listeners

    def add_synced_data(self, data):
        """
        Adds a dictionary to the synced data store under a specified unique key.

        Args:
            key (str): The unique key under which the data should be stored.
            data (dict): A dictionary containing key-value pairs to be stored.


        #notes... if you need lookups/searches in the future (like specific id's)
        use a dict.
        """
        # Check that the input data is a dictionary

        # Log the action of adding data
        #self.logger.info(f"Adding data to sync store.")

        # Add or update the dictionary under the unique key in the store
        #self.synced_data_store[key] = data
        self.synced_data_store.append(data)

        # Log the addition
        #self.logger.debug(f"Data entry added")
        #self.logger.debug(f"Size of synced_data_store: {len(self.synced_data_store)} elements")
        
    def get_client_listener(self, cid = None):
        for listener_info in self.http_listeners.values():
            listener_class_object = listener_info.get('class_object')
            if listener_class_object:
                listener_class_object.check_if_client_is_apart_of_listener(cid)
                return listener_class_object


'''
        listener_dict = {
            "class_object":"classobjectofspawnedlistener",
            "nickname":nickname
        }
'''

    


