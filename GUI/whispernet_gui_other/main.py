from PySide6.QtWidgets import QApplication
from PySide6.QtQml import QQmlApplicationEngine
#import resources

if __name__ == "__main__":
    app = QApplication([])

    engine = QQmlApplicationEngine()
    engine.load("./Frontend/content/Screen01.ui.qml")  # Replace with the path to your .ui.qml file

    if not engine.rootObjects():
        exit(-1)

    exit(app.exec())
