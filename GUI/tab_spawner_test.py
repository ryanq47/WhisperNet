from PySide6.QtWidgets import QMainWindow, QTabWidget, QVBoxLayout, QPushButton, QWidget, QLabel, QApplication
import sys
from QtComponents.SimpleC2.simplec2 import simplec2

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Tab widget
        self.tab_widget = QTabWidget()
        
        # Button to add new tab
        self.addButton = QPushButton("Add Tab")
        #self.addButton.clicked.connect(self.add_new_tab)
        self.addButton.clicked.connect(self.custom_add_new_tab)

        # Main layout
        self.mainWidget = QWidget()
        self.mainLayout = QVBoxLayout(self.mainWidget)
        self.mainLayout.addWidget(self.addButton)
        self.mainLayout.addWidget(self.tab_widget)

        # Set central widget
        self.setCentralWidget(self.mainWidget)

    def add_new_tab(self):
        # Create a new QWidget for the tab
        new_tab = QWidget()
        new_tab_layout = QVBoxLayout(new_tab)

        # Add some content to the new tab
        new_tab_label = QLabel("This is a new tab")
        new_tab_layout.addWidget(new_tab_label)

        # Add the new tab to the tab widget
        self.tab_widget.addTab(new_tab, "New Tab")

    def custom_add_new_tab(self):
        new_tab = simplec2()  # Your custom widget
        self.tab_widget.addTab(new_tab, "New Tab")
        ## Need to add widget to tab


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
