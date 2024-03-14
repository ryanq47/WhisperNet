# EncryptionHandler Documentation

## Overview

The `PasswordManager` class in the EncryptionHandler module provides functionalities for hashing passwords and verifying passwords against their hashed versions. It leverages the bcrypt hashing algorithm for enhanced security. The module is designed to be used wherever password management is required within the application, ensuring consistent and secure handling of user passwords.

## Classes

### `PasswordManager`

#### Methods

- **`hash_password(password: str) -> bytes`**

    - **Description**: Hashes a plain text password using bcrypt.
    - **Parameters**:
        - `password`: A `str` representing the plain text password to hash.
    - **Returns**: A `bytes` object containing the hashed password.
    - **Exceptions**: Raises an exception if there is an error during the hashing process.

- **`verify_password(password: str, hashed_password: bytes) -> bool`**

    - **Description**: Verifies a plain text password against a hashed password.
    - **Parameters**:
        - `password`: A `str` representing the plain text password to verify.
        - `hashed_password`: A `bytes` object representing the hashed password to compare against.
    - **Returns**: A `bool` indicating whether the verification succeeded (`True`) or failed (`False`).
    - **Exceptions**: Raises an exception if there is an error during the verification process.

## Logging

The module utilizes a logger obtained from `LoggingSingleton` for logging various stages of the password hashing and verification processes, including:
- Debug logs for the start and successful completion of hashing and verification processes.
- An info log if the password verification is successful.
- A warning log if the password verification fails.
- Error logs containing exceptions if any errors occur during hashing or verification.

## Usage

To use the `PasswordManager` module, simply import it into your application and call the static methods `hash_password` and `verify_password` as needed. Ensure that exception handling is implemented to catch and handle any errors that may arise during password management operations.
