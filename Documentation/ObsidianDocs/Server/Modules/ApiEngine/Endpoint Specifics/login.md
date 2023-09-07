
/login is the default API endpoint for logging in. Each log in request requires a few thigns to succesfully authencticate:
1) Valid Username & Password
2) Correctly Formatted JSON



## 1) Valid User & Pass

A valid username & password is required to log into the server. These are pulled from the 'DataBases/users.db'

function overview here & bcrypt


## 2) Correctly Formatted JSON
The JSON format should be this:

```
{
    "username": "admin",
    "password": "1234"
}
```