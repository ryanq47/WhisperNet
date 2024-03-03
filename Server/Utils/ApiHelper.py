## A collection of helper functions for the API - Doc when this is more cmplete
from flask import jsonify


def api_response(status_code=None, message=None, **kwargs):
    '''
    Helper function to create a response json_str to send back to the user. 
    
    status_code(int): Status code
    message(str): Message to send along with the response
    data(Any): Data to be sent back 
    
    Note! You can include custom keys with kwargs:
    ex:

    return api_response(
        code=200, 
        message="Login successful", 
        data=None,
        access_token=access_token,  ## Kwarg
        error_code="AUTH_FAILURE"## Kwarg
    )

    '''
    response = {
        'status': status_code,
        'message': message
        ## kwargs will get added here, see next line
    }
    # Update the response with any additional keyword arguments
    response.update(kwargs)
    return jsonify(response), status_code