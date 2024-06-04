# What happens when I... Queue/Run an HTTP commmand:

delme: mini docs on what happens when things happen. move to userdocs or somewhere else later? Also used for me to make sure things work as expected.

## GUI

Inputted command(s): 

`powershell whoami`

`powershell whoami /all`

[NOT IMPLEMENTED] Those commands are parsed, and put into the appropriate sync keys within a vessel structure.

```
{
  "rid": "1234-5678-9876-0000", 
  "timestamp": 1710442988,
  "status": "success",
  //Data from diff plugins/things
  "data": {
    "ListenerHttpCommandSync":[
        {"client_nickname":"0234-1234-1234-1235","action": "powershell","executable": "ps.exe","command": "whoami", "aid":"standin_aid"},
        {"client_nickname":"0234-1234-1234-1235","action": "powershell","executable": "ps.exe","command": "whoami /all", "aid":"standin_aid"}
    ]
  },
  //stand in error message
  "error": [
    {"message":"error_msg", "aid":"1234", "rid":"1234"}
    ]
}

```

From there, they are forwarded to the server

## Server

The server takes the Vessel at its Sync endpoint, in this case: `/api/sync`

#### Server Logs: 
Note, for brevity, the timestamps have been removed from this output, and replaced with numbers.

```
1. [*] Sync.handle_sync_request - Received SYNC request from 127.0.0.1
2. [D] SyncHandler._parse_result - Processing recieved data with ListenerHttpSync
3. [D] SyncHandler._parse_result - Storing recieved data [{'client_nickname': '0234-1234-1234-1235', 'action': 'powershell', 'executable': 'ps.exe', 'command': 'whoami', 'aid': 'standin_aid'}, {'client_nickname': '0234-1234-1234-1235', 'action': 'powershell', 'executable': 'ps.exe', 'command': 'whoami', 'aid': 'standin_aid'}]
4. [D] ListenerHttpSync.store_response - Storing data
5. [D] ListenerHttpSync.store_response - Data from the response has been stored successfully.
6. [D] Listener.check_if_client_is_apart_of_listener - Client 0234-1234-1234-1235 exists in listener 1234-1234-1234-1234
7. [D] Listener.forward_request - forwarding request to listener 1234-1234-1234-1234 at http://127.0.0.1:5001///http/sync
```
1.: The Sync request has been received by the server. This does *not* mean that the sync request was correctly formatted, etc, only that a request *has* been placed to the sync endpoint. 


2-5.: The SyncHandler class uses it's _parse_result method to parse the inputted sync request. It iterates through each SyncKey in the request to find a matching method to parse that type of data. Ex, if the SyncKey is `ListenerHttpCommandSync`, it will be parsed with the `ListenerHttpCommandSync` class. (These logic/mappings are defined in the `SyncHandler` subclass). 

In this case, it recieved a `ListenerHttpCommandSync` key. (All keys & Definitions [here](../Communication/JSON%20Communication.md)). The `ListenerHttpCommandSync` is used to pass commands for clients to wherever they need to go. 

6-7.:Each key is iterated over, and the CID (Client ID) is extracted from each entry. This CID is used to perform a lookup of what listener the intended client is on. Once a listener has been identified, the entry is forwarded on to that listener, at its sync endpoint. 


## Listener

Similar to the server, the listener also recieves its sync request to the sync endpoint, in this case, `/http/sync`. All requests to this endpoint go through a near identical process as the Server Sync Handler. 

In fact, the whole process up until forwarding the request is nearly the same. Instead of forwarding the request, the Listener does a lookup to check if a client has an entry on the listener, (if not, it creates one), and then queues the entry to be sent off to the client. 


## Client
On heartbeat/check-ins from the client, it reaches out to the `/http/post` endpoint. (add link to more details of this process here). 
A lookup is done with the client's CID to make sure the client exists. The listener then dequeues the front item from that client's queue, and sends it to the client. 

The client then parses the response, in a similar manner to the Listener, and Server. It then performs actions based on the parsed response, (such as running powershell). The result of that command is packaged up in a `ClientExfilSync` SyncKey inside of a vessel, and posted to the `/http/sync` endpoint. 

Note, The process of getting that response back to the server has not been built out yet.
