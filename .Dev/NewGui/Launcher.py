import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QTextBrowser

## Netowrk Stuff
from PySide6.QtNetwork import QNetworkAccessManager, QNetworkRequest, QNetworkReply
from PySide6.QtCore import Qt, Slot, Signal, QUrl


class MyApplication(QMainWindow):
    def __init__(self):
        super().__init__()
        loader = QUiLoader()
        ui_file = loader.load('WhisperNetGui.ui')
        self.setCentralWidget(ui_file)

        self.init_objects_from_ui(ui_file = ui_file)
        self.initUI()

    def init_objects_from_ui(self, ui_file):
        '''
        Inits objects from the UI file, and sets them here as class vars
        '''
        
        self.FileHost_PushButton = ui_file.findChild(QPushButton, "FileHost_PushButton")  # Replace "QtWidgets" with the appropriate module
        self.FileHost_TextBox= ui_file.findChild(QTextBrowser, "FileHost_TextBox")  # Replace "QtWidgets" with the appropriate module



    def initUI(self):
        # You can access UI elements like buttons, labels, etc. here
        self.setWindowTitle("WhisperNet")

        ##FileHost
        self.FileHost_PushButton.clicked.connect(self.test)


    def test(self):
        self.manager = WebRequestManager()
        self.manager.request_finished.connect(self.handle_response)
        self.manager.send_get_request("http://127.0.0.1:5000/")

    def handle_response(self, reply):
        if reply.error() == QNetworkReply.NoError:
            response_data = reply.readAll().data().decode()
            self.FileHost_TextBox.setText(response_data)

## Class for handling data ops
class WebRequestManager(QNetworkAccessManager):
    request_finished = Signal(QNetworkReply)

    def send_post_request(self, url, data):
        request = QNetworkRequest(url)
        request.setHeader(QNetworkRequest.ContentTypeHeader, "application/json")
        
        reply = self.post(request, data)
        reply.finished.connect(self.handle_response)

    def send_get_request(self, url):
        request = QNetworkRequest(url)
        request.setHeader(QNetworkRequest.ContentTypeHeader, "application/json")
        
        reply = self.get(request)
        reply.finished.connect(self.handle_response)

    def handle_response(self):
        reply = self.sender()
        self.request_finished.emit(reply)




if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyApplication()
    window.show()
    sys.exit(app.exec())
