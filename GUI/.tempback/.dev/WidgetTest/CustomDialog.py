from PySide6.QtWidgets import QDialog
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile, QIODevice

class CustomDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.load_ui()

    def load_ui(self):
        loader = QUiLoader()
        ui_file = QFile("./add_network_popup.ui")
        ui_file.open(QIODevice.ReadOnly)

        # Load the UI
        self.ui = loader.load(ui_file, self)
        ui_file.close()

        # After loading you can connect signals to slots
        # For example: self.ui.someButton.clicked.connect(self.some_method)
