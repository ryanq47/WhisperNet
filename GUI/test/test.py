import sys
from PySide6.QtWidgets import QApplication, QPushButton
from PySide6.QtQuick import QQuickView
from PySide6.QtCore import QUrl, Qt
from PySide6.QtQml import QQmlApplicationEngine

app = QApplication(sys.argv)

# Create an instance of the engine.
engine = QQmlApplicationEngine()

# Load the QML file
engine.load(QUrl("Main.qml"))

# Find the root object of the QML file, assuming it's a window.
root_window = engine.rootObjects()[0]

# Create a QWidget or any derived class instance
widget = QPushButton("Press Me")
widget.show()

# Embed QWidget into the QML root window if needed
# Note: This requires the QML root object to be prepared to display/embed Widgets,
# typically using QQuickWidget or creating a container for it.

sys.exit(app.exec())