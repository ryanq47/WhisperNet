from PySide6.QtWidgets import QWidget, QTextEdit, QMessageBox, QTreeWidgetItem, QTreeWidget, QPushButton, QMenu
from PySide6.QtGui import QIcon
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import Qt

class Simplec2(QWidget):
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
            self.add_client.clicked.connect(self.add_client_to_widget)

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

    def add_client_to_widget(self, data_dict = None):
        '''
        Adds a host to the GUI widget/window
        
        data_dict will hold data needed to populate the entry (eventually)
        '''
        ## Main entry
        client_entry = QTreeWidgetItem(["Item 1", "This is item 1"])
        client_entry.setIcon(0, QIcon("Assets/client.png"))
        self.client_tree.addTopLevelItem(client_entry)

        ## Sub Items
        #                         parent,        stuff         stuff
        subItem = QTreeWidgetItem(client_entry, ["Subitem 1", "This is subitem 1"])
        #subItem.setIcon(0, QIcon("path/to/icon.png"))#if you want an icon
        # Check CSS for more icon stuff, under : /*QTree Item thingy*/
        ## force expanded
        #client_entry.setExpanded(True)
