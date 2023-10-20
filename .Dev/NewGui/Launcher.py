import json
from symbol import arglist
import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QTextBrowser, QTableWidgetItem, QTableWidget

## Netowrk Stuff
from PySide6.QtNetwork import QNetworkAccessManager, QNetworkRequest, QNetworkReply
from PySide6.QtCore import Qt, Slot, Signal, QUrl, QTimer

import inspect
import logging

logging.basicConfig(level=logging.DEBUG)
## Change the path to the system path + a log folder/file somewhere
logging.basicConfig(filename='WhisperNetGui.log', filemode='a', format='%(asctime)s - %(levelname)s - %(message)s', force=True, datefmt='%Y-%m-%d %H:%M:%S')
#logging.getLogger().addHandler(logging.StreamHandler())
function_debug_symbol = "[*]"

class MyApplication(QMainWindow):
    ## these auto get put in "self.xxxx"... i assume throuth the QMainWindow inheretence somewhere
    filehost_response_received = Signal(str)
    nodelogs_response_received = Signal(str)

    def __init__(self):
        super().__init__()
        loader = QUiLoader()
        ui_file = loader.load('WhisperNetGui.ui')
        self.setCentralWidget(ui_file)

        self.init_objects_from_ui(ui_file = ui_file)
        self.initUI()
        ## starts events & timers
        self.filehost_timer = QTimer()
        self.events_and_timers()


    def init_objects_from_ui(self, ui_file):
        '''
        Inits objects from the UI file, and sets them here as class vars
        '''
        try:
            self.FileHost_PushButton = ui_file.findChild(QPushButton, "FileHost_PushButton")  # Replace "QtWidgets" with the appropriate module
            self.FileHost_TextBox= ui_file.findChild(QTextBrowser, "FileHost_TextBox")  # Replace "QtWidgets" with the appropriate module
            self.FileHost_FileLogTable = ui_file.findChild(QTableWidget, "FileHost_FileLogTable")  
            self.FileHost_NodeLogTable = ui_file.findChild(QTableWidget, "FileHost_NodeLogTable")
        except Exception as e:
            print(e)

    def initUI(self):
        # You can access UI elements like buttons, labels, etc. here
        logging.debug(f"{function_debug_symbol} {inspect.stack()[0][3]}")

        self.setWindowTitle("WhisperNet")

        ##FileHost
        self.FileHost_PushButton.clicked.connect(self.filehost_event_update)

    def filehost_debug(self):
        logging.debug(f"{function_debug_symbol} {inspect.stack()[0][3]}")
        self.manager = WebRequestManager()
        self.manager.request_finished.connect(self.handle_response)
        self.manager.send_get_request("http://127.0.0.1:5000/")

    def events_and_timers(self):
        ## setting to 5 secodns... otherwise logs are INSANSE
        self.filehost_timer.timeout.connect(self.filehost_event_update)
        self.filehost_timer.start(5000)

    def filehost_event_update(self):
        '''
        Test for updating stuff all at once 

        Note, each web reqeust needs its own WebRequestManager implementation, casue otherwise the requests won't work right.

        '''
        ## Request filedata
        self.filehost_manager = WebRequestManager()
        #self.manager.request_finished.connect(self.handle_response)
        self.filehost_manager.request_finished.connect(lambda response: self.handle_response(response, self.filehost_response_received))
        self.filehost_manager.send_get_request("http://127.0.0.1:5000/api/filehost/files")
        ## On response/emit of handle_response, update table
        self.filehost_response_received.connect(self.filehost_api_files_update_table)
        #self.filehost_api_files_update_table(data="None")

        ## Request node data/logs
        self.nodelog_manager = WebRequestManager()
        self.nodelog_manager.send_get_request("http://127.0.0.1:5000/api/filehost/nodelogs")
        self.nodelog_manager.request_finished.connect(lambda response: self.handle_response(response, self.nodelogs_response_received))
        ## On response/emit of handle_response, update table
        self.nodelogs_response_received.connect(self.filehost_api_nodelogs_update_table)

    ## Naming Scheme:
    ##  Plugin   Api Section Action Item
    def filehost_api_files_update_table(self, data):
        '''
        Parses, and updates the table of files in FileHost
        
        '''
        logging.debug(f"{function_debug_symbol} {inspect.stack()[0][3]}")

        data_dict = Utils.json_to_dict(json_string = data)

        if not data_dict:
            self.FileHost_FileLogTable.setRowCount(1)  # Set the number of rows
            self.FileHost_FileLogTable.setItem(0, 0, QTableWidgetItem("Error"))
            self.FileHost_FileLogTable.setItem(0, 1, QTableWidgetItem("With"))
            self.FileHost_FileLogTable.setItem(0, 2, QTableWidgetItem("JSON"))

        elif data_dict == "empty":
            self.FileHost_NodeLogTable.setRowCount(1)  # Set the number of rows
            self.FileHost_NodeLogTable.setItem(0, 0, QTableWidgetItem(""))
            self.FileHost_NodeLogTable.setItem(0, 1, QTableWidgetItem(""))
            self.FileHost_NodeLogTable.setItem(0, 2, QTableWidgetItem(""))
            self.FileHost_NodeLogTable.setItem(0, 3, QTableWidgetItem("Empty, no logs from server"))


        else:
            '''data = [
                ("Alice", 30, "USA"),
                ("Bob", 25, "Canada"),
                ("Charlie", 35, "UK"),
            ]'''

            self.FileHost_FileLogTable.setRowCount(len(data_dict))  # Set the number of rows
            #self.FileHost_FileLogTable.setRowCount(3)
            row_num = 0
            ## For each entry into the data 
            '''
            {
                entry {
                    data...
                }
            }
            
            '''
            for entry in data_dict:

                ## Pulling each data value
                '''
                {
                    entry {
                        filedir:123,
                        filehash:456
                    }
                }
                
                '''
                filedir = data_dict[entry]['filedir']
                filehash = data_dict[entry]['filehash']
                filename = data_dict[entry]['filename']
                filesize = data_dict[entry]['filesize']

                self.FileHost_FileLogTable.setItem(row_num, 0, QTableWidgetItem(filename))
                ## Flipping into MB real quick
                self.FileHost_FileLogTable.setItem(row_num, 1, QTableWidgetItem(str(round(filesize / (1024 * 1024), 4))))
                self.FileHost_FileLogTable.setItem(row_num, 2, QTableWidgetItem(filedir))

                ## bumping row number to next
                row_num = row_num + 1

    def filehost_api_nodelogs_update_table(self, data):
        '''
        Parses, and updates the table of node logs in the FileHost section
        
        '''
        logging.debug(f"{function_debug_symbol} {inspect.stack()[0][3]}")

        data_dict = Utils.json_to_dict(json_string = data)

        if not data_dict:
            self.FileHost_NodeLogTable.setRowCount(1)  # Set the number of rows
            self.FileHost_NodeLogTable.setItem(0, 0, QTableWidgetItem("Error"))
            self.FileHost_NodeLogTable.setItem(0, 1, QTableWidgetItem("With"))
            self.FileHost_NodeLogTable.setItem(0, 2, QTableWidgetItem("JSON"))
            self.FileHost_NodeLogTable.setItem(0, 3, QTableWidgetItem(""))

        elif data_dict == "empty":
            self.FileHost_NodeLogTable.setRowCount(1)  # Set the number of rows
            self.FileHost_NodeLogTable.setItem(0, 0, QTableWidgetItem("Empty"))

        else:
            self.FileHost_NodeLogTable.setRowCount(len(data_dict))  # Set the number of rows
            #self.FileHost_FileLogTable.setRowCount(3)
            row_num = 0
            ## For each entry into the data 
            '''
            {
                entry {
                    data...
                }
            }
            
            '''
            for entry in data_dict:

                ## Pulling each data value
                '''
                {
                    entry {
                        filedir:123,
                        filehash:456
                    }
                }
                
                '''

                nodeip = data_dict[entry]['ip']
                nodemessage = data_dict[entry]['message']
                nodename = data_dict[entry]['name']
                nodetimestamp = data_dict[entry]['timestamp']

                self.FileHost_NodeLogTable.setItem(row_num, 0, QTableWidgetItem(str(nodename)))
                self.FileHost_NodeLogTable.setItem(row_num, 1, QTableWidgetItem(str(nodeip)))
                self.FileHost_NodeLogTable.setItem(row_num, 2, QTableWidgetItem(str(nodemessage)))
                self.FileHost_NodeLogTable.setItem(row_num, 3, QTableWidgetItem(str(nodetimestamp)))

                ## bumping row number to next
                row_num = row_num + 1

    def handle_response(self, reply, signal):        
        '''
        Handles a web request response. 

        Emits a SIGNAL, named 'response_received'. This signal 
        contains the web request response. 
        
        This will trigger signals in the respective functions that called it.
        

        reply: web reply
        signal: The signal to return/emit to. this is so signals dont have the same data passed between them 
        causing issues

        '''
        logging.debug(f"{function_debug_symbol} {inspect.stack()[0][3]}")
        if reply.error() == QNetworkReply.NoError:
            response_data = reply.readAll().data().decode()
            signal.emit(response_data)  # Emit the custom signal
        else:
            string = f"Error with request: {reply.error()}"
            signal.emit(string)  # Emit the custom signal

