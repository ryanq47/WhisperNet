

The authentication handler is a library that handles all authentication related tasks for the server. 

For a quick visual, see <span style="color: red;">-- Add links here --</span>
- [Here for the client logon process](obsidian://open?vault=ObsidianDocs&file=Clients%2FPython%20Client%2FDev%20Docs%2FMindMaps%2FAuthentication%20Map.canvas)
- Here for the server logon process


#### Definitions/Clarifications:
- **Logon**: In simple terms, a logon is when you provide your credentials and get access
- **Authentication**:  Authentication is more focused on proving who you are, i.e. what you know/have/are, etc. <span style="color: #FFA500;">Currently, the server only supports logons, not "real" authentication, despite the name (08/22/23)</span>

## Function Dive


## Authentication.generate_random_cookie

This static method generates a random authentication cookie that can be used for secure user identification. It retrieves character options, minimum and maximum length settings, from a configuration file (The currently loaded YAML Client Profile)

The method then assembles a random cookie by selecting characters from the given set within the specified length range. If any errors occur during this process, they are logged for further investigation.

- <span style="color: #FF0000;">Currently, on an exception, 'False' is returned. The false value is handled by server.py</span>


```python
@staticmethod
def generate_random_cookie():
    logging.debug(f"{function_debug_symbol} {inspect.stack()[0][3]}")

    try:
        ## temp hardcode
        client_profile = Utils.UtilsHandler.yaml_load(yaml_file=r"Config\ClientProfiles\default.yaml")

        char_string = client_profile["Authentication"]["Cookies"]["Characters"]
        min_length  = client_profile["Authentication"]["Cookies"]["MinLength"]
        max_length  = client_profile["Authentication"]["Cookies"]["MaxLength"]

        ## Generate a random cookie
        random_cookie = ''.join(random.SystemRandom().choice(char_string) for _ in range(min_length, max_length))
        return random_cookie
    except Exception as e:
        logging.debug(f"[generate_random_cookie] {e}")
```

## Authentication.validate_password


This static method validates a given password against a predefined server password stored in a configuration file (The currently loaded YAML Client Profile). 

It loads the server password from the configuration, and then compares it with the provided password. If the two passwords match, the method returns `True`, indicating successful validation. Otherwise, it returns `False`.

```python
@staticmethod
def validate_password(password):
    logging.debug(f"{function_debug_symbol} {inspect.stack()[0][3]}")

    client_profile = Utils.UtilsHandler.yaml_load(yaml_file=r"Config\ClientProfiles\default.yaml")
    '''
    Load password from somewhere

    if server_password == password:
        return True

    else:
        return False


    '''
    server_password = client_profile["Authentication"]["Server"]["Password"]

    ## Need validation that the server_password is actually something

    if server_password == password:
        return True
    else:
        return False
```

## Authentication.validate_cookie

This static method, named `validate_cookie`, serves as a comparison tool to authenticate a received cookie against a valid cookie stored within a class instance. It returns `True` if the received `request_cookie` matches the stored `valid_cookie`, indicating successful validation. 

This function is designed to prevent unauthorized access by ensuring that both cookies are not empty and that they match. If the comparison fails, the method returns `False` and logs the occurrence.

```python
    @staticmethod
    def validate_cookie(request_cookie = None, valid_cookie = None):
        '''

        A comparison cookie tool. Returns True of the request cookie == valid_cookie

        request_cookie: the cookie from the requester/client

        valid_cookie: the current valid cookie for the client. Stored in a class instance

        '''
        logging.debug(f"{function_debug_symbol} {inspect.stack()[0][3]}")

        ## preventing heckers from gaining access by sending a blank cookie

        if request_cookie == None or valid_cookie == None:
            return False
            
        if request_cookie == valid_cookie:
            logging.debug("Cookie accepted")
            return True
            
        else:
            logging.warning("Cookie rejected bitch -- This is odd.")
            return False
```

## Cookie

The cookie class is just a storage object. A new instance of the class is called for new clients, and this instance is named after the client. 

At the moment it only holds the current valid cookie for said client, to check against when the client sends a request to the server. 

```python
class Cookie:
    """
    A class for making a cookie object. Holds data about valid cookies
    """
    def __init__(self):
        self.valid_cookie = None
```
```