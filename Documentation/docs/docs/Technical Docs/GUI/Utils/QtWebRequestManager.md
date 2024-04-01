NOT REVIEWED

# WebRequestManager Documentation

## Overview

`WebRequestManager` is an enhanced network request manager tailored for PyQt or PySide applications. It extends `QNetworkAccessManager` to provide easy-to-use HTTP request capabilities with built-in JWT authentication support. This class simplifies the process of sending GET and POST requests, handling the response asynchronously, and emitting a Python dictionary with the response data through a custom signal.

## Imports and Dependencies

- **PySide6.QtNetwork**: Utilized for network communication capabilities (`QNetworkAccessManager`, `QNetworkRequest`, `QNetworkReply`, `QUrl`).
- **PySide6.QtCore**: Employed for signal-slot mechanism (`Signal`, `QByteArray`).
- **json**: Required for encoding and decoding JSON data.
- **Utils.Logger**: A custom logging utility (`LoggingSingleton`) for logging messages and errors.

## AuthManager Class

Before diving into the `WebRequestManager`, it's important to note the `AuthManager` class, a placeholder for an authentication management system, which is crucial for managing JWT tokens used in HTTP requests.

### Methods

- `get_jwt_token()`: Returns a JWT token as a string - PURELY stand in for the JWT in the data singleton. DELETE ME

## WebRequestManager Class

`WebRequestManager` handles the complexities of network requests, including setting headers, managing tokens, and parsing the response.

### Signals

- `request_finished`: Emitted when a network request is completed. The signal sends a dictionary containing the response data.

### Constructor

```python
def __init__(self):
    super().__init__()
    self.logger = LoggingSingleton.get_logger()
    self.finished.connect(self._handle_finished)
```
Initializes a new instance of WebRequestManager, setting up logging and connecting the internal finished signal to the _handle_finished slot.

## Public Methods
### send_request

```
def send_request(self, url: str, data=None, method="GET"):
    """
    Sends an HTTP request to the specified URL with optional data and JWT authentication.
    Supports both GET and POST methods.

    :param url: The URL to send the request to.
    :param data: Optional data to send with the request (for POST).
    :param method: The HTTP method to use ('GET' or 'POST').
    """
```
This method prepares and sends an HTTP request. For POST requests, data should be a dictionary or a list, which is then converted into a JSON string.

## Private Methods

### _handle_finished
```
def _handle_finished(self, reply: QNetworkReply):
    """
    Internal method to handle the 'finished' signal from a request.
    Parses the JSON response and emits the custom `request_finished` signal.
    """
```

This slot is called when a request is finished, processing the reply, extracting data, and emitting the request_finished signal with the response.

## Usage Examples

To use WebRequestManager, you first instantiate it, connect the request_finished signal to a custom slot, and then call send_request with the desired URL and parameters.

```
Copy code
def get_all_data(self):
    self.request_manager = WebRequestManager()
    self.request_manager.request_finished.connect(self.some_method_to_take_the_data)
    self.request_manager.send_request("http://example.com/api/data")

```

In this example, handle_response would be a method defined in your class that takes a dictionary as its only parameter, handling the response data.

Remarks
WebRequestManager abstracts away much of the boilerplate code associated with making HTTP requests and handling responses in a PyQt or PySide application, allowing developers to focus on the core functionality of their applications.