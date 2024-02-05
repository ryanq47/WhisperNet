from PySide6.QtCore import QObject, Property
from PyCode.Authentication.Login import Login
from PyCode.Utils.BaseLogging import BaseLogging

class Authentication(QObject, BaseLogging):
    def __init__(self, parent=None):
        super().__init__(parent)
        self._login = Login(self)
        self.logger.debug(f"Initialized Backend Component: {self.__class__.__name__}")


    @Property(QObject)
    def login(self):
        return self._login

