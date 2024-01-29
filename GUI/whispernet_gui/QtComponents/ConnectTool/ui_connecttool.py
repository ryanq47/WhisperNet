# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'connecttool.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QPushButton,
    QSizePolicy, QTextEdit, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(292, 233)
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.protocol_combobox = QComboBox(Form)
        self.protocol_combobox.addItem("")
        self.protocol_combobox.addItem("")
        self.protocol_combobox.addItem("")
        self.protocol_combobox.setObjectName(u"protocol_combobox")

        self.verticalLayout.addWidget(self.protocol_combobox)

        self.target_box = QTextEdit(Form)
        self.target_box.setObjectName(u"target_box")
        self.target_box.setMaximumSize(QSize(16777215, 25))

        self.verticalLayout.addWidget(self.target_box)

        self.user_box = QTextEdit(Form)
        self.user_box.setObjectName(u"user_box")
        self.user_box.setMaximumSize(QSize(16777215, 25))

        self.verticalLayout.addWidget(self.user_box)

        self.password_box = QTextEdit(Form)
        self.password_box.setObjectName(u"password_box")
        self.password_box.setMaximumSize(QSize(16777215, 25))

        self.verticalLayout.addWidget(self.password_box)

        self.port_box = QTextEdit(Form)
        self.port_box.setObjectName(u"port_box")
        self.port_box.setMaximumSize(QSize(16777215, 25))

        self.verticalLayout.addWidget(self.port_box)

        self.connect_button = QPushButton(Form)
        self.connect_button.setObjectName(u"connect_button")

        self.verticalLayout.addWidget(self.connect_button)


        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.protocol_combobox.setItemText(0, QCoreApplication.translate("Form", u"SSH", None))
        self.protocol_combobox.setItemText(1, QCoreApplication.translate("Form", u"FTP", None))
        self.protocol_combobox.setItemText(2, QCoreApplication.translate("Form", u"Other", None))

        self.target_box.setPlaceholderText(QCoreApplication.translate("Form", u"Target", None))
        self.user_box.setHtml(QCoreApplication.translate("Form", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.user_box.setPlaceholderText(QCoreApplication.translate("Form", u"Username", None))
        self.password_box.setHtml(QCoreApplication.translate("Form", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.password_box.setPlaceholderText(QCoreApplication.translate("Form", u"Password", None))
        self.port_box.setPlaceholderText(QCoreApplication.translate("Form", u"Port", None))
        self.connect_button.setText(QCoreApplication.translate("Form", u"Connect", None))
    # retranslateUi

