# Database Documentation for Authentication System

## Overview

The Authentication system utilizes a SQLite database to manage user authentication, roles, and permissions. This document outlines the structure and functionality of the database as managed by the `AuthenticationSQLDBHandler` class.

## Database Structure

The database consists of three primary tables:

- `api_users`: Stores user credentials and information.
- `roles`: Defines available roles within the system.
- `user_roles`: Associates users with their roles, facilitating many-to-many relationships.

### `api_users` Table

- `user_id`: INTEGER PRIMARY KEY, auto-incremented unique identifier for each user.
- `username`: VARCHAR(255), the user's unique username.
- `password_hash`: BLOB, the bcrypt hash of the user's password.

### `roles` Table

- `role_id`: INT PRIMARY KEY, unique identifier for each role.
- `role_name`: VARCHAR(255) UNIQUE, the name of the role.

### `user_roles` Table

- `user_id`: INT, references `user_id` in `api_users`.
- `role_id`: INT, references `role_id` in `roles`.
- PRIMARY KEY (`user_id`, `role_id`), ensures unique combinations of user-role associations.

## Key Operations

### User Management (High level view of what these operations do)

- **Create User**: Inserts a new user into `api_users`, hashing the password before storage.
- **Delete User**: Removes a user and their associated roles from the database.
- **Change User Password**: Updates a user's password hash in `api_users`.

### Role Management

- **Add Role to User**: Inserts entries into `user_roles` to associate a user with one or more roles.
- **Remove Role from User**: Deletes entries from `user_roles`, dissociating a user from one or more roles.
- **Fetch User Roles**: Retrieves all roles associated with a specific user.

## Initialization and Maintenance

- **Database Connection**: Establishes a connection to the SQLite database file specified by `db_path`.
- **Table Creation**: Checks for the existence of necessary tables upon initialization and creates them if missing.
- **Database Reset**: Provides functionality to wipe and recreate all tables, including redefining roles.

## Security

- Passwords are stored as bcrypt hashes to enhance security.
- Roles and permissions are managed through the database, allowing for flexible access control.

