# VesselBuilder Class and API Functions Documentation

## Overview

The `VesselBuilder` class is designed to construct a JSON structure for communication between different components of a system. This structure includes various Sync Keys such as Actions, ListenerHttpCommandSync, ClientExfilSync, and ClientInfo. Additionally, the `api_request` and `api_response` functions help in creating and handling the request and response JSON structures, respectively.

## Classes and Functions
---

## `MessageHelper` Class

---

Helper class to generate unique IDs and timestamps.

#### Methods

```python
@staticmethod
def generate_unique_id() -> str:
    """
    Generate a unique UUIDv4 string.
    """
    return str(uuid.uuid4())

@staticmethod
def generate_timestamp() -> int:
    """
    Generate the current timestamp in seconds since the epoch.
    """
    return int(time.time())
```

### `api_request` Function

Helper function to create a request Dict structure. 

#### Parameters

- `status` (str): Status of the request, e.g., "success" or "failure".
- `data` (dict): Data to be included in the request.
- `error_message` (str): Error message, if any.

#### Returns

- `dict`: The constructed request dictionary.

```python
def api_request(status: str = "success", data: dict = None, error_message: str = None) -> dict:
    return {
        "rid": MessageHelper.generate_unique_id(),
        "timestamp": MessageHelper.generate_timestamp(),
        "status": status,
        "data": data if data else {},
        "error": {"message": error_message, "aid": [], "rid": None} if error_message else {}
    }
```

### `api_response` Function

Helper function to create a response JSON structure. Used accross the project as the default return method for API requests

#### Parameters

- `status` (str): Status of the response, e.g., "success" or "failure".
- `data` (dict): Data to be sent back in the response.
- `error_message` (str): Error message, if any.
- `data_items` (list): List of tuples (key, value) to add to the data dict.
- `**kwargs`: Additional keyword arguments to include in the response.

#### Returns

- `tuple`: A tuple containing the JSON response and the status code.

```python
def api_response(status: str = "success", data: dict = None, error_message: str = None, data_items: list = None, **kwargs) -> tuple:
    response = {
        "rid": MessageHelper.generate_unique_id(),
        "timestamp": MessageHelper.generate_timestamp(),
        "status": status,
        "data": data if data else {},
        "error": error_message if error_message else {}
    }

    if data_items:
        for key, value in data_items:
            response["data"][key] = value

    if not response["error"]:
        del response["error"]

    if not response["data"]:
        del response["data"]

    response.update({k: v for k, v in kwargs.items() if v is not None})

    return jsonify(response), 200
```

## `VesselBuilder` Class

---

Class to build the vessel structure with various Sync Keys.

#### Methods

```python
def __init__(self):
    self.vessel = {"data": {}}

def add_action(self, client_nickname: str, action: str, executable: str, command: str, aid: str):
    """
    Add an action to the Actions Sync Key.
    """
    action_entry = {
        "client_nickname": client_nickname,
        "action": action,
        "executable": executable,
        "command": command,
        "aid": aid
    }
    self._add_to_sync_key("Actions", action_entry)
    return self

def add_listener_http_command_sync(self, client_nickname: str, action: str, executable: str, command: str):
    """
    Add a command to the ListenerHttpCommandSync Sync Key.
    """
    listener_command = {
        "client_nickname": client_nickname,
        "action": action,
        "executable": executable,
        "command": command
    }
    self._add_to_sync_key("ListenerHttpCommandSync", listener_command)
    return self

def add_client_exfil_sync(self, data: str, chunk: int, size: int, encoding: str, cid: str):
    """
    Add data to the ClientExfilSync Sync Key.
    """
    client_exfil_sync = {
        "data": data,
        "chunk": chunk,
        "size": size,
        "encoding": encoding,
        "cid": cid
    }
    self._add_to_sync_key("ClientExfilSync", client_exfil_sync)
    return self

def add_client_info(self, nickname: str):
    """
    Add client information to the ClientInfo Sync Key.
    """
    client_info = {"nickname": nickname}
    self.vessel["data"]["ClientInfo"] = client_info
    return self

def _add_to_sync_key(self, key: str, entry: dict):
    """
    Helper method to add entries to the correct Sync Key.
    """
    if key not in self.vessel["data"]:
        self.vessel["data"][key] = []
    self.vessel["data"][key].append(entry)

def build(self, status: str = "success", error_message: str = None) -> dict:
    """
    Finalize the construction and return the complete JSON structure.
    """
    return api_request(status=status, data=self.vessel["data"], error_message=error_message)
```

## Example Usage

---

### Building a Vessel

```python
# Initialize the builder
builder = VesselBuilder()

# Add actions
builder.add_action("clientname", "powershell1", "ps.exe", "net user /domain add bob", "1234")
builder.add_action("clientname", "powershell2", "ps.exe", "net group /add Domain Admins Bob", "1235")

# Add listener HTTP command sync
builder.add_listener_http_command_sync("clientname", "powershell1", "ps.exe", "net user /domain add bob")

# Add client exfil sync
builder.add_client_exfil_sync("sensitivedata123", 0, 4096, "base64", "uuid-uuid-uuid-uuid")

# Add client information
builder.add_client_info("name")

# Build the vessel
vessel = builder.build()

# Print the vessel JSON
print(json.dumps(vessel, indent=2))
```

### Generating a Response

```python
# Generate a response using the api_response function
response = api_response(status="success", data=vessel["data"], error_message=None)

# Print the response JSON
print(json.dumps(response, indent=2))
```
