# Handlers & Plugins

## Introduction

The Flask-Plugin pattern is designed around the concept of plugins that, in turn, leverage handlers to implement standardized operations, similar to the way the Windows API functions. This architecture allows plugins to stick to established ways of performing tasks, ensuring consistency and modularity within the project.

## Plugins

### Overview

Plugins are user-created, (ideally) rapidly developed tools designed to extend the server's functionality.

### Standard for Plugins

#### Catching Exceptions

- **Purpose**: Explain why it's crucial for plugins to catch exceptions, possibly to ensure stability or to provide custom error handling.
- **Guidelines**: Offer guidelines on how exceptions should be caught within plugins (e.g., specific types of exceptions to catch, logging standards).

#### Calling Handlers

- **Purpose**: When a plugin may need to do somethign somewhat complicated (authentication, etc) it can use a handler for this. 


## Handlers

### Overview

Handlers are predefined, tightly controlled implementations of libraries or modules within the server. They are not designed for user customization or development but rather provide a consistent interface for performing tasks in a uniform manner throughout the server.

### Standard for Handlers

#### Raising Exceptions

- **Purpose**: Handlers *raise* exceptions (instead of returning a value). This allows for plugins to *catch* these exceptions. 

Ex:

  ```
    raise Utils.ErrorDefinitions.FILE_LOAD_ERROR
  ```


