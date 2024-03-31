# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'notes.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QPushButton, QSizePolicy,
    QSpacerItem, QTextEdit, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1098, 754)
        self.gridLayout_2 = QGridLayout(Form)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.saveButton = QPushButton(Form)
        self.saveButton.setObjectName(u"saveButton")

        self.gridLayout_2.addWidget(self.saveButton, 1, 1, 1, 1)

        self.loadButton = QPushButton(Form)
        self.loadButton.setObjectName(u"loadButton")

        self.gridLayout_2.addWidget(self.loadButton, 1, 2, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 1, 0, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_2, 1, 3, 1, 1)

        self.notesTextEdit = QTextEdit(Form)
        self.notesTextEdit.setObjectName(u"notesTextEdit")

        self.gridLayout_2.addWidget(self.notesTextEdit, 0, 0, 1, 4)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.saveButton.setText(QCoreApplication.translate("Form", u"Save", None))
        self.loadButton.setText(QCoreApplication.translate("Form", u"Load", None))
    # retranslateUi

