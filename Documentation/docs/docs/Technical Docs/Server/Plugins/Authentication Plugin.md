# AuthenticationPlugin Documentation

## Overview

This document provides a detailed overview of the `AuthenticationPlugin`, designed for a Flask application. The plugin is built to handle API authentication, allowing users to log in through a dedicated endpoint.

## `Info` Class

### Purpose

Contains metadata for the plugin, crucial for its identification and operation within the plugin framework.

### Attributes

- `name`: "AuthenticationPlugin" - The unique name of the plugin.
- `author`: "ryanq47" - The author of the plugin.
- `endpoint`: "/authentication" - The main endpoint associated with the plugin (though specific usage may vary).
- `classname`: "AuthenticationPlugin" - The class name of the plugin.
- `plugin_type`: "Builtin" - Indicates that this plugin is a built-in part of the application.

## `AuthenticationPlugin` Class

### Purpose

Integrates with the Flask application to provide an API authentication mechanism. It defines routes for authentication and potentially for logging out.

### Initialization

- **Parameters**:
  - `app`: The Flask application instance.
- **Actions**:
  - Initializes logging through `LoggingSingleton`.
  - Stores the Flask app instance.
  - Accesses shared data paths through `DataSingleton`.

### Key Methods

#### `main()`

- **Purpose**: Acts as the entry point for the plugin, responsible for loading the plugin and registering its routes.
- **Actions**:
  - Logs the loading of the plugin.
  - Calls `register_routes()` to set up the plugin's endpoints.

#### `register_routes()`

- **Purpose**: Registers the Flask routes necessary for the plugin's operations.
- **Endpoints**:
  - `/api/login`: Handles the login process.

#### `api_user_login()`

- **Purpose**: Processes login requests, authenticating users against stored credentials.
- **Process**:
    - Extracts `username` and `password` from the request data.
    - Utilizes the `Authentication` class to validate credentials.
    - Generates a JWT access token upon successful authentication.
- **Responses**:

    - Returns a success response with a JWT access token if authentication is successful.
  
    - Returns a failure response if authentication fails.

### Security Considerations

- **Password Handling**: Uses the `Authentication` class to securely handle password verification.
- **JWT Management**: Generates JWT tokens for authenticated sessions, with a configurable expiration time.

### Usage

To utilize the authentication functionality provided by this plugin, send a POST request to `/api/login` with a JSON payload containing `username` and `password`. Upon successful authentication, an access token will be returned, which should be used for subsequent authenticated requests to the API.

## Future Enhancements

- Implement a logout endpoint to invalidate JWT tokens.
- Extend user role management to support multiple roles and permissions.

## Conclusion

The `AuthenticationPlugin` provides a robust mechanism for API authentication within a Flask application, leveraging JWT for session management and offering a secure, efficient login process.
