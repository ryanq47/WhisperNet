from PySide6.QtWidgets import QWidget, QTextEdit, QMessageBox, QPushButton, QLineEdit
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import Signal, QTimer
from Utils.QtWebRequestManager import WebRequestManager
from PySide6.QtNetwork import QNetworkReply
import json

class Console(QWidget):
    signal_server_response= Signal(str)

    def __init__(self, id=None):
        super().__init__()
        
        loader = QUiLoader()
        ## This NEEDS self as a second arg for some reason.
        self.ui_file = loader.load('QtComponents/Console/console.ui', self)
        self.id = id
        self.name = "Console"
        self.__ui_load()
        self.init_console()

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

            self.console_shell = self.ui_file.findChild(QTextEdit, "console_shell")  # Replace "QtWidgets" with the appropriate module
            self.console_send = self.ui_file.findChild(QPushButton, "console_send")  # Replace "QtWidgets" with the appropriate module
            self.console_send.clicked.connect(self.get_command_from_input)
            #self.console_send.clicked.connect(self.connect_to_server) ## This temporarily triggers server

            self.console_input = self.ui_file.findChild(QLineEdit, "console_input")  # Replace "QtWidgets" with the appropriate module

            #self.c2_systemshell.setText("test")

            ## MUST GO LAST!!!
            self.setLayout(self.ui_file.layout())

        except Exception as e:
            QMessageBox.critical(self, "Error", f"An error occurred: {e}")
            print(f"[!] {e}")

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

    def init_console(self):
        '''
        Sets up the console with stuff
        '''
        if self.id == None:
            self.console_shell.setText("ID not provided. Cannot init console")
            return

        ## Test Connect to server
        self.connect_to_server()

    
    def connect_to_server(self):
        '''
        Connects to server console API stuff. Basically checks to make sure the correct
        console item is reachable.

        POSTS
        {
            "id":id,
            "user":""

        }
        '''
        # Send msg to server
        self.request_manager = WebRequestManager()

        ## get from client input eventually
        temp_data = {
            "action":"powershell",
            "arguments":"whoami",
            "id":"1234"
        }

        temp_json_data = json.dumps(temp_data)
        # turn into bytes
        temp_json_data = self.request_manager.encode_str_to_bytes(temp_json_data)

        #post request for now. Subject to chagne
        self.request_manager.send_post_request(
            url = "http://127.0.0.1:5000/api/simplec2/clients",
            data = temp_json_data
        )

        ## Wait on response

        self.request_manager.request_finished.connect(
            ##  send request                                      ## Signal that holds data
            lambda response: self.handle_response(response, self.signal_server_response)
        )

        self.signal_server_response.connect(self.update_console_window)


    def update_console_window(self,text=None, json_data=None):
        '''
        Updates the console window. Can take 2 arguments/forms of data:

        text: For plaintext data, or whatever you want really. Gets converted to a str anyways.

        json_data: for JSON data, specificaly from the server. _DO NOT_ use this unless its for a server response. 
        Will fill injson scheme later

        Ignore this blabber:
        # if ok:
        #temp
        #client_id = "client_id123"

            ## If all is good:
        #self.console_shell.setText(f"Connection to server successful. Channel to {client_id} is open! - not really. the psot request worked apparently so thats good")
        #self.console_shell.setText("You should see raw JSON of the request: " + str(data) + "This need to do some magic still for a pretty output/not raw data")
        
        ## This bugs out if a node is down, I dunno why. Def a bug

        '''

        if json_data:
            try:
                data_object = json.loads(json_data)

                command_results = data_object["message"]

                self.console_shell.setText(command_results)

            except Exception as e:
                self.console_shell.setText(f"Error with console: {e}")
                print(e)

            #else:
            #self.console_shell.setText(f"Error <details>!")

        ## Handles text input
        elif text:
            try:
                self.console_shell.setText(str(text))
            except Exception as e:
                self.console_shell.setText(f"Error with console: {e}")

    def get_command_from_input(self):
        '''
        Gets command form the input box in the consoel gui.

        From here, it's parsed and a subsequent method is done. 

        name: console_input
        button: console_send
        '''

        text = self.console_input.text()
        self.update_console_window(text)


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