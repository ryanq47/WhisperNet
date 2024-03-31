from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Host List")

        # Create the table widget with 3 columns
        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(4)  # Example row count
        self.tableWidget.setColumnCount(3)  # For example, IP, Hostname, Status
        self.tableWidget.setHorizontalHeaderLabels(["IP Address", "Hostname", "Status"])

        # Add items to the table
        self.tableWidget.setItem(0, 0, QTableWidgetItem("192.168.1.1"))
        self.tableWidget.setItem(0, 1, QTableWidgetItem("host1.local"))
        self.tableWidget.setItem(0, 2, QTableWidgetItem("Online"))

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.tableWidget)
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

app = QApplication([])
window = MainWindow()
window.show()
app.exec_()
