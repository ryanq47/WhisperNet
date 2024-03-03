# Data and Paths Documentation

## Data Class

### Overview

The `Data` class serves as a Singleton for managing data paths within an application.

### Methods

#### `__new__(cls)`

- Ensures only one instance of the class is created.
- **Returns**: The instance of the class.

#### `__init__(self)`

- Initializes the `Data` class with a single instance of the `Paths` class.

## Paths Class

### Overview

The `Paths` class provides functionality for managing file paths, including database and system paths, with logging capabilities.

### Methods

#### `__init__(self)`

- Initializes the `Paths` class with a logger instance obtained from `LoggingSingleton`.
- Initializes private attributes `_db_path` and `_sys_path` to `None`.

#### `db_path`

- Property: Getter method for retrieving the database path.
  - Logs the access to the database path.
  - **Returns**: The database path.

- Setter method for setting the database path.
  - Logs the new database path being set.

#### `sys_path`

- Property: Getter method for retrieving the system path.
  - Logs the access to the system path.
  - **Returns**: The system path.

- Setter method for setting the system path.
  - Logs the new system path being set.

## Logging

- The `LoggingSingleton` is imported from `Utils.Logger`, which handles logging functionality within the `Paths` class.

## Accessing Data:

```
#Example:
from Utils.DataSingleton import Data

self.Data = Data()

path = self.Data.Paths.sys_path

```