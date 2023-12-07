from PySide6.QtWidgets import QMainWindow, QMenu, QTabWidget, QVBoxLayout, QPushButton, QWidget, QLabel, QApplication, QGridLayout, QSplitter
from PySide6.QtGui import QAction
from PySide6.QtCore import Qt
import sys
from PySide6.QtUiTools import QUiLoader
from functools import partial
import subprocess
from QtComponents.SimpleC2.simplec2 import Simplec2
from QtComponents.FileHost.filehost import Filehost
from QtComponents.Secrets.secrets import Secrets
from QtComponents.Console.console import Console

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Load the base UI from a file
        self.load_base_ui("QtComponents/Base/base_window.ui")

        # Create two QTabWidget instances
        self.tab_widget_top = QTabWidget()
        self.tab_widget_bottom = QTabWidget()

        # Create a splitter and add the tab widgets to it
        splitter = QSplitter(Qt.Vertical)  # Vertical splitter
        splitter.addWidget(self.tab_widget_top)
        splitter.addWidget(self.tab_widget_bottom)

        # Create a container widget and set the grid layout
        containerWidget = QWidget()
        gridLayout = QGridLayout(containerWidget)
        gridLayout.addWidget(splitter, 0, 0, 1, 1)  # Add the splitter to the layout

        # Set minimum size and window title
        self.setMinimumSize(1000, 600)  # Set minimum size
        self.setWindowTitle('Whisper Net')

        # Set the container widget as the central widget of the QMainWindow
        self.setCentralWidget(containerWidget)

        # Setup default tabs as needed
        self.init_tab_setup()
        self.add_menu_bar()

        # Set Stylesheet
        self.global_set_stylesheet()

    def add_menu_bar(self):
        '''
        Adds a menu bar
        '''
        # Create a menu bar
        menu_bar = self.menuBar()

        # Add menus to the menu bar
        file_menu = menu_bar.addMenu("File")
        #edit_menu = menu_bar.addMenu("Edit")
        view_menu = menu_bar.addMenu("View")

        # Add actions to the menus (example)
        #file_menu.addAction("Open")
        #file_menu.addAction("Save")
        file_menu.addSeparator()

        file_menu_restart = QAction("Restart", self)
        file_menu_restart.triggered.connect(self.restart)
        file_menu.addAction(file_menu_restart)

        file_menu_exit = QAction("Exit", self)
        file_menu_exit.triggered.connect(partial(exit,"Exiting..."))
        file_menu.addAction(file_menu_exit)


        ## Can definently optizime this later/shorten it up.
        #### Upper/Lower menu
        upper_menu = QMenu('Upper', self)
        view_menu.addMenu(upper_menu)

        # Create 'Lower' submenu under 'View'
        lower_menu = QMenu('Lower', self)
        view_menu.addMenu(lower_menu)

        ## Add Upper View options
        view_simplec2 = QAction("SimpleC2", self)
        view_simplec2.triggered.connect(partial(self.add_new_tab, Simplec2(), "upper"))
        upper_menu.addAction(view_simplec2)        

        view_filehost = QAction("FileHost", self)
        view_filehost.triggered.connect(partial(self.add_new_tab, Filehost(), "upper"))
        upper_menu.addAction(view_filehost)

        view_secrets = QAction("Secrets", self)
        view_secrets.triggered.connect(partial(self.add_new_tab, Secrets(), "upper"))
        upper_menu.addAction(view_secrets)   

        view_console = QAction("Console", self)
        view_console.triggered.connect(partial(self.add_new_tab, Console(), "upper"))
        upper_menu.addAction(view_console)  

        ## Add Lower View options
        view_simplec2 = QAction("SimpleC2", self)
        view_simplec2.triggered.connect(partial(self.add_new_tab, Simplec2(), "lower"))
        lower_menu.addAction(view_simplec2)        

        view_filehost = QAction("FileHost", self)
        view_filehost.triggered.connect(partial(self.add_new_tab, Filehost(), "lower"))
        lower_menu.addAction(view_filehost)

        view_secrets = QAction("Secrets", self)
        view_secrets.triggered.connect(partial(self.add_new_tab, Secrets(), "lower"))
        lower_menu.addAction(view_secrets)   

        view_console = QAction("Console", self)
        view_console.triggered.connect(partial(self.add_new_tab, Console(), "lower"))
        lower_menu.addAction(view_console)  

    def init_tab_setup(self):
        '''
        Sets the needed init tabs, and a couple tab settings
        '''
        self.tab_widget_top.setTabsClosable(True)
        self.tab_widget_top.tabCloseRequested.connect(self.close_tab_upper)
        self.tab_widget_bottom.setTabsClosable(True)
        self.tab_widget_bottom.tabCloseRequested.connect(self.close_tab_lower)

        self.add_new_tab(tab_obj=Simplec2(), location="upper")
        self.add_new_tab(tab_obj=Secrets(), location="lower")

    #def load_ui_elements(self):
        #self.lower_tab_widget = self.ui_file.findChild(QTextEdit, "test_text")

    def keyPressEvent(self, event):
        '''
        Sets up key proess events. Not changing method name as I'm not sure if that will break it.
        '''
        if event.key() == Qt.Key_R and event.modifiers() == Qt.ControlModifier:
            print("Ctrl + R pressed")
            self.restart() 

    def load_base_ui(self, ui_file_path):
        """
        Load the base UI from the specified UI file
        """
        loader = QUiLoader()
        base_widget = loader.load(ui_file_path, self)

        if base_widget is None:
            print("Error: UI file not loaded.")
            return

        # Set the loaded UI as the central widget
        self.setCentralWidget(base_widget)

        # Access the tab widget from the loaded UI
        self.tab_widget_top = base_widget.findChild(QTabWidget, 'base_tab_widget')
        if self.tab_widget_top is None:
            print("Error: QTabWidget not found in the UI file.")
            return

    def global_set_stylesheet(self):
        '''
        Sets the global stylesheet for the qt program
        '''
        file_path = "Assets/StyleSheet1-aggro.txt.css"
        try:
            with open(file_path, 'r') as file:
                stylesheet = file.read()
                self.setStyleSheet(stylesheet)
        except FileNotFoundError:
            print(f"Error: '{file_path}' not found.")
        except Exception as e:
            print(f"An error occurred: {e}")

    def add_new_tab(self, tab_obj, location="upper"):
        '''
        Adds a new tab from a widget.
        tab_obj: instance of widget. 
        '''
        if location == "upper":
            try:
                new_tab = tab_obj
                self.tab_widget_top.addTab(new_tab, tab_obj.name)
            except Exception as e:
                print(f"An error occurred: {e}")
        if location == "lower":
            try:
                new_tab = tab_obj
                self.tab_widget_bottom.addTab(new_tab, tab_obj.name)
            except Exception as e:
                print(f"An error occurred: {e}")

        else:
            print("Invalid location for tab")
    
    def close_tab_upper(self, index):
        # Close the tab at the given index
        self.tab_widget_top.removeTab(index)
    def close_tab_lower(self, index):
        # Close the tab at the given index
        self.tab_widget_bottom.removeTab(index)

    def restart(self):
        '''
        Temp/hacky restart of program
        '''
        subprocess.Popen([sys.executable, __file__])
        QApplication.quit()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())