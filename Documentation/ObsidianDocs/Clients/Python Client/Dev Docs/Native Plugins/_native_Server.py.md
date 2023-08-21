# Plugin Documentation

## Description

This plugin provides functionality for interacting with a server and performing various actions. It includes classes for handling actions, communication, data manipulation, and more.

## Table of Contents

- [Info](#info)
- [ClassData](#classdata)
- [Tree](#tree)
- [Actions](#actions)
- [Handler](#handler)


# Classes
## Info
- `name`: Server
- `author`: ryanq.47
- `dir`: home/server

## ClassData

A data storage class containing shared data for non-static classes. This essentially is a 'struct', and it's kind of a weird implementation. 

- `cookie`: Holds the server cookie.
- `socket`: Holds the server socket connection.
- `server_details`: Holds server connection details, as a tuple: (192.168.0.1 , 80)
- `username`: Holds the client's username. <span style='color:orange'> Note, username may be interchanged with client_id </span>

## Tree

The `Tree` class controls user inputs, invokes respective methods, and returns the results.

### Methods

- `tree_input(user_input=None, data_manager=None)`: Processes user input and dispatches the corresponding action. Returns a dictionary containing the output from the action, the current directory, and debugging information.

## Actions

The `Actions` class contains methods for executing various commands and actions.

### Methods

- `_display_help()`: Displays a help menu with available commands and explanations.
- `_start_server()`: Placeholder for starting a server (not implemented).
- `_connect_to_server()`: Connects to a server instance, retrieves a cookie, and sets `ClassData` attributes.
- `_show_connection_details()`: Displays connection details.
- `_run_server_command(command=None)`: Sends a command to the server and returns the response.

## Handler

The `Handler` class handles actions related to shell operations.

### Methods

- `_get_cookie(socket=None, client_id=None, password=None)`: Retrieves a cookie from the server using provided credentials.
- `_create_socket_connection(server_details_tuple=("127.0.0.1", 80))`: Creates a socket connection to the server.
- `_send_recv_command_to_server(cookie=None, client_id=None, msg_to=None, msg_command=None, socket=None)`: Sends and receives messages to/from the server using the provided cookie.

---

This documentation provides an overview of the classes, methods, and functionality contained within the plugin. Use this as a reference while working with the codebase.


# General: