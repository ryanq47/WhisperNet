import json
#from Utils.LoggingBaseClass import BaseLogging
from Utils.Logger import LoggingSingleton

########################################
# Client Auth
########################################
class ClientAuth:
    def __init__(self, user=None, password=None, auth_hash=None, kerb=None, other=None):
        self.logger = LoggingSingleton.get_logger()
        self._user = user if user else User()
        self._password = password if password else Password()
        self._hash = auth_hash if auth_hash else Hash() # hash is a func in python, whoops. Switching to auth_hash
        self._kerb = kerb if kerb else Kerb() 
        self._other = other if other else Other() 

    
    # User getter and setter
    @property
    def user(self):
        return self._user

    @user.setter
    def user(self, value):
        # Validation logic here
        self._user = value

    # Password getter and setter
    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        # Validation logic here
        self._password = value

    # Auth_hash getter and setter
    @property
    def auth_hash(self):
        return self._hash

    @auth_hash.setter
    def auth_hash(self, value):
        # Validation logic here
        self._hash = value

    # Kerb getter and setter
    @property
    def kerb(self):
        return self._kerb

    @kerb.setter
    def kerb(self, value):
        # Validation logic here
        self._kerb = value

    # Other getter and setter
    @property
    def other(self):
        return self._other

    @other.setter
    def other(self, value):
        # Validation logic here
        self._other = value

    def to_dict(self):
        return {
            'user': self.user.to_dict(),
            'password': self.password.to_dict(),
            'hash': self.auth_hash.to_dict(),
            'kerb': self.kerb.to_dict(),
            'other':self.other.to_dict(),
        }   


class User:
    def __init__(self, username = None, SID = None):
        self.logger = LoggingSingleton.get_logger()
        self._username = username
        self._SID = SID

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, value):
        # Validation logic here
        self._username = value

    @property
    def SID(self):
        return self._SID

    @SID.setter
    def SID(self, value):
        # Validation logic here
        self._SID = value


    def to_dict(self):
        return {
            'username':self._username,
            'SID':self._SID
        }


class Password:
    def __init__(self, p_type=None, value=None):
        self.logger = LoggingSingleton.get_logger()
        self._type = p_type
        self._value = value

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        # Validation logic here
        self._type = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        # Validation logic here
        self._value = value

    def to_dict(self):
        return {
            'type':self._type,
            'value':self._value
        }

class Hash:
    def __init__(self, h_type=None, value=None):
        self.logger = LoggingSingleton.get_logger()
        self._type = h_type
        self._value = value

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        # Validation logic here
        self._type = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        # Validation logic here
        self._value = value

    def to_dict(self):
        return {
            'type':self._type,
            'value':self._value
        }

class Kerb:
    def __init__(self, k_type=None, value=None):
        self.logger = LoggingSingleton.get_logger()
        self._type = k_type
        self._value = value

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        # Validation logic here
        self._type = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        # Validation logic here
        self._value = value

    def to_dict(self):
        return {
            'type':self._type,
            'value':self._value
        }

class Other:
    def __init__(self, o_type=None, value=None):
        self.logger = LoggingSingleton.get_logger()
        self._type = o_type
        self._value = value

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        # Validation logic here
        self._type = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        # Validation logic here
        self._value = value

    def to_dict(self):
        return {
            'type':self._type,
            'value':self._value
        }

########################################
# Action
########################################
class Action:
    def __init__(self, action=None, arguments=None, timeout=None, std_output=None, std_error=None, execution_context=None):
        self.logger = LoggingSingleton.get_logger()
        self._action = action
        self._arguments = arguments
        self._timeout = timeout
        self._std_output = std_output
        self._std_error = std_error
        self._execution_context = std_error

    
    #action
    @property
    def action(self):
        return self._action

    @action.setter
    def action(self, value):
        # Validation logic here
        self._action = value

    #argument
    @property
    def arguments(self):
        return self._arguments

    @action.setter
    def arguments(self, value):
        # Validation logic here
        self._arguments = value

    #execution_context
    @property
    def execution_context(self):
        return self._execution_context

    @execution_context.setter
    def execution_context(self, value):
        # Validation logic here
        self._execution_context = value

    #timeout
    @property
    def timeout(self):
        return self._timeout

    @timeout.setter
    def timeout(self, value):
        # Validation logic here
        self._timeout = value

    #timeout
    @property
    def std_output(self):
        return self._std_output

    @std_output.setter
    def std_output(self, value):
        # Validation logic here
        self._std_output = value

    # std error
    @property
    def std_error(self):
        return self._std_error

    @std_error.setter
    def std_error(self, value):
        # Validation logic here
        self._std_error = value


    def to_dict(self):
        #return {k.lstrip('_'): v for k, v in self.__dict__.items() if v is not None}
        return {
            'action': self.action,
            'arguments': self.arguments,
            'execution_context': self.execution_context,
            'timeout': self.timeout,
            'std_output':self.std_output,
            'std_error':self.std_error
        }


