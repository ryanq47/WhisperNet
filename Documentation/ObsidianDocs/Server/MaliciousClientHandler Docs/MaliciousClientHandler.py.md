## Introduction

The Malicious Client Handler is a class designed to manage individual client connections on a server. Each instance of this class is created to handle communication with a specific client that connects to the server. The purpose of this class is to facilitate communication with malicious clients and provide basic functionality to send and receive* messages from them. <del> Additionally, it updates JSON keys with information about the malicious clients, enabling GUI features like a client viewer. </del>

\*: Note, ServerMaliciousClientHandler itself does not receive messages, it gets passed them from the server.



## Class: ServerMaliciousClientHandler

### Description

This class manages communication with individual malicious clients that connect to the server. Each malicious client is assigned an instance of this class to handle their communications. The class holds information about the client, such as their connection details (IP and port) and an ID that uniquely identifies them on the server. It also includes a command queue to manage commands to be sent to the client.

### Class Variables

- `clientsocket`: Represents the socket object associated with the client's connection.
- `ip`: Stores the IP address of the client.
- `port`: Stores the port number through which the client is connected.
- `id`: Represents the unique ID assigned to the client on the server.
- `fullname`: A string that represents a formatted name for the client based on their IP and ID.
- `command_queue`: An instance of the `QueueHandler` class used to store and manage commands to be sent to the client.

### Methods

1. `__init__(self)`: Constructor method to initialize the class object. It sets up the class variables and adds initial commands to the command queue.
2. `handle_client(self, response_from_client, clientsocket, clientid)`: This method is called to handle a newly connected client. It takes the JSON response from the client, the client socket, and the client ID as input arguments. The method processes the client's response and performs operations accordingly.
3. `send_command(self)`: Sends a message to the connected client. It retrieves the next command from the command queue and sends it to the client using the client's socket connection. If the queue is empty or an error occurs, it sends a "sleep" command to the client.
4. 