# main.py
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from settings_panel import SettingsPanel

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PySide6 App Structure Example")

        # Main widget and layout
        self.mainWidget = QWidget()
        self.mainLayout = QVBoxLayout()
        self.mainWidget.setLayout(self.mainLayout)

        # Settings panel
        self.settingsPanel = SettingsPanel()
        self.mainLayout.addWidget(self.settingsPanel)

        # Set the central widget of the window
        self.setCentralWidget(self.mainWidget)

if __name__ == "__main__":
    app = QApplication([])
    mainWindow = MainWindow()
    mainWindow.show()
    app.exec()