## Class for handling data ops - move to a util file eventually
class WebRequestManager(QNetworkAccessManager):
    request_finished = Signal(QNetworkReply)

    def send_post_request(self, url, data):
        logging.debug(f"{function_debug_symbol} {inspect.stack()[0][3]}")
        request = QNetworkRequest(url)
        request.setHeader(QNetworkRequest.ContentTypeHeader, "application/json")
        
        reply = self.post(request, data)
        reply.finished.connect(self.handle_response)

    def send_get_request(self, url):
        logging.debug(f"{function_debug_symbol} {inspect.stack()[0][3]}")

        request = QNetworkRequest(url)
        request.setHeader(QNetworkRequest.ContentTypeHeader, "application/json")
        
        reply = self.get(request)
        reply.finished.connect(self.handle_response)

    def handle_response(self):
        logging.debug(f"{function_debug_symbol} {inspect.stack()[0][3]}")

        reply = self.sender()
        self.request_finished.emit(reply)

class Utils:
    def json_to_dict(json_string = None):
        logging.debug(f"{function_debug_symbol} {inspect.stack()[0][3]}")

        try:

            if len(json_string) == 0:
                return "empty"

            data = json.loads(json_string)
            return data
        
        except json.JSONDecodeError as je:
            logging.warning(f"{function_debug_symbol} JSON to Dict failed - JSON decode error: {je}")
            return False

        except Exception as e:
            logging.warning(f"{function_debug_symbol} JSON to Dict failed: {e}")
            return False





if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyApplication()
    window.show()
    sys.exit(app.exec())
