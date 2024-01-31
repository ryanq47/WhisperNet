from PySide6.QtCore import QObject, Slot
from PySide6.QtWidgets import QApplication
from PySide6.QtQml import QQmlApplicationEngine

class Backend(QObject):
    def __init__(self):
        super().__init__()


       ## takes in command given from GUI
    @Slot(str, result=str)
    def processCommand(self, command):
        # Process the command here and return output
        print("Command received:", command)
        # For demonstration, just echoing the command
        return "Echo from backend: " + command

if __name__ == "__main__":
    app = QApplication([])
    engine = QQmlApplicationEngine()

    # Expose the Backend class to QML
    backend = Backend()
    engine.rootContext().setContextProperty("backend", backend)

    engine.load("main.qml")

    if not engine.rootObjects():
        exit(-1)

    exit(app.exec())
