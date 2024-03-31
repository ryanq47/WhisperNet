from PySide6.QtWidgets import QApplication, QMainWindow, QListView, QVBoxLayout, QWidget
from PySide6.QtGui import QStandardItemModel, QStandardItem

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Host List")

        self.listView = QListView()
        model = QStandardItemModel(self.listView)

        # Adding items to the model
        for ip in ['192.168.1.1', '192.168.1.2', '192.168.1.3']:
            item = QStandardItem(ip)
            model.appendRow(item)

        self.listView.setModel(model)

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.listView)
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

app = QApplication([])
window = MainWindow()
window.show()
app.exec_()
