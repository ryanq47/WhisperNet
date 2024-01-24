import json

class MyJsonObject:
    def __init__(self):
        self.data = {
            "auth": {},
            "action": {},
            "callback": {}
        }

    def add_auth(self, user=None, password=None, hash=None, kerb=None, other=None):
        if user:
            self.data['auth']['user'] = user
        if password:
            self.data['auth']['password'] = password
        if hash:
            self.data['auth']['hash'] = hash
        if kerb:
            self.data['auth']['kerb'] = kerb
        if other:
            self.data['auth']['other'] = other

    def set_action(self, action, arguments=None, execution_context=None, timeout=None, std_output=None, std_error=None):
        self.data['action']['action'] = action
        if arguments:
            self.data['action']['arguments'] = arguments
        if execution_context:
            self.data['action']['execution_context'] = execution_context
        if timeout:
            self.data['action']['timeout'] = timeout
        if std_output:
            self.data['action']['std_output'] = std_output
        if std_error:
            self.data['action']['std_error'] = std_error


    def add_callback(self, hostname=None, address=None, port=None, path=None, 
                     max_retries=None, retry_interval=None, data_format=None):
        """
        Adds or updates the callback configuration in the JSON data structure.

        Parameters:
        hostname (str, optional): The hostname for the server. Default is None.
        address (str, optional): The IP address or domain name for the server. Default is None.
        port (str, optional): The port number on which the server is running. Default is None.
        path (str, optional): The path for the server's endpoint. Default is None.
        max_retries (str, optional): The maximum number of retries for the callback. Default is None.
        retry_interval (str, optional): The interval between retries in seconds. Default is None.
        data_format (str, optional): The data format for the callback (e.g., 'json'). Default is None.

        Returns:
        None: This method updates the internal data structure and does not return a value.

        Example:
        # Example usage of add_callback
        obj.add_callback(hostname='example.com', port='8080', max_retries='5', retry_interval='15', data_format='json')

        Note:
        [Your additional notes here]

        """
        if any([hostname, address, port, path]):
            self.data['callback']['server'] = {}
            if hostname is not None:
                self.data['callback']['server']['hostname'] = hostname
            if address is not None:
                self.data['callback']['server']['address'] = address
            if port is not None:
                self.data['callback']['server']['port'] = port
            if path is not None:
                self.data['callback']['server']['path'] = path

        if any([max_retries, retry_interval]):
            self.data['callback']['retry_policy'] = {}
            if max_retries is not None:
                self.data['callback']['retry_policy']['max_retries'] = max_retries
            if retry_interval is not None:
                self.data['callback']['retry_policy']['retry_interval'] = retry_interval

        if data_format is not None:
            self.data['callback']['data_format'] = data_format

    def add_source_ip(self, src_ip):
        if 'server' not in self.data['callback']:
            self.data['callback']['server'] = {}
        self.data['callback']['server']['source_ip'] = src_ip

    def to_json(self):
        return json.dumps(self.data)

    def print_json(self):
        return json.dumps(self.data, indent=4)


# Example Usage
obj = MyJsonObject()
obj.set_action('powershell', arguments='whoami /all')
#obj.add_source_ip('192.168.1.1')

obj.add_callback(
    address="192.168.0.1",
    port="8080",
    path="/",
    max_retries="123"
)

print(obj.print_json())
