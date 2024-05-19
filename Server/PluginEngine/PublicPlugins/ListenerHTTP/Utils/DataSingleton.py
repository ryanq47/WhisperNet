## DataSIngleton for Listener ops

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
        self.Plugin = Plugin()
        self.Clients = Clients()
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
            self.logger.info(f"Client '{client_name}' exists.")
            return True
        else:
            self.logger.info(f"Client '{client_name}' does not exist.")
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
