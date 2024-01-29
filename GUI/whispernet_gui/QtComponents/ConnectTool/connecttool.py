from PySide6.QtWidgets import QWidget, QTextEdit, QMessageBox
from PySide6.QtUiTools import QUiLoader

class ConnectTool(QWidget):
    def __init__(self, username=None, password=None, target=None, port=None):
        super().__init__()
        
        loader = QUiLoader()
        ## This NEEDS self as a second arg for some reason.
        self.ui_file = loader.load('QtComponents/ConnectTool/connecttool.ui', self)

        self.username = username
        self.password = password
        self.port = port
        self.target = target

        self.__ui_load()
        self.global_set_stylesheet()
        self.set_gui_values()
        self.name = "ConnectTool"

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
            pass

            self.username_box = self.ui_file.findChild(QTextEdit, "user_box")
            self.password_box = self.ui_file.findChild(QTextEdit, "password_box")
            self.port_box = self.ui_file.findChild(QTextEdit, "port_box")
            self.target_box = self.ui_file.findChild(QTextEdit, "target_box")

            #self.c2_systemshell = self.ui_file.findChild(QTextEdit, "test_text")  # Replace "QtWidgets" with the appropriate module
            #self.c2_systemshell.setText("test")

            ## MUST GO LAST!!!
            self.setLayout(self.ui_file.layout())
        except Exception as e:
            QMessageBox.critical(self, "Error", f"An error occurred: {e}")
            print(f"[!] {e}")

    def global_set_stylesheet(self):
        '''
        Have to set stylesheet here as it opens in a new window, and does not apply the other one
        '''

        file_path = "StyleSheet1-aggro.txt.css"
        try:
            with open(file_path, 'r') as file:
                stylesheet = file.read()
                self.setStyleSheet(stylesheet)
        except FileNotFoundError:
            print(f"Error: '{file_path}' not found.")
        except Exception as e:
            print(f"An error occurred: {e}")

    def set_gui_values(self):
        '''
        Fills in the values in the gui
        
        '''

        if self.username != None:
            self.username_box.setText(self.username)

        if self.password != None:
            self.password_box.setText(self.password)

        if self.target != None:
            self.target_box.setText(self.target)

        if self.port != None:
            self.port_box.setText(self.port)

    def show_test_message(self):
        '''
        A test popup box for debugging/etc
        '''
        msg = QMessageBox()
        msg.setWindowTitle("Test Message")
        msg.setText("This is a test popup message.")
        msg.setIcon(QMessageBox.Information)
        msg.exec_()
