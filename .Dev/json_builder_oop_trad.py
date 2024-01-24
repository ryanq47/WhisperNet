class Server:
    def __init__(self, hostname=None, address=None, port=None, path=None):
        self.hostname = hostname
        self.address = address
        self.port = port
        self.path = path

class RetryPolicy:
    def __init__(self, max_retries=None, retry_interval=None):
        self.max_retries = max_retries
        self.retry_interval = retry_interval

class Callback:
    def __init__(self, server=None, retry_policy=None, data_format=None):
        self.server = server if server else Server()
        self.retry_policy = retry_policy if retry_policy else RetryPolicy()
        self.data_format = data_format

class MyJsonObject:
    def __init__(self):
        self.server = Server()
        self.callback = Callback()

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

# Example usage
obj = MyJsonObject()
obj.update_server(hostname="example.com", port="8080")
obj.update_callback(max_retries="3", retry_interval="10", data_format="json")
print(obj.callback.data_format)
