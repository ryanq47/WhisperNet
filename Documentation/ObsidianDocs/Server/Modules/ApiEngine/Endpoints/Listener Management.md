

#### /list
Protected URL!
Method: Post

Spawns a listener. 

JSON Request:
```
{
	ip = "ip_to_listen_on" (str)
	port = "port to listen on" (str)
}
```

Full Request:
```
POST /createuser HTTP/1.1
Host: 127.0.0.1:5000
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY5NDU4MTAxMCwianRpIjoiNTdhMzMzM2UtYzRhOS00Y2QwLWEwMTUtOGUyYThmMDZkMGE0IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6InVzZXJuYW1lIiwibmJmIjoxNjk0NTgxMDEwLCJleHAiOjE2OTQ1ODE5MTB9.FawMrMHs8iMDT6L38obSAw-iN-y_zNdBuxf9OCSfSLk
Content-Type: application/json
Content-Length: 70

{
    "ip":"0.0.0.0",
    "port":"8080"
}
```

Response:

```
Success - Listener started on 0.0.0.0:8080
```