## Logging:

from PyCode.Utils.BaseLogging import BaseLogging
import inspect

```
class CLASSNAME(QObject, BaseLogging):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.logger.debug(f"Initialized Backend Component: {self.__class__.__name__}")

```



- #### Error Logging: (This pulls classname + method name)
```
self.logger.error(f"{self.__class__.__name__}.{inspect.currentframe().f_code.co_name}: {e}")
```


Doing Setters N Getters N stuff

```
class Auth(QObject, BaseLogging):
    jwtChanged = Signal(str)  # Signal emitting the new JWT value

    def __init__(self, parent=None):
        super().__init__(parent)
        self._jwt = None

        self.logger.debug(f"Initialized Backend Component: {self.__class__.__name__}")

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

```
