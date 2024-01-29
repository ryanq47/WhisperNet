# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'filehost_horizontal_back.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QHeaderView, QLabel,
    QPushButton, QSizePolicy, QTableWidget, QTableWidgetItem,
    QTextEdit, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1655, 978)
        self.gridLayout_2 = QGridLayout(Form)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 3, 0, 1, 1)

        self.textEdit = QTextEdit(Form)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setMaximumSize(QSize(10000, 50))

        self.gridLayout.addWidget(self.textEdit, 0, 0, 1, 1)

        self.FileHost_UploadFileButton = QPushButton(Form)
        self.FileHost_UploadFileButton.setObjectName(u"FileHost_UploadFileButton")

        self.gridLayout.addWidget(self.FileHost_UploadFileButton, 2, 0, 1, 1)

        self.FileHost_FileAccessLogsTable = QTableWidget(Form)
        if (self.FileHost_FileAccessLogsTable.columnCount() < 5):
            self.FileHost_FileAccessLogsTable.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.FileHost_FileAccessLogsTable.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.FileHost_FileAccessLogsTable.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.FileHost_FileAccessLogsTable.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.FileHost_FileAccessLogsTable.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.FileHost_FileAccessLogsTable.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.FileHost_FileAccessLogsTable.setObjectName(u"FileHost_FileAccessLogsTable")
        self.FileHost_FileAccessLogsTable.setAutoFillBackground(False)
        self.FileHost_FileAccessLogsTable.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.FileHost_FileAccessLogsTable.setAlternatingRowColors(False)
        self.FileHost_FileAccessLogsTable.horizontalHeader().setStretchLastSection(True)

        self.gridLayout.addWidget(self.FileHost_FileAccessLogsTable, 2, 0, 1, 2)

        self.FileHost_FileLogTable = QTableWidget(Form)
        if (self.FileHost_FileLogTable.columnCount() < 3):
            self.FileHost_FileLogTable.setColumnCount(3)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.FileHost_FileLogTable.setHorizontalHeaderItem(0, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.FileHost_FileLogTable.setHorizontalHeaderItem(1, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.FileHost_FileLogTable.setHorizontalHeaderItem(2, __qtablewidgetitem7)
        self.FileHost_FileLogTable.setObjectName(u"FileHost_FileLogTable")
        self.FileHost_FileLogTable.setAutoFillBackground(False)
        self.FileHost_FileLogTable.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.FileHost_FileLogTable.setAlternatingRowColors(False)
        self.FileHost_FileLogTable.horizontalHeader().setStretchLastSection(True)

        self.gridLayout.addWidget(self.FileHost_FileLogTable, 4, 0, 1, 2)

        self.label = QLabel(Form)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)

        self.FileHost_NodeLogTable = QTableWidget(Form)
        if (self.FileHost_NodeLogTable.columnCount() < 4):
            self.FileHost_NodeLogTable.setColumnCount(4)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.FileHost_NodeLogTable.setHorizontalHeaderItem(0, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.FileHost_NodeLogTable.setHorizontalHeaderItem(1, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.FileHost_NodeLogTable.setHorizontalHeaderItem(2, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.FileHost_NodeLogTable.setHorizontalHeaderItem(3, __qtablewidgetitem11)
        self.FileHost_NodeLogTable.setObjectName(u"FileHost_NodeLogTable")
        self.FileHost_NodeLogTable.setAutoFillBackground(False)
        self.FileHost_NodeLogTable.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.FileHost_NodeLogTable.setAlternatingRowColors(False)
        self.FileHost_NodeLogTable.horizontalHeader().setStretchLastSection(True)

        self.gridLayout.addWidget(self.FileHost_NodeLogTable, 6, 0, 1, 2)

        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")

        self.gridLayout.addWidget(self.pushButton, 0, 1, 1, 1)

        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 5, 0, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Files (On server)", None))
        self.textEdit.setHtml(QCoreApplication.translate("Form", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">SomeData</p></body></html>", None))
        self.FileHost_UploadFileButton.setText(QCoreApplication.translate("Form", u" >> Upload File <<", None))
        ___qtablewidgetitem = self.FileHost_FileAccessLogsTable.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"File Name", None));
        ___qtablewidgetitem1 = self.FileHost_FileAccessLogsTable.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"Accessor IP", None));
        ___qtablewidgetitem2 = self.FileHost_FileAccessLogsTable.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"Node Name", None));
        ___qtablewidgetitem3 = self.FileHost_FileAccessLogsTable.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form", u"HTTP Code ", None));
        ___qtablewidgetitem4 = self.FileHost_FileAccessLogsTable.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Form", u"TimeStamp", None));
        ___qtablewidgetitem5 = self.FileHost_FileLogTable.horizontalHeaderItem(0)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Form", u"File Name", None));
        ___qtablewidgetitem6 = self.FileHost_FileLogTable.horizontalHeaderItem(1)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("Form", u"Size (MB)", None));
        ___qtablewidgetitem7 = self.FileHost_FileLogTable.horizontalHeaderItem(2)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("Form", u"FilePath", None));
        self.label.setText(QCoreApplication.translate("Form", u"Files (Access Logs)", None))
        ___qtablewidgetitem8 = self.FileHost_NodeLogTable.horizontalHeaderItem(0)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("Form", u"Node Name", None));
        ___qtablewidgetitem9 = self.FileHost_NodeLogTable.horizontalHeaderItem(1)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("Form", u"IP", None));
        ___qtablewidgetitem10 = self.FileHost_NodeLogTable.horizontalHeaderItem(2)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("Form", u"Contents", None));
        ___qtablewidgetitem11 = self.FileHost_NodeLogTable.horizontalHeaderItem(3)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("Form", u"TimeStamp", None));
        self.pushButton.setText(QCoreApplication.translate("Form", u"[broken] Upload", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"File Nodes", None))
    # retranslateUi

