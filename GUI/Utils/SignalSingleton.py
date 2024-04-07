from PySide6.QtCore import QObject, Signal, Property
from Utils.Logger import LoggingSingleton

class SignalSingleton(QObject):
    instance = None
    _is_initialized = False
    # Example signals
    #userLoggedIn = Signal(str)  # Signal emitting a string (username)
    #dataUpdated = Signal(int)  # Signal emitting an integer (data ID)

    def __new__(cls, *args, **kwargs):
        if not cls.instance:
            cls.instance = super(SignalSingleton, cls).__new__(cls, *args, **kwargs)
        return cls.instance

    def __init__(self, parent=None):
        if not self._is_initialized:  # Check if already initialized, sanity check
            super().__init__(parent)
            self.logger = LoggingSingleton.get_logger()
            self._auth = Auth(self)
            self._server = Server(self)

            self._is_initialized = True

    # special setter/getter options for qt
            
    @Property(QObject)
    def auth(self):
        return self._auth

    @Property(QObject)
    def server(self):
        return self._server


class Auth(QObject):
    # For *when* the user logs on
    userSuccessfulLogin = Signal(bool)
    # For checking if user is CURRENTLY logged in to the server
    userLoggedOn = Signal(bool)



class Server(QObject):
    serverAddressUpdated = Signal(str)
    serverPortUpdated = Signal(str)