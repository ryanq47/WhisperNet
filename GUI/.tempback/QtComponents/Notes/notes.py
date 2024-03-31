from PySide6.QtWidgets import QWidget, QTextEdit, QMessageBox, QVBoxLayout, QPushButton
from PySide6.QtUiTools import QUiLoader

class Notes(QWidget):
    def __init__(self):
        super().__init__()
        
        loader = QUiLoader()
        self.ui_file = loader.load('QtComponents/Notes/notes.ui', self)

        self.__ui_load()
        self.name = "NotesWidget"
        self.load_notes()

    def __ui_load(self):
        '''
        Load UI elements
        '''
        if self.ui_file is None:
            errmsg = "UI File could not be loaded"
            QMessageBox.critical(self, "Error", errmsg)
            print(errmsg)
            return

        try:
            self.notes_text_edit = self.ui_file.findChild(QTextEdit, "notesTextEdit")
            self.save_button = self.ui_file.findChild(QPushButton, "saveButton")
            self.load_button = self.ui_file.findChild(QPushButton, "loadButton")

            # Connect buttons to functions
            self.save_button.clicked.connect(self.save_notes)
            self.load_button.clicked.connect(self.load_notes)

            self.setLayout(self.ui_file.layout())
        except Exception as e:
            QMessageBox.critical(self, "Error", f"An error occurred: {e}")
            print(f"[!] {e}")

    def save_notes(self):
        '''
        Save the notes to a file
        '''
        with open('notes.txt', 'w') as file:
            file.write(self.notes_text_edit.toPlainText())
        QMessageBox.information(self, "Notes", "Notes saved successfully.")

    def load_notes(self):
        '''
        Load the notes from a file
        '''
        try:
            with open('notes.txt', 'r') as file:
                self.notes_text_edit.setText(file.read())
            #QMessageBox.information(self, "Notes", "Notes loaded successfully.")
        except FileNotFoundError:
            QMessageBox.warning(self, "Notes", "No saved notes found.")
