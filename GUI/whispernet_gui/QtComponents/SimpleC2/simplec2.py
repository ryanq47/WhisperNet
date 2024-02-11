from PySide6.QtWidgets import QWidget, QTextEdit, QMessageBox, QTreeWidgetItem, QTreeWidget, QPushButton, QMenu, QToolButton
from PySide6.QtGui import QIcon, QAction
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

class Simplec2(QWidget):
    #signal_get_client_data= Signal(str)
    #signal_get_network_data = Signal(str)
    signal_get_all_data = Signal(str)

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
        self.ui_file = loader.load('QtComponents/SimpleC2/c2_layout_widgets.ui', self)

        self.__ui_load()
        self.__q_timer()
        self.init_options()
        self.name = "SimpleC2"
        self.client_items = {}
        self.network_items ={}
        #self.get_all_data()


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

            #self.c2_systemshell = self.ui_file.findChild(QTextEdit, "test_text")  # Replace "QtWidgets" with the appropriate module
            #self.c2_systemshell.setText("test")
            self.client_tree = self.ui_file.findChild(QTreeWidget, "client_tree_widget")
            
            #self.add_client = self.ui_file.findChild(QPushButton, "add_client")
            #self.refresh_manually = self.ui_file.findChild(QPushButton, "refresh_manually")
            
            self.options_button = self.ui_file.findChild(QToolButton, "options_button")
            self.options_button.setText("Options")
            self.info_bar = self.ui_file.findChild(QTextEdit, "info_bar")


            # temp
            data_dict = None
            #self.add_client.clicked.connect(partial(self.add_client_to_widget,data_dict))

            #self.refresh_manually.clicked.connect(partial(self.get_client_data))


            ## MUST GO LAST!!!
            self.setLayout(self.ui_file.layout())
        except Exception as e:
            QMessageBox.critical(self, "Error", f"An error occurred: {e}")
            print(f"[!] {e}")

    def __q_timer(self):
        '''
        A qtimer for updating events. 
        '''
        '''self.one_sec_timer = QTimer(self)
        self.one_sec_timer.timeout.connect(self.get_client_data)
        self.one_sec_timer.start(1000)'''

        #pleas don't break
        #self.event_loop.add_to_event_loop(self.get_client_data)
        self.event_loop.add_to_event_loop(self.get_all_data)


    def contextMenuEvent(self, event):
        # Find the item at the cursor position
        #print("MEEEEEE")
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
        #self.options_button
        menu = QMenu(self)

        # Add actions to the menu
        add_host = QAction("Add Host", self)
        add_network = QAction("Add Network", self)

        #hide_debug_console = QAction("Hide Debug Console", self)

        #action2 = QAction("Option 2", self)
        menu.addAction(add_host)
        menu.addAction(add_network)

        # Connect actions to functions
        add_host.triggered.connect(lambda _add_host: self.info_bar.setText("add_host"))
        add_network.triggered.connect(lambda _add_network: self.info_bar.setText("add_network"))

        self.options_button.setMenu(menu)
        self.options_button.setPopupMode(QToolButton.InstantPopup)

    ## Getting Data Stuff
        
    def get_all_data(self):
        '''
        Gets all the simplec2 data from the server
        '''
        self.logger.info(f"{self.__class__.__name__}.{inspect.currentframe().f_code.co_name}: Getting data from server")
        self.request_manager = WebRequestManager()

        #post request for now. Subject to chagne
        self.request_manager.send_get_request(
            url = "http://127.0.0.1:5000/api/simplec2/general/everything")

        ## stupid way of doing this but whatever. 

        self.request_manager.request_finished.connect(
            ##  send request                                      ## Signal that holds data
            lambda response: self.handle_response(response, self.signal_get_all_data)
        )## I don't fully remeber why we have to pass response to the function as well. 

        ## Somehwere in here the data is not showing up, "data:" prints nothing.
        ## Somehow fixed. wtf.
        ## now getting called multiple times. 
        print("get_all_data")
        #self.signal_get_all_data.connect(self.update_data)

        self.signal_get_all_data.connect(self.update_data)
        # Once we have data, loop call add_client_to_widget, or make it auto loop? not sure.
        # May not have to worry about indexing items as QT will (should) have options for that. 



    def update_client_tree_options(self):
        '''
        Does any updates tot he client tree, such as resizing cells, etc
        '''

        for column in range(self.client_tree.columnCount()):
            self.client_tree.resizeColumnToContents(column)

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
        Temp for printing data
        '''
        #print("PRINTING DATA1====")
        #print(data)

        self.logger.debug(f"{self.__class__.__name__}.{inspect.currentframe().f_code.co_name}: Updating data in self.data.simplec2.db_data, len: {len(data)}")

        ## Updates the db_data in the data singleton
        self.data.simplec2.db_data = data
        #print(self.data.simplec2.db_data)
        #print(f"Data Length: {self.data.simplec2.db_data}")
        #print(f"Data: {data} --")

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