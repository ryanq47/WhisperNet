Protected Url: True

The user management section of the server has 2 endpoints:
- /createuser
- /deleteuser

They create/delete a user.


#### /createuser
Protected URL!
Method: Post

Creates a user in the user.db DB

JSON Request:
```
{
	username = "username_to_create"
	password = "pass_of_account"
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
    "username": "bobthebuilder5",
    "password": "password123"
}
```
---
#### /deleteuser

Protected URL! 
Method: Post

Deletes a user from the user.db DB

JSON Request
```
{
	username = "username_to_delete"
}
```

Full Request:
```
POST /deleteuser HTTP/1.1
Host: 127.0.0.1:5000
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY5NDU4MTAxMCwianRpIjoiNTdhMzMzM2UtYzRhOS00Y2QwLWEwMTUtOGUyYThmMDZkMGE0IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6InVzZXJuYW1lIiwibmJmIjoxNjk0NTgxMDEwLCJleHAiOjE2OTQ1ODE5MTB9.FawMrMHs8iMDT6L38obSAw-iN-y_zNdBuxf9OCSfSLk
Content-Type: application/json
Content-Length: 70

{
    "username": "bobthebuilder5",
    "password": "password123"
}

```
---