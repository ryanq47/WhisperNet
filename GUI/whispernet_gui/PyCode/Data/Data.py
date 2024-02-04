## Singleton class, holds all data stuff needed
## Make OOP as fuck
from PySide6.QtCore import QObject, Property, Slot

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
            self._authentication = Auth()

            self._is_initialized = True  # Mark as initialized

    # have to do special getter/setter for qt
    @Property(QObject)
    def auth(self):
        return self._authentication

    '''Don't need a setter for this
    @user.setter
    def user(self, value):
        self._user = value
    '''

## apparently not being init/defined for qml. somethings up, same issue I had befoer
class Auth(QObject):
    def __init__(self, parent=None):
        super().__init__(parent)
        self._jwt = None

    #@Slot()
    def get_jwt(self):
        return self._jwt

    #@Slot(str)
    def set_jwt(self, value):
        if self._jwt != value:
            self._jwt = value
            # Emit signal if needed, e.g., self.jwtChanged.emit(value)

    # getter/setters a little dif. Define the property, access with just class.class.jwt,
    jwt = Property(str, get_jwt, set_jwt)
