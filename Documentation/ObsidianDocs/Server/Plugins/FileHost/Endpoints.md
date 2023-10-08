
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