# Sync Handler for data

'''
{
  "response_id": "matching_request_identifier",
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

import json

from Utils.Logger import LoggingSingleton

# - Questions: Where does this data go? Sinlgeton somewhere?

# Called once per response
class SyncHandler:

    def __init__(self):
        self.logger = LoggingSingleton.get_logger()
        self.data = None
        self.handlers = {
            'client_name': lambda x: print("client_name"),#self.handle_client_name,
            'data': lambda x: print("data")#self.handle_data
        }

        ## Move these to a dict? need to weigh pros & cons
        self.request_id = None
        self.response_id = None
        self.timestamp = None
        self.status = None

    def parse_response(self, response):
        """
        Parses the JSON response from a server or a service and dispatches data to appropriate handlers.

        Parameters:
            response (str): JSON string representing the server response.
        """
        try:
            data = json.loads(response)
            if data['status'] == 'success':
                # Can make this better w setter/getter prolly
                self.data = data
                self._parse_details()
                self._parse_result()
                # parse whatever else part
            else:
                self.handle_error(data['error'])

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

            self.response_id = self.data["response_id"]
            self.request_id = self.data["request_id"]
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
        result_data = self.data["result"]

        # iterate over key,
        for key in result_data:
            if key in self.handlers:
                # call respective handler
                handler_function = self.handlers[key]
                handler_function(result_data[key])
                self.logger.debug(handler_function)

            else:
                self.logger.warning(f"Key '{key}' not found while parsing response {self.response_id}")


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