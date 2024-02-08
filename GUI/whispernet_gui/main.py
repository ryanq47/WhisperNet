from PySide6.QtWidgets import QMainWindow, QDockWidget, QMessageBox, QMenu, QTabWidget, QVBoxLayout, QPushButton, QWidget, QLabel, QApplication, QGridLayout, QSplitter
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
from QtComponents.Notes.notes import Notes
from QtComponents.ClientGraphics.clientgraphics import ClientGraphics
from QtComponents.Login.login import Login
from Utils.Data import Data

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Load the base UI from a file
        self.load_base_ui("QtComponents/Base/base_window.ui")

        # Create two QTabWidget instances
        tab_widget_top = QTabWidget()
        tab_widget_bottom = QTabWidget()

        # Create a splitter and add the tab widgets to it
        #splitter = QSplitter(Qt.Vertical)  # Vertical splitter
        #splitter.addWidget(tab_widget_top)
        #splitter.addWidget(tab_widget_bottom)

        # Create dock widgets and add the splitter to it
        dock_widget = QDockWidget("Dockable Panel", self)
        #dock_widget.setWidget(splitter)
        dock_widget.setAllowedAreas(Qt.AllDockWidgetAreas)  # Allow docking anywhere

        # Add the dock widget to the main window
        #self.addDockWidget(Qt.RightDockWidgetArea, dock_widget)  # Add dock widget to the right

        # Set minimum size and window title
        self.setMinimumSize(1000, 600)  # Set minimum size
        self.setWindowTitle('Whisper Net')

        # Setup default tabs as needed
        self.init_window_setup()
        self.add_menu_bar()
        
        #self.setCentralWidget(Simplec2())

        self.init_items()

        # Set Stylesheet
        self.global_set_stylesheet()

    def init_items(self):
        '''
        Inits important stuff 
        '''
        ## Create init singleton
        self.data = Data()

    def add_menu_bar(self):
        '''
        Adds a menu bar
        '''
        # Create a menu bar
        menu_bar = self.menuBar()

        # Add menus to the menu bar
        file_menu = menu_bar.addMenu("File")


        file_menu_login = QAction("Login to Server", self)
        file_menu_login.triggered.connect(partial(self.pop_new_window, Login()))
        file_menu.addAction(file_menu_login)

        #edit_menu = menu_bar.addMenu("Edit")
        layout_menu = menu_bar.addMenu("Layout")

        ## Layout Menu
        layout_menu_init = QAction("init", self)
        layout_menu_init.triggered.connect(self.init_window_setup)
        layout_menu.addAction(layout_menu_init)

        layout_menu_1 = QAction("Layout2", self)
        layout_menu_1.triggered.connect(self.layout_one)
        layout_menu.addAction(layout_menu_1)

        layout_menu_21_9 = QAction("21:9", self)
        layout_menu_21_9.triggered.connect(self.layout_21_9)
        layout_menu.addAction(layout_menu_21_9)

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
        #upper_menu = QMenu('Upper', self)
        #view_menu.addMenu(upper_menu)

        # Create 'Lower' submenu under 'View'
        #lower_menu = QMenu('Lower', self)
        #view_menu.addMenu(lower_menu)

        view_menu = menu_bar.addMenu("View")
        ## Add Upper View options
        view_simplec2 = QAction("SimpleC2", self)
        view_simplec2.triggered.connect(partial(self.pop_new_widget, Simplec2()))
        view_menu.addAction(view_simplec2)        

        view_filehost = QAction("FileHost", self)
        view_filehost.triggered.connect(partial(self.pop_new_widget, Filehost()))
        view_menu.addAction(view_filehost)

        view_secrets = QAction("Secrets", self)
        view_secrets.triggered.connect(partial(self.pop_new_widget, Secrets()))
        view_menu.addAction(view_secrets)   

        view_console = QAction("Console", self)
        view_console.triggered.connect(partial(self.pop_new_widget, Console()))
        view_menu.addAction(view_console) 

    def add_dock_widget(self, title, position, object):
        dock = QDockWidget(title)
        dock.setWidget(object)#WIDGETNAME)
        if position == "left":
            self.addDockWidget(Qt.LeftDockWidgetArea, dock)
        elif position == "right":
            self.addDockWidget(Qt.RightDockWidgetArea, dock)
        elif position == "bottom":
            self.addDockWidget(Qt.BottomDockWidgetArea, dock)
        elif position == "top":
            self.addDockWidget(Qt.TopDockWidgetArea, dock)

    def init_window_setup(self):
        '''
        Sets the needed init windows, and a couple tab settings
        '''

        #return
        '''
        self.tab_widget_top.setTabsClosable(True)
        self.tab_widget_top.tabCloseRequested.connect(self.close_tab_upper)
        self.tab_widget_bottom.setTabsClosable(True)
        self.tab_widget_bottom.tabCloseRequested.connect(self.close_tab_lower)

        self.add_new_tab(tab_obj=Simplec2(), location="upper")
        self.add_new_tab(tab_obj=Secrets(), location="lower")'''
        
        ## Here so wehn the user clicks init, it wipes the layout. might spit a warning on startup
        self.clear_dock_widgets()

        self.add_dock_widget(Console().name, "bottom", Console())
        self.add_dock_widget(Console().name, "top", Simplec2())

        #self.add_dock_widget("Assets", "left", Secrets())
        #self.add_dock_widget("Assets", "right", Secrets())

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

    def pop_new_widget(self, object_instance):
        """ Slot to pop up a new widget """
        new_dock_widget = QDockWidget(object_instance.name, self)
        new_object = object_instance  # Example widget, you can replace with your desired widget
        new_dock_widget.setWidget(new_object)
        new_dock_widget.setAllowedAreas(Qt.AllDockWidgetAreas)
        self.addDockWidget(Qt.RightDockWidgetArea, new_dock_widget)

        # Optionally, you can set features like closable, movable, floatable, etc.
        new_dock_widget.setFeatures(QDockWidget.DockWidgetMovable | QDockWidget.DockWidgetClosable)

    def pop_new_window(self, object_instance):
        """ Slot to pop up a new window with the given widget """
        new_window = QMainWindow(self)  # Create a new QMainWindow instance
        new_object = object_instance  # Example widget, replace with your desired widget

        new_window.setCentralWidget(new_object)  # Set the central widget of the new window
        new_window.setAttribute(Qt.WA_DeleteOnClose)  # Ensure the window is deleted when closed

        # Optionally, set window title, size, or other properties here
        new_window.setWindowTitle(object_instance.name)

        new_window.show() 

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

    def show_test_message(self):
        '''
        A test popup box for debugging/etc
        '''
        msg = QMessageBox()
        msg.setWindowTitle("Test Message")
        msg.setText("This is a test popup message.")
        msg.setIcon(QMessageBox.Information)
        msg.exec_()

    def layout_one(self):
        self.clear_dock_widgets()

    def clear_dock_widgets(self):
        """ Remove all dock widgets and rearrange them """
        # Remove all existing dock widgets
        for dock_widget in self.findChildren(QDockWidget):
            self.removeDockWidget(dock_widget)
            dock_widget.deleteLater()

    ## MOve me to file

    def layout_21_9(self):
        '''
        21:9 layout

        Limitation: Have to do in a qsplitter :(. QDockWidget does not support any resizing.
        '''
        self.clear_dock_widgets()

        # Bottom area with consoles
        bottom_splitter = QSplitter(Qt.Horizontal)
        for _ in range(3):  # Assuming 4 consoles in the bottom area
            console = Console()  # Create a new instance for each console
            bottom_splitter.addWidget(console)

        bottom_splitter.addWidget(Notes())

        bottom_dock = QDockWidget("Bottom Dock", self)
        bottom_dock.setWidget(bottom_splitter)
        self.addDockWidget(Qt.BottomDockWidgetArea, bottom_dock)



        # Top area with different widgets
        top_splitter = QSplitter(Qt.Horizontal)
        top_splitter.addWidget(Simplec2())
        top_splitter.addWidget(ClientGraphics())

        top_dock = QDockWidget("Top Dock", self)
        top_dock.setWidget(top_splitter)
        self.addDockWidget(Qt.TopDockWidgetArea, top_dock)

        total_width = self.width()

        # Set the sizes of the splitter widgets to distribute space equally
        bottom_splitter.setSizes([100]*4)  # Equally distribute space among 4 widgets
        top_splitter.setSizes([total_width//2, total_width//2])


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())