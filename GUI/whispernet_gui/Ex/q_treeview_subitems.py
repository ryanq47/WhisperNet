from PySide6.QtWidgets import QApplication, QTreeWidget, QTreeWidgetItem
from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon

app = QApplication([])

tree = QTreeWidget()
tree.setHeaderLabels(["Name", "Description"])

topLevelItem = QTreeWidgetItem(["Item 1", "This is item 1"])
tree.addTopLevelItem(topLevelItem)

subItem = QTreeWidgetItem(topLevelItem, ["Subitem 1", "This is subitem 1"])
subItem.setIcon(0, QIcon("path/to/icon.png"))
subItem.setCheckState(0, Qt.CheckState.Unchecked)

tree.show()

app.exec()
