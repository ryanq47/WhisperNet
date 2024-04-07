from PySide6.QtWidgets import QWidget, QTextEdit, QMessageBox, QPushButton, QLineEdit, QToolButton, QMenu, QPlainTextEdit, QDialog
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
from Utils.SignalSingleton import SignalSingleton
#from Utils.YamlLoader import YamlLoader

class Login(QDialog):
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
        self.signals = SignalSingleton()

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

            self.request_manager = WebRequestManager()
            self.request_manager.request_finished.connect(self.validate_login_status) # or whatever func you want to send data to
            self.request_manager.send_request(f"http://{server}/api/login", data=login_dict, method="POST")
        
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

    def validate_login_status(self, response_dict):
        '''
            Validates login status
        '''
        success_text = "Login has succeded!"
        fail_text = "Login failed"
        
        #print(response_json)

        try:
            #response_dict = json.loads(response_json)

            if response_dict["access_token"] != "":
                self.update_login_attempt_text(success_text)
                self.data.auth.jwt = response_dict["access_token"]
                self.logger.info("Successful login to server!")
                # hide window on successful logon
                # WELP taht doesnt work
                #self.close()#hide()

                ## MOVE THIS TO POST SIGNAL EMIT, temp debug spot:
                #self.event_loop = Event()
                #self.event_loop.start_event_loop()
                self.signals.auth.userSuccessfulLogin.emit(True)
                # close dialog on successful logon
                self.close()

            else:
                self.update_login_attempt_text(fail_text)
        except Exception as e:
            self.update_login_attempt_text(fail_text)
            self.logger.error(e)

    def update_login_attempt_text(self, message_to_append):
        '''
        Updates the login attepmt text
        '''
        try:
            current_text = self.login_attempt_textbox.toPlainText()

            new_text = current_text + f"{message_to_append}\n"

            self.login_attempt_textbox.setText(new_text)
        except Exception as e:
            self.logger.error(e)

