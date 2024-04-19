import time
import json
import requests

def send_request(data, url="http://127.0.0.1:9999/http/post"):
    """
    Sends a request to the specified URL with JSON data.

    Args:
        data (dict): The data to be sent as a request.
        url (str): The URL to which the request will be sent.
    
    Returns:
        dict: Response from the server.
    """
    headers = {'Content-Type': 'application/json'}  # Set the headers to send JSON data.
    try:
        response = requests.post(url, json=data, headers=headers)
        return response.json()  # Assuming the server responds with JSON.
    except requests.exceptions.RequestException as e:
        # Handle connection errors
        return {"status": "error", "message": str(e)}

# Example JSON data structure for the request.
request_template = {
    "request_id": "unique_request_identifier",
    "timestamp": 1710442988,
    "status": "success",
    "result": {
        "data": "Example result data"
    },
    "error": {
        "code": None,
        "message": None
    }
}

# Continuous loop to send requests.
while True:
    current_time = int(time.time())
    request_template["timestamp"] = current_time  # Update timestamp for each request
    request_template["request_id"] = f"req_{current_time}"  # Generate a unique request ID
    
    # Send the request and receive a response.
    response = send_request(request_template)
    print("Received response:", json.dumps(response, indent=4))
    
    # Sleep for a while before sending the next request.
    time.sleep(0.01)  # Sleep for 5 seconds

    # Add any conditional break if necessary.
    # For example:
    # if some_condition:
    #     break
