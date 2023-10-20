Todo
- [ ] implement file access logs, both node, and server side

Server HTTP

| Endpoint | Desc | Auth Req'd |
|--------------|-----------|------------|
| /filehost | The filehost homepage & dashboard | yes |
| /filehost/upload | The upload endpoint | Yes |


Server API

| Endpoint | Desc | Method | Auth Req'd |
|--------------|-----------|------------|------------|
| /api/filehost/command | The API endpoint for external filehost plugins getting commadns | GET | yes (JWT) |
| /api/filehost/files | The API endpoint for getting info on the files stored by the control server| GET | yes (JWT) |


## Per Endpoint Details

#### /api/filehost/files

Displays JSON data of the current files on the control server. 

```
{
    "myfile00.txt": {
        "filedir": "/filehost/myfile00.txt",
        "filename": "myfile00.txt",
        "filesize": 28
    },
    "myfile01.txt": {
        "filedir": "/filehost/myfile01.txt",
        "filename": "myfile01.txt",
        "filesize": 28
    },
    "myfile02.txt": {
        "filedir": "/filehost/myfile02.txt",
        "filename": "myfile02.txt",
        "filesize": 28
    },
    "this.png": {
        "filedir": "/filehost/this.png",
        "filename": "this.png",
        "filesize": 104280
    },
    "this2.png": {
        "filedir": "/filehost/this2.png",
        "filename": "this2.png",
        "filesize": 79815
    }
}

```

#### /api/filehost/nodelogs

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


#### /api/filehost/checkin
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


#### /api/filehost/updatefilelogs

POST
Auth Required

fileaccess logs, a post endpoint. 

```
        {
            "filename":"notsafefile.exe",
            "accessorip":"y.y.y.y"
            "hostip":"x.x.x.x",
            "hostingserver":"fh01"
            "timestamp":"010101"
        }

```

#### /api/filehost/filelogs

GET
Auth Required

Where to retrieve file access logs from. Note that this is limited to 30 updating items. so, 
each request (should) contain new data as it comes in, while holding up to 30 past entries

Created from data posted to updatefilelogs

```
{
        1:{
            "filename":"notsafefile.exe",
            "accessorip":"y.y.y.y"
            "hostip":"x.x.x.x",
            "hostingserver":"fh01"
            "timestamp":"010101"
        },
        2:{
            "filename":"notsafefile.exe",
            "accessorip":"y.y.y.y"
            "hostip":"x.x.x.x",
            "hostingserver":"fh01"
            "timestamp":"010101"
        },
}

```
