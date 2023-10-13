## not using requestst, this ensures better compatability/less pip installs
import urllib.request
from Utils.LoggingBaseClass import BaseLogging
import inspect
import time
import json
import requests
from Utils.ControlServerHandler import ControlServerHandler
#from dotenv import load_dotenv
import os
import time

class ExternalBasePlugin(BaseLogging):
    def __init__(self):
        
        self.control_server_url = None
        self.control_server_command_endpoint = None
        self.heartbeat_time = 60
        self.JWT = None
        self.api_password = None
        self.api_username = None

        ## stats stuff
        self.name = "fh01"
        self.plugin_type = "filehost_external"
        self.external_ip = None


    def heartbeat_daemon(self):
        while True:
            print("Heartbeat")

            ## spin up class with data to sync files
            sync = ControlServerHandler(
                jwt = self.JWT,
                server_url = "",
                server_port = ""
            )

            sync.sync_files()
            self.checkin_to_server(message="Heartbeat")
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
    

    def load_creds(self):
        '''
        Loads Credentials from .env file
        
        '''
        self.api_username = "api_admin"
        self.api_password = "1234"

    
        #load_dotenv()

        #self.api_username = os.getenv("CONTROLSERVER_API_USERNAME")
        #self.api_password = os.getenv("CONTROLSERVER_API_PASSWORD")



    def login_to_server(self):
        '''
            Logs into server. Sets self.JWT on success
        '''
        try: 

            auth_data = {
                "username":self.api_username,
                "password":self.api_password
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


    def checkin_to_server(self, message=None):
        '''
        Sends checkin to server

        {
            "name":"fh01",
            "plugin_type":"filehost_external"
            "ip":"123.0.0.0",
            "message":"syncing | sync successful | sync failed | error"
            "timestamp":""
        }

        '''

        dict_data = {
            "name":self.name,
            "plugin_type":self.plugin_type,
            "ip":self.external_ip,
            "message":message,
            "timestamp":time.asctime()
        }

        json_data = json.dumps(dict_data)

        headers = {
                "Content-Type": "application/json"
        }

        r = requests.post(
            url = "http://127.0.0.1:5000/api/filehost/checkin",
            headers = headers,
            data = json_data
        )

    def get_external_ip(self):
        '''
        Gets external ip
        '''

        return "123.0.0.1"

