from PySide6.QtCore import QObject, Property, Slot
from PyCode.Utils.BaseLogging import BaseLogging

class Login(QObject, BaseLogging):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.logger.debug(f"Initialized Backend Component: {self.__class__.__name__}")

    @Slot(str, str, str)
    def to_server(self, username=None, password=None, server=None):
        '''
        Stuff, creates login json & then makes the request, returns jwt. Need to figure out where to set JWT so it can be accesed by everything needed
                                                                        maybe create a data something class, init at start, expose to qml.
        '''
        print(username)

