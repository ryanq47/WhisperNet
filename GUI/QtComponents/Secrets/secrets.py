from PySide6.QtWidgets import QWidget, QMessageBox, QTableWidget, QHeaderView
from PySide6.QtUiTools import QUiLoader

class Secrets(QWidget):
    def __init__(self):
        super().__init__()
        
        loader = QUiLoader()
        ## This NEEDS self as a second arg for some reason.
        self.ui_file = loader.load('QtComponents/Secrets/secrets.ui', self)

        self.__ui_load()
        self.layout_settings()
        self.name = "Secrets"

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
            self.setLayout(self.ui_file.layout())

            self.secrets_table = self.ui_file.findChild(QTableWidget, "secrets_table_widget")
            #if self.secrets_table == None:
            #    print("No secrets table found")

            #self.c2_systemshell = self.ui_file.findChild(QTextEdit, "test_text")  # Replace "QtWidgets" with the appropriate module
            #self.c2_systemshell.setText("test")

        except Exception as e:
            QMessageBox.critical(self, "Error", f"An error occurred: {e}")
            print(f"[!] {e}")

    def layout_settings(self):
        '''
        Layout settings if needed
        '''
        ## Makes top labels stretch accross the screen
        pass
        #self.secrets_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

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
