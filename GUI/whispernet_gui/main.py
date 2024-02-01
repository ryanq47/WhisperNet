# This Python file uses the following encoding: utf-8
import sys
from pathlib import Path

from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine

## Named pycode to not cause conflicts
from PyCode.Style import Style
from PyCode.NetworkManager import NetworkManager


if __name__ == "__main__":
    app = QGuiApplication(sys.argv)

    engine = QQmlApplicationEngine()

    ## Adding in style class for QML to be able to access
    style = Style()
    engine.rootContext().setContextProperty("Style", style)

    net_manager = NetworkManager()
    engine.rootContext().setContextProperty("networkManager", net_manager)

    qml_file = Path(__file__).resolve().parent / "Qml/base.qml"
    engine.load(qml_file)
    if not engine.rootObjects():
        sys.exit(-1)
    sys.exit(app.exec())
