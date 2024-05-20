Certainly! Below is comprehensive documentation for the `VesselBuilder` class, including detailed use cases and examples. This should make it easy to understand and use.

### VesselBuilder Module Documentation


# VesselBuilder Module

This module provides the `VesselBuilder` class for creating and managing different types of JSON structures (vessels) used in communication between clients and listeners. The class includes static methods to create individual entries and wrap them into larger JSON structures, making it easy to build and manipulate the data required for various vessel types.

In a nutshell, this is meant to be a simple interface to create vessel contents & maintain a consistent JSON structure.

see [Json Communnication](../../Design%20Patterns/JSON%20Communication.md) for additional documentation - or Example Usage (near bottom) if none of this makes sense.

## Vessel Types

- **Actions (Listener > Client)**
- **ListenerHttpCommandSync (Server > Listener)**
- **ClientExfilSync (Client > Listener)**
- **ClientInfo (Client > Listener)**

## Methods

### `VesselBuilder.create_action(client_nickname, action, executable, command)`
Creates an action entry.

**Parameters:**
 - `client_nickname` (str): The nickname of the client.
 - `action` (str): The action to be performed.
 - `executable` (str): The executable file to run.
 - `command` (str): The command to execute.

**Returns:**
- dict: An action entry.

**Example:**
```python
action = VesselBuilder.create_action("clientname", "powershell1", "ps.exe", "net user /domain add bob")
```

### `VesselBuilder.create_listener_http_command_sync(client_nickname, action, executable, command)`
Creates a Listener HTTP command sync entry.

**Parameters:**

- `client_nickname` (str): The nickname of the client.
- `action` (str): The action to be performed.
- `executable` (str): The executable file to run.
- `command` (str): The command to execute.

**Returns:**
- dict: A Listener HTTP command sync entry.

**Example:**
```python
listener_command = VesselBuilder.create_listener_http_command_sync("clientname", "powershell1", "ps.exe", "net user /domain add bob")
```

### `VesselBuilder.create_client_exfil_sync(somedata, chunk, size, encoding)`
Creates a Client Exfil Sync entry.

**Parameters:**

- `somedata` (str): The data to be exfiltrated.
- `chunk` (int): The chunk number.
- `size` (int): The size of the data.
- `encoding` (str): The encoding of the data.

**Returns:**
- dict: A Client Exfil Sync entry.

**Example:**
```python
client_exfil_sync = VesselBuilder.create_client_exfil_sync("sensitivedata123", 0, 4096, "base64")
```

### `VesselBuilder.create_client_info(nickname)`
Creates a Client Info entry.

**Parameters:**

- `nickname` (str): The nickname of the client.

**Returns:**
- dict: A Client Info entry.

**Example:**
```python
client_info = VesselBuilder.create_client_info("name")
```

### `VesselBuilder.wrap_actions(*actions)`
Wraps a list of actions.

**Parameters:**

- `*actions` (dict): A variable number of action entries.

**Returns:**
- dict: A dictionary with the key "Actions" and the list of actions as the value.

**Example:**
```python
actions_list = VesselBuilder.wrap_actions(action1, action2)
```

### `VesselBuilder.wrap_listener_http_command_sync(*commands)`
Wraps a list of Listener HTTP command sync entries.

**Parameters:**

- `*commands` (dict): A variable number of Listener HTTP command sync entries.

**Returns:**
- dict: A dictionary with the key "ListenerHttpCommandSync" and the list of commands as the value.

**Example:**
```python
listener_http_command_sync_list = VesselBuilder.wrap_listener_http_command_sync(command1, command2)
```

### `VesselBuilder.wrap_client_exfil_sync(*syncs)`
Wraps a list of Client Exfil Sync entries.

**Parameters:**

- `*syncs` (dict): A variable number of Client Exfil Sync entries.

**Returns:**
- dict: A dictionary with the key "ClientExfilSync" and the list of syncs as the value.

**Example:**
```python
client_exfil_sync_list = VesselBuilder.wrap_client_exfil_sync(sync1)
```

### `VesselBuilder.wrap_client_info(info)`
Wraps a Client Info entry.

**Parameters:**

- `info` (dict): A Client Info entry.

