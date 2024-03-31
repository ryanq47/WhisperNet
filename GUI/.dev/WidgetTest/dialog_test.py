from PySide6.QtWidgets import QApplication, QMainWindow, QToolBar
from CustomDialog import CustomDialog  # Make sure this import is correct based on your file structure

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Main Window")
        
        # Setup Toolbar
        self.toolbar = QToolBar("My Toolbar", self)
        self.addToolBar(self.toolbar)
        
        # Add action to the toolbar
        open_dialog_action = self.toolbar.addAction("Open Custom Dialog")
        open_dialog_action.triggered.connect(self.show_custom_dialog)
    
    def show_custom_dialog(self):
        dialog = CustomDialog(self)
        dialog.show()

if __name__ == "__main__":
    app = QApplication([])
    mainWindow = MainWindow()
    mainWindow.show()
    app.exec()
