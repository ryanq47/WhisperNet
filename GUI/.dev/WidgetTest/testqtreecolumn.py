from PySide6.QtWidgets import QApplication, QTreeView
from PySide6.QtGui import QStandardItemModel, QStandardItem

app = QApplication([])

# Create the model with a specified number of columns
model = QStandardItemModel()
model.setHorizontalHeaderLabels(['IP', 'Last Check-in', 'OS'])  # Setting column headers

# Create a parent item (network)
network_item = QStandardItem('192.168.1.0/24')
last_checkin = QStandardItem('2024-02-13')
os = QStandardItem('Router OS')

# Add columns for the parent item
network_row = [network_item, last_checkin, os]
model.appendRow(network_row)

# Create a child item (client)
client_item = QStandardItem('192.168.1.100')
client_last_checkin = QStandardItem('2024-02-13 12:34')
client_os = QStandardItem('Windows 10')

# Add columns for the child item
client_row = [client_item, client_last_checkin, client_os]
network_item.appendRow(client_row)

# Setup the QTreeView
tree_view = QTreeView()
tree_view.setModel(model)
tree_view.expandAll()  # Expand all items for visibility
tree_view.show()

app.exec_()
