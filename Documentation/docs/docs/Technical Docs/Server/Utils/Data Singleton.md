"""
# Data Singleton Documentation

## Overview

The Data Singleton pattern ensures a single instance of the Data class across the application, facilitating centralized management of shared resources like paths and configurations.

In less wordy terms, it's a temporary data structure/data base to hold things that the server needs. 

## Data Class

### Description

Acts as a Singleton to manage data paths and listener configurations, providing a global access point.

### Methods

- `__new__(cls)`: Ensures a single instance.
- `__init__(self)`: Initializes Paths and Listeners classes.

## Paths Class

### Methods/Attributes

- `__init__(self)`: Sets up logging and path defaults.
- `users_db_path`: Getter/setter for the users database path.
- `sys_path`: Getter/setter for the system path.
- `load_data(self)`: Loads essential data paths.


## Listeners Class

### Description

Manages HTTP listeners, holding references and providing management functions.

### Methods

- `__init__(self)`: Initializes Http class instance for HTTP listeners management.

    - Attributes:
        - `Http` An instance of the HTTP Class, `Http()`. 

## Http Class

### Description

Manages HTTP listeners, maintaining a collection and adding listeners.

### Methods

- `__init__(self)`: Sets up logging and initializes listeners collection.

    - Attributes:
        - `http_listeners`: The dictionary of HTTP listeners. 

- `add_listener(self, process=None, info=None)`: Adds an HTTP listener.

    - Parameters:
        - `process`: Associated process object.
        - `info`: Dictionary with listener information including `nickname` for quick lookup.

    - Example `info` structure:


```python
        info = {
            "bind_port": bind_port,
            "bind_address": bind_address,
            "nickname": nickname
        }
```

  - Usage example:


```python
        p = Process(target=listener_instance.main)
        p.start()
        
        info = {
            "bind_port": bind_port,
            "bind_address": bind_address,
            "nickname": nickname
        }

        data_instance.Listeners.Http.add_listener(process=p, info=info)
```

## Usage Examples

- Accessing system path and adding an HTTP listener:
    
```python
    from Utils.DataSingleton import Data

    data_instance = Data()
    system_path = data_instance.Paths.sys_path

    data_instance.Listeners.Http.add_listener(process=myProcess, info={"nickname": "listener1"})
```

