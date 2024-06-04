# Command Forwarding

Command forwarding is used for forwarding certain SyncKeys from the Server, to a Listener.

Current keys that can be forwarded:

 - `ListenerHttpCommandSync`

Vessel (inbound to sync) -> SyncHandler/Parser -> each individual key parsed, if needed to be forwarded -> forward_request() > recondsturct vessel > send

## Steps:

---

#### 1. Request comes into Sync endpoint

The request comes into the server Sync endpoint. 

```
{
  "rid": "request_identifier", 
  "timestamp": 1710442988,
  "status": "success",
  "data": {
    "ListenerHttpCommandSync":[
        {"client_nickname":"23ce9b6d-4946-4f4d-9345-c772cdb515ba","action": "powershell","executable": "ps.exe","command": "whoami", "aid":"standin_aid"},
        {"client_nickname":"0234-1234-1234-1235","action": "powershell","executable": "ps.exe","command": "whoami", "aid":"standin_aid"}
    ]
  },
  "error": [{}]
}
```

#### 2. Parsing
The reqest is parsed with the SyncPlugin, and each SyncKey is handled by its respective handler. If the key is one of the following (key names), it automatically gets forwarded to the respective listener. 

How do we know what listener to forward to? A lookup is done with the data in the key. In the case of 'ListenerHttpCommandSync', the client_nickname key is used. 

```
{"client_nickname":"23ce9b6d-4946-4f4d-9345-c772cdb515ba","action": "powershell","executable": "ps.exe","command": "whoami", "aid":"standin_aid"}
```

The server stores data about the current connected listeners, and their connected clients. This data is used to find exactly what listener a client is on, and get the correct details for forwarding to it. 

#### 3. Forwarding:
Once the listener has been identified, it can be forwarded to. Each listener class has a `forward_request()` method, which takes two arguments:

- The name of the SyncKey to be forwarded (Ex: ListenerHttpCommandSync)
- That SyncKey's data. (ex: `{"client_nickname":"0234-1234-1234-1235","action": "powershell","executable": "ps.exe","command": "whoami", "aid":"standin_aid"}`)

From there, it constructs a new vessel, and forwards it to the listener.

Ex: 

```
{
  "rid": "new_request_identifier", 
  "timestamp": 1710442988,
  "status": "success",
  "data": {
    "ListenerHttpCommandSync":[
        {"client_nickname":"23ce9b6d-4946-4f4d-9345-c772cdb515ba","action": "powershell","executable": "ps.exe","command": "whoami", "aid":"standin_aid"},
        {"client_nickname":"0234-1234-1234-1235","action": "powershell","executable": "ps.exe","command": "whoami", "aid":"standin_aid"}
    ]
  },
  "error": [{}]
}
```