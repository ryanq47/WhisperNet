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


## Widget Dev:
Use the DevWidget (rename me) for the base widget. This effectively "imports" it


```
DevWidget {
    widgetName: "CustomDevWidget"

    // Override properties or add new functionality
    Component.onCompleted: {
        console.log(widgetName + " is ready.");
    }

    // Adding custom content specific to this widget
    Rectangle {
        width: 100; height: 50
        color: "red"
        anchors.centerIn: parent
    }
}
```

## Accessing data:
PLEASE, access/pull data from the Data singleton for "public/non internal" functions, it keeps things cleaner, and you don't have to worry about passing args accross items.

Goal: make public funcs callable without args, so they can be called from wherever is needed without extra data bs

It's okay if you want to init the data in the __init__ as like self.data, but it's easier to just do this:

```
    def get_clients_from_network_data(self):
        '''
        Filters out clients from the network_data, returns a list of dicts.
        
        [
            {}
        ]

        '''
        network_data = self.data.simplec2.db_data ## << Pulling data from singleton for most up to date data
        ## Scope it down a bit
        network_data = network_data["data"]["nodes"]
```

#### General rules:
 - If getting NEW data, or if possible, use an API call.
        Ex, if you just need a list of clients, api call.
 - store all relevant data that COULD be accessed by other items in the singleton (Data singleton)
 