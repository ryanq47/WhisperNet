# Python Class Structure for HTTP JSON Request Builder

This documentation covers the Python classes designed to build, manipulate, and serialize/deserialize HTTP requests in a structured manner using JSON. It is composed of multiple classes, each serving a distinct purpose in the construction of a complex request object.

the TDLR: This is how a HTTP listener request *for* a client is generated. See [Usage Example](#usage-example) for the final JSON structure. 

## Overview

The code defines a collection of classes designed to encapsulate various aspects of a client authentication process, action execution, server callback configuration, and the overarching request builder. These classes are:

- `ClientAuth`
- `User`, `Password`, `Hash`, `Kerb`, `Other`
- `Action`
- `Callback`, `RetryPolicy`, `Server`
- `HTTPJsonRequestBuilder`

Each class is equipped with methods to convert instances to dictionaries (`to_dict`) for easy JSON serialization, among other utility functions.

## Class Definitions

### ClientAuth Class

Represents client authentication details including user credentials, password, authentication hash, Kerberos tickets, and other custom authentication methods.

#### Properties
- User
- Password
- Auth_hash
- Kerb
- Other

#### Methods
- `to_dict()`: Converts the instance into a dictionary.

### User Class

Encapsulates user identification details.

#### Properties
- Username
- SID (Security Identifier)

#### Methods
- `to_dict()`: Converts the instance into a dictionary.

### Password Class

Stores password information.

#### Properties
- Type
- Value

#### Methods
- `to_dict()`: Converts the instance into a dictionary.

### Hash Class

Represents a generic hash value.

#### Properties
- Type
- Value

#### Methods
- `to_dict()`: Converts the instance into a dictionary.

### Kerb Class

Holds Kerberos authentication details.

#### Properties
- Type
- Value

#### Methods
- `to_dict()`: Converts the instance into a dictionary.

### Other Class

A flexible class to accommodate additional authentication information.

#### Properties
- Type
- Value

#### Methods
- `to_dict()`: Converts the instance into a dictionary.

### Action Class

Describes an action to be performed, including its arguments and execution context.

#### Properties
- Action
- Arguments
- Timeout
- Std_output
- Std_error
- Execution_context

#### Methods
- `to_dict()`: Converts the instance into a dictionary.

### Callback Class

Configures callback behavior including the server to call back to, retry policy, and data format.

#### Properties
- Server
- Retry_policy
- Data_format

#### Methods
- `to_dict()`: Converts the instance into a dictionary.

### RetryPolicy Class

Defines retry behavior.

#### Properties
- Max_retries
- Retry_interval

#### Methods
- `to_dict()`: Converts the instance into a dictionary.

### Server Class

Describes server connection details.

#### Properties
- Hostname
- Address
- Port
- Path

#### Methods
- `to_dict()`: Converts the instance into a dictionary.

### HTTPJsonRequestBuilder Class

The main class that brings together all components to build a JSON-formatted HTTP request.

#### Methods
- `to_dict()`: Converts the entire request into a dictionary.
- `to_json(include_empty_keys=False)`: Serializes the request to a JSON string, optionally including keys with `None` values.
- `remove_none_values(d)`: Recursively removes keys with `None` values from a dictionary.
- `from_json(json_data)`: Deserializes a JSON string into the request object.
- `generate_json(request_id=None)`: Generates a template JSON string with default or null values for request components.

## Usage Example

To utilize these classes, instantiate an `HTTPJsonRequestBuilder` object, configure its properties and nested objects as required, then use `to_json()` to serialize the configuration into a JSON string suitable for HTTP requests:

```

# Import/Init class:
myrequest = HTTPJsonRequestBuilder()

## Set items

myrequest.callback.server = 192.168.0.50
myrequest.callback.port = 8080

#get json to be sent:
myrequest_json = myrequest.generate_json(id=request_id)


```

And once generated...:

```
{
  "request_id": "unique_request_identifier",
  "timestamp": "2024-03-14T12:34:56Z",
  "action": {
    "command": "operation_name",
    "parameters": {
        "param1": "value1",
        "param2": "value2"
        // Additional parameters as needed
    }
  },

  "authentication": {
    "user": {
      "username": null,
      "SID": null
    },
    "password": {
      "type": null,
      "value": null
    },
    "hash": {
      "type": null,
      "value": null
    },
    "kerb": {
      "type": null,
      "value": null
    },
    "other": {
      "type": null,
      "value": null
    }
  },
  "callback": {
    "server": {
      "hostname": null,
      "address": "192.168.0.50",
      "port": 8080,
      "path": null
    }
  }
}      

```