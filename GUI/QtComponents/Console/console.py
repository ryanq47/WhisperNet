from PySide6.QtWidgets import QWidget, QTextEdit, QMessageBox, QPushButton, QLineEdit, QToolButton, QMenu
from PySide6.QtUiTools import QUiLoader
from PySide6.QtGui import QAction
from PySide6.QtCore import Signal, QTimer
from Utils.QtWebRequestManager import WebRequestManager
from PySide6.QtNetwork import QNetworkReply
import json
import yaml

#from Utils.YamlLoader import YamlLoader

class Console(QWidget):
    signal_server_response= Signal(str)

    def __init__(self, id=None):
        super().__init__()
        
        loader = QUiLoader()
        ## This NEEDS self as a second arg for some reason.
        self.ui_file = loader.load('QtComponents/Console/console.ui', self)
        self.id = id
        self.name = "Console"


        self.__yaml_load()
        self.__ui_load()
        self.init_console()
        self.init_options()


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
            self.console_send.clicked.connect(self.handle_command_from_input)
            #self.console_send.clicked.connect(self.connect_to_server) ## This temporarily triggers server

            self.console_input = self.ui_file.findChild(QLineEdit, "console_input")  # Replace "QtWidgets" with the appropriate module

            self.debug_console = self.ui_file.findChild(QTextEdit, "debug_console")  # Replace "QtWidgets" with the appropriate module
            self.debug_console.hide()

            self.options_button = self.ui_file.findChild(QToolButton, "options_button")
            #self.c2_systemshell.setText("test")

            ## MUST GO LAST!!!
            self.setLayout(self.ui_file.layout())

        except Exception as e:
            QMessageBox.critical(self, "Error", f"An error occurred: {e}")
            print(f"[!] {e}")

    def __yaml_load(self):
        '''
        Loads yaml stuff for any config

        got annoyed with making a class/wrapper library for it so I said fuck it and did this
        '''
        try:
            with open("Config/Strings.yaml", 'r') as file:
                self.yaml_strings = yaml.safe_load(file)
                print(self.yaml_strings)  # Add this line to check the loaded content
        except Exception as e:
            print(e)

        if self.yaml_strings == None:
            print("none")

    def init_options(self):
        '''
        Sets options for the options button (bottom left button with '...')
        '''
        #self.options_button
        menu = QMenu(self)

        # Add actions to the menu
        show_debug_console = QAction("Show Debug Console", self)
        hide_debug_console = QAction("Hide Debug Console", self)

        #action2 = QAction("Option 2", self)
        menu.addAction(show_debug_console)
        menu.addAction(hide_debug_console)

        # Connect actions to functions
        show_debug_console.triggered.connect(lambda _show_debug_console: self.debug_console.show())
        hide_debug_console.triggered.connect(lambda _show_debug_console: self.debug_console.hide())

        self.options_button.setMenu(menu)
        self.options_button.setPopupMode(QToolButton.InstantPopup)

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


    def update_console_window(self,text=None, json_data=None, ):
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

        self.debug_console.setText("Debug Console Placeholder\n" + "{'action': 'test', 'command': 'command', 'error': None}")

    def handle_command_from_input(self):
        '''
        Gets command form the input box in the consoel gui.

        From here, it's parsed and a subsequent method is done. 

        name: console_input
        button: console_send
        '''

        text = self.console_input.text()

        if text == None or text == "":
            parsed_text = self.yaml_strings["Console"]["emptyinput"]

        ## Parse text
        else:
            parsed_text = self.parse_user_input(user_input = text)
            
            ## temp reflecting all input
            #self.update_console_window(text)
            
        self.update_console_window(parsed_text)


    def parse_user_input(self, user_input):
        '''
        Parses user input from the GUI console_input field

        user_input: (str) the input

        returns a dict with data
        '''
        console_debug_dict = {
            "action":None,
            "command":None,
            "error":None
        }
        ## Strip leading/tail whitespace & fixes most input problems
        user_input = user_input.strip()

        ## Extra empty handling, shouldn't be needed as this is handled in handle_command_from_input,
        # but just in case.
        if not user_input:
            return console_debug_dict 
        
        try:
            action = user_input.split(" ")[0]

            ## Get length of action & remove that many chars from the original input
            
            ##len(action) to get lenfth of action, +1 to remove the extra space
            command = user_input[len(action) + 1:]

            #print(action)
            #print(command)

            console_debug_dict["action"] = action
            console_debug_dict["command"] = command

            return console_debug_dict

        except Exception as e:
            console_debug_dict["error"] = f"Error with input: {e}"
            return console_debug_dict 


        ####
        '''
        Big question: 
            How are we going to return the input command_dict, and server_response_dict? (2nd is not implemented yet)

            I'm thinking a dict of dicts, so:
            {
                server_response: server_response_dict,
                console_debug: console_debug_dict
            }

            I would need to rework the update_console_window to parse the server_response, and the console_debug dict
            correctly. this is gonna be cool af tho.

        '''
        ####

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