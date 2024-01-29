# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'console.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLineEdit, QPushButton,
    QSizePolicy, QTabWidget, QTextEdit, QToolButton,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(573, 526)
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.c2_shell_tab_2 = QTabWidget(Form)
        self.c2_shell_tab_2.setObjectName(u"c2_shell_tab_2")
        self.c2_shell_tab_2.setMinimumSize(QSize(0, 0))
        self.c2_shell_tab_2.setAutoFillBackground(False)
        self.c2_shell_tab_2.setStyleSheet(u"")
        self.c2_shell_tab_2.setTabShape(QTabWidget.Rounded)
        self.c2_shell_tab_2.setTabsClosable(False)
        self.c2_shell_tab_2.setMovable(True)
        self.RemoteShell_Layout_2 = QWidget()
        self.RemoteShell_Layout_2.setObjectName(u"RemoteShell_Layout_2")
        self.gridLayout_43 = QGridLayout(self.RemoteShell_Layout_2)
        self.gridLayout_43.setObjectName(u"gridLayout_43")
        self.gridLayout_43.setContentsMargins(0, 0, 0, 0)
        self.console_send = QPushButton(self.RemoteShell_Layout_2)
        self.console_send.setObjectName(u"console_send")
        self.console_send.setEnabled(True)

        self.gridLayout_43.addWidget(self.console_send, 2, 3, 1, 1)

        self.console_shell = QTextEdit(self.RemoteShell_Layout_2)
        self.console_shell.setObjectName(u"console_shell")
        self.console_shell.setEnabled(True)
        palette = QPalette()
        brush = QBrush(QColor(220, 220, 220, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(1, 1, 1, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        self.console_shell.setPalette(palette)
        font = QFont()
        font.setBold(True)
        self.console_shell.setFont(font)
        self.console_shell.setStyleSheet(u"background-color: rgb(1, 1, 1);border-radius: 2px;")
        self.console_shell.setReadOnly(True)

        self.gridLayout_43.addWidget(self.console_shell, 0, 1, 1, 3)

        self.debug_console = QTextEdit(self.RemoteShell_Layout_2)
        self.debug_console.setObjectName(u"debug_console")
        self.debug_console.setEnabled(False)
        self.debug_console.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.debug_console.setReadOnly(True)

        self.gridLayout_43.addWidget(self.debug_console, 1, 1, 1, 3)

        self.options_button = QToolButton(self.RemoteShell_Layout_2)
        self.options_button.setObjectName(u"options_button")

        self.gridLayout_43.addWidget(self.options_button, 2, 2, 1, 1)

        self.console_input = QLineEdit(self.RemoteShell_Layout_2)
        self.console_input.setObjectName(u"console_input")
        self.console_input.setFont(font)
        self.console_input.setStyleSheet(u"border-radius: 2px;")
        self.console_input.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.console_input.setClearButtonEnabled(True)

        self.gridLayout_43.addWidget(self.console_input, 2, 1, 1, 1)

        self.c2_shell_tab_2.addTab(self.RemoteShell_Layout_2, "")

        self.gridLayout.addWidget(self.c2_shell_tab_2, 0, 0, 1, 1)


        self.retranslateUi(Form)

        self.c2_shell_tab_2.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
#if QT_CONFIG(tooltip)
        self.c2_shell_tab_2.setToolTip(QCoreApplication.translate("Form", u"Enter", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.c2_shell_tab_2.setWhatsThis(QCoreApplication.translate("Form", u"Enter", None))
#endif // QT_CONFIG(whatsthis)
#if QT_CONFIG(tooltip)
        self.console_send.setToolTip(QCoreApplication.translate("Form", u"Hit the Enter Key", None))
#endif // QT_CONFIG(tooltip)
        self.console_send.setText(QCoreApplication.translate("Form", u"-->> Send <<-- ", None))
#if QT_CONFIG(shortcut)
        self.console_send.setShortcut(QCoreApplication.translate("Form", u"Return", None))
#endif // QT_CONFIG(shortcut)
#if QT_CONFIG(tooltip)
        self.console_shell.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.console_shell.setHtml(QCoreApplication.translate("Form", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:600; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Cantarell'; font-size:11pt; font-weight:400;\"><br /></p></body></html>", None))
        self.console_shell.setPlaceholderText(QCoreApplication.translate("Form", u"root@127.0.0.1> ", None))
        self.options_button.setText(QCoreApplication.translate("Form", u"...", None))
#if QT_CONFIG(tooltip)
        self.console_input.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.console_input.setPlaceholderText(QCoreApplication.translate("Form", u"Enter Command Here!", None))
        self.c2_shell_tab_2.setTabText(self.c2_shell_tab_2.indexOf(self.RemoteShell_Layout_2), QCoreApplication.translate("Form", u"Console", None))
    # retranslateUi

