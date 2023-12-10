from PySide6.QtWidgets import QWidget, QTextEdit, QMessageBox
from PySide6.QtUiTools import QUiLoader

class Console(QWidget):
    def __init__(self, id=None):
        super().__init__()
        
        loader = QUiLoader()
        ## This NEEDS self as a second arg for some reason.
        self.ui_file = loader.load('QtComponents/Console/console.ui', self)
        self.id = id
        self.name = "Console"
        self.__ui_load()
        self.init_console()

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

            self.console_shell = self.ui_file.findChild(QTextEdit, "console_shell")  # Replace "QtWidgets" with the appropriate module
            #self.c2_systemshell.setText("test")

            ## MUST GO LAST!!!
            self.setLayout(self.ui_file.layout())

        except Exception as e:
            QMessageBox.critical(self, "Error", f"An error occurred: {e}")
            print(f"[!] {e}")

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

    def init_console(self):
        '''
        Sets up the console with stuff
        '''
        if self.id == None:
            self.console_shell.setText("ID not provided. Cannot init console")
            return

        ## Test Connect to server
        self.connect_to_server()

    
    def connect_to_server(self):
        '''
        Connects to server console API stuff. Basically checks to make sure the correct
        console item is reachable.

        POSTS
        {
            "id":id,
            "user":""

        }
        '''
        # Send msg to server

        ## Wait on response

        # if ok:
        #temp
        client_id = "client_id123"

        ## If all is good:
        self.console_shell.setText(f"Connection to server successful. Channel to {client_id} is open!")

        #else:
        #self.console_shell.setText(f"Error <details>!")
