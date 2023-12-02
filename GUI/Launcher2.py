from PySide6.QtWidgets import QMainWindow, QTabWidget, QVBoxLayout, QPushButton, QWidget, QLabel, QApplication
import sys
from QtComponents.SimpleC2.simplec2 import simplec2
from PySide6.QtUiTools import QUiLoader


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Load the base UI from a file
        self.load_base_ui("QtComponents/Base/base_window.ui")
        self.tab_widget = QTabWidget()

        # Set the QTabWidget as the central widget of the QMainWindow
        self.setCentralWidget(self.tab_widget)

        ## Setup default tabs as needed
        self.init_tab_setup()
        self.add_menu_bar()

        ## Set Stylesheet
        self.global_set_stylesheet()

    def add_menu_bar(self):
        '''
        Adds a menu bar
        '''
        # Create a menu bar
        menu_bar = self.menuBar()

        # Add menus to the menu bar
        file_menu = menu_bar.addMenu("File")
        edit_menu = menu_bar.addMenu("Edit")
        view_menu = menu_bar.addMenu("View")

        # Add actions to the menus (example)
        file_menu.addAction("Open")
        file_menu.addAction("Save")
        file_menu.addSeparator()
        file_menu.addAction("Exit")

    def init_tab_setup(self):
        '''
        Sets the needed init tabs, and a couple tab settings
        '''
        self.tab_widget.setTabsClosable(True)
        self.tab_widget.tabCloseRequested.connect(self.close_tab)

        self.add_new_tab(tab_obj=simplec2())

    def load_base_ui(self, ui_file_path):
        """
        Load the base UI from the specified UI file.
        """
        loader = QUiLoader()
        base_widget = loader.load(ui_file_path, self)

        if base_widget is None:
            print("Error: UI file not loaded.")
            return

        # Set the loaded UI as the central widget
        self.setCentralWidget(base_widget)

        # Access the tab widget from the loaded UI
        self.tab_widget = base_widget.findChild(QTabWidget, 'base_tab_widget')
        if self.tab_widget is None:
            print("Error: QTabWidget not found in the UI file.")
            return

    def global_set_stylesheet(self):
        '''
        Sets the global stylesheet for the qt program
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

    def add_new_tab(self, tab_obj):
        '''
        Adds a new tab from a widget.
        tab_obj: instance of widget. 
        '''
        try:
            new_tab = tab_obj
            self.tab_widget.addTab(new_tab, tab_obj.name)
        except Exception as e:
            print(f"An error occurred: {e}")
    

    def close_tab(self, index):
        # Close the tab at the given index
        self.tab_widget.removeTab(index)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())