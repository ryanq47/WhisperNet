# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'startup_projectbox.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
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
from PySide6.QtWidgets import (QApplication, QDialog, QGridLayout, QHeaderView,
    QLabel, QPushButton, QRadioButton, QSizePolicy,
    QTableView, QWidget)

class Ui_startup_projectbox(object):
    def setupUi(self, startup_projectbox):
        if not startup_projectbox.objectName():
            startup_projectbox.setObjectName(u"startup_projectbox")
        startup_projectbox.resize(846, 413)
        self.gridLayout = QGridLayout(startup_projectbox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.tableView = QTableView(startup_projectbox)
        self.tableView.setObjectName(u"tableView")

        self.gridLayout.addWidget(self.tableView, 4, 0, 1, 2)

        self.label = QLabel(startup_projectbox)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.label_2 = QLabel(startup_projectbox)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 3, 0, 1, 1)

        self.radioButton_3 = QRadioButton(startup_projectbox)
        self.radioButton_3.setObjectName(u"radioButton_3")

        self.gridLayout.addWidget(self.radioButton_3, 2, 0, 1, 1)

        self.radioButton = QRadioButton(startup_projectbox)
        self.radioButton.setObjectName(u"radioButton")

        self.gridLayout.addWidget(self.radioButton, 1, 0, 1, 1)

        self.pushButton = QPushButton(startup_projectbox)
        self.pushButton.setObjectName(u"pushButton")

        self.gridLayout.addWidget(self.pushButton, 5, 0, 1, 1)

        self.pushButton_2 = QPushButton(startup_projectbox)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.gridLayout.addWidget(self.pushButton_2, 5, 1, 1, 1)


        self.retranslateUi(startup_projectbox)

        QMetaObject.connectSlotsByName(startup_projectbox)
    # setupUi

    def retranslateUi(self, startup_projectbox):
        startup_projectbox.setWindowTitle(QCoreApplication.translate("startup_projectbox", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("startup_projectbox", u"TextLabel", None))
        self.label_2.setText(QCoreApplication.translate("startup_projectbox", u"Recent Projects", None))
        self.radioButton_3.setText(QCoreApplication.translate("startup_projectbox", u"Load Project", None))
        self.radioButton.setText(QCoreApplication.translate("startup_projectbox", u"New Project", None))
        self.pushButton.setText(QCoreApplication.translate("startup_projectbox", u"Open", None))
        self.pushButton_2.setText(QCoreApplication.translate("startup_projectbox", u"Cancel", None))
    # retranslateUi

# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'startup_projectbox.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
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
from PySide6.QtWidgets import (QApplication, QDialog, QHeaderView, QLabel,
    QPushButton, QRadioButton, QSizePolicy, QTableView,
    QWidget)

class Ui_startup_projectbox(object):
    def setupUi(self, startup_projectbox):
        if not startup_projectbox.objectName():
            startup_projectbox.setObjectName(u"startup_projectbox")
        startup_projectbox.resize(846, 413)
        self.label = QLabel(startup_projectbox)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(9, 9, 66, 19))
        self.radioButton = QRadioButton(startup_projectbox)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setGeometry(QRect(9, 34, 108, 25))
        self.radioButton_3 = QRadioButton(startup_projectbox)
        self.radioButton_3.setObjectName(u"radioButton_3")
        self.radioButton_3.setGeometry(QRect(9, 65, 109, 25))
        self.tableView = QTableView(startup_projectbox)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setGeometry(QRect(9, 121, 831, 241))
        self.label_2 = QLabel(startup_projectbox)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(9, 96, 104, 19))
        self.pushButton = QPushButton(startup_projectbox)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(670, 380, 80, 27))
        self.pushButton_2 = QPushButton(startup_projectbox)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(760, 380, 80, 27))

        self.retranslateUi(startup_projectbox)

        QMetaObject.connectSlotsByName(startup_projectbox)
    # setupUi

    def retranslateUi(self, startup_projectbox):
        startup_projectbox.setWindowTitle(QCoreApplication.translate("startup_projectbox", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("startup_projectbox", u"TextLabel", None))
        self.radioButton.setText(QCoreApplication.translate("startup_projectbox", u"New Project", None))
        self.radioButton_3.setText(QCoreApplication.translate("startup_projectbox", u"Load Project", None))
        self.label_2.setText(QCoreApplication.translate("startup_projectbox", u"Recent Projects", None))
        self.pushButton.setText(QCoreApplication.translate("startup_projectbox", u"Open", None))
        self.pushButton_2.setText(QCoreApplication.translate("startup_projectbox", u"Cancel", None))
    # retranslateUi

# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'startup_projectbox.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
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
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QPushButton,
    QRadioButton, QSizePolicy, QWidget)

