from PySide6.QtWidgets import QWidget, QMessageBox, QVBoxLayout, QDialog
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import Qt, Signal
from functools import partial
from Utils.EventLoop import Event
from Utils.Data import Data
from Utils.BaseLogging import BaseLogging
import inspect

# For things such as popups
class ListenerPopup(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.logger = BaseLogging.get_logger()

        self.logger.debug(f"{self.__class__.__name__}.{inspect.currentframe().f_code.co_name}: Initializing class {self}")

        loader = QUiLoader()
        #Access Event Loop
        self.event_loop = Event()
        # Access data singleton
        self.data = Data()
        ## This NEEDS self as a second arg for some reason.
        self.ui_file = loader.load('QtComponents/PathOfUi', self)

        self.__ui_load()
        self.__q_timer()
        self.__signal_setup()
        self.init_options()
        self.name = "NAME_HERE"

    def __ui_load(self):
        '''
        Load UI elements
        '''
        if self.ui_file == None:
            errmsg = "UI File could not be loaded"
            QMessageBox.critical(self, "Error", f"{errmsg}: {e}")
            self.logger.error(errmsg)

        try:
            ## Sets layout
            #self.setLayout(self.ui_file.layout())

            #self.c2_systemshell = self.ui_file.findChild(QTextEdit, "test_text")  # Replace "QtWidgets" with the appropriate module
            #self.c2_systemshell.setText("test")

            ## MUST GO LAST!!!
            self.setLayout(self.ui_file.layout())
        except Exception as e:
            QMessageBox.critical(self, "Error", f"An error occurred: {e}")
            print(f"[!] {e}")


    def __q_timer(self):
        '''
        A qtimer/event loop queuer for updating events. 
        '''

        # add to even loop
        #self.event_loop.add_to_event_loop(self.get_listener_data)
        pass

    def __signal_setup(self):
        '''
            Sets up signals for the entire plugin
        '''
        #self.data.simplec2.db_data_updated.connect(self.update_client_widget)
        pass


    def init_options(self):
        '''
        Sets options for the options button (bottom left button with '...')
        '''
        pass

