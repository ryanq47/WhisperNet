
# NOT COMPLETE/IN DEV

# HttpListenerHandler Documentation

The `HttpListenerHandler` class is designed to encapsulate the logic for managing HTTP listeners, separate from the core functionalities of plugins. This separation allows plugins to focus solely on handling Flask requests and other specific tasks, while `HttpListenerHandler` takes care of listener setup, initiation, and management. The class primarily uses static methods for interaction.



## Dependencies

- `ListenerHTTP` from `PluginEngine.PublicPlugins.ListenerHTTP.ListenerHTTP`
- `Data` from `Utils.DataSingleton`
- `LoggingSingleton` from `Utils.Logger`
- `Process` from `multiprocessing`

## Methods

### `start(bind_address=None, bind_port=None, nickname=None)`

Starts an HTTP listener with the specified bind address, port, and nickname, and adds it to the Data Singleton for centralized management.

- **Parameters**:
    - `bind_address`: The IP address on which the listener will bind and listen. Default is `None`.
    - `bind_port`: The port number on which the listener will bind and listen. Default is `None`.
    - `nickname`: A unique identifier for the listener. Default is `None`.

- **Functionality**:
    1. Validates whether a listener with the same nickname already exists within the Data Singleton to avoid duplicates.
    2. Initializes an instance of `ListenerHTTP` with the provided bind address, port, and nickname.
    3. Starts the listener in a separate process to ensure it doesn't block or hang the main application flow, particularly important for HTTP calls.
    4. Adds listener information to the Data Singleton for easy management and access across the application.
    5. Logs the successful start of the listener.

- **Usage**:
  This method is a wrapper around the listener's native startup procedures, facilitating the process with additional checks and the integration with the Data Singleton for better management and oversight.

### `stop(bind_address=None, bind_port=None)`

Stops an HTTP listener identified by its bind address and port. This method is a placeholder in the current documentation, indicating future functionality for stopping listeners.

- **Parameters**:
    - `bind_address`: The IP address on which the listener is bound. Default is `None`.
    - `bind_port`: The port number on which the listener is bound. Default is `None`.

- **Functionality**:
    1. Checks if a listener with the specified address and port exists within the Data Singleton.
    2. If found, initiates the shutdown process for the listener and removes it from the Data Singleton.
    3. Logs the event of stopping the listener.


## Example Usage

To start an HTTP listener:

```python
HttpListenerHandler.start(bind_address='127.0.0.1', bind_port=8080, nickname='MainListener')
```


On a successful start, the following should show up in the console:

![](../../../../../../Images/Server/Plugins/SimpleC2/http_listener_successful_start.png)
