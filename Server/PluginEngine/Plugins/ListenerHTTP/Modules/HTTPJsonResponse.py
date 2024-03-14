import json

class C2Response:
    def __init__(self, response_id=None, request_id=None, timestamp=None, status=None, result=None, error=None):
        self.response_id = response_id
        self.request_id = request_id
        self.timestamp = timestamp
        self.status = status
        self.result = result if result is not None else {}
        self.error = error if error is not None else {"code": None, "message": None}

    def decode(self, json_data):
        """
        Decode a JSON string to populate the C2Response object.
        """
        try:
            data = json.loads(json_data)
            self.response_id = data.get('response_id')
            self.request_id = data.get('request_id')
            self.timestamp = data.get('timestamp')
            self.status = data.get('status')
            self.result = data.get('result', {})
            self.error = data.get('error', {"code": None, "message": None})
        except json.JSONDecodeError as e:
            print(f"JSON decode error: {e}")
        except Exception as e:
            print(f"General error in decoding JSON: {e}")

    def to_json(self):
        """
        Convert the C2Response object back into a JSON string.
        """
        return json.dumps({
            "response_id": self.response_id,
            "request_id": self.request_id,
            "timestamp": self.timestamp,
            "status": self.status,
            "result": self.result,
            "error": self.error
        }, default=str)  # Using default=str to handle any non-serializable objects gracefully

    @staticmethod
    def from_json(json_data):
        """
        Static method to create a C2Response object directly from a JSON string.
        """
        response = C2Response()
        response.decode(json_data)
        return response


"""
## For testing
json_str = '''{
  "response_id": "matching_request_identifier",
  "request_id": "unique_request_identifier",
  "timestamp": "2024-03-14T12:35:56Z",
  "status": "success",
  "result": {
    "data": "Example result data"
  },
  "error": {
    "code": null,
    "message": null
  }
}'''

# Decode the JSON string into a C2Response object
response = C2Response.from_json(json_str)

print(f"Response ID: {response.response_id}")
print(f"Request ID: {response.request_id}")
print(f"Timestamp: {response.timestamp}")
print(f"Status: {response.status}")
print(f"Result: {response.result}")
print(f"Error Code: {response.error['code']}")
print(f"Error Message: {response.error['message']}")

# Convert a C2Response object back into JSON (if needed)
json_output = response.to_json()
print(json_output)
"""