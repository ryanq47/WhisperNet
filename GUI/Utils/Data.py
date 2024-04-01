'''
some notes


Every attribute starts as None. On errors when trying to set thigns, set them back to none. See Login.py at the json decoding for this
'''

## Singleton class, holds all data stuff needed
## Make OOP as fuck
from typing import Optional
from PySide6.QtCore import QObject, Property, Slot, Signal
from Utils.Logger import LoggingSingleton
import json
import inspect


class Data(QObject):
    _instance = None
    _is_initialized = False  # Add an initialization flag


    # signleton stuff
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(Data, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self, parent=None):
        if not self._is_initialized:  # Check if already initialized, sanity check
            super().__init__(parent)
            self.logger = LoggingSingleton.get_logger()
            self._auth = Auth(self)
            self._simplec2 = SimpleC2Data(self)

            # object is getting created correctly
            #self._auth.jwt = "balls"
            #print(self._auth.jwt)

            self._is_initialized = True  # Mark as initialized
            #self.logger.debug(f"Initialized Backend Component: {self.__class__.__name__}")

    # have to do special getter/setter for qt
    @Property(QObject)
    def auth(self):
        return self._auth

    @Property(QObject)
    def simplec2(self):
        return self._simplec2


## apparently not being init/defined for qml. somethings up, same issue I had befoer
class Auth(QObject):
    jwtChanged = Signal(str)  # Signal emitting the new JWT value

    def __init__(self, parent=None):
        super().__init__(parent)
        self._jwt = None

        #self.logger.debug(f"Initialized Backend Component: {self.__class__.__name__}")

    @Slot()
    def get_jwt(self):
        return self._jwt

    ## works now, DOC THIS TOMORROW OR WHENEVER. +1 for signals being cool, lets keep this format of signals after (any?) item is changed in data class, or wherver necessary
    @Slot(str)
    def set_jwt(self, value):
        if self._jwt != value:
            self._jwt = value
            # Emit signal if needed, e.g., self.jwtChanged.emit(value)
            self.jwtChanged.emit(self._jwt)  # Emit signal with new value

    # getter/setters a little dif. Define the property, access with just class.class.jwt,
    jwt = Property(str, get_jwt, set_jwt)


class SimpleC2Data(QObject):
    client_data_updated = Signal(list)
    db_data_updated = Signal()
    db_network_data_updated = Signal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.logger = LoggingSingleton.get_logger()
        self._listeners = Listener(self)
        self._db_data = None # Current Database Data, in dict
        self._db_network_data = None
        # might need one just for json later. 

    @Slot()
    def get_db_data(self):
        return self._db_data

    @Property(QObject)
    def listener(self):
        return self._listeners

    ## works now, DOC THIS TOMORROW OR WHENEVER. +1 for signals being cool, lets keep this format of signals after (any?) item is changed in data class, or wherver necessary
    @Slot(str)
    def set_db_data(self, data):
        if type(data) == str:
            self.logger.debug(f"{self.__class__.__name__}.{inspect.currentframe().f_code.co_name}: 'data' was in JSON format, converting to dict before setting self._db_data")
            data = json.loads(data)


        self._db_data = data
        self.db_data_updated.emit()
        
        #print("settign data in data")
        #print(data)
        #print(self._db_data)

            #self.jwtChanged.emit(self._jwt)  # Emit signal with new value
    db_data = Property(str, get_db_data, set_db_data)

    ## db_network_data
    @Slot()
    def get_db_network_data(self):
        return self._db_data

    ## works now, DOC THIS TOMORROW OR WHENEVER. +1 for signals being cool, lets keep this format of signals after (any?) item is changed in data class, or wherver necessary
    @Slot(str)
    def set_db_network_data(self, data):
        if type(data) == str:
            self.logger.debug(f"{self.__class__.__name__}.{inspect.currentframe().f_code.co_name}: 'data' was in JSON format, converting to dict before setting self.db_network_data")
            data = json.loads(data)
        self._db_network_data = data
        self.db_network_data_updated.emit()
        
    db_network_data = Property(str, get_db_network_data, set_db_network_data)

        
    ## don't need anymore
    def parse_data_for_gui(self) -> list:#-> tuple[dict]:
        '''
        Parses the data from JSON/PyDict (in self._db_data) into a list of dicts. 

        # Dev notes, maybe add an option to pass in data through an arg, then check if that arg is empty or not, to determine where to pull data from        
        '''
        self.logger.debug(f"{self.__class__.__name__}.{inspect.currentframe().f_code.co_name}: parsing self._db_data into tuple of dicts")

        if self._db_data is None:
            self.logger.warning(f"{self.__class__.__name__}.{inspect.currentframe().f_code.co_name}: self._db_data was empty, cannot parse data.")
            return {}
        

        output_list = []
        #print(type(self._db_data))

        for node_key in self._db_data["data"]["nodes"]:
            node = self._db_data["data"]["nodes"][node_key]
            print(node["properties"]["nickname"])

            # a bit inneficent as we aer just recreating the data in node, but this offers more control at the moment
            output_dict = {
                "identity": node["identity"],
                "labels": node["labels"],
                "properties": node["properties"]
            }

            #print(output_dict["properties"]["name"])
            #return output_dict
            output_list.append(output_dict)

        self.client_data_updated.emit(output_list)
        #return output_list


