from PySide6.QtWidgets import QWidget, QTextEdit, QMessageBox, QTreeWidgetItem, QTreeWidget, QPushButton, QMenu
from PySide6.QtGui import QIcon
from PySide6.QtUiTools import QUiLoader
from PySide6.QtNetwork import QNetworkReply
from PySide6.QtCore import Qt, Signal
from functools import partial
from Utils.QtWebRequestManager import WebRequestManager
import json

class Simplec2(QWidget):
    signal_get_client_data= Signal(str)
    def __init__(self):
        super().__init__()
        
        loader = QUiLoader()
        ## This NEEDS self as a second arg for some reason.
        self.ui_file = loader.load('QtComponents/SimpleC2/c2_layout_widgets.ui', self)

        self.__ui_load()
        self.name = "SimpleC2"


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
            
            self.add_client = self.ui_file.findChild(QPushButton, "add_client")
            self.refresh_manually = self.ui_file.findChild(QPushButton, "refresh_manually")


            # temp
            data_dict = None
            self.add_client.clicked.connect(partial(self.add_client_to_widget,data_dict))

            self.refresh_manually.clicked.connect(partial(self.get_client_data))


            ## MUST GO LAST!!!
            self.setLayout(self.ui_file.layout())
        except Exception as e:
            QMessageBox.critical(self, "Error", f"An error occurred: {e}")
            print(f"[!] {e}")

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
            action1.triggered.connect(lambda: self.action1_triggered(item))
            action2.triggered.connect(lambda: self.action2_triggered(item))

            # Display the menu
            menu.exec(event.globalPos())

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

    def add_client_to_widget(self, json_data = None):
        '''
        Adds a host to the GUI widget/window
        
        json_data will hold data needed to populate the entry (eventually)
        json_data: A json dict. Gets turned into a pyobject
        '''
        #print(data_dict)

        ## Flip to obj
        data_dict = json.loads(json_data)
        
        if data_dict == None:
            data_dict = {
                "client":"ERROR",
                "ip":"",
                "port":"",
                "listener":"",
                "sleep":"",
                "username":"",
                "client_type":""
            }

        #print(data_dict)

        for data in data_dict:
            print(data)
            #print("data_dict:", data_dict, "type:", type(data_dict))
            ## Main entry
            client_entry = QTreeWidgetItem([data["client"], data["ip"], 
                                            data["port"], data["listener"], 
                                            data["sleep"]])
            
            client_entry.setIcon(0, QIcon("Assets/client.png"))
            self.client_tree.addTopLevelItem(client_entry)

            ## Sub Items
            #                         parent,        stuff         stuff
            username_subitem = QTreeWidgetItem(client_entry, ["User:", data["username"]])
            clienttype_subitem = QTreeWidgetItem(client_entry, ["Client Type:", data["client_type"]])

            #subItem.setIcon(0, QIcon("path/to/icon.png"))#if you want an icon
            # Check CSS for more icon stuff, under : /*QTree Item thingy*/
            ## force expanded
            #client_entry.setExpanded(True)
        
        self.update_client_tree_options()

    def get_client_data(self):
        '''
        Communicates with server to get client data. 

        Eventually will be run in a qtimer loop thingymabober
        '''
        ## have to use this for async communication/to fit QT
        self.request_manager = WebRequestManager()

        #post request for now. Subject to chagne
        self.request_manager.send_get_request(
            url = "https://67ea750d-d74e-490d-ac09-0167215b8b23.mock.pstmn.io/simplec2/clients",
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