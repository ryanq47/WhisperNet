Todo:

## Per Endpoint Details

#### /api/simplec2/nodelogs

GET
Auth Required

Contains the currently active FIlehost Nodes. Note that the primary key is the name of the node, so no duplicates here. These are just status updates

```

{
  "filehost01": {
    "ip": null,
    "message": "Heartbeat",
    "name": "filehost01",
    "timestamp": "2023-10-19 20:55:59"
  },
  "filehost02": {
    "ip": null,
    "message": "Heartbeat",
    "name": "filehost02",
    "timestamp": "2023-10-19 20:55:57"
  },
  "filehost03": {
    "ip": null,
    "message": "Heartbeat",
    "name": "filehost03",
    "timestamp": "2023-10-19 20:55:57"
  },
  "filehost04": {
    "ip": null,
    "message": "Heartbeat",
    "name": "filehost04",
    "timestamp": "2023-10-19 20:55:59"
  }
}


```


#### /api/simplec2/nodecheckin
POST
Auth Required

Checkin endpoint for nodes
```
        {
            "name":"",
            "ip":"",
            "message":"syncing | sync successful | sync failed | error"
            "timestamp":""
        }
```