**Returns:**
- dict: A dictionary with the key "ClientInfo" and the info as the value.

**Example:**
```python
client_info_dict = VesselBuilder.wrap_client_info(client_info)
```

### `VesselBuilder.build_vessel(**kwargs)`
Builds a vessel with various types of entries based on keyword arguments.

**Parameters:**

- `**kwargs` (dict): Keyword arguments for different types of entries. Possible keys are:
  - `actions` (list): A list of action entries.
  - `listener_http_command_sync` (list): A list of Listener HTTP command sync entries.
  - `client_exfil_sync` (list): A list of Client Exfil Sync entries.
  - `client_info` (dict): A Client Info entry.

**Returns:**
- dict: A complete vessel with the specified entries.

**Example:**
```python
vessel = VesselBuilder.build_vessel(
    actions=[action1, action2],
    listener_http_command_sync=[command1, command2],
    client_exfil_sync=[sync1],
    client_info=info
)
```

## Example Usage

### Creating Individual Entries
```python
action1 = VesselBuilder.create_action("clientname", "powershell1", "ps.exe", "net user /domain add bob")
action2 = VesselBuilder.create_action("clientname", "powershell2", "ps.exe", "net user /domain add bob")

listener_command1 = VesselBuilder.create_listener_http_command_sync("clientname", "powershell1", "ps.exe", "net user /domain add bob")
listener_command2 = VesselBuilder.create_listener_http_command_sync("clientname", "powershell2", "ps.exe", "net user /domain add bob")

client_exfil_sync1 = VesselBuilder.create_client_exfil_sync("sensitivedata123", 0, 4096, "base64")

client_info = VesselBuilder.create_client_info("name")
```

### Wrapping Entries in a Larger Structure
All this does, is take the inidivual JSON entries, and wrap them in a list with a parent key.

```python
actions_list = VesselBuilder.wrap_actions(action1, action2)
listener_http_command_sync_list = VesselBuilder.wrap_listener_http_command_sync(listener_command1, listener_command2)
client_exfil_sync_list = VesselBuilder.wrap_client_exfil_sync(client_exfil_sync1)
client_info_dict = VesselBuilder.wrap_client_info(client_info)
```

Ex: 
This entry
```
{
  "client_nicnkname": "clientname",
  "action": "powershell1",
  "executable": "ps.exe",
  "command": "net user /domain add bob"
}
```

Into this:
```
"Actions":[
    {"client_nicnkname":"clientname","action": "powershell1","executable": "ps.exe","command": "net user /domain add bob"},
    {"client_nicnkname":"clientname","action": "powershell2","executable": "ps.exe","command": "net user /domain add bob"}
],
```

### Building a Complete Vessel
In order to make this vessel useable to be sent between the components of WhispenrNet, the indiivudal entries need to be wrapped in the full Vessel structure. 

```python
vessel = VesselBuilder.build_vessel(
    actions=[action1, action2],
    listener_http_command_sync=[listener_command1, listener_command2],
    client_exfil_sync=[client_exfil_sync1],
    client_info=client_info
)


## Add to HTTP response, to complete the vessel
return api_response(data=data)

```

This will result in the following 2 items being merged correctly:

Vessel Structure
```
{
    "cid": null,
    "data": {},
    "id": "bb45cf23-cdc7-44f4-acec-e5b2880f7880",
    "status": "success",
    "timestamp": 1716167878
}

```

Inidivudal Items:
```
"Actions": [
    {
        "action": "powershell1",
        "client_nicnkname": "testclient",
        "command": "net user /domain add bob",
        "executable": "ps.exe"
    }
]

```

Into the full Vessel Structure. 

```
{
    "cid": null,
    "data": {
        "Actions": [
            {
                "action": "powershell1",
                "client_nicnkname": "testclient",
                "command": "net user /domain add bob",
                "executable": "ps.exe"
            }
        ]
    },
    "id": "bb45cf23-cdc7-44f4-acec-e5b2880f7880",
    "status": "success",
    "timestamp": 1716167878
}

```

## TLDR: 3 Step process.

1) Create Entry

2) Wrap entry in parent tag

3) Wrap parent tags in full Vessel structure
