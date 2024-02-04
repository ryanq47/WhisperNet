# This Python file uses the following encoding: utf-8
import sys
from pathlib import Path

from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine

## Named pycode to not cause conflicts
from PyCode.Style import Style
from PyCode.Network.NetworkManager import NetworkManager
from PyCode.Authentication.Authentication import Authentication
from PyCode.Data.Data import Data
if __name__ == "__main__":
    app = QGuiApplication(sys.argv)

    engine = QQmlApplicationEngine()

    ## Adding in style class for QML to be able to access
    style = Style()
    engine.rootContext().setContextProperty("Style", style)

    net_manager = NetworkManager()
    engine.rootContext().setContextProperty("networkManager", net_manager)

    authentication = Authentication()
    engine.rootContext().setContextProperty("authentication", authentication)

    data = Data()
    engine.rootContext().setContextProperty("data", data)

    qml_file = Path(__file__).resolve().parent / "Qml/base.qml"
    engine.load(qml_file)
    if not engine.rootObjects():
        sys.exit(-1)
    sys.exit(app.exec())

'''
Notes for classing stuff. Each gui element will have a backend, and itll be exposed to QML.
This way each element can access the stuff it needs.


Alt way could be to have one/a few main classes with multiple subclass instances, limiting how much I have to exposed
Also no params on class init as a design choice

Bonus being I can recreate/recall classes if needed this way?

Should prolly do proper getter/setters too

figure out pycode structure too.

ex:
    authentication.login.to_server()
'''
