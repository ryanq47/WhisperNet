import sys
from PyQt5 import QtWidgets, uic

qtcreator_file  = "NAME.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtcreator_file)


class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        ## connector
        ##self.pushButton.clicked.connect(self.CalculateTax)

    ## FUnction
    def CalculateTax(self):
        pass
            ## Blah Blah data edit
            #self.Results_window.setText("Le Output")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())