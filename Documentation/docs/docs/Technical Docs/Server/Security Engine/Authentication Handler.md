# Authentication and User Management Documentation

## Overview

This documentation provides a comprehensive overview of the `Authentication` and `UserManagement` classes, which are central to handling authentication, user creation, role management, and password operations within a Flask application framework.

These are Handlers, meant to be called from within plugins. 

## `Authentication` Class

### Purpose

Manages API authentication processes, including user validation and password checking, to ensure secure access to API endpoints.

### Methods

#### `__init__(self, db_path="DataBases/users.db")`
- Initializes the `Authentication` class with a connection to the user database.
- **Parameters**:
  - `db_path`: The path to the database file containing user credentials and roles. You can find this in the Data singleton

#### `api_authentication_eval(self, username, password) -> bool`
- Evaluates the provided username and password against stored credentials.
- **Returns**: `True` if authentication is successful; otherwise, `False`.

#### `_validate_api_password(self, username, password) -> bool`
- Validates the provided password against the hashed password stored in the database.
- **Returns**: `True` if the password is correct; otherwise, `False`.

#### `api_get_user_role(self, username) -> list`
- Fetches the roles associated with the provided username.
- **Returns**: A list of roles assigned to the user.

## `UserManagement` Class

Inherits from `Authentication`.

### Purpose

Handles operations related to user management, such as creating and deleting users, changing passwords, and managing user roles.

### Methods

#### `create_user(self, username, password, roles)`
- Creates a new user with the specified username, password, and roles.
- **Returns**: `True` if the user is created successfully; otherwise, `False`.

#### `delete_user(self, username)`
- Deletes the user with the specified username from the database.
- **Returns**: `True` if the user is successfully deleted; otherwise, `False`.

#### `change_user_password(self, username, password)`
- Changes the password for the specified user.
- **Returns**: `True` if the password is changed successfully; otherwise, `False`.

#### `add_user_role(self, username, roles)`
- Adds the specified roles to the user.
- **Returns**: `True` if roles are added successfully; otherwise, `False`.

#### `delete_user_role(self, username, roles)`
- Removes the specified roles from the user.
- **Returns**: `True` if roles are deleted successfully; otherwise, `False`.

#### `default_role_check_and_setup(self)`
- Ensures the presence of default roles and creates them if necessary.
- Intended for setting up essential roles upon application initialization.

## `AccessManagement` Class

### Purpose

Provides a decorator to enforce role-based access control on Flask routes.

### Method

#### `role_required(*required_roles)`
- A decorator that verifies if the current user has any of the required roles to access the decorated route.
- **Usage**: Apply this decorator to Flask route functions to restrict access based on user roles.

## Security Considerations

- **Password Hashing**: Utilizes `bcrypt` for secure password hashing and verification.
- **JWT Authentication**: Leverages Flask-JWT-Extended for managing JWTs, enhancing API security.
- **Role-Based Access Control**: Employs custom logic for validating user roles, ensuring that users can only access permitted functionalities.

## Usage Example

```python
@app.route('/secure-endpoint')
@AccessManagement.role_required('admin')
def secure_endpoint():
    return jsonify({'message': 'Access granted to admin user.'})
```