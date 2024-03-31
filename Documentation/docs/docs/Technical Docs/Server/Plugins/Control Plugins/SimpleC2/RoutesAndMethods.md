TODO 

 - Response Blocks/Responses of each endpoint
 - Update overview

# SimpleC2 Plugin API Endpoints and Parameters    - 

## Overview
This documentation details the API endpoints within the SimpleC2 plugin, mapping functions to their corresponding Flask routes and describing the expected HTTP request methods and parameters. The SimpleC2 plugin is designed for command and control (C2) operations, including network and client management, and listener configurations.

## Network Management Endpoints

### Add Network
- **Function**: `neo4j_add_network(self)`
- **HTTP Method**: POST
- **Route**: `/api/simplec2/network/add`
- **Request Parameters**:
    - `cidr`: The CIDR notation for the network being added.
    - `nickname`: An optional nickname for the network.

### Remove Network
- **Function**: `neo4j_remove_network(self)`
- **HTTP Method**: POST
- **Route**: `/api/simplec2/network/remove`
- **Request Parameters**:
    - `nickname`: The nickname of the network to remove.

### Get Network Properties
- **Function**: `neo4j_get_network_properties(self)`
- **HTTP Method**: POST
- **Route**: `/api/simplec2/network/properties`
- **Request Parameters**:
    - `nickname`: The nickname of the network whose properties are being requested.

### Add Network Properties
- **Function**: `neo4j_add_network_properties(self)`
- **HTTP Method**: POST
- **Route**: `/api/simplec2/network/addproperties`
- **Request Parameters**:
    - `nickname`: The nickname of the network.
    - `property`: The name of the property to add or update.
    - `value`: The value of the property.

### Retrieve Clients in Network
- **Function**: `neo4j_retrieve_clients_in_network(self)`
- **HTTP Method**: POST
- **Route**: `/api/simplec2/network/clients`
- **Request Parameters**:
    - `nickname`: The nickname of the network for which clients are being requested.

### Retrieve All Networks
- **Function**: `neo4j_retrieve_all_networks(self)`
- **HTTP Method**: GET
- **Route**: `/api/simplec2/network/networks`
- **Request Parameters**: None

## Client Management Endpoints

### Add Client
- **Function**: `neo4j_add_client(self)`
- **HTTP Method**: POST
- **Route**: `/api/simplec2/client/add`
- **Request Parameters**:
    - `nickname`: A unique nickname for the client being added.

### Remove Client
- **Function**: `neo4j_remove_client(self)`
- **HTTP Method**: POST
- **Route**: `/api/simplec2/client/remove`
- **Request Parameters**:
    - `nickname`: The nickname of the client to remove.

### Get Client Properties
- **Function**: `neo4j_get_client_properties(self)`
- **HTTP Method**: POST
- **Route**: `/api/simplec2/client/properties`
- **Request Parameters**:
    - `nickname`: The nickname of the client whose properties are being requested.

### Add Client Properties
- **Function**: `neo4j_add_client_properties(self)`
- **HTTP Method**: POST
- **Route**: `/api/simplec2/client/addproperties`
- **Request Parameters**:
    - `nickname`: The nickname of the client.
    - `property`: The name of the property to add or update.
    - `value`: The value of the property.

## Listener Management Endpoints

### Listeners List
- **Function**: `listener_list(self)`
- **HTTP Method**: GET
- **Route**: `/api/simplec2/listener`
- **Request Parameters**: None

### Start HTTP Listener
- **Function**: `http_listener_start(self)`
- **HTTP Method**: POST
- **Route**: `/api/simplec2/listener/http/start`
- **Request Parameters**:
    - `port`: The port on which the HTTP listener should listen.
    - `address`: The address on which the HTTP listener should bind.
    - `nickname`: A unique nickname for the listener.

### Stop HTTP Listener
- **Function**: `http_listener_stop(self)`
- **HTTP Method**: POST
- **Route**: `/api/simplec2/listener/http/stop`
- **Request Parameters**:
    - `nickname`: The nickname of the HTTP listener to stop.

