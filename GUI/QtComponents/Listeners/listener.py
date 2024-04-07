import inspect
import json
from PySide6.QtWidgets import QWidget, QMessageBox, QMenu, QMainWindow, QToolButton, QVBoxLayout, QPushButton, QTreeView
from PySide6.QtGui import QIcon, QAction, QStandardItemModel, QStandardItem, QBrush, QColor, QCursor
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
        self.name = "Listeners"


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
            self.listener_tree_view = self.ui_file.findChild(QTreeView, "listener_tree_view")
            self.listener_tree_view_model = QStandardItemModel()
            self.listener_tree_view.setModel(self.listener_tree_view_model)
            # Set header labels if necessary
            self.listener_tree_view_model.setHorizontalHeaderLabels(['Name', 'Address', 'Port', 'Type'])


            self.listener_option_button = self.ui_file.findChild(QToolButton, "listener_options_button")
            self.listener_option_button.setText("Options")
            
            ## GOES LAST
            # Wrap the loaded UI in a container widget
            #container = QWidget()
            self.setLayout(self.ui_file.layout())

            # Create a new layout for self to include both the container and the toolbar
            #layout = QVBoxLayout(self)
            #layout.addWidget(container)  # Add the UI container as the main content
            #self.setLayout(layout)
            #self.main_container = container  # Keep a reference if needed

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
        #self.add_toolbar()

        # Add buttons to options button
        
        menu = QMenu(self)

        # Add actions to the menu
        add_host = QAction("Add Listener", self)

        menu.addAction(add_host)

        # Connect actions to functions
        #add_host.triggered.connect(lambda _add_host: self.info_bar.setText("add_host"))
        add_host.triggered.connect(lambda: GuiUtils.open_dialog(ListenerPopup, self))

        self.listener_option_button.setMenu(menu)
        self.listener_option_button.setPopupMode(QToolButton.InstantPopup)


    '''    def add_toolbar(self):
        """
        Adds a toolbar to the widget at the bottom, considering the UI is loaded from a file.
        """
        toolbar = QToolBar("Tools", self)
        new_listener = toolbar.addAction("New Listener")
        # Assuming GuiUtils.open_dialog is correctly implemented
        new_listener.triggered.connect(lambda: GuiUtils.open_dialog(ListenerPopup, self))

        # Ensure the layout is a QVBoxLayout; otherwise, adjust your layout accordingly.
        if not isinstance(self.layout(), QVBoxLayout):
            print("The current layout is not a QVBoxLayout. Adjusting...")
            new_layout = QVBoxLayout(self)
            new_layout.addLayout(self.layout())  # Move the current layout into the new QVBoxLayout

        # Insert the toolbar at the bottom of the QVBoxLayout
        self.layout().addWidget(toolbar)
    '''


    def get_listener_data(self):
        '''
        Gets all the simplec2 data from the server
        '''
        self.logger.info(f"{self.__class__.__name__}.{inspect.currentframe().f_code.co_name}: Getting data from server")

        self.request_manager = WebRequestManager()
        self.request_manager.request_finished.connect(self.update_listener_tree_view_widget) # or whatever func you want to send data to
        self.request_manager.send_request("http://127.0.0.1:5000/api/simplec2/listener")

    def update_listener_tree_view_widget(self, data):
        '''
        Updates the listener tree view with the given data.
        This includes adding new items, and removing items that are no longer present.
        The "name" key is used as a unique identifier.
        '''

        # Remember existing items to avoid duplicates
        existing_items = {}
        for row in range(self.listener_tree_view_model.rowCount()):
            item = self.listener_tree_view_model.item(row, 0)  # Column 0 for names
            if item:
                existing_items[item.text()] = row

        new_data_identifiers = set(data["data"].keys())

        # Identify which identifiers have been removed
        identifiers_to_remove = set(existing_items.keys()) - new_data_identifiers

        # Remove entries that are no longer present
        for identifier in identifiers_to_remove:
            row = existing_items[identifier]
            self.listener_tree_view_model.removeRow(row)

        # Add or update new entries
        for name, details in data["data"].items():
            if name in identifiers_to_remove or name not in existing_items:
                # Creating new entries as rows
                entries = [
                    QStandardItem(name),
                    QStandardItem(details['bind_address']),
                    QStandardItem(details['bind_port']),
                    QStandardItem(details['type'])
                ]
                self.listener_tree_view_model.appendRow(entries)
 

    def print_data(self, data):
        '''
        Temp for printing data, meant to bea debug method
        '''
        self.logger.debug(f"Printing Data:")
        print(data)

## Context Menus
        
    def show_context_menu(self, position):
        # Create the context menu
        context_menu = QMenu(self)
        edit_action = QAction("Edit", self)
        delete_action = QAction("Delete", self)
        
        # Add actions to the context menu
        #context_menu.addAction(edit_action)
        #context_menu.addAction(delete_action)
        
        # Connect actions to slots
        #edit_action.triggered.connect(self.edit_item)
        #delete_action.triggered.connect(self.delete_item)
        
        # Display the context menu at the requested position
        context_menu.exec(self.listener_tree_view.viewport().mapToGlobal(position))
        #context_menu.exec(QCursor.pos())
