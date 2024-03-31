# settings_panel.py
from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton

class SettingsPanel(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout()

        self.label = QLabel("Settings Panel")
        self.button = QPushButton("Click Me")
        self.button.clicked.connect(self.on_button_clicked)

        self.layout.addWidget(self.label)
        self.layout.addWidget(self.button)

        self.setLayout(self.layout)

    def on_button_clicked(self):
        self.label.setText("Button Clicked!")
