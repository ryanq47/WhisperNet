import sys
from PySide6.QtWidgets import QApplication, QTableWidget, QTableWidgetItem, QMenu

class CustomTableWidget(QTableWidget):
    def __init__(self, rows, columns):
        super().__init__(rows, columns)

        # Sample data
        for i in range(rows):
            for j in range(columns):
                self.setItem(i, j, QTableWidgetItem(f"Item {i},{j}"))

    def contextMenuEvent(self, event):
        row = self.rowAt(event.pos().y())
        if row >= 0:  # Ensure that the right-click is on a row
            menu = QMenu(self)
            action1 = menu.addAction("Action 1")
            action2 = menu.addAction("Action 2")
            action3 = menu.addAction("Action 3")

            action = menu.exec(event.globalPos())

            if action == action1:
                print(f"Action 1 selected on row {row}")

            elif action == action2:
                print(f"Action 2 selected on row {row}")
            elif action == action3:
                print(f"Action 3 selected on row {row}")

app = QApplication(sys.argv)
table = CustomTableWidget(5, 3)  # 5 rows, 3 columns
table.show()
sys.exit(app.exec())
