# UserPlugin Documentation

## Overview

This documentation outlines the `UserPlugin`, designed to handle user-related operations within a Flask application framework. This plugin facilitates user management tasks such as creating, deleting users, changing passwords, and managing user roles.

## `Info` Class

### Attributes

    - `name`: "UserHandler" - Identifies the plugin within the system.
    - `author`: "ryanq.47" - Specifies the author of the plugin.
    - `endpoint`: "/user" - Defines the base endpoint for user management operations.
    - `classname`: "UserPlugin" - The class name of the plugin.
    - `plugin_type`: "Builtin" - Indicates the plugin's nature as a core part of the application.

## `UserPlugin` Class

### Initialization

- Sets up logging, data paths, and application context for managing user operations.

### Key Methods

#### `main()`

- Initializes the plugin and registers its routes within the Flask application.

#### `register_routes()`

- Registers endpoints for various user management tasks.

### Endpoints

    - `GET /user`: Displays basic plugin information.
    - `POST /api/user/create`: Handles user creation.
    - `POST /api/user/delete`: Facilitates user deletion.
    - `POST /api/user/changepass`: Allows changing a user's password.
    - `POST /api/user/role/add`: Adds roles to a user.
    - `POST /api/user/role/delete`: Removes roles from a user.

### Route Handlers

#### `userhandler_base()`

- Returns basic information about the `UserPlugin`.

#### `create_user()`

- **Functionality**: Creates a new user with specified username, password, and roles.
- **Security**: Protected by JWT authentication and role-based access control.

#### `delete_user()`

- **Functionality**: Deletes an existing user based on username.
- **Security**: Requires JWT authentication and 'iam_admin' role.

#### `change_user_password()`

- **Functionality**: Updates the password for a specified user.
- **Security**: Access controlled by JWT and administrative privileges.

#### `add_user_role()`

- **Functionality**: Assigns additional roles to a user.
- **Security**: Guarded by JWT authentication and administrative role checks.

#### `remove_user_role()`

- **Functionality**: Removes specified roles from a user.
- **Security**: Ensured through JWT authentication and 'iam_admin' role requirement.

### Security Considerations

- **JWT Authentication**: Ensures that all user management operations are performed by authenticated users.
- **Role-Based Access Control (RBAC)**: Utilizes `AccessManagement` to restrict sensitive operations to users with appropriate roles.

### Usage Example

To create a user:

```python
POST /api/user/create
{
    "username": "newuser",
    "password": "securepassword",
    "roles": ["iam_user"]
}
```