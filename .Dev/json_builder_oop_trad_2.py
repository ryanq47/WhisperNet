########################################
# Action
########################################
class Action:
    def __init__(self, action=None, arguments=None, timeout=None, std_output=None, std_error=None):
        self._action = action
        self._arguments = arguments
        self._timeout = timeout
        self._std_output = std_output
        self._std_error = std_error

    
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
class MyJsonObject:
    def __init__(self):
        self.server = Server()
        self.callback = Callback()
        self.action = Action()

    ''' Not used, but optional
    # Example of a method to update server details
    def update_server(self, hostname=None, address=None, port=None, path=None):
        self.server.hostname = hostname if hostname is not None else self.server.hostname
        self.server.address = address if address is not None else self.server.address
        self.server.port = port if port is not None else self.server.port
        self.server.path = path if path is not None else self.server.path

    # Example of a method to update callback details
    def update_callback(self, server=None, max_retries=None, retry_interval=None, data_format=None):
        if server:
            self.callback.server = server
        if max_retries or retry_interval:
            self.callback.retry_policy = RetryPolicy(max_retries, retry_interval)
        if data_format:
            self.callback.data_format = data_format
    '''

    def to_dict(self):
        '''Turns everyhting into the final dict'''

        return {
            "action":self.action.to_dict(),
            "callback":self.callback.to_dict()

        }


obj = MyJsonObject()
#obj.server.hostname = "example.com"
#obj.server.port = "8080"

## action testing[x]
obj.action.action = "powershell"
obj.action.arguments = "whoami"
obj.action.execution_context = "current"
obj.action.timeout = "30"
obj.action.std_output = ""
obj.action.std_error = ""

## Callback testing [x]
obj.callback.server.hostname = "safe.com"
obj.callback.server.address = "1.2.3.4"
obj.callback.server.port = "8080"
obj.callback.server.path = "/"

obj.callback.retry_policy.max_retries = "3"
obj.callback.retry_policy.retry_interval = "10"

obj.callback.data_format = "json"

print(obj.server.hostname)
print(obj.callback.data_format)
print(obj.callback.to_dict())

print(obj.action.to_dict())
print(obj.to_dict())