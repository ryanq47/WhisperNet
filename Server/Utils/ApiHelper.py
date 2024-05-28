import uuid
import time
from flask import jsonify
from PluginEngine.PublicPlugins.ListenerHTTP.Utils.DataSingleton import Data

class MessageHelper:
    @staticmethod
    def generate_unique_id():
        """Generate a unique message ID using UUIDv4."""
        return str(uuid.uuid4())

    @staticmethod
    def generate_timestamp():
        """Generate a current timestamp."""
        return int(time.time())

def api_response(status="success", data=None, error_message=None, data_items=None, **kwargs):
    '''
    Helper function to create/construct a response json_str to send back to the user. 

    status(str): Status of the response, e.g., "success" or "failure"
    data(dict): Data to be sent back in the response
    error_code(str): Error code, if any
    error_message(str): Error message, if any
    data_items(list): List of tuples (key, value) to add to the data dict
    kwargs: Additional keyword arguments to include in the response

    Example:

    return api_response(
        status="success", 
        data={"listenerHTTP": [{"listener_id": "listenerHTTP01"}]}, # any sub keys here.
        access_token=access_token,  # Kwarg
        user_id="12345"  # Kwarg
    )
    '''
    data_singleton = Data()

    # Initialize response structure
    response = {
        "rid": MessageHelper.generate_unique_id(),  # Unique identifier for this request
        "timestamp": MessageHelper.generate_timestamp(),  # Current timestamp
        "status": status,
        "data": data if data else {},
        "error": error_message if error_message else {}
    }

    # Add additional data items if provided
    if data_items:
        for key, value in data_items:
            response["data"][key] = value

    # Remove error key if it has no useful content
    if data_singleton.Config.get_value("responses.return_error_message"):
        #print("Error responses are on")
        if not response["error"]:
            del response["error"]
     
    # remove data key if it has no useful content
    # Might cause some problems from the client side
    if not response["data"]:
        del response["data"]

    # Add any additional keyword arguments, excluding None values
    response.update({k: v for k, v in kwargs.items() if v is not None})

    # Return JSON response with appropriate status code
    return jsonify(response), 200

# Example usage
'''
data = {
    "listenerHTTP": [{"listener_id": "listenerHTTP01"}]
}

additional_data_items = [
    ("newKey1", "newValue1"),
    ("newKey2", "newValue2")
]

response = api_response(
    status="success", 
    data=data, 
    data_items=additional_data_items,
    access_token="some_access_token",  # Kwarg
    user_id="12345"  # Kwarg
)

print(response)
'''
