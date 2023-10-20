import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QTextBrowser, QTableWidgetItem

## Netowrk Stuff
from PySide6.QtNetwork import QNetworkAccessManager, QNetworkRequest, QNetworkReply
from PySide6.QtCore import Qt, Slot, Signal, QUrl


class MyApplication(QMainWindow):
    response_received = Signal(str)  # Custom signal to pass response data



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
        try:
            self.FileHost_PushButton = ui_file.findChild(QPushButton, "FileHost_PushButton")  # Replace "QtWidgets" with the appropriate module
            self.FileHost_TextBox= ui_file.findChild(QTextBrowser, "FileHost_TextBox")  # Replace "QtWidgets" with the appropriate module
            self.FIleHost_FileLogTable = ui_file.findChild(QTableWidgetItem, "FileHost_FileLogTable")  
        except Exception as e:
            print(e)

    def initUI(self):
        # You can access UI elements like buttons, labels, etc. here
        self.setWindowTitle("WhisperNet")

        ##FileHost
        self.FileHost_PushButton.clicked.connect(self.filehost_event_update)


    def filehost_debug(self):
        self.manager = WebRequestManager()
        self.manager.request_finished.connect(self.handle_response)
        self.manager.send_get_request("http://127.0.0.1:5000/")


    def filehost_event_update(self):
        '''
        Test for updating stuff all at once 
        '''
        print("called")

        ## Request stuff <filedata>
        self.manager = WebRequestManager()
        self.manager.request_finished.connect(self.handle_response)
        self.manager.send_get_request("http://127.0.0.1:5000/")
        ## On response/emit of handle_response, update table
        self.response_received.connect(self.filehost_api_files_update_table)


    def filehost_api_files_update_table(self, data):
        '''
        Parses, and updates the table of files in FileHost
        
        '''
        data = [
            ("Alice", 30, "USA"),
            ("Bob", 25, "Canada"),
            ("Charlie", 35, "UK"),
        ]

        self.FileHost_FileLogTable.setRowCount(len(data))  # Set the number of rows

        for row, (name, age, country) in enumerate(data):
            self.tableWidget.setItem(row, 0, QTableWidgetItem(name))
            self.tableWidget.setItem(row, 1, QTableWidgetItem(str(age)))
            self.tableWidget.setItem(row, 2, QTableWidgetItem(country))


        self.FileHost_TextBox.setText(data)


    def handle_response(self, reply):
        '''
        Handles a web request response. 

        Emits a SIGNAL, named 'response_received'. This signal 
        contains the web request response. 
        
        This will trigger signals in the respective functions that called it.
        

        Potential issues, if this gets called multiple times, by multiple different functinos, the slots could
        get a litte weird & messed up. To fix, maybe create a dedicated handle_response function for each page
        '''
        if reply.error() == QNetworkReply.NoError:
            response_data = reply.readAll().data().decode()
            #self.FileHost_TextBox.setText(response_data)
            self.response_received.emit(response_data)  # Emit the custom signal

        else:
            string = f"Error with request: {reply.error()}"
            self.response_received.emit(string)  # Emit the custom signal

            #self.FileHost_TextBox.setText(f"Error with request: {reply.error()}")

## Class for handling data ops - move to a util file eventually
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
