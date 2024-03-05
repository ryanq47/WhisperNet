# Neo4jConnection Class Documentation

## Overview

This document provides a comprehensive overview of the `Neo4jConnection` class, which facilitates interaction with the Neo4j database. This class is designed to manage connections, perform queries, and handle transactions within the context of a Python application.

See details on Neo4j's existence & usecase here

## Viz

![Neo4j Connection Visualization](../../../Images/Database/Neo4jConnection/neo4j_connection_overview.png)

## `Neo4jConnection` Class

### Purpose

Serves as the primary interface for executing Cypher queries, managing transactions, and interacting with the Neo4j graph database. It encapsulates the logic for connecting to the database, executing queries, and handling results.

### Initialization

Upon instantiation, the class:

- Initializes a logger instance using `LoggingSingleton`.

- Sets up a Neo4j driver connection using credentials loaded from a `.env` file.

- Automatically calls `load_env()`, `connect()`, and `create_constraints()` methods to prepare the environment and database for interaction.


### Key Methods

#### `load_env()`

- **Purpose**: Loads the database connection credentials from a `.env` file.
- **Actions**:

    - Uses `load_dotenv()` to read the `.env` file.

    - Sets the URI, user, and password for the database connection.

#### `connect()`

- **Purpose**: Establishes a connection to the Neo4j database.
- **Actions**:

    - Creates a Neo4j driver instance with the loaded credentials.

    - Logs the successful connection establishment.

#### `close()`

- **Purpose**: Closes the database connection.
- **Actions**:
    - Closes the Neo4j driver session.

    - Logs the closure of the connection.


#### `custom_query(query, parameters=None, db=None)`

- **Purpose**: Executes a custom Cypher query against the Neo4j database.
- **Parameters**:
    - `query`: The Cypher query string.

    - `parameters`: A dictionary of parameters for the query.

    - `db`: The target database name (optional).

- **Returns**: A list of query results.

#### `get_everything()`

- **Purpose**: Retrieves all nodes, their properties, relationships, and related nodes from the database.
- **Returns**: A comprehensive map of the network including nodes and relationships.

#### `add_network_node(cidr, nickname)`

- **Purpose**: Adds a new network node to the database with the specified CIDR and nickname.
- **Parameters**:

    - `cidr`: The network's CIDR notation.

    - `nickname`: A unique identifier for the network node.

- **Returns**: The result of the Cypher query execution.

#### `create_constraints()`

- **Purpose**: Creates unique constraints for `Network` and `Client` nodes to ensure data integrity.
- **Actions**:

    - Checks for existing constraints and creates them if they are not present.

### Security Considerations

- **Parameterization**: Uses parameterized queries to prevent Cypher injection attacks.
- **Connection Management**: Ensures that database connections are securely managed and closed properly to prevent resource leaks.

### Usage

To use the `Neo4jConnection` class, instantiate it and utilize its methods to perform database operations. Ensure that a `.env` file with the necessary Neo4j connection credentials (`NEO4J_URI`, `NEO4J_USER`, and `NEO4J_PASSWORD`) is present and accessible.

## Future Enhancements

- Implement more specific query methods to abstract common database operations.
- Enhance error handling and recovery mechanisms for more robust database interaction.

## Conclusion

The `Neo4jConnection` class provides a structured and secure way to interact with a Neo4j graph database, making it easier to perform CRUD operations, manage transactions, and navigate complex relationships within the database.
