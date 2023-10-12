## not using requestst, this ensures better compatability/less pip installs
import urllib.request
from Utils.LoggingBaseClass import BaseLogging
import inspect
import time
import json
import requests

class ExternalBasePlugin(BaseLogging):
    def __init__(self):
        
        self.control_server_url = None
        self.control_server_command_endpoint = None
        self.heartbeat_time = 60
        self.JWT = None

    def heartbeat_daemon(self):
        while True:
            print("Heartbeat")
            self.sync_files()
            time.sleep(self.heartbeat_time)

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
    
    def login_to_server(self, username, password):
        '''
            Logs into server. Sets self.JWT on success
        '''
        try: 

            auth_data = {
                "username":username,
                "password":password
            }

            headers = {
                "Content-Type": "application/json"
            }

            json_auth_data = json.dumps(auth_data)

            r = requests.post(
                url = "http://127.0.0.1:5000/api/login",
                data=json_auth_data,
                headers=headers
            )

            try: 
                json_data = json.loads(r.text)

                jwt = json_data["access_token"]

                self.JWT = jwt
                self.logger.info(f"{self.logging_info_symbol} Authentication to ControlServer successful")
            
            except Exception as e:
                self.logger.warning(f"{self.logging_warning_symbol} Error logging into ControlServer: {e}")
        

        except Exception as e:
            self.logger.warning(f"{self.function_debug_symbol} {inspect.stack()[0][3]}")



