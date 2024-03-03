## not using requestst, this ensures better compatability/less pip installs
import urllib.request
from Utils.LoggingBaseClass import BaseLogging
import inspect

## delete this, only exists so the plugin loader doesn't yell about not having the attribute "info"
class Info:
    name    = "empty"
    author  = "empty"
    endpoint = "/empty"
    classname = "empty"
    plugin_type = "empty"

class ExternalBasePlugin(BaseLogging):
    def __init__(self):
        
        self.control_server_url = None
        self.control_server_command_endpoint = None



    def get_command(self):
        '''
        Reach out to control server & get command for this plugin
        '''
        try:
            response = urllib.request.urlopen(f"{self.control_server_url}{self.control_server_command_endpoint}")
            encoded_data = response.read()
            data = encoded_data.decode('utf-8')
            return data
        
        except Exception as e:
            self.logger.warning(f"{self.function_debug_symbol} {inspect.stack()[0][3]}")
            return None
    
