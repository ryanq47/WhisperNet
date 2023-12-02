from PySide6.QtWidgets import QWidget
from PySide6.QtUiTools import QUiLoader

class CLASSNAME(QWidget):
    def __init__(self):
        super().__init__()
        
        loader = QUiLoader()
        self.ui_file = loader.load('WhisperNetGui.ui')

    def __ui_load(self):
        '''
        Load UI elements
        '''
        try:

            self.FileHost_TextBox = self.ui_file.findChild("(widegtname)QTextBrowser", "(id name)FileHost_TextBox")  # Replace "QtWidgets" with the appropriate module
        except Exception as e:
            print(f"[!] {e}")

    def func_name(self):
        '''
        func
        '''
        ...
        ##self.uielement.setText("test")
