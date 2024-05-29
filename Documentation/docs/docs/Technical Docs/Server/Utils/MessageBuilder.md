# Message Helper and API Utilities Documentation

## Overview

This document provides an overview and usage guide for the `MessageHelper` class and various API utility functions. These components facilitate the generation of unique message IDs, timestamps, and the construction of request and response JSON objects for communication within the application.

## MessageHelper Class

### Description

The `MessageHelper` class provides static methods to generate unique message IDs and current timestamps.

### Methods

- `generate_unique_id() -> str`: Generates a unique message ID using UUIDv4.
- `generate_timestamp() -> int`: Generates the current timestamp in seconds since the epoch.

### Example Usage

```python
unique_id = MessageHelper.generate_unique_id()
timestamp = MessageHelper.generate_timestamp()
```

## API Utility Functions

Note, api_request, and api_response are *very* similar. Key differences:

- api_request: used to build a dictionary, that can be converted into a JSON object to send somewhere. 

- api_response: used to build a RESPONSE to an inbound request. Usually used in place of the traditional flask "return jsonify(mydata), statuscode".

### `api_request`

Creates and constructs a request JSON string to be sent between parts of the stack.

#### Parameters

- `status` (str): Status of the request, e.g., "success" or "failure". Default is "success".
- `data` (dict): Data to be included in the request. Default is None.
- `error_message` (str): Error message, if any. Default is None.
- `data_items` (list): List of tuples (key, value) to add to the data dictionary. Default is None.
- `**kwargs`: Additional keyword arguments to include in the request.

#### Returns

- `dict`: The constructed request dictionary.

### Example Usage

```python
request_data = api_request(
    status="success",
    data={"key": "value"},
    error_message=None,
    data_items=[("extra_key", "extra_value")],
    additional_key="additional_value"
)
```

### `api_response`

Creates and constructs a response JSON string to be sent back as a response. 

#### Parameters

- `status` (str): Status of the response, e.g., "success" or "failure". Default is "success".
- `data` (dict): Data to be sent back in the response. Default is None.
- `error_message` (str): Error message, if any. Default is None.
- `data_items` (list): List of tuples (key, value) to add to the data dictionary. Default is None.
- `**kwargs`: Additional keyword arguments to include in the response.

#### Returns

- `tuple`: A tuple containing the JSON response and the status code.

### Example Usage

```python
response_data, status_code = api_response(
    status="success",
    data={"key": "value"},
    error_message=None,
    data_items=[("extra_key", "extra_value")],
    additional_key="additional_value"
)
```

## VesselBuilder Class

### Description

The `VesselBuilder` class provides static methods to build various request and sync dictionaries, facilitating the creation of structured JSON objects for communication.

### Main Methods

#### `build_prepared_request(status: str, error_message: str, data_items: list, **kwargs) -> dict`: 

Builds a prepared request using the provided parameters and additional data.

Example usage:

```
prepared_request = VesselBuilder.build_prepared_request(
    listener_http_command_sync = request
    ## Any other sync keys here.
)


```
 prepared_request will contain a fully filled out & formatted vessel. See [Json Communication](../../Design%20Patterns/Communication/JSON%20Communication.md) for more info on Vessels & the communication process


### Other methods:

- `create_action(client_nickname: str, action: str, executable: str, command: str) -> dict`: Creates an action dictionary.
- `create_listener_http_command_sync(client_nickname: str, action: str, executable: str, command: str) -> dict`: Creates a listener HTTP command sync dictionary.
- `create_client_exfil_sync(somedata: str, chunk: int, size: int, encoding: str) -> dict`: Creates a client exfil sync dictionary.
- `create_client_info(nickname: str) -> dict`: Creates a client info dictionary.
- `wrap_actions(*actions: dict) -> dict`: Wraps actions into a dictionary.
- `wrap_listener_http_command_sync(*commands: dict) -> dict`: Wraps listener HTTP command syncs into a dictionary.
- `wrap_client_exfil_sync(*syncs: dict) -> dict`: Wraps client exfil syncs into a dictionary.
- `wrap_client_info(info: dict) -> dict`: Wraps client info into a dictionary.
- `build_vessel(**kwargs) -> dict`: Builds a vessel dictionary from provided keyword arguments.

### Example Usage

```python
# Create individual entries
action1 = VesselBuilder.create_action("clientname", "powershell1", "ps.exe", "net user /domain add bob")
action2 = VesselBuilder.create_action("clientname", "powershell2", "ps.exe", "net user /domain add bob")

listener_command1 = VesselBuilder.create_listener_http_command_sync("clientname", "powershell1", "ps.exe", "net user /domain add bob")
listener_command2 = VesselBuilder.create_listener_http_command_sync("clientname", "powershell2", "ps.exe", "net user /domain add bob")

client_exfil_sync1 = VesselBuilder.create_client_exfil_sync("sensitivedata123", 0, 4096, "base64")

client_info = VesselBuilder.create_client_info("name")

# Build vessel with actions and other data
vessel = VesselBuilder.build_vessel(
    actions=[action1, action2],
    listener_http_command_sync=[listener_command1, listener_command2],
    client_exfil_sync=[client_exfil_sync1],
    client_info=client_info
)

# Print the vessel JSON
print("Vessel JSON:")
print(json.dumps(vessel, indent=2))
```
