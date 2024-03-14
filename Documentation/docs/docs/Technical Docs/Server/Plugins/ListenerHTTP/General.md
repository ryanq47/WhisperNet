# HTTP Listener

The HTTP Listener is designed as a standalone listener for HTTP Command and Control (C2) communications, primarily used within a plugin architecture. Its primary function is to handle incoming HTTP requests and manage client interactions through a defined API, without direct interaction with underlying databases or storage systems such as Neo4j. All database interactions are expected to be performed through calls to the main server API.

## Visualization

A graphical representation of the HTTP Listener's role within the server and plugin architecture is provided:

![HTTP Listener](../../../../Images/Server/Plugins/http_listener.png)

## Overview

- **Plugin Name:** ListenerHTTP
- **Author:** ryanq47
- **Endpoint:** `/http`
- **Class Name:** `ListenerHTTP`
- **Plugin Type:** Portable

## Description

`ListenerHTTP` acts as an HTTP listener within a plugin-based system, utilizing Flask to register and manage HTTP routes for GET and POST methods. This plugin is designed to be integrated into a larger application framework, requiring an instance of a Flask application (`app`) passed to it upon initialization. 

## Key Components

- **LoggingSingleton:** A logging utility ensuring that all log messages are consistent and centralized.
- **Client:** Represents the client making requests to the ListenerHTTP. It is responsible for managing client-specific information and interactions.

## Functionality

### Initialization

Upon initialization, `ListenerHTTP`:

1. Acquires a logger instance from `LoggingSingleton` for consistent logging across the application.
2. Stores the Flask application instance (`app`) passed during instantiation.
3. Initializes an empty dictionary (`client_class_dict`) to keep track of client-specific class instances.

### Main Entry Point

The `main` method serves as the entry point for the plugin, where it performs the following actions:

1. Logs the entry into the main function.
2. Loads the plugin name from the `Info` class.
3. Registers HTTP routes for GET and POST methods by calling `register_routes`.

### Route Registration

`register_routes` method dynamically registers Flask routes based on the endpoint specified in the `Info` class. It supports:

- A GET route at `/http/get` that is handled by `listener_http_get_endpoint`.
- A POST route at `/http/post` that is handled by `listener_http_post_endpoint`.

### Endpoints

- **GET Endpoint (`listener_http_get_endpoint`):** Designed for retrieving data. Currently, it responds with a placeholder message.
- **POST Endpoint (`listener_http_post_endpoint`):** Handles initial client check-ins, registering new clients if necessary and directing them to a specific URL for future communications.

### Client Check-in Validation

`client_checkin_validation` is a placeholder method intended to validate client check-ins. It outlines steps for client verification and registration but does not implement them, indicating where future database interactions and client instance creation should occur.



## Future Enhancements

Future versions of the HTTP Listener are expected to implement database interactions, client validation, and dynamic client management, turning the placeholders into functional components.
