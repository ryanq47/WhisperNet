from PySide6.QtWidgets import QWidget, QTextEdit, QMessageBox, QTreeWidgetItem, QTreeView, QPushButton, QMenu, QToolButton
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
        self.__signal_setup()
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

            ## Setting up View + Model.
            self.client_tree = self.ui_file.findChild(QTreeView, "client_tree_widget")
            self.client_tree_model = QStandardItemModel()
            self.client_tree_model.setHorizontalHeaderLabels(['Network Name', 'CIDR', 'Other'])
            self.client_tree.setModel(self.client_tree_model)
            #self.client_tree.setHorizontalHeaderLabels(['IP', 'OS', 'Check-in'])
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

    def __signal_setup(self):
        '''
            Sets up signals for the entire plugin
        '''
        self.data.simplec2.client_data_updated.connect(self.update_client_widget)

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

        # in RGB(a)
        self.host_label_row_color = QColor(99,102,106)


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
        self.data.simplec2.parse_data_for_gui()

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

    '''
    def update_client_widget(self, data_dict):
        #
            #Parses & Updates the client data.

           # data: The dict data to update

            #Triggers off of a signal. 
        
        #
        # data showung up as blank...great. Fixed it, signal was a str not a list duuuh...

        self.logger.debug(f"{self.__class__.__name__}.{inspect.currentframe().f_code.co_name}: Updating Client Widget")

        #print(data_dict)



        for item in data_dict:
            print(item["labels"])
            if "Network" in item["labels"]:
                print(item)
                # Create the item
                category_item = QStandardItem(item["properties"]["nickname"])#client["properties"]["nickname"])

                name = QStandardItem(item["properties"]["nickname"]) #QStandardItem("test")#"test"#QStandardItem(client["properties"]["nickname"])
                cidr = QStandardItem(item["properties"]["cidr"]) #QStandardItem("test")#"ip"#QStandardItem(client["properties"]["ip"])

                category_item.appendRow([name, cidr])

                self.client_tree_model.appendRow(category_item)
            else:
                print("not A Network")
        #print("post")

        # works, to figure out:
                # how to add hosts to networks with the above, maybe split into a func to add a host to a net, takes net as an arg?
                # How to NOT duplicate the data, and have it update without overwriting the current user mouse (ex if selected, don't unselect)
    '''

    ########################################
    # C2 Client Tree Model
    ########################################

    ## NOTE! Due to the "label" row, everythign might need to be +1 when indexing/accessing data and context menus. 

    ## LOG THESE THINGS

    ## works as excpeted, maybe move to a class or sepearte file for the helper functions
    def update_client_widget(self, data_dict):
        '''
        Parses & Updates the client data based on the updated structure.
        '''
        self.logger.debug(f"{self.__class__.__name__}.{inspect.currentframe().f_code.co_name}: Updating Client Widget")

        # First, update or add networks and clients
        for item in data_dict:
            ## Check to make sure the item is a network item otherwise the cidr key doesn't exist. 
            if "Network" in item["labels"]:
                self.add_or_update_network(item)
                
        # Then, remove networks that are no longer present
        self.remove_stale_networks(data_dict)

    def add_or_update_network(self, network_data):
        '''
        Adds a new network item or updates an existing one.
        ##Also manages client items as children of the network, including a label row for clients. NAAAAh that's changing slightly
        '''
        self.logger.debug(f"{self.__class__.__name__}.{inspect.currentframe().f_code.co_name}: Attempting to add/update network")

        network_name = network_data["properties"]["nickname"]
        network_cidr = network_data["properties"]["cidr"]
        # using network name alone is fine as nickname is constrained to be unique in the db
        network_id = f"{network_name}"

        self.logger.debug(f"{self.__class__.__name__}.{inspect.currentframe().f_code.co_name}: Network Name: '{network_name}' Network CIDR: '{network_cidr}' Network Id: '{network_id}'")

        # Unique identifier for the network, assuming name + CIDR is unique
        #network_id = f"{network_name}_[{cidr}]"

        ## Something broke with first row

            #network_item.appendRow(label_items) (line 377)
            #AttributeError: 'list' object has no attribute 'appendRow'

        # Find if this network already exists, just searches for it
        network_item = None
        for row in range(self.client_tree_model.rowCount()):
            item = self.client_tree_model.item(row)
            if item and item.text() == network_id:
                network_item = item
                break

        if network_item is None:
            self.logger.debug(f"{self.__class__.__name__}.{inspect.currentframe().f_code.co_name}: Network '{network_name}' does not exist, creating")

            # Network does not exist, so create it
            ## okay, gotta make each data point into a QStandardItem, THEN turn them both into a list & append to the model

            network_item = QStandardItem(network_id)  # This is the main item for the network
            cidr_item = QStandardItem(network_cidr)  # Additional detail for the network

            # Append the network and CIDR as part of the same row
            self.client_tree_model.appendRow([network_item, cidr_item])

            # Add a label row directly under the new network
            self.add_label_row(network_item)

        # Example client data to add, replace with actual client handling logic
            
        ## needs to change/get all cliens with the current net name, and loop/add them as children
            '''
            for child in child_data.whatevermehtod():
                name = baby
                row.appendChild(name) #or something
            
            '''

        self.logger.debug(f"{self.__class__.__name__}.{inspect.currentframe().f_code.co_name}: Adding client data to network")
        client_data = {"name": "testclient"}
        self.add_client_to_network(network_item, client_data)

    def add_label_row(self, network_item):
        '''
        Adds a label row under the specified network item, used ONLY for the first row under a network
        '''
        self.logger.debug(f"{self.__class__.__name__}.{inspect.currentframe().f_code.co_name}: Adding label row to first row in parent '{network_item.text()}'")

        # Define the labels for the columns under this network
        labels = ["IP", "Name", "Last Check-in"]
        label_items = [QStandardItem(label) for label in labels]

        # Set background color for each label item
        color = QBrush(self.host_label_row_color)  # Light gray color; adjust as needed
        for item in label_items:
            item.setBackground(color)

        # Append an empty item at the start if your network label row needs to be indented
        network_item.appendRow(label_items)

    def add_client_to_network(self, network_item, client_data):
        '''
        Adds a client as a child to the specified network item.
        '''
        # Assuming client_data is a dictionary with at least a 'name' key
        # You might want to expand this with real client data handling
        client_items = [QStandardItem(client_data.get("IP", "")), 
                        QStandardItem(client_data.get("name", "")), 
                        QStandardItem(client_data.get("Last Check-in", ""))]
        network_item.appendRow(client_items)

    def directly_add_client_to_network(self, network_name, client_data):
        '''
            For if you want to directly add a client to a network. Untested
        '''
        # Assuming network_name is the unique identifier for the network
        network_id = f"{network_name} [{client_data['cidr']}]"
            
        found_network_item = None
        for row in range(self.client_tree_model.rowCount()):
            item = self.client_tree_model.item(row)
            if item.text() == network_id:
                found_network_item = item
                break
            
        if found_network_item:
            self.add_client_to_network(found_network_item, client_data)
        else:
            print("Network not found, cannot add client.")

    def remove_stale_networks(self, data_dict):
        '''
        Removes networks that are no longer present in the incoming data_dict.
        '''
        self.logger.debug(f"{self.__class__.__name__}.{inspect.currentframe().f_code.co_name}: Checking for any stale networks")

        current_network_names = {f"{item['properties']['nickname']}" for item in data_dict if "Network" in item["labels"]}
        items_to_remove = []

        for row in range(self.client_tree_model.rowCount()):
            item = self.client_tree_model.item(row)
            if item.text() not in current_network_names:
                #print("item.text")
                #print(item.text()) # Network2 
                #print("current_network_names")
                #print(current_network_names) # {'Network2', 'Network1'}
                items_to_remove.append(row)
                self.logger.debug(f"{self.__class__.__name__}.{inspect.currentframe().f_code.co_name}: Queuing '{item.text()}' in row '{row}' to be removed")


        # Reverse removal to avoid index shifting issues
        for row in reversed(items_to_remove):
            self.logger.debug(f"{self.__class__.__name__}.{inspect.currentframe().f_code.co_name}: Removing stale network rows")
            self.client_tree_model.removeRow(row)