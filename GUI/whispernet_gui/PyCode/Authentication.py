from PySide6.QtCore import QObject, Property

from PyCode.Login import Login


class Authentication(QObject):
    def __init__(self, parent=None):
        super().__init__(parent)
        self._login = Login(self)

    @Property(QObject)
    def login(self):
        return self._login

