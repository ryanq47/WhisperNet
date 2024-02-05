import sys
from PySide6.QtWidgets import QApplication
from PySide6.QtQuick import QQuickView
from PySide6.QtCore import QUrl

app = QApplication(sys.argv)

view = QQuickView()
url = QUrl("treeViewTest.qml")

view.setSource(url)
view.setResizeMode(QQuickView.SizeRootObjectToView)
view.show()

sys.exit(app.exec())
