# AuthenticationSQLDBHandler Documentation

## Overview

The `AuthenticationSQLDBHandler` class is responsible for managing the SQLite database that stores user authentication information, including usernames, password hashes, and roles. It provides methods for interacting with the database, such as creating users, validating passwords, and managing user roles.

## Initialization

- **Purpose**: Establishes a connection to the specified SQLite database and prepares a cursor for executing SQL statements.
- **Parameters**:
  - `db_path`: The file path to the SQLite database.

## Key Methods

### `connect_to_db(db_path)`

- **Functionality**: Opens a connection to the SQLite database at the specified path and initializes a cursor.
- **Parameters**:
  - `db_path`: Path to the database file.

### `nuke_and_recreate_db()`

- **Functionality**: Deletes the existing database tables and recreates them, including predefined roles.

### `get_api_username(username) -> bool`

- **Functionality**: Checks if a username exists in the database.
- **Returns**: `True` if the username exists, `False` otherwise.

### `get_api_password_blob(username) -> bytes`

- **Functionality**: Retrieves the password hash for a given username from the database.
- **Returns**: The password hash as a blob if the user exists, `False` otherwise.

### `change_api_user_password(username, password_hash) -> bool`

- **Functionality**: Updates the password hash for a given username.
- **Returns**: `True` if the password was successfully updated, `False` otherwise.

### `create_api_user(username, password_blob) -> bool`

- **Functionality**: Creates a new user with the provided username and password hash.
- **Returns**: `True` if the user is successfully created, `False` if the user already exists.

### `delete_api_user(username)`

- **Functionality**: Deletes a user and their associated roles from the database based on the username.
- **Returns**: `True` if the user is successfully deleted, `False` otherwise.

### `add_api_role(username, roles)`

- **Functionality**: Assigns the specified roles to a user.
- **Returns**: `True` if the roles are successfully added, `False` otherwise.

### `delete_api_role(username, roles)`

- **Functionality**: Removes the specified roles from a user.
- **Returns**: `True` if the roles are successfully deleted, `False` otherwise.

### `get_all_api_user_roles(username)`

- **Functionality**: Fetches all roles assigned to a specific user.
- **Returns**: A list of roles for the user.

### `get_api_users_with_role(role_name)`

- **Functionality**: Retrieves all users who have been assigned a specific role.
- **Returns**: A list of users with the role.

### `get_api_user_id(username)`

- **Functionality**: Fetches the user ID for a given username.
- **Returns**: The user ID if the user exists, `None` otherwise.

### Internal Methods

#### `_create_tables()`

- **Functionality**: Creates the necessary tables in the database if they do not already exist.

#### `_wipe_db()`

- **Functionality**: Deletes the existing database tables.

#### `_add_roles()`

- **Functionality**: Adds predefined roles to the database.

## Database Schema

- `api_users`: Stores user information including usernames and password hashes.
- `roles`: Defines roles that can be assigned to users.
- `user_roles`: Associates users with their roles.

## Security Considerations

- Passwords are stored as bcrypt hashes to enhance security.
- The database schema includes role-based access control mechanisms.

## Usage

This class is utilized by other components of the system to perform authentication-related tasks, such as validating user login requests and managing user roles. It is not intended to be directly accessed by end-users.

## Conclusion

The `AuthenticationSQLDBHandler` class provides a robust backend for managing user authentication and roles within a Flask-based application, leveraging SQLite for data storage.
