## HTTP Listener JSON Communication

This outlines how communication is hanlded between the nodes and the clients for the HTTP listener. 

To see construction of how to generate these:

 - [HTTPJsonRequest](../../../Server/Plugins/ListenerHTTP/HTTPJsonRequest.md)

#### Data
the data sent TO the clients. 
```
{
    "request_id": null,      
    "timestamp": 1710442988, 
    "action": {
        "command": null,     
        "parameters": null   
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
            "address": null,
            "port": null,
            "path": null
        },
        "retry_policy": {
            "max_retries": null,
            "retry_interval": null
        },
        "data_format": null
    }
}

```


#### From Clients
The data sent BACK from clients, to the server
```
{
  "response_id": "matching_request_identifier",
  "request_id": "unique_request_identifier",
  "timestamp": 1710442988,
  "status": "success",
  "result": {
    "data": "Example result data "
  },
  "error": {
    "code": null,
    "message": null
  }
}

```