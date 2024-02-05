'''
some notes


Every attribute starts as None. On errors when trying to set thigns, set them back to none. See Login.py at the json decoding for this
'''

## Singleton class, holds all data stuff needed
## Make OOP as fuck
from PySide6.QtCore import QObject, Property, Slot, Signal
#from Utils.BaseLogging import BaseLogging

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
            self._auth = Auth(self)

            # object is getting created correctly
            #self._auth.jwt = "balls"
            #print(self._auth.jwt)

            self._is_initialized = True  # Mark as initialized
            #self.logger.debug(f"Initialized Backend Component: {self.__class__.__name__}")

    # have to do special getter/setter for qt
    @Property(QObject)
    def auth(self):
        return self._auth



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
