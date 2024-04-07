import inspect
import json
from PySide6.QtWidgets import QWidget, QMessageBox, QMenu, QMainWindow, QToolBar, QVBoxLayout, QPushButton, QListView
from PySide6.QtGui import QIcon, QAction, QStandardItemModel, QStandardItem, QBrush, QColor
from PySide6.QtUiTools import QUiLoader
from PySide6.QtNetwork import QNetworkReply
from PySide6.QtCore import Qt, Signal, QStringListModel, QTimer
from functools import partial
from Utils.QtWebRequestManager import WebRequestManager
from Utils.EventLoop import Event
from Utils.Data import Data
from Utils.BaseLogging import BaseLogging
from Utils.Utils import GuiUtils
from QtComponents.Listeners.listener_popup import ListenerPopup

class Listeners(QWidget):
    #signal_get_client_data= Signal(str)
    #signal_get_network_data = Signal(str)
    signal_get_all_data = Signal(str)
    signal_get_network_data = Signal(str)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.logger = BaseLogging.get_logger()

        #QWidget.__init__(self, parent)
        #BaseLogging.__init__(self)
        self.logger.debug(f"{self.__class__.__name__}.{inspect.currentframe().f_code.co_name}: Initializing class {self}")

        loader = QUiLoader()
        self.event_loop = Event()
        self.data = Data()
        ## This NEEDS self as a second arg for some reason.
        self.ui_file = loader.load('QtComponents/Listeners/listener_layout_widgets.ui', self)

        self.__ui_load()
        self.__q_timer()
        self.__signal_setup()
        self.init_options()
        self.name = "Listener"


    def __ui_load(self):
        """
        Adjusted to accommodate additional widgets like a toolbar.
        """
        if self.ui_file is None:
            errmsg = "UI File could not be loaded"
            QMessageBox.critical(self, "Error", errmsg)
            print(errmsg)
            return

        try:

            
            # load items
            #self.c2_systemshell = self.ui_file.findChild(QTextEdit, "test_text")  # Replace "QtWidgets" with the appropriate module
            #self.c2_systemshell.setText("test")

            # showing up as none. 
            self.listener_list_view = self.ui_file.findChild(QListView, "listener_list_view")


            ## GOES LAST
            # Wrap the loaded UI in a container widget
            container = QWidget()
            container.setLayout(self.ui_file.layout())

            # Create a new layout for self to include both the container and the toolbar
            layout = QVBoxLayout(self)
            layout.addWidget(container)  # Add the UI container as the main content
            self.setLayout(layout)
            self.main_container = container  # Keep a reference if needed

        except Exception as e:
            QMessageBox.critical(self, "Error", f"An error occurred: {e}")
            print(f"[!] {e}")


    def __q_timer(self):
        '''
        A qtimer/event loop queuer for updating events. 
        '''

        # add to even loop
        self.event_loop.add_to_event_loop(self.get_listener_data)

    def __signal_setup(self):
        '''
            Sets up signals for the entire plugin
        '''
        #self.data.simplec2.db_data_updated.connect(self.update_client_widget)

    def contextMenuEvent(self, event):
        # Find the item at the cursor position
        item = self.client_tree.itemAt(event.pos())
        if item:
            # Create context menu
            menu = QMenu(self)

            # Add actions
            action1 = menu.addAction("Something")
            action2 = menu.addAction("Something2")

            # Connect actions to methods or use lambda functions
            #action1.triggered.connect(lambda: self.action1_triggered(item))
            #action2.triggered.connect(lambda: self.action2_triggered(item))
            action1.triggered.connect(self.show_test_message)
            action2.triggered.connect(self.show_test_message)

            # Display the menu
            menu.exec(event.globalPos())

    def init_options(self):
        '''
        Sets options for the options button (bottom left button with '...')
        '''
        self.add_toolbar()

    def add_toolbar(self):
        """
        Adds a toolbar to the widget, considering the UI is loaded from a file.
        """
        toolbar = QToolBar("Tools", self)
        new_listener = toolbar.addAction("New Listener")
        new_listener.triggered.connect(lambda: GuiUtils.open_dialog(ListenerPopup, self))

        # Assuming __ui_load has been called and the main layout set
        self.layout().insertWidget(0, toolbar)


    def get_listener_data(self):
        '''
        Gets all the simplec2 data from the server
        '''
        self.logger.info(f"{self.__class__.__name__}.{inspect.currentframe().f_code.co_name}: Getting data from server")

        self.request_manager = WebRequestManager()
        self.request_manager.request_finished.connect(self.update_listener_list_view_widget) # or whatever func you want to send data to
        self.request_manager.send_request("http://127.0.0.1:5000/api/simplec2/listener")

    def update_listener_list_view_widget(self, data):
        '''
        Updates the listener list view with the given data.
        This includes adding new items, and removing items that are no longer present.
        The "name" key is used as a unique identifier.
        '''

        # Initialize the model if it does not exist
        if not hasattr(self, 'listener_list_view_model') or self.listener_list_view_model is None:
            self.listener_list_view_model = QStringListModel()
            self.listener_list_view.setModel(self.listener_list_view_model)

        current_entries = self.listener_list_view_model.stringList()
        current_identifiers = set(entry.split(' - ')[0] for entry in current_entries)
        new_data_identifiers = set(data["data"].keys())

        # Identify which identifiers have been removed and which are new
        identifiers_to_remove = current_identifiers - new_data_identifiers
        identifiers_to_add = new_data_identifiers - current_identifiers

        # Remove entries that are no longer present
        updated_entries = [
            entry for entry in current_entries
            if entry.split(' - ')[0] not in identifiers_to_remove
        ]

        # Add new entries
        for name, details in data["data"].items():
            if name in identifiers_to_add:
                entry = f"{name} - {details['bind_address']}:{details['bind_port']} - {details['type']}"
                updated_entries.append(entry)

        # Update the model with the new list
        self.listener_list_view_model.setStringList(updated_entries)
 

    def show_test_message(self):
        '''
        A test popup box for debugging/etc
        '''
        msg = QMessageBox()
        msg.setWindowTitle("Test Message")
        msg.setText("This is a test popup message.")
        msg.setIcon(QMessageBox.Information)
        msg.exec_()

    def print_data(self, data):
        '''
        Temp for printing data, meant to bea debug method
        '''
        self.logger.debug(f"{self.__class__.__name__}.{inspect.currentframe().f_code.co_name}: Printing Data:")
        print(data)

    def update_data(self, data):
        '''
        Updates current data in the singleton
        '''
        pass


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
            #print(reply.readAll().data().decode())
            if reply.error() == QNetworkReply.NoError:
                response_data = reply.readAll().data().decode()
                #print("data form handle response received")
                #print(response_data)
                signal.emit(response_data)  # Emit the custom signal
                ## Disconnecting signal post emit, otherwise it starts to multiply
                signal.disconnect()

            else:
                string = f"Error with request: {reply.error()}"
                #print(reply)
                signal.emit(string)  # Emit the custom signal
                signal.disconnect()
        except Exception as e:
            self.logger.error(f"{self.__class__.__name__}.{inspect.currentframe().f_code.co_name}: {e}")
            #logging.debug(f"{function_debug_symbol} Error with handle_response: {e}")

