# Sync Handler for data - HTTP Listener edition

'''
{
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
import logging
from Utils.Logger import LoggingSingleton
from PluginEngine.PublicPlugins.ListenerHTTP.Modules.ListenerHttpCommandSync import ListenerHttpCommandSync
# Called once per response
class SyncHandler:

    def __init__(self):
        #wants log level for some reason.
        self.logger = LoggingSingleton.get_logger(log_level=logging.DEBUG)
        self.data = None
        self.handlers = {
            #'listenerHTTP': ListenerHttpSync #self.handle_client_name,
            #clientcommand: parser for client commands
            'ListenerHttpCommandSync': ListenerHttpCommandSync
        }

        ## Move these to a dict? need to weigh pros & cons
        self.request_id = None
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

            self.request_id = self.data["rid"]
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

        # iterate over key,
        for key in result_data:
            if key in self.handlers:
                # call respective handler (ListenerHttpSync for listenerHTTP data, based on handler dict)
                handler_function = self.handlers[key]
                self.logger.debug(f"Processing recieved data with {handler_function.__name__}")

                # init class
                handler_function = handler_function()

                # handle data with respective handler
                self.logger.debug(f"handling recieved data {result_data[key]}")
                handler_function.handle_data(result_data[key])

            else:
                self.logger.warning(f"Key '{key}' not found while parsing response {self.request_id}. Cannot properly handle.")
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