########################################
# Callback Section
########################################
class Callback:
    """
        Initializes a new Callback instance.

        This constructor initializes the Callback object with optional server, retry policy, 
        and data format configurations. If any of these parameters are not provided, 
        they are set to their default values.

        Parameters:
        server (Server, optional): An instance of the Server class representing the server
            configuration. If not provided, a default Server object is created.

        retry_policy (RetryPolicy, optional): An instance of the RetryPolicy class representing
            the retry policy configuration. If not provided, a default RetryPolicy object is created.

        data_format (str, optional): A string representing the data format (e.g., 'json'). 
            If not provided, it defaults to None.

        Example:
        callback = Callback(
            server=Server(hostname="example.com", port="8080"),
            retry_policy=RetryPolicy(max_retries="3", retry_interval="10"),
            data_format="json"
        )
    """
    def __init__(self, server=None, retry_policy=None, data_format=None):
        self.logger = LoggingSingleton.get_logger()
        self._server = server if server else Server()
        self._retry_policy = retry_policy if retry_policy else RetryPolicy()
        self._data_format = data_format

    @property
    def server(self):
        return self._server

    @server.setter
    def server(self, value):
        # Assuming value is an instance of Server
        self._server = value

    # Similar for retry_policy and data_format
    @property
    def retry_policy(self):
        return self._retry_policy

    @retry_policy.setter
    def retry_policy(self, value):
        # Assuming value is an instance of Server
        self._retry_policy = value

    @property
    def data_format(self):
        return self._data_format

    @data_format.setter
    def data_format(self, value):
        # Assuming value is an instance of Server
        self._data_format = value

    def to_dict(self):
        # could rework this in the future if needed, to grab nested obj & to_dict it
        #return {k.lstrip('_'): v for k, v in self.__dict__.items() if v is not None}
        return {
            'server': self.server.to_dict() if self.server else None,
            'retry_policy': self.retry_policy.to_dict() if self.retry_policy else None,
            'data_format': self.data_format
        }

class RetryPolicy:
    def __init__(self, max_retries=None, retry_interval=None):
        self.logger = LoggingSingleton.get_logger()
        self._max_retries = max_retries
        self._retry_interval = retry_interval

    @property
    def max_retries(self):
        return self._max_retries

    @max_retries.setter
    def max_retries(self, value):
        # Validation logic here
        self._max_retries = value

    # Same for retry_interval

    @property
    def retry_interval(self):
        return self._retry_interval

    @retry_interval.setter
    def retry_interval(self, value):
        # Validation logic here
        self._retry_interval = value

    def to_dict(self):
        #return {k.lstrip('_'): v for k, v in self.__dict__.items() if v is not None}
        return {
            'max_retries': self.max_retries,
            'retry_interval': self.max_retries
        }

class Server:
    def __init__(self, hostname=None, address=None, port=None, path=None):
        self.logger = LoggingSingleton.get_logger()
        self._hostname = hostname
        self._address = address
        self._port = port
        self._path = path

    @property
    def hostname(self):
        return self._hostname

    @hostname.setter
    def hostname(self, value):
        # Add any validation if needed
        self._hostname = value

    # Repeat the above pattern for address, port, and path
    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        # Add any validation if needed
        self._address = value

    # port
    @property
    def port(self):
        return self._port

    @port.setter
    def port(self, value):
        # Add any validation if needed
        self._port = value

    # path
    @property
    def path(self):
        return self._path

    @path.setter
    def path(self, value):
        # Add any validation if needed
        self._path = value

    def to_dict(self):
        return {
            'hostname'  :self.hostname,
            'address'   :self.address,
            'port'      :self.port,
            "path"      :self.path
        } 
        


########################################
# ACtion
########################################


