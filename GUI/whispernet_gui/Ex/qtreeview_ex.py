from PySide6.QtWidgets import QApplication, QTreeView
from PySide6.QtGui import QStandardItemModel, QStandardItem

# Create the application instance
app = QApplication([])

# Create a QTreeView
treeView = QTreeView()

# Create the model
model = QStandardItemModel()

# Create a top-level item
topLevelItem = QStandardItem("Top Level Item")

# Create and add subitems to the top-level item
subItem1 = QStandardItem("Subitem 1")
subItem2 = QStandardItem("Subitem 2")
topLevelItem.appendRow(subItem1)
topLevelItem.appendRow(subItem2)

# Add the top-level item to the model
model.appendRow(topLevelItem)

# Set the model on the tree view
treeView.setModel(model)

# Show the tree view
treeView.show()

# Run the application
app.exec()
