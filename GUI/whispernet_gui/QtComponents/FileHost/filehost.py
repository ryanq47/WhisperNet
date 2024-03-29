from PySide6.QtWidgets import QWidget, QTextEdit, QMessageBox, QTableWidgetItem, QPushButton, QTextBrowser, QTableWidget, QFileDialog
from PySide6.QtUiTools import QUiLoader
from PySide6.QtNetwork import QNetworkAccessManager, QNetworkRequest, QNetworkReply
from PySide6.QtCore import Signal, QTimer
import json
import logging
import inspect

logging.basicConfig(level=logging.WARNING)
## Change the path to the system path + a log folder/file somewhere
logging.basicConfig(filename='WhisperNetGui.log', filemode='a', format='%(asctime)s - %(levelname)s - %(message)s', force=True, datefmt='%Y-%m-%d %H:%M:%S')
logging.getLogger().addHandler(logging.StreamHandler())
function_debug_symbol = "[*]"


class Filehost(QWidget):
    filehost_response_received = Signal(str)
    nodelogs_response_received = Signal(str)
    fileaccesslog_response_received = Signal(str)
    filehost_upload_response_received = Signal(str)

    def __init__(self):
        super().__init__()
        loader = QUiLoader()
        ## This NEEDS self as a second arg for some reason.
        self.ui_file = loader.load('QtComponents/FileHost/filehost.ui', self)
        self.name = "FileHost"
        self.__ui_load()
        self.__q_timer()

    def __ui_load(self):
        '''
        Load UI elements
        '''
        if self.ui_file == None:
            errmsg = "UI File could not be loaded"
            QMessageBox.critical(self, "Error", f"{errmsg}: {e}")
            print(errmsg)

        try:
            self.FileHost_TextBox= self.ui_file.findChild(QTextBrowser, "FileHost_TextBox")  # Replace "QtWidgets" with the appropriate module
            self.FileHost_FileLogTable = self.ui_file.findChild(QTableWidget, "FileHost_FileLogTable")  
            self.FileHost_NodeLogTable = self.ui_file.findChild(QTableWidget, "FileHost_NodeLogTable")
            self.FileHost_FileAccessLogsTable = self.ui_file.findChild(QTableWidget, "FileHost_FileAccessLogsTable")
            self.FileHost_UploadFileButton = self.ui_file.findChild(QPushButton, "FileHost_UploadFileButton")
            #self.c2_systemshell = self.ui_file.findChild(QTextEdit, "test_text")  # Replace "QtWidgets" with the appropriate module
            #self.c2_systemshell.setText("test")

            ## MUST GO LAST!!!
            self.setLayout(self.ui_file.layout())

        except Exception as e:
            QMessageBox.critical(self, "Error", f"An error occurred: {e}")
            print(f"[!] {e}")

    def __q_timer(self):
        ## setting to 5 secodns... otherwise logs are INSANSE
        self.filehost_timer = QTimer()
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

        self.fileaccesslog_manager = WebRequestManager()
        self.fileaccesslog_manager.send_get_request("http://127.0.0.1:5000/api/filehost/filelogs")
        self.fileaccesslog_manager.request_finished.connect(lambda response: self.handle_response(response, self.fileaccesslog_response_received))
        ## On response/emit of handle_response, update table
        self.fileaccesslog_response_received.connect(self.filehost_api_fileaccesslogs_update_table)

    ## Naming Scheme:
    ##  Plugin   Api Section Action Item
    def filehost_api_files_update_table(self, data):
        '''
        Parses, and updates the table of files in FileHost
        
        '''
        logging.debug(f"{function_debug_symbol} {inspect.stack()[0][3]}")

        if self.FileHost_FileLogTable == None:
            logging.warning(f"{function_debug_symbol} self.FileHost_FileLogTable == None. File Log Table will not load.")

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

        if self.FileHost_NodeLogTable == None:
            logging.warning(f"{function_debug_symbol} self.FileHost_NodeLogTable == None. Node Log Table will not load.")

        data_dict = Utils.json_to_dict(json_string = data)

        if not data_dict:
            self.FileHost_NodeLogTable.setRowCount(1)  # Set the number of rows
            self.FileHost_NodeLogTable.setItem(0, 0, QTableWidgetItem("Error"))
            self.FileHost_NodeLogTable.setItem(0, 1, QTableWidgetItem("With"))
            self.FileHost_NodeLogTable.setItem(0, 2, QTableWidgetItem("JSON"))
            self.FileHost_NodeLogTable.setItem(0, 3, QTableWidgetItem(""))

        elif data_dict == "empty" or data_dict == None:
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

    def filehost_api_fileaccesslogs_update_table(self, data):
        '''
        Parses, and updates the table of node logs in the FileHost section
        
        '''
        logging.debug(f"{function_debug_symbol} {inspect.stack()[0][3]}")

        data_dict = Utils.json_to_dict(json_string = data)

        if self.FileHost_FileAccessLogsTable == None:
            logging.warning(f"{function_debug_symbol} self.FileHost_FileAccessLogsTable == None. File Access Log Table will not load.")

        if not data_dict:
            self.FileHost_FileAccessLogsTable.setRowCount(1)  # Set the number of rows
            self.FileHost_FileAccessLogsTable.setItem(0, 0, QTableWidgetItem("Error"))
            self.FileHost_FileAccessLogsTable.setItem(0, 1, QTableWidgetItem("With"))
            self.FileHost_FileAccessLogsTable.setItem(0, 2, QTableWidgetItem("JSON"))
            self.FileHost_FileAccessLogsTable.setItem(0, 3, QTableWidgetItem(""))
            self.FileHost_FileAccessLogsTable.setItem(0, 4, QTableWidgetItem(""))

        elif data_dict == "empty":
            self.FileHost_FileAccessLogsTable.setRowCount(1)  # Set the number of rows
            self.FileHost_FileAccessLogsTable.setItem(0, 0, QTableWidgetItem("Empty"))

        else:
            self.FileHost_FileAccessLogsTable.setRowCount(len(data_dict))  # Set the number of rows
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

                accessorip = data_dict[entry]['accessorip']
                filename = data_dict[entry]['filename']
                nodename = data_dict[entry]['hostingserver'] ## chane to hosting node
                accesstimestamp = data_dict[entry]['timestamp']
                httpstatuscode = data_dict[entry]['httpstatuscode']

                self.FileHost_FileAccessLogsTable.setItem(row_num, 0, QTableWidgetItem(str(filename)))
                self.FileHost_FileAccessLogsTable.setItem(row_num, 1, QTableWidgetItem(str(accessorip)))
                self.FileHost_FileAccessLogsTable.setItem(row_num, 2, QTableWidgetItem(str(nodename)))
                self.FileHost_FileAccessLogsTable.setItem(row_num, 3, QTableWidgetItem(str(httpstatuscode)))
                self.FileHost_FileAccessLogsTable.setItem(row_num, 4, QTableWidgetItem(str(accesstimestamp)))


                ## bumping row number to next
                row_num = row_num + 1

    def filehost_upload_file(self):
        logging.debug(f"{function_debug_symbol} {inspect.stack()[0][3]}")

        # Open a file dialog to select files for upload
        file_dialog = QFileDialog()
        files = file_dialog.getOpenFileNames(self, "Select File(s) to Upload")[0]

        if files:
            # URL of the web server to which you want to send the files
            server_url = "http://127.0.0.1:5000/api/filehost/upload"

            # Prepare a dictionary of files to send in the POST request
            #files_to_upload = []
            for file in files:
                #files_to_upload.append(("file", (file_path, open(file_path, "rb"))))
                with open(file,'rb') as f:
                    file_bytes = f.read()

                    try:
                        self.filehost_post_manager = WebRequestManager()
                        self.filehost_post_manager.send_post_request(
                            url = server_url,
                            ## issue ehre with the type of data being sent. Server jtakes json with bytes, qt is being a pITA
                            data = {'file': file_bytes}
                        )
                        #self.filehost_post_manager.request_finished.connect(lambda response: print("It worked? or at lteast connected"))
                        ## Handle response
                        self.filehost_post_manager.request_finished.connect(lambda response: self.handle_response(response, self.filehost_upload_response_received))

                        ## Upon recieveing response, do action with response
                        self.filehost_upload_response_received.connect(self.filehost_upload_file_completed)
                        #print("Theoretically if you're seeing this... this should have worked")

                    except Exception as e:
                        print(f"Error: {e}")

    def filehost_upload_file_completed(self, response):
        print(response)

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
        try:
            if reply.error() == QNetworkReply.NoError:
                response_data = reply.readAll().data().decode()
                signal.emit(response_data)  # Emit the custom signal
            else:
                string = f"Error with request: {reply.error()}"
                signal.emit(string)  # Emit the custom signal
        except Exception as e:
            logging.debug(f"{function_debug_symbol} Error with handle_response: {e}")

## Class for handling data ops - move to a util file eventually
class WebRequestManager(QNetworkAccessManager):
    request_finished = Signal(QNetworkReply)

    def send_post_request(self, url, data):
        logging.debug(f"{function_debug_symbol} {inspect.stack()[0][3]}")
        try:
            request = QNetworkRequest(url)
            request.setHeader(QNetworkRequest.ContentTypeHeader, "application/json")
            #application/octet-stream
            #request.setHeader(QNetworkRequest.ContentTypeHeader, "application/octet-stream")

            reply = self.post(request, data)
            reply.finished.connect(self.handle_response)
        except Exception as e:
            logging.warning(f"{function_debug_symbol} Error sending post request: {e}")

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
            #logging.warning(f"{function_debug_symbol} JSON to Dict failed - JSON decode error: {je}")
            return False

        except Exception as e:
           #logging.warning(f"{function_debug_symbol} JSON to Dict failed: {e}")
            return False