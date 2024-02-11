from PySide6.QtNetwork import QNetworkAccessManager, QNetworkRequest, QNetworkReply
from PySide6.QtCore import Signal
import inspect

from Utils.BaseLogging import BaseLogging

class WebRequestManager(QNetworkAccessManager):
    request_finished = Signal(QNetworkReply)

    def __init__(self):
        super().__init__()
        self.logger = BaseLogging.get_logger()


    def send_post_request(self, url, data):
        try:
            self.logger.debug(f"{self.__class__.__name__}.{inspect.currentframe().f_code.co_name}: Making Post request to '{url}'")

            ## Just incase data is not in byte form
            if not isinstance(data, bytes):
                self.logger.debug(f"{self.__class__.__name__}.{inspect.currentframe().f_code.co_name}: 'data' variable is not in byte form, converting from: '{type(data)}' to bytes")
                data = self.encode_str_to_bytes(data)

            request = QNetworkRequest(url)
            request.setHeader(QNetworkRequest.ContentTypeHeader, "application/json")
            #application/octet-stream
            #request.setHeader(QNetworkRequest.ContentTypeHeader, "application/octet-stream")

            reply = self.post(request, data)
            reply.finished.connect(self.handle_response)
            self.logger.debug(f"{self.__class__.__name__}.{inspect.currentframe().f_code.co_name}: Successful Post request to '{url}'")

        except Exception as e:
            self.logger.error(f"{self.__class__.__name__}.{inspect.currentframe().f_code.co_name}: {e}")

    def send_get_request(self, url):
        try:
            self.logger.debug(f"{self.__class__.__name__}.{inspect.currentframe().f_code.co_name}: Making Get request to '{url}'")

            request = QNetworkRequest(url)
            request.setHeader(QNetworkRequest.ContentTypeHeader, "application/json")
            
            reply = self.get(request)
            reply.finished.connect(self.handle_response)
            self.logger.debug(f"{self.__class__.__name__}.{inspect.currentframe().f_code.co_name}: Successful Get request to '{url}'")

        except Exception as e:
            self.logger.error(f"{self.__class__.__name__}.{inspect.currentframe().f_code.co_name}: {e}")


    def handle_response(self):

        reply = self.sender()
        self.request_finished.emit(reply)

    def encode_str_to_bytes(self, data):
        '''
        Turn a str into bytes
        '''
        return data.encode()

    def decode_bytes_to_str(self, data):
        '''
        Turn a str into bytes
        '''
        return data.decode()