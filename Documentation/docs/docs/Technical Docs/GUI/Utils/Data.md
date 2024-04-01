TODO

 - Add examples/skeletons of what each property holds, ex the JSON structure of the listener dict
 
# Data Singleton

## Overview

TLDR: The data singleton for the GUI. Holds all temporary/quickly accessible data. It uses Getters/Setters (& signals, thanks to PySide) to access/set all variables.

This documentation provides an overview of the Data management system designed for PyQt or PySide applications. It emphasizes an Object-Oriented Programming approach and utilizes Qt's Property, Signal, and Slot mechanisms to manage and communicate changes in data throughout the application. The system is structured around a singleton pattern to ensure a single instance manages all data interactions.

## Imports and Dependencies

- **PySide6.QtCore**: Includes QObject for base class inheritance, Property for property management, Slot for marking methods as slots, and Signal for emitting custom signals.
- **typing**: Provides support for type hints.
- **json**: Used for parsing JSON data.
- **inspect**: Utilized for retrieving the current function name for logging purposes.
- **Utils.Logger**: A custom utility for logging messages and errors.

## Singleton Pattern

The Data management system implements the singleton pattern to ensure that only one instance of the `Data` class is created. This is achieved through the use of a class attribute `_instance` and the overriding of the `__new__` method.

## Classes

### Hieracrhy 

- **Data (Singleton)**: The root class acting as a container for all shared application data. Being a singleton ensures that a single instance manages all data interactions within the application.

    - **auth**: Manages authentication-related data, primarily focused on handling JWT tokens.

    - **simplec2**: Handles data specifically related to SimpleC2 operations, including database data and listener configurations.

        - **listener**: A subclass within `SimpleC2Data` dedicated to managing listener-related data.

    - **server**: Manages server-specific settings like address and port.

    Everything is accessible with the folowing syntax:

```
    Data.class.subclass
    
    Data.simplec2.listener.listener_data # This would return listener data
```

### Data

The main singleton class responsible for holding all application data.

#### Properties

- **auth**: Returns an instance of the `Auth` class.
- **simplec2**: Returns an instance of the `SimpleC2Data` class.

### Auth

A class for managing authentication data.

#### Methods

- **get_jwt**: Retrieves the JWT token.
- **set_jwt**: Sets the JWT token and emits a signal upon change.

#### Signals

- **jwtChanged**: Emitted when the JWT token is updated.

#### Properties

- **jwt**: A property to get or set the JWT token.

### SimpleC2Data

A class for managing SimpleC2 related data.

#### Methods

- **get_db_data**: Retrieves the database data.
- **set_db_data**: Sets the database data and emits a signal upon change.

#### Signals

- **client_data_updated**: Emitted when client data is updated.
- **db_data_updated**: Emitted when database data is updated.
- **db_network_data_updated**: Emitted when database network data is updated.

#### Properties

- **db_data**: A property to get or set the database data.
- **db_network_data**: A property to get or set the database network data.
- **listener**: Returns an instance of the `Listener` class.

### Listener

A class for managing listener data within the SimpleC2Data context.

#### Methods

- **get_listener_data**: Retrieves listener data.
- **set_listener_data**: Sets listener data and emits a signal upon change.

#### Signals

- **listenerDataChanged**: Emitted when listener data is updated.

#### Properties

- **listener_data**: A property to get or set current listener data. (dict)

### Server

A class for managing server-related data.

#### Methods

- **get_server_address**: Retrieves the server address.
- **set_server_address**: Sets the server address and emits a signal upon change.
- **get_server_port**: Retrieves the server port.
- **set_server_port**: Sets the server port and emits a signal upon change.

#### Signals

- **serverAddressUpdated**: Emitted when the server address is updated.
- **serverPortUpdated**: Emitted when the server port is updated.

#### Properties

- **server_address**: A property to get or set the server address.
- **server_port**: A property to get or set the server port.

## Usage

The Data management system is designed to be instantiated once and accessed throughout the application for managing and observing changes in data related to authentication, SimpleC2 operations, listener configurations, and server settings.

## Remarks

This documentation outlines the structured approach to managing application-wide data in a PyQt or PySide project, leveraging Qt's powerful Property, Signal, and Slot mechanisms. The emphasis on an Object-Oriented approach ensures that the codebase remains modular, maintainable, and scalable.
