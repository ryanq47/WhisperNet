from PySide6.QtWidgets import QApplication, QMainWindow, QTreeView, QVBoxLayout, QWidget
from PySide6.QtGui import QStandardItemModel, QStandardItem

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Host List")

        # Initialize the tree view and the standard item model
        self.treeView = QTreeView()
        self.model = QStandardItemModel()
        self.treeView.setModel(self.model)

        # Set the header for the model
        self.model.setHorizontalHeaderLabels(['Host Details', 'Status'])

        # Add categories and hosts to the model
        self.addHosts()

        # Layout setup
        layout = QVBoxLayout()
        layout.addWidget(self.treeView)
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def addHosts(self):
        """Add categories and hosts to the tree view."""
        # Sample categories
        categories = {
            'Network Segment 1': [('192.168.1.1', 'Online'), ('192.168.1.2', 'Offline')],
            'Network Segment 2': [('10.0.0.1', 'Online'), ('10.0.0.2', 'Online')],
        }

        for category_name, hosts in categories.items():
            # Create an item for the category
            category_item = QStandardItem(category_name)

            # Add host items to the category
            for host_ip, status in hosts:
                host_item = QStandardItem(host_ip)
                status_item = QStandardItem(status)

                # Append the host item as a child of the category
                category_item.appendRow([host_item, status_item])

            # Add the category item to the model
            self.model.appendRow(category_item)

        # Optionally, expand all categories by default
        self.treeView.expandAll()

# Initialize the application and display the main window
app = QApplication([])
window = MainWindow()
window.show()
app.exec_()
