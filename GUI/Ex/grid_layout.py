import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QDockWidget, QTextEdit, QListWidget
from PySide6.QtCore import Qt
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Main Window Settings
        self.setWindowTitle("Unity-like Layout")
        self.setGeometry(100, 100, 800, 600)

        # Adding a central widget
        self.central_widget = QTextEdit()
        self.setCentralWidget(self.central_widget)

        # Scene View
        self.add_dock_widget("Scene View", "left")

        # Game View
        self.add_dock_widget("Game View", "bottom")

        # Inspector
        self.add_dock_widget("Inspector", "right")

        # Hierarchy
        self.add_dock_widget("Hierarchy", "left")

        # Asset Panel
        self.add_dock_widget("Assets", "bottom")

    def add_dock_widget(self, title, position):
        dock = QDockWidget(title)
        dock.setWidget(QListWidget())
        if position == "left":
            self.addDockWidget(Qt.LeftDockWidgetArea, dock)
        elif position == "right":
            self.addDockWidget(Qt.RightDockWidgetArea, dock)
        elif position == "bottom":
            self.addDockWidget(Qt.BottomDockWidgetArea, dock)
        elif position == "top":
            self.addDockWidget(Qt.TopDockWidgetArea, dock)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
