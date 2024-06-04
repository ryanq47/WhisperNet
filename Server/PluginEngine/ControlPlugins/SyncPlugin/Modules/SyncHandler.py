# Sync Handler for data

'''
{
  "rid": "matching_request_identifier",
  "request_id": "unique_request_identifier",
  "timestamp": 1710442988,
  "status": "success",
  "result": {
    "client_name":"client_name"
    "data": "Example result data "
  },
  "error": {
    "code": null,
    "message": null
  }
}
'''

'''
Quick how it works notes


Req -> /api/sync (SyncPlugin)
    > Sync Handler - Figures out where to send next
        > Individial JSON key data handler 
        - Dumps/alters/handles data into resepective data singleton class/object (*could* db this but like ew)
        - *then*, full circle, plugins pull from data singleton to send out those objects. 
        - So this is just a fancy storage system basically, all in JSON/Dicts
    
'''

import json

from Utils.Logger import LoggingSingleton
from PluginEngine.ControlPlugins.SyncPlugin.Modules.ListenerHttpCommandSync import ListenerHttpCommandSync
from PluginEngine.ControlPlugins.SyncPlugin.Modules.ListenerHttpClientSync import ListenerHttpClientSync
from PluginEngine.ControlPlugins.SyncPlugin.Modules.ListenerInfo import ListenerInfo

# - Questions: Where does this data go? Sinlgeton somewhere?

# Called once per response
class SyncHandler:

    def __init__(self):
        self.logger = LoggingSingleton.get_logger()
        self.data = None
        self.handlers = {
            #'listenerHTTP': ListenerHttpSync #self.handle_client_name,
            'ListenerHttpCommandSync': ListenerHttpCommandSync,
            'ListenerHttpClientSync': ListenerHttpClientSync,
            'ListenerInfo': ListenerInfo
        }

        ## Move these to a dict? need to weigh pros & cons
        self.rid = None
        self.timestamp = None
        self.status = None

    def parse_response(self, response):
        """
        Parses the JSON response from a server or a service and dispatches data to appropriate handlers.

        Parameters:
            response (str): JSON string representing the server response.
        """
        try:
            if response['status'] == 'success':
                # Can make this better w setter/getter prolly
                self.data = response
                self._parse_details()
                self._parse_result()
                # parse whatever else part
            else:
                self.handle_error(response['error'])

        except json.JSONDecodeError:
            self.logger.error("Failed to decode JSON response")
        except KeyError as e:
            self.logger.warning(f"Missing expected key: {e}")


        ## Parse the json in response var

        ## Pass respective parsed data into correct methods

    def _parse_details(self):
        """
            Parses the top level keys of the response, aka all the important details
        """
        if self.data != None:

            self.rid = self.data["rid"]
            self.timestamp = self.data["timestamp"]
            self.status = self.data["status"]

        else:
            self.logger.warning("No data in self.data! Cannot parse response")


    def _parse_result(self):
        """
            Results, dynamically pulls & parses json in the results key
            
            Ex:
                "result": {
                    "client_name":"client_name"
                    "data": "Example result data "
                }

        """
        result_data = self.data["data"]
        #self.logger.debug(f"Result Data: {result_data}")

        ######################################
        """
            Big Issue/Vuln: (mitigated)

                Listener request will have ALL the keys processed even when not verified, because there is no check to make
                sure the listener is verified first. FUCK. ideas:

                options:
                 - [X] If ListenerInfo present, check that listener is good to go before. 
                 - Put a "lock" on the listener object to prevent it from doing anything. 

                Both might be a good option

        """
        ######################################
        # key check

        # Check if ListenerInfo exists and process it first
        # Can be used for other items that need this processing first, such as GUI > server.
        if "ListenerInfo" in result_data:
            self.logger.debug("ListenerInfo present in reqeust. Making sure listener is okay before doing other actions.")
            listener_info = result_data["ListenerInfo"]
            
            handler_function = self.handlers['ListenerInfo']
            # init function
            handler_function = handler_function()
            if handler_function.store_response(listener_info):
                self.logger.debug(f"Listener {listener_info['lid']} found and verified. Continuing actions")

            else:
                self.logger.warning(f"Listener {listener_info['lid']} NOT verified. Not processing any data recieved by Listener.")


        # iterate over key,
        for key in result_data:
            if key in self.handlers:
                # call respective handler (ListenerHttpSync for listenerHTTP data, based on handler dict)
                handler_function = self.handlers[key]
                self.logger.debug(f"Processing recieved data with {handler_function.__name__}")

                # init class
                handler_function = handler_function()

                #self.logger.debug(handler_function)
                #self.logger.debug(f"Sending {result_data[key]} to sync func")
                #handler_function(result_data[key])
                self.logger.debug(f"Storing recieved data {result_data[key]}")
                handler_function.store_response(result_data[key])

            else:
                self.logger.warning(f"Key '{key}' not found while parsing response {self.rid}. Cannot properly handle.")
                self.logger.debug("This means that there is no class defined to handle this type of data.")

        # for each recognized key, call the proper function/subsystem to handle that data
            ## Note: Suggest better options if you can think of some

    def handle_error(self, error):
        """
        Handles errors reported in the response.

        Parameters:
            error (dict): Dictionary containing the 'error' part of the response.
        """
        error_code = error.get('code')
        error_message = error.get('message')

        if error_code or error_message:
            self.logger.error(f"Error {error_code}: {error_message}")
        else:
            self.logger.error("Unknown error occurred")