
## JSON Transport Vessel/Comms

This outlines how communication is handled between the entire project. To see how it is tied together/implemented, check out the [Sync Process](../Communication/Sync%20Process.md).

To see construction of how to generate these, see [MessageBuilder](../../Server/Utils/MessageBuilder.md).

### Universal Comms

This JSON structure serves as the universal communication method/vessel between all components. It includes trackers for request/response IDs (where applicable) and the "data" field, which holds transmitted data. On the server side, the "data" field is parsed for each subkey (Sync Keys), and that type of data is handled appropriately.

### Definitions

- **Vessel**: The entire JSON structure.
- **Sync Keys**: Individual subkeys under the `data` key. See [Usage](#usage) below for more information.


### Vessel Example:
```json
{
  "rid": "unique_request_identifier",
  "timestamp": 1710442988,
  "status": "success",
  "data": {
    // Example data types
    "Actions": [
      {"Action": "powershell","executable": "ps.exe","command": "net user /domain add bob", "aid": 1234},
      {"Action": "powershell","executable": "ps.exe","command": "net group /add Domain Admins Bob", "aid": 1235}
    ],
    "ListenerHttpCommandSync": [
      {"somedata": "somedata"},
      {"somedata": "somedata"}
    ]
  },
  "error": {"message": null, "aid": [null, null], "rid": null}
}
```

### Usage

The `data` key can include multiple data types, which are JSON subkeys. These are called `Sync Keys`. Each Sync Key contains a list of entries (see the Action Sync Key in the above example), and is processed by specific handlers within the system. See [Sync Key Types](#sync-key-types) for current Sync Keys.

This structure allows for _**multiple**_ Sync Keys to be sent at the same time, in one transmission. By including these various Sync Keys within the `data` key, the system can handle complex interactions and communications in a single JSON payload. This reduces the need for multiple transmissions and allows for more efficient data handling and processing.

## Sync Key Types

### **Actions** (Listener > Client)

Used to define a sequence of executable commands, in a JSON list. Each action includes the executable file and the command to run.

#### Contents of individual key entry:

```json
{
  "client_nickname": "clientname",
  "action": "powershell1",
  "executable": "ps.exe",
  "command": "net user /domain add bob"
}
```

#### Example in Sync Key:

```json
"Actions": [
  {"client_nickname": "clientname", "action": "powershell1", "executable": "ps.exe", "command": "net user /domain add bob"},
  {"client_nickname": "clientname", "action": "powershell2", "executable": "ps.exe", "command": "net user /domain add bob"}
]
```

### **ListenerHttpCommandSync** (Server > Listener)

Used for synchronizing HTTP commands. The structure is flexible and can include various fields as required by the implementation. Generally used Server -> Listener. Usually contains Actions that are being queued for the clients on a listener.

#### Contents of individual key entry:

```json
{
  "client_nickname": "clientname",
  "action": "powershell1",
  "executable": "ps.exe",
  "command": "net user /domain add bob"
}
```

#### Example in Sync Key:

```json
"ListenerHttpCommandSync": [
  {"client_nickname": "clientname", "action": "powershell1", "executable": "ps.exe", "command": "net user /domain add bob"},
  {"client_nickname": "clientname", "action": "powershell2", "executable": "ps.exe", "command": "net user /domain add bob"}
]
```

### **ClientExfilSync** (Client > Listener)

Used for clients to exfiltrate data & command results from their hosts. This is the main method that clients use to get data back to the server/listeners. It uses the `cid` to track what request it came from/it correlates to.

#### Contents of individual key entry:

```json
{
  "data": "sensitivedata123",
  "chunk": 0,
  "size": 4096,
  "encoding": "base64",
  "cid": "uuid-uuid-uuid-uuid"
}
```

#### Example in Sync Key:

```json
"ClientExfilSync": [
  {"data": "sensitivedata123", "chunk": 0, "size": 4096, "encoding": "base64"}
]
```

### **ClientInfo** (Client > Listener)

Used by clients for checking in to the listeners.

#### Contents of individual key entry:

```json
{
  "nickname": "name"
}
```

#### Example in Sync Key:

```json
"ClientInfo": {
  "nickname": "name"
}
```

### **ListenerInfo** (Listener > Server)

Used by listeners for checking in to the server.

#### Contents of individual key entry:

```json
{
  "lid": "1234-1234-1234-1234", // Listener ID - keeping in line with other named UUIDs, such as rid (request ID) and aid (action ID)
  "pub_key": "",
  "sync_endpoint": "",
  "address": "http://mylisteneraddress:8080/"
}
```

#### Example in Sync Key:

```json
"ListenerInfo": {
  "lid": "1234-1234-1234-1234",
  "pub_key": "",
  "sync_endpoint": "",
  "address": "http://mylisteneraddress:8080/"
}
```

### **ListenerHttpClientSync** (Listener > Server)

Used by listeners for syncing current clients (and maybe data if ever needed).

#### Contents of individual key entry:

```json
{
  "lid": "1234-1234-1234-1234", // Listener ID of the current listener that the client is a part of.
  "cid": "1234-1234-1234-1234"  // Client ID of the client.
}
```

#### Example in Sync Key:

```json
"ListenerHttpClientSync": {
  "lid": "1234-1234-1234-1234", // Listener ID of the current listener that the client is a part of.
  "cid": "1234-1234-1234-1234"  // Client ID of the client.
}
```
