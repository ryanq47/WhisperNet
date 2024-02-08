from PySide6.QtNetwork import QNetworkAccessManager, QNetworkRequest, QNetworkReply
from PySide6.QtCore import Signal

class WebRequestManager(QNetworkAccessManager):
    request_finished = Signal(QNetworkReply)

    def send_post_request(self, url, data):
        #logging.debug(f"{function_debug_symbol} {inspect.stack()[0][3]}")
        try:
            ## Just incase data is not in byte form
            if not isinstance(data, bytes):
                data = self.encode_str_to_bytes(data)

            request = QNetworkRequest(url)
            request.setHeader(QNetworkRequest.ContentTypeHeader, "application/json")
            #application/octet-stream
            #request.setHeader(QNetworkRequest.ContentTypeHeader, "application/octet-stream")

            reply = self.post(request, data)
            reply.finished.connect(self.handle_response)
        except Exception as e:
            print(e)
            #logging.warning(f"{function_debug_symbol} Error sending post request: {e}")

    def send_get_request(self, url):
        #logging.debug(f"{function_debug_symbol} {inspect.stack()[0][3]}")

        request = QNetworkRequest(url)
        request.setHeader(QNetworkRequest.ContentTypeHeader, "application/json")
        
        reply = self.get(request)
        reply.finished.connect(self.handle_response)

    def handle_response(self):
        #logging.debug(f"{function_debug_symbol} {inspect.stack()[0][3]}")

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