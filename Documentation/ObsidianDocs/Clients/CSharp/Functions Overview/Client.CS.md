# Client Documentation

## Overview

This documentation provides an overview and detailed explanation of the `Client` program, which establishes a connection to a server and performs data communication using sockets. The program is designed to periodically check in with the server, exchange messages, and process jobs based on a decision tree mechanism.

## Introduction

The `Client` program establishes a socket connection with a server, performs regular check-ins, sends and receives messages, and processes jobs based on a decision tree. The program's functionality is divided into three main components: the `Main` function, the `ConnectToServer` function, and the `NetOps` class.

## Usage

Compile and run the `Client` program. Ensure that the appropriate libraries are referenced and that the necessary network configurations are in place. The program will connect to a specified server IP address and port, perform check-ins, exchange messages, and process jobs as defined by the decision tree.

## Code Structure

The `Client` program consists of the following components:

1. **Main Function:** Entry point of the program. Generates relevant data, creates an IP address and endpoint, and initiates the connection to the server using the `ConnectToServer` function.
    
2. **ConnectToServer Function:** Manages the socket connection with the server. It performs the following steps:
    
    - Creates a socket using the `NetOps.CreateSocket` function.
    - Connects to the server using the provided IP address and port.
    - Sends a heartbeat/check-in message to the server with initial data during the first iteration.
    - Sends previous iteration's results to the server in subsequent iterations.
    - Receives a job/message from the server.
    - Processes the received job using a decision tree and sends back the results.
    - Closes the socket after each iteration.

1. **NetOps Class:** Contains critical networking operations functions. It includes:
    
    - `CreateSocket`: Creates a socket for communication.
    - `CreateEndpoint`: Creates an endpoint (IP address and port combination).
    - `CreateIPObject`: Creates an IP address object from a given IP string.

## Functions

### Main Function

The `Main` function serves as the entry point of the program. It performs the following tasks:

- Generates necessary data using `Client.PropertyHandler.Properties.GenerateData`.
- Defines the server IP address and port.
- Creates an IP address object using `NetOps.CreateIPObject`.
- Creates an endpoint using `NetOps.CreateEndpoint`.
- Initiates the connection to the server by invoking `ConnectToServer`.

### ConnectToServer Function

The `ConnectToServer` function handles the socket connection and communication with the server. It implements the following logic:

- Initializes variables to track iterations and decision tree results.
- Enters an infinite loop to continuously perform communication with the server.
- Inside the loop:
    - Creates a socket using `NetOps.CreateSocket`.
    - Connects to the server using the specified endpoint.
    - Sends a message to the server, either the initial check-in message or previous iteration's results.
    - Receives a job/message from the server.
    - Processes the job using a decision tree from `Client.Logic.Trees.decisionTree`.
    - Closes the socket after each iteration.

### NetOps Class

The `NetOps` class contains functions related to networking operations. These functions are critical and throw exceptions on errors. The class includes:

- `CreateSocket`: Creates a new socket with the specified parameters.
- `CreateEndpoint`: Creates an `IPEndPoint` object using the provided IP address and port.
- `CreateIPObject`: Parses the given IP string and returns an `IPAddress` object.