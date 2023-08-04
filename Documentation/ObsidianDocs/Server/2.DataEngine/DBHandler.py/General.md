**Documentation for SQLDBHandler Class**

**Introduction**

This documentation explains the `SQLDBHandler` class, which is designed to manage a SQLite database for handling client commands and responses. The class provides methods to enqueue and dequeue messages, track queue numbers, and maintain tables for clients' messages and queue tracking.

**Setup**

Before using the class, you need to set up the necessary tables and rows.

1. `create_client_table(client_name)`: Creates a table for a specific client with four fields: ID, message (msg), response, and requester.
    
2. `create_client_queuetrack_table()`: Creates a table for tracking queue numbers.
    
3. `create_client_queuetrack_row(client_name)`: Creates a row in the queue tracking table for the specified client.
    

**Enqueuing and Dequeuing**

1. `enqueue_mclient_row(client_name, msg, response, requester)`: Enqueues a command to the queue.
    
    - `client_name`: The name of the client.
    - `msg`: The JSON message going to the client.
    - `response`: The JSON response from the client.
    - `requester`: The client that requested the action.
2. `dequeue_next_cmd(client_name)`: Dequeues the next command from the queue.
    
    This method retrieves the next queue number, retrieves the corresponding message from the database, increments the queue numbers, and returns the message.
    
    - `client_name`: The name of the client.

**Utility Functions**

1. `check_if_row_exists(client_name, id)`: Checks if a message ID already exists in the table.
    
2. `get_next_queue_number(client_name)`: Gets the ID number of the next message in the queue for a specific client.
    
3. `get_current_queue_number(client_name)`: Gets the ID number of the message currently in the queue for a specific client. This is used for entering responses.
    
4. `increment_queue_number(client_name)`: Increments both the current queue number and next queue number for a specific client.
    

**Usage**

To use the class, create an instance of `SQLDBHandler` and call the respective methods based on your needs. You only need to pass the `client_name` parameter.