from PySide6.QtWidgets import QWidget, QMessageBox, QTableWidget, QHeaderView, QTableWidgetItem, QPushButton
from PySide6.QtUiTools import QUiLoader
from PySide6.QtNetwork import QNetworkAccessManager, QNetworkRequest, QNetworkReply
from PySide6.QtCore import Signal

class Secrets(QWidget):
    get_secrets_response = Signal(str)

    def __init__(self):
        super().__init__()
        
        loader = QUiLoader()
        ## This NEEDS self as a second arg for some reason.
        self.ui_file = loader.load('QtComponents/Secrets/secrets.ui', self)
        if self.ui_file == None:
            print("None!!!!!")
        print(self.ui_file.findChildren(QTableWidget)) 

        self.__ui_load()
        self.layout_settings()
        self.name = "Secrets"
        self.get_secrets()

    def __ui_load(self):
        '''
        Load UI elements
        '''
        if self.ui_file == None:
            errmsg = "UI File could not be loaded"
            QMessageBox.critical(self, "Error", f"{errmsg}: {e}")
            print(errmsg)

        try:
            ## Sets layout
            #self.setLayout(self.ui_file.layout())
            self.secrets_table = self.ui_file.findChild(QTableWidget, "secrets_table_widget")
            self.secrets_table_update = self.ui_file.findChild(QPushButton, "secrets_update")

            self.secrets_table_update.clicked.connect(self.update_secrets)

            
            #if self.secrets_table == None:
            #    print("No secrets table found")
            #self.secrets_table = self.ui_file.findChild(QTableWidget, "secrets_table_widget

            #self.c2_systemshell = self.ui_file.findChild(QTextEdit, "test_text")  # Replace "QtWidgets" with the appropriate module
            #self.c2_systemshell.setText("test")

        except Exception as e:
            QMessageBox.critical(self, "Error", f"An error occurred: {e}")
            print(f"[!] {e}")

    def layout_settings(self):
        '''
        Layout settings if needed
        '''
        ## Makes top labels stretch accross the screen
        pass
        #self.secrets_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

    def func_name(self):
        '''
        func
        '''
        ...
        ##self.uielement.setText("test")

    def show_test_message(self):
        '''
        A test popup box for debugging/etc
        '''
        msg = QMessageBox()
        msg.setWindowTitle("Test Message")
        msg.setText("This is a test popup message.")
        msg.setIcon(QMessageBox.Information)
        msg.exec_()


    ## Works!
    def get_secrets(self):
        '''
        Makes a request to the server to get secrets data
        '''
        self.fileaccesslog_manager = WebRequestManager()
        self.fileaccesslog_manager.send_get_request("https://67ea750d-d74e-490d-ac09-0167215b8b23.mock.pstmn.io/data/secrets")
        self.fileaccesslog_manager.request_finished.connect(lambda response: self.handle_response(response, self.get_secrets_response))
        ## Now need to connect to update func
        self.get_secrets_response.connect(self.update_secrets)

    ## Not set up yet
    def update_secrets(self, data):
        '''
        Updates secrets
        '''
        ## not getting updated... hmm

        #print(data)
        print("update secrets")
        row_num = 0

        data = ["","","","","","","","","","","","","","","","",""]
        self.secrets_table.setRowCount(5)  # Set the number of rows

        #self.secrets_table.setItem(1, 0, QTableWidgetItem("stuff"))

        ## Flip json to pyobj
        ## Once in pydict form, this can count how many items
        #self.secrets_table.setRowCount((len(data_dict)))  # Set the number of rows
        
        for secret in data:
            user     = "test"#secret["username"]
            password = "test"#secret["password"]
            domain   = "test"#secret["domain"]
            comment  = "test"#secret["comment"]
            host     = "test"#secret["host"]
            
            #issue with this being none, somethings fucked up
            self.secrets_table.setItem(row_num, 0, QTableWidgetItem(user))
            self.secrets_table.setItem(row_num, 1, QTableWidgetItem(password))
            self.secrets_table.setItem(row_num, 2, QTableWidgetItem(domain))
            self.secrets_table.setItem(row_num, 3, QTableWidgetItem(comment))
            self.secrets_table.setItem(row_num, 4, QTableWidgetItem(host))
            
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
        #logging.debug(f"{function_debug_symbol} {inspect.stack()[0][3]}")
        try:
            if reply.error() == QNetworkReply.NoError:
                response_data = reply.readAll().data().decode()
                signal.emit(response_data)  # Emit the custom signal
            else:
                string = f"Error with request: {reply.error()}"
                signal.emit(string)  # Emit the custom signal
        except Exception as e:
            print(e)
            #logging.debug(f"{function_debug_symbol} Error with handle_response: {e}")

class WebRequestManager(QNetworkAccessManager):
    request_finished = Signal(QNetworkReply)

    def send_post_request(self, url, data):
        #logging.debug(f"{function_debug_symbol} {inspect.stack()[0][3]}")
        try:
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