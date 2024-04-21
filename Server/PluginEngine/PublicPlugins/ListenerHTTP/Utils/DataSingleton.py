## DataSIngleton for Listener ops

## This is universal between standalone mode and integrated mode
#from Utils.DataSingleton import Data

## Universal path between standalone mode and integrated mode
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
        #add a getter
        self.http_listeners = {}


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
