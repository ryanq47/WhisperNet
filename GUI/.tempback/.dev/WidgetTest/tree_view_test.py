from PySide6.QtWidgets import QApplication, QMainWindow, QTreeView, QVBoxLayout, QWidget
from PySide6.QtGui import QStandardItemModel, QStandardItem

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Host List")

        self.treeView = QTreeView()
        self.model = QStandardItemModel()
        self.model.setHorizontalHeaderLabels(['Host Details'])

        # Adding sample data
        root_node = self.model.invisibleRootItem()
        group1 = QStandardItem('Group 1')
        host1 = QStandardItem('192.168.1.1 - Online')
        group1.appendRow(host1)
        root_node.appendRow(group1)

        self.treeView.setModel(self.model)

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.treeView)
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

app = QApplication([])
window = MainWindow()
window.show()
app.exec_()
