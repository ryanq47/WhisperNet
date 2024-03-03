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
        self._initialized = True


# Info about the models/where they are at, etc
class Paths:
    def __init__(self):
        self.logger = LoggingSingleton.get_logger()
        self._db_path = None
        self._sys_path = None

    # Getter and setter for db_path
    @property
    def db_path(self):
        self.logger.debug("Accessing db_path: %s", self._db_path)
        return self._db_path

    @db_path.setter
    def db_path(self, value):
        self._db_path = value
        self.logger.debug(f"db_path set to: {value}")

    # Getter and setter for sys_path
    @property
    def sys_path(self):
        self.logger.debug("Accessing sys_path: %s", self._sys_path)
        return self._sys_path

    @sys_path.setter
    def sys_path(self, value):
        self._sys_path = value
        self.logger.debug(f"sys_path set to: {value}")


