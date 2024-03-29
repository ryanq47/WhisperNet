## not using requestst, this ensures better compatability/less pip installs
import urllib.request
from Utils.LoggingBaseClass import BaseLogging
import inspect
import time
import json
import requests
from Utils.ControlServerHandler import ControlServerHandlerFileSync
from dotenv import load_dotenv
import os
import time
from datetime import datetime
from Utils.YamlLoader import PluginConfig


## Deals with pure server interactions
class ServerConnector:
    def __init__(self, config_object):
        '''
        config_object: The config object for interacting with the config file. 
        
        Upon init of this class, it will set configuration items, load credentials form the .env file, and then log into the server
        '''
        self.config = config_object
        self.logger = BaseLogging(name="ServerConnectorLogger", level=self.config.get_value("plugin.logging.level"), print_to_screen=True)
        self.control_server_url = None
        self.control_server_command_endpoint = None
        self.heartbeat_time = 5
        self.JWT = None
        self.api_password = None
        self.api_username = None

        ## stats stuff
        self.external_ip = None

        self.set_config_items()
        self.load_creds()
        self.login_to_server()

    def set_config_items(self):
        self.plugin_name = self.config.get_value("plugin.name")
        self.plugin_type = self.config.get_value("plugin.type")

    def heartbeat_daemon(self):
        while True:
            #print("Heartbeat")

            ## spin up class with data to sync files
            ## Easy feature to flip on if needed for doubling a lsitener as a fiel host
            '''sync = ControlServerHandlerFileSync(
                jwt = self.JWT,
                server_url = "",
                server_port = ""
            )

            sync.sync_files()'''
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
            self.logger.warning(f"{self.logger.function_debug_symbol} {inspect.stack()[0][3]}")
            return None

    def load_creds(self):
        '''
        Loads Credentials from .env file
        
        '''

        load_dotenv()

        self.api_username = os.getenv("CONTROLSERVER_API_USERNAME")
        self.api_password = os.getenv("CONTROLSERVER_API_PASSWORD")

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
                self.logger.info(f"{self.logger.logging_info_symbol} Authentication to ControlServer successful")
            
            except Exception as e:
                self.logger.warning(f"{self.logger.logging_warning_symbol} Error logging into ControlServer: {e}")
        

        except Exception as e:
            self.logger.warning(f"{self.logger.function_debug_symbol} {inspect.stack()[0][3]}")

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
            "name":self.plugin_name,
            "plugin_type":self.plugin_type,
            "ip":self.external_ip,
            "message":message,
            "timestamp":self.get_timestamp()
        }

        json_data = json.dumps(dict_data)

        headers = {
                "Content-Type": "application/json"
        }

        try:
            r = requests.post(
                url = "http://127.0.0.1:5000/api/filehost/checkin",
                headers = headers,
                data = json_data
            )
        except Exception as e:
            self.logger.warning(f"{self.logger.logging_warning_symbol} Could not contact server at __ : {e}")

    def post_file_logs(self, filename = None, accessorip = None, http_status_code = None):
        '''
        Sends file log data to server. 
        
        dict_data = {
            "filename":"notsafefile.exe",
            "accessorip":"y.y.y.y",
            "hostip":"x.x.x.x",
            "hostingserver":"fh01",
            "timestamp":"010101"

        }

        '''

        dict_data = {
            "filename":filename,
            "accessorip":accessorip,
            "hostip":self.external_ip,
            "hostingserver":"controlserver",#self.control_server_name,
            "timestamp":self.get_timestamp(),
            "httpstatuscode":http_status_code
        }

        json_data = json.dumps(dict_data)

        headers = {
                "Content-Type": "application/json"
        }

        r = requests.post(
            url = "http://127.0.0.1:5000/api/filehost/updatefilelogs",
            headers = headers,
            data = json_data
        )

    def get_external_ip(self):
        '''
        Gets external ip
        '''

        return "123.0.0.1"

    def post_clientdata_entries(self, client_data):
        '''
        Designed to post client data entries to the server

        
        '''

        try:
            dict_data = {
                "id":"id",
                "timestamp":"timestamp",
                "data":"data"
            }

            json_data = json.dumps(dict_data)

            headers = {
                    "Content-Type": "application/json"
            }

            r = requests.post(
                url = "http://127.0.0.1:5000/api/simplec2/clientdata",
                headers = headers,
                data = json_data
            )
        except Exception as e:
            self.logger.warning(f"{self.logger.logging_warning_symbol} Error with posting client data to server: {e}")


    def get_timestamp(self):
        try:
            return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        except Exception as e:
            self.logger.warning(f"{self.logger.logging_warning_symbol} Error getting timestamp: {e}")
            return "Error getting timestamp"