########################################
# Parent/Construction of everything
########################################
class JsonObject():
    def __init__(self):
        self.logger = LoggingSingleton.get_logger()
        #BaseLogging.__init__(self)  
        self.server = Server()
        self.callback = Callback()
        self.action = Action()
        self.client_auth = ClientAuth()

    def to_dict(self):
        '''Turns all supplied values into the final dict.
        Call this method to get a DICT from the object. 

        Returns: Dict
        
        
        '''
        py_dict = {}

        try:
            py_dict = {
                "action":self.action.to_dict(),
                "callback":self.callback.to_dict(),
                "client_auth":self.client_auth.to_dict()
            }
        except Exception as e:
            print(f"Could not create a dict: {e}")

        return py_dict
    


    def to_json(self, inlcude_empty_keys=False):
        """
        Turns all supplied values into a final dict and removes keys with None values.
        Call this method to get a JSON string from the object. 

        Returns: 
            str: A JSON string representation of the object with 'None' values omitted.
        """
        try:
            py_dict = self.to_dict()

            ## Just in case this is needed in the future. 
            if inlcude_empty_keys:
                dict_with_empty = json.dumps(py_dict)
                return json.dumps(dict_with_empty)

            else:
                # Recursively remove keys where the value is None
                cleaned_dict = self.remove_none_values(py_dict)

                # Convert the cleaned dictionary to JSON
                json_data = json.dumps(cleaned_dict)

                return json_data

        except Exception as e:
            print(f"Could not create a JSON object: {e}")
            return None

    def remove_none_values(self, d):
        """ Recursively remove keys with None values from a dictionary. """
        if not isinstance(d, dict):
            return d
        return {k: self.remove_none_values(v) for k, v in d.items() if v is not None}

    def from_json(self, json_data):
        """
        Create an instance of MyJsonObject from a JSON string.
        
        Args:
            json_data (str): A JSON string representation of the object.
            
        Returns:
            MyJsonObject: An instance of MyJsonObject populated with data from the JSON string.
        """

        ## Alrighty this looks complicated, but all it's doing is pulling keys from the JSON, and 
        ## Putting them into the args of each class, thus creating our pydict object
        ## If the key is not present, then it gets a value of None
        try:
            data = json.loads(json_data)

            # Creating Action instance from JSON
            action_data = data.get("action", {})
            self.action = Action(
                action=action_data.get("action", None),
                arguments=action_data.get("arguments", None),
                timeout=action_data.get("timeout", None),
                std_output=action_data.get("std_output", None),
                std_error=action_data.get("std_error", None),
                execution_context=action_data.get("execution_context", None)

            )

            # Creating ClientAuth instance from JSON
            auth_data = data.get("client_auth", {})
            user_data = auth_data.get("user", {})
            password_data = auth_data.get("password", {})
            hash_data = auth_data.get("hash", {})
            kerb_data = auth_data.get("kerb", {})
            other_data = auth_data.get("other", {})

            self.client_auth = ClientAuth(
                user=User(username=user_data.get("username", None), SID=user_data.get("SID", None)),
                password=Password(p_type=password_data.get("type", None), value=password_data.get("value", None)),
                auth_hash=Hash(h_type=hash_data.get("type", None), value=hash_data.get("value", None)),
                kerb=Kerb(k_type=kerb_data.get("type", None), value=kerb_data.get("value", None)),
                other=Other(o_type=other_data.get("type", None), value=other_data.get("value", None))
            )

            # Creating Callback instance from JSON
            callback_data = data.get("callback", {})
            server_data = callback_data.get("server", {})
            retry_policy_data = callback_data.get("retry_policy", {})

            self.callback = Callback(
                server=Server(
                    hostname=server_data.get("hostname", None),
                    address=server_data.get("address", None),
                    port=server_data.get("port", None),
                    path=server_data.get("path", None)
                ),
                retry_policy=RetryPolicy(
                    max_retries=retry_policy_data.get("max_retries", None),
                    retry_interval=retry_policy_data.get("retry_interval", None)
                ),
                data_format=callback_data.get("data_format", None)
            )

            return self

        except Exception as e:
            #self.logger.error(f"Error parsing JSON data: {e}")
            print(f"Error parsing JSON data: {e}")
            return None


"""

{
  "action": {
    "action": null,
    "arguments": null,
    "timeout": null,
    "std_output": null,
    "std_error": null,
    "execution_context": null
  },
  "client_auth": {
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


"""

"""
{
  "request_id": "unique_request_identifier",
  "timestamp": "2024-03-14T12:34:56Z",
  "action": {
    "command": "operation_name",
    "parameters": {
        "param1": "value1",
        "param2": "value2"
        // Additional parameters as needed
    }
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
    }
  },
}       



"""