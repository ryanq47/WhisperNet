## DataSIngleton for Listener ops

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
        self.Plugin = Plugin()
        self.Clients = Clients()
        self.Config = Config()

        self._initialized = True

class Plugin:
    def __init__(self):
        self.logger = LoggingSingleton.get_logger()
        #add a getter
        self._standalone = False

    @property
    def standalone(self):
        self.logger.debug("Accessing _standalone: %s", self._sys_path)
        return self._standalone

    @standalone.setter
    def standalone(self, value=bool):
        self._standalone = value
        self.logger.debug(f"standalone set to: {value}")


class Clients:
    def __init__(self):
        self.logger = LoggingSingleton.get_logger()
        self._clients = {}

    def add_new_client(self, client_name, client_object, **client_info):
        """Add new client to self._clients dict.

            Add new client info arguments as needed, such as IP, etc. 

        Args:
            client_name (str): The name of the client to add.
            **client_info: Additional details about the client.
        """
        self._clients[client_name] = {
                "info": client_info,
                "object": client_object
        }
        self.logger.info(f"Added new client: {client_name}")
        #if client_name not in self._clients:
            #client_obj = Client(client_name, **client_info)

        #else:
            # should not happen - but just in case it does.
            #self.logger.warning(f"Client '{client_name}' already exists.")

    def remove_client(self, client_name):
        """Remove client from _clients dict.

        Args:
            client_name (str): The name of the client to remove.

        Returns:
            bool: True if the client was removed, False if the client was not found.
        """
        if client_name in self._clients:
            del self._clients[client_name]
            self.logger.info(f"Removed client: {client_name}")
            return True
        else:
            self.logger.warning(f"Client '{client_name}' not found.")
            return False

    def check_if_client_exists(self, client_name):
        """Check if a client exists in the _clients dictionary.

        Args:
            client_name (str): The name of the client to check.

        Returns:
            bool: True if the client exists, False otherwise.
        """
        if client_name in self._clients:
            self.logger.debug(f"Client '{client_name}' exists.")
            return True
        else:
            self.logger.debug(f"Client '{client_name}' does not exist.")
            return False

    def get_client_info(self, client_name):
        """Retrieve the client info.

        Args:
            client_name (str): The name of the client.

        Returns:
            dict: The client's info if found, None otherwise.
        """
        if client_name in self._clients:
            return self._clients[client_name]["info"]
        else:
            self.logger.warning(f"Client '{client_name}' not found.")
            return None

    def get_client_object(self, client_name):
        """Retrieve the client class object.

        Args:
            client_name (str): The name of the client.

        Returns:
            Client: The client class object if found, None otherwise.
        """
        if client_name in self._clients:
            return self._clients[client_name]["object"]
        else:
            self.logger.warning(f"Client '{client_name}' not found.")
            return None
        
class Paths:
    def __init__(self):
        self.logger = LoggingSingleton.get_logger()
        self._sys_path = None

    # Getter and setter for sys_path
    @property
    def sys_path(self):
        self.logger.debug("Accessing sys_path: %s", self._sys_path)
        return self._sys_path

    @sys_path.setter
    def sys_path(self, value):
        self._sys_path = value
        self.logger.debug(f"sys_path set to: {value}")


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


# Example usage:
'''
if __name__ == "__main__":
    config_file_path = "sample_plugin_config.yaml"  # Replace with your config file path
    plugin_config = PluginConfig(config_file_path)

    if plugin_config.load_config():
        option1_value = plugin_config.get_value("configuration.option1")
        option2_value = plugin_config.get_value("configuration.option2")
        
        print(f"Option 1 value: {option1_value}")
        print(f"Option 2 value: {option
'''