# Signal Singleton

## Overview

TLDR: The Signal Singleton for managing signals and data in a PySide-based GUI. It ensures that signals and shared data are managed through a single instance using the singleton pattern. The class uses PySide's QObject features to emit signals and manage data properties efficiently.

## Imports and Dependencies

- **PySide6.QtCore**: Includes QObject for base class inheritance, Signal for emitting custom signals, and Property for managing property attributes.
- **Utils.Logger**: A custom utility for logging messages and errors.

## Singleton Pattern

The Signal management system is implemented as a singleton to ensure that only one instance of the `SignalSingleton` class is created across the application. This is achieved through the use of a class attribute `instance` and the overriding of the `__new__` method.

## Classes

### Hierarchy

- **SignalSingleton (Singleton)**: The root class acting as a container for all signal and data management within the application.

    - **Auth**: Manages authentication-related signals and data.
    - **Server**: Manages server-specific signals and data.

### SignalSingleton

The main singleton class responsible for holding all signal and data interactions related to the application.

#### Properties

- **auth**: Returns an instance of the `Auth` class.
- **server**: Returns an instance of the `Server` class.

#### Initialization

The `__init__` method includes a check (`_is_initialized`) to ensure that the singleton instance is initialized only once.

### Auth

A class for managing authentication signals and data.

#### Signals

- **userSuccessfulLogin**: Emitted when a user logs in successfully, carrying a boolean status.
- **userLoggedOn**: Emitted to indicate whether a user is currently logged into the server, carrying a boolean status.

### Server

A class for managing server-related signals.

#### Signals

- **serverAddressUpdated**: Emitted when the server address is updated, carrying the new address as a string.
- **serverPortUpdated**: Emitted when the server port is updated, carrying the new port as a string.

## Usage

The Signal management system is designed to be instantiated once and accessed throughout the application for managing and observing changes in authentication and server settings via signals.

```python
signal_instance = SignalSingleton()
```

#### Accessing Properties & Emiting Signals

```
auth_instance = signal_instance.auth
server_instance = signal_instance.server

## Alternatively, you can just access them directly with the following.
## I prefer this method for code clarity.
signal_instance.server.serverAddressUpdated.emit()
signal_instance.server.serverAddressUpdated.connect()

```

#### Emiting Signals
```
auth_instance.userSuccessfulLogin.emit(True)
```

#### Connecting/Listening signals

```
auth_instance.userSuccessfulLogin.connect(handle_login)
server_instance.serverAddressUpdated.connect(update_server_address_display)
```
