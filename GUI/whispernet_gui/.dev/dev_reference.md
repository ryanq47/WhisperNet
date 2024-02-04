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
