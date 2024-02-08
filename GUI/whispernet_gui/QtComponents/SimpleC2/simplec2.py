from PySide6.QtWidgets import QWidget, QTextEdit, QMessageBox, QTreeWidgetItem, QTreeWidget, QPushButton, QMenu, QToolButton
from PySide6.QtGui import QIcon, QAction
from PySide6.QtUiTools import QUiLoader
from PySide6.QtNetwork import QNetworkReply
from PySide6.QtCore import Qt, Signal, QTimer
from functools import partial
from Utils.QtWebRequestManager import WebRequestManager
from Utils.EventLoop import Event
import json

class Simplec2(QWidget):
    signal_get_client_data= Signal(str)
    def __init__(self):
        super().__init__()
        
        loader = QUiLoader()
        self.event_loop = Event()
        ## This NEEDS self as a second arg for some reason.
        self.ui_file = loader.load('QtComponents/SimpleC2/c2_layout_widgets.ui', self)

        self.__ui_load()
        self.__q_timer()
        self.init_options()
        self.name = "SimpleC2"
        self.client_items = {}


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
        self.event_loop.add_to_event_loop(self.get_client_data)


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

    def show_test_message(self):
        '''
        A test popup box for debugging/etc
        '''
        msg = QMessageBox()
        msg.setWindowTitle("Test Message")
        msg.setText("This is a test popup message.")
        msg.setIcon(QMessageBox.Information)
        msg.exec_()

    def add_client_to_widget(self, json_data=None):
        '''
        Adds a host to the GUI widget/window

        '''
        try:
            data_dict = json.loads(json_data) if json_data else []
        except Exception as e:
            print(f"Error with JSON data: {e}")
            return

        # Dictionary to keep track of existing clients
          # Reset or initialize this appropriately

        for data in data_dict:
            client_name = data["client"]
            if client_name in self.client_items:
                #print("UPDATE")
                # Update existing client
                self.update_client_row(client_name, data)
            else:
                # Add new client
                #print("NEWROW")
                self.add_client_row(data)

    def add_client_row(self, data):
        client_entry = QTreeWidgetItem([data["client"], data["ip"], data["port"], data["listener"], data["sleep"]])
        client_entry.setIcon(0, QIcon("Assets/client.png"))
        self.client_tree.addTopLevelItem(client_entry)
        
        # Sub items
        username_subitem = QTreeWidgetItem(client_entry, ["User:", data["username"]])
        clienttype_subitem = QTreeWidgetItem(client_entry, ["Client Type:", data["client_type"]])

        # Add to the reference dictionary
        self.client_items[data["client"]] = client_entry

    def update_client_row(self, client_name, data):
        # Retrieve the existing item
        client_entry = self.client_items[client_name]

        # Update the relevant data
        client_entry.setText(0, data["client"])
        client_entry.setText(1, data["ip"])
        client_entry.setText(2, data["port"])
        client_entry.setText(3, data["listener"])
        client_entry.setText(4, data["sleep"])

        # Assuming you have the subitems as children of the client_entry,
        # update them as well
        client_entry.child(0).setText(1, data["username"])  # Update username subitem
        client_entry.child(1).setText(1, data["client_type"])

    def clear_client_widget(self):
        '''
        Clears ALL items fromthe client widget. A bit extreme and only temp
        '''
        self.client_tree.clear()

    def get_client_data(self):
        '''
        Communicates with server to get client data. 

        Eventually will be run in a qtimer loop thingymabober
        '''
        ## have to use this for async communication/to fit QT
        self.request_manager = WebRequestManager()

        #post request for now. Subject to chagne
        self.request_manager.send_get_request(
            url = "http://127.0.0.1:5000/api/simplec2/clients",
            #data = ""
        )

        self.request_manager.request_finished.connect(
            ##  send request                                      ## Signal that holds data
            lambda response: self.handle_response(response, self.signal_get_client_data)
        )## I don't fully remeber why we have to pass response to the function as well. 

        # when signal is triggerd, called add_client_to_widget
        self.signal_get_client_data.connect(self.add_client_to_widget)
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