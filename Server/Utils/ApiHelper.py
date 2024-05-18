## A collection of helper functions for the API - Doc when this is more cmplete
from flask import jsonify
import time
import uuid

def api_response(status="success", data=None, error_code=None, error_message=None, **kwargs):
    '''
    Helper function to create/construct a response json_str to send back to the user. 
    
    status(str): Status of the response, e.g., "success" or "failure"
    data(dict): Data to be sent back in the response
    error_code(str): Error code, if any
    error_message(str): Error message, if any
    kwargs: Additional keyword arguments to include in the response
    
    Example:

    return api_response(
        status="success", 
        data={"listenerHTTP": [{"listener_id": "listenerHTTP01"}]},
        access_token=access_token,  # Kwarg
        user_id="12345"  # Kwarg
    )
    '''

    # Generate response and request identifiers
    response_id = "random_id" #str(uuid.uuid4()) - Use a ssytem here to get the next available request/response id
    request_id = "random_id" #kwargs.get("request_id", str(uuid.uuid4()))

    # Initialize response structure
    response = {
        "request_id": request_id,  # Unique identifier for this request
        "timestamp": int(time.time()),  # Current timestamp
        "status": status,
        "data": data if data else {},
        "error": {
            "code": error_code,
            "message": error_message
        }
    }

    # OPTIONAL - handy if parsed out of original message. Update to loop over all keys in data.
    # Add response_id to each entry in listenerHTTP if it exists
    #if "listenerHTTP" in response["data"]:
    #    for listener in response["data"]["listenerHTTP"]:
    #        listener["response_id"] = response_id

    # Remove error key if it has no useful content
    if not response["error"]["code"] and not response["error"]["message"]:
        del response["error"]

    # Add any additional keyword arguments, excluding None values
    response.update({k: v for k, v in kwargs.items() if v is not None})

    # Return JSON response with appropriate status code
    return jsonify(response), 200 if status == "success" else 400