class Ui_startup_projectbox(object):
    def setupUi(self, startup_projectbox):
        if not startup_projectbox.objectName():
            startup_projectbox.setObjectName(u"startup_projectbox")
        startup_projectbox.resize(549, 114)
        self.label = QLabel(startup_projectbox)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(9, 9, 88, 19))
        self.startup_radio_newproject = QRadioButton(startup_projectbox)
        self.startup_radio_newproject.setObjectName(u"startup_radio_newproject")
        self.startup_radio_newproject.setGeometry(QRect(9, 47, 108, 25))
        self.startup_radio_loadproject = QRadioButton(startup_projectbox)
        self.startup_radio_loadproject.setObjectName(u"startup_radio_loadproject")
        self.startup_radio_loadproject.setGeometry(QRect(9, 79, 109, 25))
        self.startup_project_open = QPushButton(startup_projectbox)
        self.startup_project_open.setObjectName(u"startup_project_open")
        self.startup_project_open.setGeometry(QRect(188, 78, 171, 27))
        self.startup_project_cancel = QPushButton(startup_projectbox)
        self.startup_project_cancel.setObjectName(u"startup_project_cancel")
        self.startup_project_cancel.setGeometry(QRect(367, 78, 171, 27))

        self.retranslateUi(startup_projectbox)

        QMetaObject.connectSlotsByName(startup_projectbox)
    # setupUi

    def retranslateUi(self, startup_projectbox):
        startup_projectbox.setWindowTitle(QCoreApplication.translate("startup_projectbox", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("startup_projectbox", u"Project Menu", None))
        self.startup_radio_newproject.setText(QCoreApplication.translate("startup_projectbox", u"New Project", None))
        self.startup_radio_loadproject.setText(QCoreApplication.translate("startup_projectbox", u"Load Project", None))
        self.startup_project_open.setText(QCoreApplication.translate("startup_projectbox", u"Open", None))
        self.startup_project_cancel.setText(QCoreApplication.translate("startup_projectbox", u"Cancel", None))
    # retranslateUi

# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'startup_projectbox.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
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
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QPushButton,
    QRadioButton, QSizePolicy, QWidget)

class Ui_startup_projectbox(object):
    def setupUi(self, startup_projectbox):
        if not startup_projectbox.objectName():
            startup_projectbox.setObjectName(u"startup_projectbox")
        startup_projectbox.resize(549, 114)
        self.label = QLabel(startup_projectbox)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(9, 9, 88, 19))
        self.startup_radio_newproject = QRadioButton(startup_projectbox)
        self.startup_radio_newproject.setObjectName(u"startup_radio_newproject")
        self.startup_radio_newproject.setGeometry(QRect(9, 47, 108, 25))
        self.startup_radio_loadproject = QRadioButton(startup_projectbox)
        self.startup_radio_loadproject.setObjectName(u"startup_radio_loadproject")
        self.startup_radio_loadproject.setGeometry(QRect(9, 79, 109, 25))
        self.startup_project_open = QPushButton(startup_projectbox)
        self.startup_project_open.setObjectName(u"startup_project_open")
        self.startup_project_open.setGeometry(QRect(188, 78, 171, 27))
        self.startup_project_exit = QPushButton(startup_projectbox)
        self.startup_project_exit.setObjectName(u"startup_project_exit")
        self.startup_project_exit.setGeometry(QRect(367, 78, 171, 27))

        self.retranslateUi(startup_projectbox)

        QMetaObject.connectSlotsByName(startup_projectbox)
    # setupUi

    def retranslateUi(self, startup_projectbox):
        startup_projectbox.setWindowTitle(QCoreApplication.translate("startup_projectbox", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("startup_projectbox", u"Project Menu", None))
        self.startup_radio_newproject.setText(QCoreApplication.translate("startup_projectbox", u"New Project", None))
        self.startup_radio_loadproject.setText(QCoreApplication.translate("startup_projectbox", u"Load Project", None))
        self.startup_project_open.setText(QCoreApplication.translate("startup_projectbox", u"Open", None))
        self.startup_project_exit.setText(QCoreApplication.translate("startup_projectbox", u"Exit", None))
    # retranslateUi

# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'startup_projectbox.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
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
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QPushButton,
    QRadioButton, QSizePolicy, QWidget)

class Ui_startup_projectbox(object):
    def setupUi(self, startup_projectbox):
        if not startup_projectbox.objectName():
            startup_projectbox.setObjectName(u"startup_projectbox")
        startup_projectbox.resize(549, 114)
        self.label = QLabel(startup_projectbox)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(9, 9, 88, 19))
        self.startup_radio_newproject = QRadioButton(startup_projectbox)
        self.startup_radio_newproject.setObjectName(u"startup_radio_newproject")
        self.startup_radio_newproject.setGeometry(QRect(9, 47, 108, 25))
        self.startup_radio_loadproject = QRadioButton(startup_projectbox)
        self.startup_radio_loadproject.setObjectName(u"startup_radio_loadproject")
        self.startup_radio_loadproject.setGeometry(QRect(9, 79, 109, 25))
        self.startup_project_openproject = QPushButton(startup_projectbox)
        self.startup_project_openproject.setObjectName(u"startup_project_openproject")
        self.startup_project_openproject.setGeometry(QRect(188, 78, 171, 27))
        self.startup_project_exit = QPushButton(startup_projectbox)
        self.startup_project_exit.setObjectName(u"startup_project_exit")
        self.startup_project_exit.setGeometry(QRect(367, 78, 171, 27))

        self.retranslateUi(startup_projectbox)

        QMetaObject.connectSlotsByName(startup_projectbox)
    # setupUi

    def retranslateUi(self, startup_projectbox):
        startup_projectbox.setWindowTitle(QCoreApplication.translate("startup_projectbox", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("startup_projectbox", u"Project Menu", None))
        self.startup_radio_newproject.setText(QCoreApplication.translate("startup_projectbox", u"New Project", None))
        self.startup_radio_loadproject.setText(QCoreApplication.translate("startup_projectbox", u"Load Project", None))
        self.startup_project_openproject.setText(QCoreApplication.translate("startup_projectbox", u"Open", None))
        self.startup_project_exit.setText(QCoreApplication.translate("startup_projectbox", u"Exit", None))
    # retranslateUi

