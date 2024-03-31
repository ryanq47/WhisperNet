# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'secrets.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHeaderView,
    QPushButton, QSizePolicy, QSpacerItem, QTableWidget,
    QTableWidgetItem, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(990, 507)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        self.gridLayout_2 = QGridLayout(Form)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.secrets_table_widget = QTableWidget(Form)
        if (self.secrets_table_widget.columnCount() < 7):
            self.secrets_table_widget.setColumnCount(7)
        __qtablewidgetitem = QTableWidgetItem()
        self.secrets_table_widget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.secrets_table_widget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.secrets_table_widget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.secrets_table_widget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.secrets_table_widget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.secrets_table_widget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.secrets_table_widget.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        self.secrets_table_widget.setObjectName(u"secrets_table_widget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.secrets_table_widget.sizePolicy().hasHeightForWidth())
        self.secrets_table_widget.setSizePolicy(sizePolicy1)
        self.secrets_table_widget.setFrameShadow(QFrame.Plain)
        self.secrets_table_widget.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.secrets_table_widget.setAutoScroll(True)
        self.secrets_table_widget.horizontalHeader().setVisible(True)
        self.secrets_table_widget.horizontalHeader().setCascadingSectionResizes(False)
        self.secrets_table_widget.horizontalHeader().setProperty("showSortIndicator", False)
        self.secrets_table_widget.horizontalHeader().setStretchLastSection(True)
        self.secrets_table_widget.verticalHeader().setCascadingSectionResizes(False)
        self.secrets_table_widget.verticalHeader().setProperty("showSortIndicator", False)
        self.secrets_table_widget.verticalHeader().setStretchLastSection(False)

        self.gridLayout.addWidget(self.secrets_table_widget, 1, 0, 1, 5)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 2, 0, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 2, 4, 1, 1)

        self.secrets_update = QPushButton(Form)
        self.secrets_update.setObjectName(u"secrets_update")

        self.gridLayout.addWidget(self.secrets_update, 2, 1, 1, 1)

        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")

        self.gridLayout.addWidget(self.pushButton, 2, 2, 1, 1)

        self.pushButton_2 = QPushButton(Form)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.gridLayout.addWidget(self.pushButton_2, 2, 3, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        ___qtablewidgetitem = self.secrets_table_widget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"Username", None));
        ___qtablewidgetitem1 = self.secrets_table_widget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"Password", None));
        ___qtablewidgetitem2 = self.secrets_table_widget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"Domain", None));
        ___qtablewidgetitem3 = self.secrets_table_widget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form", u"Host", None));
        ___qtablewidgetitem4 = self.secrets_table_widget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Form", u"Service", None));
        ___qtablewidgetitem5 = self.secrets_table_widget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Form", u"Port", None));
        ___qtablewidgetitem6 = self.secrets_table_widget.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("Form", u"Comments", None));
        self.secrets_update.setText(QCoreApplication.translate("Form", u"Refresh", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"Export", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"Connect To Service", None))
    # retranslateUi

