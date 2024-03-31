from PySide6.QtWidgets import QApplication, QMainWindow, QToolBar
from PySide6.QtGui import QIcon, QAction
from PySide6.QtCore import Qt
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set the window title
        self.setWindowTitle("PySide6 Toolbar Example")

        # Create a toolbar and add it to the QMainWindow
        self.toolbar = self.addToolBar("Main Toolbar")

        # Create an action with an icon and text (assuming you have an icon.png, otherwise leave it empty)
        action = QAction(QIcon("path/to/your/icon.png"), "My Action", self)

        # Connect the action to a function
        action.triggered.connect(self.action_clicked)

        # Add the action to the toolbar
        self.toolbar.addAction(action)

    def action_clicked(self):
        print("Action clicked!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
