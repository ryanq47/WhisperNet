
/login is the default API endpoint for logging in. Each log in request requires a few things to successfully authenticate:
1) Valid Username & Password
2) Correctly Formatted JSON



## 1) Valid User & Pass

A valid username & password is required to log into the server. These are pulled from the 'DataBases/users.db'

function overview here & bcrypt

Once a successful authentication has happened, a JWT is returned to the user via JSON

```
{
    "access_token": "tokenstring.tokenstring.tokenstring"
}
```



## 2) JSON Format
The JSON format should be this:

```
{
    "username": "admin",
    "password": "1234"
}
```


## 3) Headers
After a successful authentication, the server sends back a JWT. This is used for further authentication & access to restricted URL's


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


## Creating Users



## Deleting users