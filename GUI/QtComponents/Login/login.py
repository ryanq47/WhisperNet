from PySide6.QtWidgets import QWidget, QTextEdit, QMessageBox, QPushButton, QLineEdit, QToolButton, QMenu, QPlainTextEdit
from PySide6.QtUiTools import QUiLoader
from PySide6.QtGui import QAction
from PySide6.QtCore import Signal, QTimer
from Utils.QtWebRequestManager import WebRequestManager
from PySide6.QtNetwork import QNetworkReply
import json
import yaml
import inspect
from Utils.EventLoop import Event

from Utils.Data import Data
from Utils.Logger import LoggingSingleton
#from Utils.YamlLoader import YamlLoader

class Login(QWidget):
    signal_server_response= Signal(str)
    signal_logged_in = Signal(bool)

    def __init__(self, id=None):
        super().__init__()
        self.logger = LoggingSingleton.get_logger()
        loader = QUiLoader()
        ## This NEEDS self as a second arg for some reason.
        self.ui_file = loader.load('QtComponents/Login/Login.ui', self)
        self.id = id
        self.name = "Login"

        ## singleton, this is fine
        self.data = Data()

        self.__yaml_load()
        self.__ui_load()
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

            #self.options_button = self.ui_file.findChild(QToolButton, "options_button")
            #self.c2_systemshell.setText("test")
            self.username_input = self.ui_file.findChild(QLineEdit, "username_input")
            self.password_input = self.ui_file.findChild(QLineEdit, "password_input")
            self.server_input   = self.ui_file.findChild(QLineEdit, "server_input")
            self.login_attempt_textbox = self.ui_file.findChild(QTextEdit,"login_attempt_textbox")

            self.server_login_button = self.ui_file.findChild(QPushButton, "server_login_button")
            self.server_login_button.clicked.connect(self.send_login)

            ## MUST GO LAST!!!
            self.setLayout(self.ui_file.layout())

        except Exception as e:
            QMessageBox.critical(self, "Error", f"An error occurred: {e}")
            #print(f"[!] {e}")\
            self.logger.info(f"{self.__class__.__name__}.{inspect.currentframe().f_code.co_name}: {e}")

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

    def send_login(self):
        '''
        Sends login to the server
        '''
        try:
            username = self.username_input.text()
            password = self.password_input.text()
            server   = self.server_input.text()
            self.logger.info(f"{self.__class__.__name__}.{inspect.currentframe().f_code.co_name}: Attempting to log into server: username: {username}, server: {server}")

            login_dict = {
                "username": username,
                "password": password
            }

            login_json = json.dumps(login_dict)


            self.request_manager = WebRequestManager()

            #post request for now. Subject to chagne
            self.request_manager.send_post_request(
                url = f"http://{server}/api/login",
                data = login_json ## << FIX ME BETTER
            )

            self.request_manager.request_finished.connect(
                ##  send request                                      ## Signal that holds data
                lambda response: self.handle_response(response, self.signal_server_response)
            )## I don't fully remeber why we have to pass response to the function as well. 

            # when signal is triggerd, called validate_login_status
            self.signal_server_response.connect(self.validate_login_status)

        
        except Exception as e:
            self.logger.error(f"{self.__class__.__name__}.{inspect.currentframe().f_code.co_name}: {e}")

        #print(f"username: {username} password: {password}, server: {server}")

        '''
            Mini brain dump:
                Login request >
                Handle Response > emits signal 
                validate_login_status >
                update_login_attempt_text >

        '''

    def validate_login_status(self, response_json):
        '''
            Validates login status
        '''
        success_text = "Login has succeded!"
        fail_text = "Login failed"
        
        try:
            response_dict = json.loads(response_json)

            if response_dict["access_token"] != "":
                self.update_login_attempt_text(success_text)
                self.data.auth.jwt = response_dict["access_token"]
                self.logger.info(f"{self.__class__.__name__}.{inspect.currentframe().f_code.co_name}: Successful login to server!")
                # hide window on successful logon
                # WELP taht doesnt work
                #self.close()#hide()

                ## MOVE THIS TO POST SIGNAL EMIT, temp debug spot:
                #self.event_loop = Event()
                #self.event_loop.start_event_loop()
                self.signal_logged_in.emit(True)

            else:
                self.update_login_attempt_text(fail_text)
        except Exception as e:
            self.update_login_attempt_text(fail_text)
            self.logger.error(f"{self.__class__.__name__}.{inspect.currentframe().f_code.co_name}: {e}")

    def update_login_attempt_text(self, message_to_append):
        '''
        Updates the login attepmt text
        '''
        try:
            current_text = self.login_attempt_textbox.toPlainText()

            new_text = current_text + f"{message_to_append}\n"

            self.login_attempt_textbox.setText(new_text)
        except Exception as e:
            self.logger.error(f"{self.__class__.__name__}.{inspect.currentframe().f_code.co_name}: {e}")

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
                signal.disconnect()

            else:
                string = f"Error with request: {reply.error()}"
                signal.emit(string)  # Emit the custom signal
                signal.disconnect()

        except Exception as e:
            self.logger.info(f"{self.__class__.__name__}.{inspect.currentframe().f_code.co_name}: {e}")
            #logging.debug(f"{function_debug_symbol} Error with handle_response: {e}")
