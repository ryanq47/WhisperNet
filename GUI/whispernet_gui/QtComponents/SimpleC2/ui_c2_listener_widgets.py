# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'c2_layout_widgets.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHeaderView, QSizePolicy,
    QTextEdit, QToolButton, QTreeWidget, QTreeWidgetItem,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1046, 584)
        Form.setStyleSheet(u"QWidget {\n"
"    background-color: #1e1e1e; /* Dark grey background */\n"
"    color: #dcdcdc; /* Light grey text, bold for aggression */\n"
"    font-weight: bold;\n"
"}\n"
"QPushButton {\n"
"    background-color: #5364A5; /* Blue background for buttons */\n"
"    color: white;\n"
"    border-style: solid;\n"
"    border-width: 2px;\n"
"    border-radius: 0px; /* Sharper corners */\n"
"    border-color: #5364A5;\n"
"    padding: 6px;\n"
"    min-width: 80px;\n"
"    font-weight: bold; /* Bolder text */\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #43528B; /* Darker blue for hover */\n"
"    color: #ffffff;\n"
"    border-color: #43528B;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #333E66; /* Even darker blue when pressed */\n"
"    border-style: inset;\n"
"}\n"
"QLineEdit, QTextEdit, QPlainTextEdit, QSpinBox, QDoubleSpinBox, QComboBox {\n"
"    background-color: #2b2b2b;\n"
"    color: #dcdcdc;\n"
"    border-radius: 0px; /* Sharper edges */\n"
"    padding: 2px;\n"
"    border: 1px "
                        "solid #555;\n"
"    font-weight: bold; /* Bolder text */\n"
"}\n"
"QLabel, QCheckBox, QRadioButton {\n"
"    color: #dcdcdc;\n"
"    font-weight: bold; /* Bolder text */\n"
"}\n"
"QMenuBar, QMenu {\n"
"    background-color: #2b2b2b;\n"
"    color: #dcdcdc;\n"
"    border: 1px solid #555;\n"
"    font-weight: bold; /* Bolder text for menu */\n"
"}\n"
"QMenuBar::item:selected, QMenu::item:selected {\n"
"    background-color: #5364A5; /* Blue for selected menu items */\n"
"    color: white;\n"
"}\n"
"QScrollBar:vertical {\n"
"    border: 1px solid #2b2b2b;\n"
"    background: #2b2b2b;\n"
"    width: 10px;\n"
"    margin: 22px 0 22px 0;\n"
"}\n"
"QScrollBar::handle:vertical {\n"
"    background: #5364A5; /* Blue scrollbar handle */\n"
"    min-height: 20px;\n"
"}\n"
"QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {\n"
"    border: 1px solid #2b2b2b;\n"
"    background: #5364A5; /* Blue for scrollbar buttons */\n"
"    height: 20px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
""
                        "}\n"
"/* TABS */\n"
"QTabWidget::pane {\n"
"    border-top: 2px solid #5364A5; /* Blue top border for tabs */\n"
"}\n"
"\n"
"QTabWidget::tab-bar {\n"
"    left: 5px; /* move to the right by 5px */\n"
"}\n"
"\n"
"QTabBar::tab {\n"
"    background: #2b2b2b;\n"
"    color: #dcdcdc;\n"
"    border: 1px solid #555;\n"
"    border-bottom-color: #5364A5; /* Blue for non-selected tab border */\n"
"    border-top-left-radius: 4px;\n"
"    border-top-right-radius: 4px;\n"
"    padding: 5px;\n"
"    min-width: 80px;\n"
"    align-items: center;\n"
"    justify-content: center;\n"
"    max-height: 20px;\n"
"}\n"
"\n"
"QTabBar::tab:selected, QTabBar::tab:hover {\n"
"    background: #5364A5; /* Blue for selected/hover tab */\n"
"    color: white;\n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"    border-color: #5364A5; /* Blue border for selected tab */\n"
"    border-bottom-color: #1e1e1e; /* Same as window background color */\n"
"}\n"
"\n"
"QTabBar::tab:!selected {\n"
"    margin-top: 2px; /* Make non-selected tabs look small"
                        "er */\n"
"}\n"
"\n"
"/* Q Tree Widget */\n"
"QTreeWidget {\n"
"    border: 1px solid #555;\n"
"    background-color: #2b2b2b;\n"
"    color: #dcdcdc;\n"
"}\n"
"\n"
"QTreeWidget::item {\n"
"    border-bottom: 1px solid #555; /* Subtle separator for items */\n"
"}\n"
"\n"
"QTreeWidget::item:selected {\n"
"    background-color: #5364A5; /* Blue for selected item */\n"
"    color: white;\n"
"}\n"
"\n"
"QTreeWidget::item:hover {\n"
"    background-color: #43528B; /* Darker blue for hover item */\n"
"}\n"
"\n"
"QTreeWidget::branch {\n"
"    background: #2b2b2b;\n"
"}\n"
"\n"
"QTreeWidget::branch:has-siblings:!adjoins-item {\n"
"    border-image: url(path/to/your/line-image.png) 0; /* Custom image for branch lines */\n"
"}\n"
"\n"
"QTreeWidget::branch:has-siblings:adjoins-item {\n"
"    border-image: url(path/to/your/branch-more-image.png) 0;\n"
"}\n"
"\n"
"QTreeWidget::branch:!has-children:!has-siblings:adjoins-item {\n"
"    border-image: url(path/to/your/branch-end-image.png) 0;\n"
"}\n"
"\n"
"/* Customize scroll "
                        "bars */\n"
"QTreeWidget QScrollBar:vertical {\n"
"    border: 1px solid #2b2b2b;\n"
"    background: #2b2b2b;\n"
"    width: 10px;\n"
"    margin: 22px 0 22px 0;\n"
"}\n"
"\n"
"QTreeWidget QScrollBar::handle:vertical {\n"
"    background: #5364A5; /* Blue for tree widget scrollbar handle */\n"
"    min-height: 20px;\n"
"}\n"
"\n"
"QTreeWidget QScrollBar::add-line:vertical, QTreeWidget QScrollBar::sub-line:vertical {\n"
"    border: 1px solid #2b2b2b;\n"
"    background: #5364A5; /* Blue for tree widget scrollbar button */\n"
"    height: 20px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"/* Styles for the header (column titles) */\n"
"QHeaderView::section {\n"
"    background-color: #5364A5; /* Blue for header background */\n"
"    color: white;\n"
"    padding-left: 4px;\n"
"    border: 1px solid #5364A5; /* Blue for header border */\n"
"}\n"
"")
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.info_bar = QTextEdit(Form)
        self.info_bar.setObjectName(u"info_bar")
        self.info_bar.setMaximumSize(QSize(16777215, 25))

        self.gridLayout.addWidget(self.info_bar, 1, 0, 1, 1)

        self.options_button = QToolButton(Form)
        self.options_button.setObjectName(u"options_button")

        self.gridLayout.addWidget(self.options_button, 1, 1, 1, 1)

        self.client_tree_widget = QTreeWidget(Form)
        __qtreewidgetitem = QTreeWidgetItem(self.client_tree_widget)
        QTreeWidgetItem(__qtreewidgetitem)
        QTreeWidgetItem(__qtreewidgetitem)
        QTreeWidgetItem(__qtreewidgetitem)
        self.client_tree_widget.setObjectName(u"client_tree_widget")
        self.client_tree_widget.setStyleSheet(u"border-radius: 2px;")

        self.gridLayout.addWidget(self.client_tree_widget, 0, 0, 1, 2)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.info_bar.setHtml(QCoreApplication.translate("Form", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:600; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">&lt;Some data not sure what, maybe stats or soemthing&gt; or fill me with buttons somewhere instead of the ... over there -&gt;. Maybe do the CS and put them at the top in an action bar?</p></body></html>", None))
        self.options_button.setText(QCoreApplication.translate("Form", u"...", None))
        ___qtreewidgetitem = self.client_tree_widget.headerItem()
        ___qtreewidgetitem.setText(4, QCoreApplication.translate("Form", u"?", None));
        ___qtreewidgetitem.setText(3, QCoreApplication.translate("Form", u"?", None));
        ___qtreewidgetitem.setText(2, QCoreApplication.translate("Form", u"?", None));
        ___qtreewidgetitem.setText(1, QCoreApplication.translate("Form", u"?", None));
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("Form", u"Network", None));

        __sortingEnabled = self.client_tree_widget.isSortingEnabled()
        self.client_tree_widget.setSortingEnabled(False)
        ___qtreewidgetitem1 = self.client_tree_widget.topLevelItem(0)
        ___qtreewidgetitem1.setText(0, QCoreApplication.translate("Form", u"10.0.0.0/24", None));
        ___qtreewidgetitem2 = ___qtreewidgetitem1.child(0)
        ___qtreewidgetitem2.setText(0, QCoreApplication.translate("Form", u"10.0.0.4", None));
        ___qtreewidgetitem3 = ___qtreewidgetitem1.child(1)
        ___qtreewidgetitem3.setText(0, QCoreApplication.translate("Form", u"10.0.0.2", None));
        ___qtreewidgetitem4 = ___qtreewidgetitem1.child(2)
        ___qtreewidgetitem4.setText(0, QCoreApplication.translate("Form", u"10.0.0.10", None));
        self.client_tree_widget.setSortingEnabled(__sortingEnabled)

    # retranslateUi

