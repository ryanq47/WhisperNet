from PySide6.QtWidgets import QWidget, QTextEdit, QMessageBox, QPushButton, QLineEdit, QToolButton, QMenu, QPlainTextEdit
from PySide6.QtUiTools import QUiLoader
from PySide6.QtGui import QAction
from PySide6.QtCore import Signal, QTimer
from Utils.QtWebRequestManager import WebRequestManager
from PySide6.QtNetwork import QNetworkReply
import json
import yaml

#from Utils.YamlLoader import YamlLoader

class Login(QWidget):
    signal_server_response= Signal(str)

    def __init__(self, id=None):
        super().__init__()
        
        loader = QUiLoader()
        ## This NEEDS self as a second arg for some reason.
        self.ui_file = loader.load('QtComponents/Login/Login.ui', self)
        self.id = id
        self.name = "Login"


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


    def show_test_message(self):
        '''
        A test popup box for debugging/etc
        '''
        msg = QMessageBox()
        msg.setWindowTitle("Test Message")
        msg.setText("This is a test popup message.")
        msg.setIcon(QMessageBox.Information)
        msg.exec_()
    
