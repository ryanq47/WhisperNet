from PySide6.QtWidgets import QWidget, QTextEdit, QMessageBox
from PySide6.QtUiTools import QUiLoader

class simplec2(QWidget):
    def __init__(self):
        super().__init__()
        
        loader = QUiLoader()
        ## This NEEDS self as a second arg for some reason.
        self.ui_file = loader.load('c2_main_ui.ui', self)

        self.__ui_load()
        self.name = "TEMPNAME"

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

            #self.c2_systemshell = self.ui_file.findChild(QTextEdit, "test_text")  # Replace "QtWidgets" with the appropriate module
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
