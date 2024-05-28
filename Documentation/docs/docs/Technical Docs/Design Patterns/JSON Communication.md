## JSON Transport Vessel/Comms

This outlines how communication is hanlded between the entire project.

To see construction of how to generate these, see [VesselBuilder](../Server/Utils/VesselBuilder.md).


#### Universal Comms

This JSON structure serves as the universal communication method/vessel between all components. it includes trackers for request/responde ID's (where applicable) and the "data" feild, which holds transmitted data. 
On the server side, the "data" feild is parsed for each subkey, and that type of data is handled appropriately.


```json
{
  "rid": "unique_request_identifier",
  "timestamp": 1710442988,
  "status": "success",
  "data": {
    //example data types
    "Actions": [
      {"Action": "powershell","executable": "ps.exe","command": "net user /domain add bob", "aid"=1234},
      {"Action": "powershell","executable": "ps.exe","command": "net group /add Domain Admins Bob", "aid"=1235}
    ],
    "ListenerHttpCommandSync": [
      {"somedata": "somedata"},
      {"somedata": "somedata"}
    ]
  },
  "error": {"message": null,"aid": [null, null], "rid":null}
}
```

## Usage

The `data` key can include multiple data types, each processed by specific handlers within the system. See Vessel Types for current vessels.

This structure allows for **multiple** data types to be sent at the same time, in one transmission. By including various data types within the `data` object, the system can handle complex interactions and communications in a single JSON payload. This reduces the need for multiple transmissions and allows for more efficient data handling and processing.


# Vessel Types:

## **Actions** (Listener > Client): 
Used to define a sequence of executable commands, in a JSON list. Each action includes the executable file and the command to run.

```
{
  "client_nicnkname": "clientname",
  "action": "powershell1",
  "executable": "ps.exe",
  "command": "net user /domain add bob"
}
```

Example in Vessel:

```
"Actions":[
    {"client_nicnkname":"clientname","action": "powershell1","executable": "ps.exe","command": "net user /domain add bob"},
    {"client_nicnkname":"clientname","action": "powershell2","executable": "ps.exe","command": "net user /domain add bob"}
],

```


## **ListenerHttpCommandSync** (Server > Listener) : 

Used for synchronizing HTTP commands. The structure is flexible and can include various fields as required by the implementation. Generally used Server -> Listener. Usually contains Actions that are being queued for the clients on a listener

```
{
  "client_nicnkname": "clientname",
  "action": "powershell1",
  "executable": "ps.exe",
  "command": "net user /domain add bob"
}
```

Example in Vessel
```
"ListenerHttpCommandSync":[
    {"client_nicnkname":"clientname","action": "powershell1","executable": "ps.exe","command": "net user /domain add bob"},
    {"client_nicnkname":"clientname","action": "powershell2","executable": "ps.exe","command": "net user /domain add bob"}
],
```

## **ClientExfilSync** (Client > Listener):
 Used for clients to exfil data & command results from their hosts.

 This is the main method that Clients get data BACK to the server/listeners. 

 it uses the cid to track what request it came from/it correlates to

```
{
  "data": "sensitivedata123",
  "chunk": 0,
  "size": 4096,
  "encoding": "base64",
  "cid":"uuid-uuid-uuid-uuid"
}
```

Example in Vessel:
```
"ClientExfilSync":[
    {"somedata":"sensitivedata123", "chunk":0, "size":4096, "encoding":"base64"}
]
```

## **ClientInfo** (Client > Listener):

Used by clients for checking in to the listeners.


```
{
  "nickname":"name"
}
```

Example in Vessel:

```
"ClientInfo": {
    "nickname":"name"
}
```

## **ListenerInfo** (Listener > Server):

Used by listeners for checking in to the server.


```
{
  "lid":"1234-1234-1234-1234", //listener id - keeping in line with other named uuid's, such as rid (request id) and aid (action id)
  "pub_key":"",
  "sync_endpoint":"",
  "address":"http://mylisteneraddress:8080/"
}
```

Example in Vessel:

```
"ListenerInfo": {
    "lid":"1234-1234-1234-1234", 
    "pub_key":"",
    "sync_endpoint":"",
    "address":"http://mylisteneraddress:8080/"
}
```