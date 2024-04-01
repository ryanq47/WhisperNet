from PySide6.QtWidgets import QWidget, QMessageBox, QLineEdit, QComboBox, QToolBar, QVBoxLayout, QPushButton, QDialog
from PySide6.QtGui import QIcon, QAction, QStandardItemModel, QStandardItem, QBrush, QColor
from PySide6.QtUiTools import QUiLoader
from PySide6.QtNetwork import QNetworkReply
from PySide6.QtCore import Qt, Signal, QTimer
from functools import partial
from Utils.QtWebRequestManager import WebRequestManager
from Utils.EventLoop import Event
from Utils.Data import Data
from Utils.BaseLogging import BaseLogging
import inspect
import json

class ListenerPopup(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.logger = BaseLogging.get_logger()

        self.logger.debug(f"{self.__class__.__name__}.{inspect.currentframe().f_code.co_name}: Initializing class {self}")

        loader = QUiLoader()
        self.event_loop = Event()
        self.data = Data()
        ## This NEEDS self as a second arg for some reason.
        self.ui_file = loader.load('QtComponents/Listeners/listener_form_popup.ui', self)

        self.__ui_load()
        self.__q_timer()
        self.__signal_setup()
        self.init_options()
        self.name = "Listener Popup"
        self.setWindowTitle(self.name)

    def __ui_load(self):
        '''
        Load UI elements
        '''
        if self.ui_file == None:
            errmsg = "UI File could not be loaded"
            QMessageBox.critical(self, "Error", f"{errmsg}: {e}")
            print(errmsg)

        try:

            #self.c2_systemshell = self.ui_file.findChild(QTextEdit, "test_text")  # Replace "QtWidgets" with the appropriate module
            self.listener_name = self.ui_file.findChild(QLineEdit, "listener_popup_name")
            self.listener_address = self.ui_file.findChild(QLineEdit, "listener_popup_address")
            self.listener_port = self.ui_file.findChild(QLineEdit, "listener_popup_port")

            self.listener_type = self.ui_file.findChild(QComboBox, "listener_popup_type_combo")
            self.listener_spawn_button = self.ui_file.findChild(QPushButton, "listener_popup_spawn_button")
            # Dec tree for type - figure out where to put this based on type input.
            self.listener_spawn_button.clicked.connect(self.spawn_http_listener)

            ## MUST GO LAST!!!
            self.setLayout(self.ui_file.layout())
        except Exception as e:
            QMessageBox.critical(self, "Error", f"An error occurred: {e}")
            print(f"[!] {e}")


    def __q_timer(self):
        '''
        A qtimer/event loop queuer for updating events. 
        '''

        # add to even loop
        #self.event_loop.add_to_event_loop(self.get_listener_data)

    def __signal_setup(self):
        '''
            Sets up signals for the entire plugin
        '''
        #self.data.simplec2.db_data_updated.connect(self.update_client_widget)


    def init_options(self):
        '''
        Sets options for the options button (bottom left button with '...')
        '''
        pass

    def listener_decision_tree(self):
        """
        Sorts which listener function is called. Handy as diff listeners may have diff args, and multiple funcs is cleaner (in my opinion)
            than multiple (large) if statements in one. 

            Using .lower for all types for consistency incase I screw up something on the popup end.
        """

        if self.listener_params["type"].lower() == "http":
            self.spawn_http_listener()

        else:
            self.logger.error(f'Somehow selected a listener type that did not exist, type selected: {self.listener_params["type"]}')

    def spawn_http_listener(self):
        """
            Sends a network request to the Server, to spawn the listener

        """
        # listener endpoint takes port, address, and nickname
        listener_params = {}

        listener_params["nickname"] = self.listener_name.text()
        listener_params["address"] =  self.listener_address.text()
        listener_params["port"] = self.listener_port.text()

        self.logger.info(f'Sending request to spawn HTTP listener {listener_params["nickname"]} at {listener_params["address"]}:{listener_params["port"]}')

        # need to conv to json

        #listener_json = json.dumps(listener_params)

        #print(listener_json)


        self.request_manager = WebRequestManager()
        #self.request_manager.request_finished.connect(self.some_method_to_take_the_data)
        self.request_manager.send_request(
            url = "http://127.0.0.1:5000/api/simplec2/listener/http/start",
            data = listener_params, 
            method="POST"
            )


