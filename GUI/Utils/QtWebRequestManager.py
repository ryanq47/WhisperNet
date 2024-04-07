from PySide6.QtNetwork import QNetworkAccessManager, QNetworkRequest, QNetworkReply
from PySide6.QtCore import Signal, QByteArray, QUrl
import json
from Utils.Logger import LoggingSingleton

class WebRequestManager(QNetworkAccessManager):
    request_finished = Signal(dict)  # Emitting a Python dictionary directly

    def __init__(self):
        super().__init__()
        self.logger = LoggingSingleton.get_logger()
        self.finished.connect(self._handle_finished)  # Connect to the built-in finished signal
        self.logger.debug("WebRequestManager initialized")

    def send_request(self, url: str, data=None, method="GET"):
        """
        Sends a HTTP request to the specified URL with optional data and JWT authentication.
        Supports both GET and POST methods.

        Note, you DO NOT have to encode dict's/lists, this method will do it for you. Of course, you can still pass encoded versions in, but it's not required.
        """
        request = QNetworkRequest(QUrl(url))
        request.setHeader(QNetworkRequest.ContentTypeHeader, "application/json")

        # Include JWT token if available
        jwt_token = "FAKETOKEN"
        if jwt_token:
            request.setRawHeader(b"Authorization", f"Bearer {jwt_token}".encode('utf-8'))

        if method.upper() == "POST" and data is not None:
            # Ensure data is a QByteArray
            if isinstance(data, str):
                # Data is a string, likely JSON, convert it to QByteArray
                self.logger.debug("Passed info was not a QByteArray, converting/Encoding...")
                data = QByteArray(data.encode('utf-8'))
            elif isinstance(data, (dict, list)):
                self.logger.debug("Passed info was not a dict/list, dumping & encoding")
                # Data is a dictionary or list, convert to JSON string then to QByteArray
                data = QByteArray(json.dumps(data).encode('utf-8'))

            self.post(request, data)
        elif method.upper() == "GET":
            self.get(request)

    def _handle_finished(self, reply: QNetworkReply):
        """
        Internal slot to handle the finished signal from a request.
        """
        error = reply.error()
        if error == QNetworkReply.NoError:
            response_data = reply.readAll().data().decode()
            self.logger.debug("Request finished successfully")
            try:
                data = json.loads(response_data)
            except json.JSONDecodeError:
                data = {"error": "Failed to decode JSON"}
                self.logger.error("Failed to decode JSON from response")
        else:
            data = {"error": error, "message": reply.errorString()}
            self.logger.error(f"Request finished with error: {reply.errorString()}")

        self.request_finished.emit(data)
        reply.deleteLater()  # Ensure the reply is properly cleaned up

        """
        # Usage
        def get_all_data(self):
            self.request_manager = WebRequestManager()
            self.request_manager.request_finished.connect(self.handle_response) # or whatever func you want to send data to
            self.request_manager.send_request("http://127.0.0.1:5000/api/simplec2/general/everything")

        """ 