class Listener(QObject):
    """Class to hold listener items in the data singleton
    """
    listenerDataChanged = Signal(dict)  # Signal emitting the new JWT value

    def __init__(self, parent=None):
        super().__init__(parent)
        self._listener_data_dict = None

        #self.logger.debug(f"Initialized Backend Component: {self.__class__.__name__}")

    @Slot()
    def get_listener_data(self):
        return self._listener_data_dict

    ## works now, DOC THIS TOMORROW OR WHENEVER. +1 for signals being cool, lets keep this format of signals after (any?) item is changed in data class, or wherver necessary
    @Slot(str)
    def set_listener_data(self, value):
        # Check if items are the same, if not, update & emit signal
        if self._listener_data_dict != value:
            self._listener_data_dict = value
            # Emit signal if needed, e.g., self.jwtChanged.emit(value)
            self.listenerDataChanged.emit(self._listener_data_dict)  # Emit signal with new value

    # getter/setters a little dif. Define the property, access with just class.class.jwt,
    listener_data = Property(dict, get_listener_data, set_listener_data)

class Server(QObject):
    """Class to hold server related data in the Data singleton
    """
    serverAddressUpdated = Signal(str)  # Signal emitting the new JWT value
    serverPortUpdated = Signal(str) # could be int too

    def __init__(self, parent=None):
        super().__init__(parent)
        self._server_address = None
        self._server_port = None

        #self.logger.debug(f"Initialized Backend Component: {self.__class__.__name__}")

    @Slot()
    def get_server_address(self):
        return self._server_address

    @Slot(str)
    def set_server_address(self, value):
        # Check if items are the same, if not, update & emit signal
        if self._server_address != value:
            self._server_address = value
            # Emit signal if needed, e.g., self.jwtChanged.emit(value)
            self.serverAddressUpdated.emit(self._server_address)  # Emit signal with new value

    # getter/setters a little dif. Define the property, access with just class.class.whatever,
    server_address = Property(dict, get_server_address, set_server_address)

    @Slot()
    def get_server_port(self):
        return self._server_address

    @Slot(str)
    def set_server_port(self, value):
        # Check if items are the same, if not, update & emit signal
        if self._server_port != value:
            self._server_port = value
            # Emit signal if needed, e.g., self.jwtChanged.emit(value)
            self.serverPortUpdated.emit(self._server_port)  # Emit signal with new value

    # getter/setters a little dif. Define the property, access with just class.class.whatever,
    server_port = Property(dict, get_server_port, set_server_port)