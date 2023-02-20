# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'gui.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDoubleSpinBox,
    QFrame, QGraphicsView, QGridLayout, QHeaderView,
    QLCDNumber, QLabel, QLineEdit, QMainWindow,
    QMenu, QMenuBar, QProgressBar, QPushButton,
    QRadioButton, QScrollArea, QSizePolicy, QSpinBox,
    QTabWidget, QTableWidget, QTableWidgetItem, QTextEdit,
    QWidget)

class Ui_LogecC3(object):
    def setupUi(self, LogecC3):
        if not LogecC3.objectName():
            LogecC3.setObjectName(u"LogecC3")
        LogecC3.setWindowModality(Qt.NonModal)
        LogecC3.resize(1346, 806)
        LogecC3.setMinimumSize(QSize(850, 688))
        LogecC3.setMaximumSize(QSize(10000, 10000))
        font = QFont()
        font.setUnderline(False)
        LogecC3.setFont(font)
        LogecC3.setAcceptDrops(False)
        icon = QIcon()
        icon.addFile(u"../../.designer/backup/Modules/GUI_System/Images/icon.png", QSize(), QIcon.Normal, QIcon.Off)
        LogecC3.setWindowIcon(icon)
        LogecC3.setAnimated(True)
        LogecC3.setDocumentMode(False)
        LogecC3.setTabShape(QTabWidget.Rounded)
        self.action_Target_Listen = QAction(LogecC3)
        self.action_Target_Listen.setObjectName(u"action_Target_Listen")
        self.actionBash = QAction(LogecC3)
        self.actionBash.setObjectName(u"actionBash")
        self.action_bin_sh = QAction(LogecC3)
        self.action_bin_sh.setObjectName(u"action_bin_sh")
        self.action_Target_Python_binbash = QAction(LogecC3)
        self.action_Target_Python_binbash.setObjectName(u"action_Target_Python_binbash")
        self.action_Target_Python_binsh = QAction(LogecC3)
        self.action_Target_Python_binsh.setObjectName(u"action_Target_Python_binsh")
        self.action_Perl = QAction(LogecC3)
        self.action_Perl.setObjectName(u"action_Perl")
        self.actionShell_Type = QAction(LogecC3)
        self.actionShell_Type.setObjectName(u"actionShell_Type")
        self.actionLanguage = QAction(LogecC3)
        self.actionLanguage.setObjectName(u"actionLanguage")
        self.actionDisable_Firewall = QAction(LogecC3)
        self.actionDisable_Firewall.setObjectName(u"actionDisable_Firewall")
        self.GettingStarted_Readme = QAction(LogecC3)
        self.GettingStarted_Readme.setObjectName(u"GettingStarted_Readme")
        self.menu_Data_Download = QAction(LogecC3)
        self.menu_Data_Download.setObjectName(u"menu_Data_Download")
        self.menu_Data_Upload = QAction(LogecC3)
        self.menu_Data_Upload.setObjectName(u"menu_Data_Upload")
        self.action_Target_Ruby_NonInteractive = QAction(LogecC3)
        self.action_Target_Ruby_NonInteractive.setObjectName(u"action_Target_Ruby_NonInteractive")
        self.actionEncrypt_Files = QAction(LogecC3)
        self.actionEncrypt_Files.setObjectName(u"actionEncrypt_Files")
        self.actionLinux = QAction(LogecC3)
        self.actionLinux.setObjectName(u"actionLinux")
        self.actionOther = QAction(LogecC3)
        self.actionOther.setObjectName(u"actionOther")
        self.actionCVE_2017_0144_Eternal_Blue = QAction(LogecC3)
        self.actionCVE_2017_0144_Eternal_Blue.setObjectName(u"actionCVE_2017_0144_Eternal_Blue")
        self.action_Target_Python_win = QAction(LogecC3)
        self.action_Target_Python_win.setObjectName(u"action_Target_Python_win")
        self.actionDEBUG = QAction(LogecC3)
        self.actionDEBUG.setObjectName(u"actionDEBUG")
        self.actionRead_Me_webview = QAction(LogecC3)
        self.actionRead_Me_webview.setObjectName(u"actionRead_Me_webview")
        self.actionNetInfo = QAction(LogecC3)
        self.actionNetInfo.setObjectName(u"actionNetInfo")
        self.actionPortScan_DB = QAction(LogecC3)
        self.actionPortScan_DB.setObjectName(u"actionPortScan_DB")
        self.actionPortScan_DB_2 = QAction(LogecC3)
        self.actionPortScan_DB_2.setObjectName(u"actionPortScan_DB_2")
        self.actionHelp_DB = QAction(LogecC3)
        self.actionHelp_DB.setObjectName(u"actionHelp_DB")
        self.actionTables_DB = QAction(LogecC3)
        self.actionTables_DB.setObjectName(u"actionTables_DB")
        self.actionHelp_Menu_DB = QAction(LogecC3)
        self.actionHelp_Menu_DB.setObjectName(u"actionHelp_Menu_DB")
        self.actionTables_DB_2 = QAction(LogecC3)
        self.actionTables_DB_2.setObjectName(u"actionTables_DB_2")
        self.actionPortScan_DB_3 = QAction(LogecC3)
        self.actionPortScan_DB_3.setObjectName(u"actionPortScan_DB_3")
        self.actionOther_More_Cool_DB = QAction(LogecC3)
        self.actionOther_More_Cool_DB.setObjectName(u"actionOther_More_Cool_DB")
        self.actionPort_Scan = QAction(LogecC3)
        self.actionPort_Scan.setObjectName(u"actionPort_Scan")
        self.actionError_DB = QAction(LogecC3)
        self.actionError_DB.setObjectName(u"actionError_DB")
        self.centralwidget = QWidget(LogecC3)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_4 = QGridLayout(self.centralwidget)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setTabPosition(QTabWidget.North)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setMovable(True)
        self.tabWidget.setTabBarAutoHide(False)
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.gridLayout_3 = QGridLayout(self.tab_3)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.status_data_IPADDR = QLabel(self.tab_3)
        self.status_data_IPADDR.setObjectName(u"status_data_IPADDR")
        font1 = QFont()
        font1.setFamilies([u"Lato"])
        self.status_data_IPADDR.setFont(font1)

        self.gridLayout_3.addWidget(self.status_data_IPADDR, 2, 1, 1, 1)

        self.label = QLabel(self.tab_3)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(16777215, 15))
        self.label.setFont(font1)

        self.gridLayout_3.addWidget(self.label, 7, 0, 1, 1)

        self.status_label_IPADDR = QLabel(self.tab_3)
        self.status_label_IPADDR.setObjectName(u"status_label_IPADDR")
        self.status_label_IPADDR.setMaximumSize(QSize(200, 15))
        self.status_label_IPADDR.setFont(font1)

        self.gridLayout_3.addWidget(self.status_label_IPADDR, 2, 0, 1, 1)

        self.status_label_OS = QLabel(self.tab_3)
        self.status_label_OS.setObjectName(u"status_label_OS")
        self.status_label_OS.setFont(font1)

        self.gridLayout_3.addWidget(self.status_label_OS, 3, 0, 1, 1)

        self.status_Connected = QLabel(self.tab_3)
        self.status_Connected.setObjectName(u"status_Connected")
        self.status_Connected.setMaximumSize(QSize(16777215, 17))
        self.status_Connected.setFont(font1)

        self.gridLayout_3.addWidget(self.status_Connected, 1, 0, 1, 1)

        self.status_data_HOSTNAME = QLabel(self.tab_3)
        self.status_data_HOSTNAME.setObjectName(u"status_data_HOSTNAME")
        self.status_data_HOSTNAME.setMaximumSize(QSize(16777215, 15))
        self.status_data_HOSTNAME.setFont(font1)

        self.gridLayout_3.addWidget(self.status_data_HOSTNAME, 4, 1, 1, 1)

        self.status_label_HOSTNAME = QLabel(self.tab_3)
        self.status_label_HOSTNAME.setObjectName(u"status_label_HOSTNAME")
        self.status_label_HOSTNAME.setMaximumSize(QSize(200, 15))
        self.status_label_HOSTNAME.setFont(font1)

        self.gridLayout_3.addWidget(self.status_label_HOSTNAME, 4, 0, 1, 1)

        self.text_PortScan_tab = QTabWidget(self.tab_3)
        self.text_PortScan_tab.setObjectName(u"text_PortScan_tab")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.gridLayout_2 = QGridLayout(self.tab)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.text_Program_Output = QTextEdit(self.tab)
        self.text_Program_Output.setObjectName(u"text_Program_Output")
        self.text_Program_Output.setEnabled(True)
        font2 = QFont()
        self.text_Program_Output.setFont(font2)
        self.text_Program_Output.setReadOnly(True)

        self.gridLayout_2.addWidget(self.text_Program_Output, 0, 0, 1, 2)

        self.shell_input = QLineEdit(self.tab)
        self.shell_input.setObjectName(u"shell_input")

        self.gridLayout_2.addWidget(self.shell_input, 1, 0, 1, 1)

        self.shell_input_enter = QPushButton(self.tab)
        self.shell_input_enter.setObjectName(u"shell_input_enter")

        self.gridLayout_2.addWidget(self.shell_input_enter, 1, 1, 1, 1)

        self.text_PortScan_tab.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.gridLayout = QGridLayout(self.tab_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.table_QueryDB_Button = QPushButton(self.tab_2)
        self.table_QueryDB_Button.setObjectName(u"table_QueryDB_Button")

        self.gridLayout.addWidget(self.table_QueryDB_Button, 2, 1, 1, 1)

        self.table_RefreshDB_Button = QPushButton(self.tab_2)
        self.table_RefreshDB_Button.setObjectName(u"table_RefreshDB_Button")

        self.gridLayout.addWidget(self.table_RefreshDB_Button, 2, 0, 1, 1)

        self.DB_Query = QLineEdit(self.tab_2)
        self.DB_Query.setObjectName(u"DB_Query")

        self.gridLayout.addWidget(self.DB_Query, 1, 0, 1, 2)

        self.table_SQLDB = QTableWidget(self.tab_2)
        self.table_SQLDB.setObjectName(u"table_SQLDB")

        self.gridLayout.addWidget(self.table_SQLDB, 0, 0, 1, 2)

        self.text_PortScan_tab.addTab(self.tab_2, "")

        self.gridLayout_3.addWidget(self.text_PortScan_tab, 14, 0, 1, 10)

        self.status_data_OS = QLabel(self.tab_3)
        self.status_data_OS.setObjectName(u"status_data_OS")
        self.status_data_OS.setFont(font1)

        self.gridLayout_3.addWidget(self.status_data_OS, 3, 1, 1, 1)

        self.line_2 = QFrame(self.tab_3)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setMinimumSize(QSize(20, 0))
        self.line_2.setFrameShape(QFrame.VLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.gridLayout_3.addWidget(self.line_2, 1, 2, 7, 2)

        self.lineEdit_5 = QLineEdit(self.tab_3)
        self.lineEdit_5.setObjectName(u"lineEdit_5")

        self.gridLayout_3.addWidget(self.lineEdit_5, 2, 4, 1, 1)

        self.tabWidget.addTab(self.tab_3, "")
        self.tab_53 = QWidget()
        self.tab_53.setObjectName(u"tab_53")
        self.bruteforce_panel_2 = QTabWidget(self.tab_53)
        self.bruteforce_panel_2.setObjectName(u"bruteforce_panel_2")
        self.bruteforce_panel_2.setGeometry(QRect(970, 320, 385, 531))
        self.tab_55 = QWidget()
        self.tab_55.setObjectName(u"tab_55")
        self.gridLayout_40 = QGridLayout(self.tab_55)
        self.gridLayout_40.setObjectName(u"gridLayout_40")
        self.bruteforce_currentbatch_2 = QTextEdit(self.tab_55)
        self.bruteforce_currentbatch_2.setObjectName(u"bruteforce_currentbatch_2")

        self.gridLayout_40.addWidget(self.bruteforce_currentbatch_2, 0, 0, 1, 1)

        self.bruteforce_panel_2.addTab(self.tab_55, "")
        self.tab_54 = QWidget()
        self.tab_54.setObjectName(u"tab_54")
        self.gridLayout_39 = QGridLayout(self.tab_54)
        self.gridLayout_39.setObjectName(u"gridLayout_39")
        self.bruteforce_goodcreds_2 = QTextEdit(self.tab_54)
        self.bruteforce_goodcreds_2.setObjectName(u"bruteforce_goodcreds_2")
        self.bruteforce_goodcreds_2.setMaximumSize(QSize(1677700, 16777215))

        self.gridLayout_39.addWidget(self.bruteforce_goodcreds_2, 0, 0, 1, 1)

        self.bruteforce_panel_2.addTab(self.tab_54, "")
        self.tab_56 = QWidget()
        self.tab_56.setObjectName(u"tab_56")
        self.gridLayout_41 = QGridLayout(self.tab_56)
        self.gridLayout_41.setObjectName(u"gridLayout_41")
        self.bruteforce_errlog_2 = QTextEdit(self.tab_56)
        self.bruteforce_errlog_2.setObjectName(u"bruteforce_errlog_2")

        self.gridLayout_41.addWidget(self.bruteforce_errlog_2, 0, 0, 1, 1)

        self.bruteforce_panel_2.addTab(self.tab_56, "")
        self.text_PortScan_tab_2 = QTabWidget(self.tab_53)
        self.text_PortScan_tab_2.setObjectName(u"text_PortScan_tab_2")
        self.text_PortScan_tab_2.setGeometry(QRect(10, 287, 951, 571))
        self.tab_57 = QWidget()
        self.tab_57.setObjectName(u"tab_57")
        self.gridLayout_42 = QGridLayout(self.tab_57)
        self.gridLayout_42.setObjectName(u"gridLayout_42")
        self.text_Program_Output_2 = QTextEdit(self.tab_57)
        self.text_Program_Output_2.setObjectName(u"text_Program_Output_2")
        self.text_Program_Output_2.setEnabled(True)
        self.text_Program_Output_2.setFont(font2)
        self.text_Program_Output_2.setStyleSheet(u"background-color: rgb(29, 29, 29);")
        self.text_Program_Output_2.setReadOnly(True)

        self.gridLayout_42.addWidget(self.text_Program_Output_2, 0, 0, 1, 2)

        self.shell_input_2 = QLineEdit(self.tab_57)
        self.shell_input_2.setObjectName(u"shell_input_2")

        self.gridLayout_42.addWidget(self.shell_input_2, 1, 0, 1, 1)

        self.shell_input_enter_2 = QPushButton(self.tab_57)
        self.shell_input_enter_2.setObjectName(u"shell_input_enter_2")

        self.gridLayout_42.addWidget(self.shell_input_enter_2, 1, 1, 1, 1)

        self.text_PortScan_tab_2.addTab(self.tab_57, "")
        self.tab_58 = QWidget()
        self.tab_58.setObjectName(u"tab_58")
        self.gridLayout_43 = QGridLayout(self.tab_58)
        self.gridLayout_43.setObjectName(u"gridLayout_43")
        self.table_QueryDB_Button_2 = QPushButton(self.tab_58)
        self.table_QueryDB_Button_2.setObjectName(u"table_QueryDB_Button_2")

        self.gridLayout_43.addWidget(self.table_QueryDB_Button_2, 2, 1, 1, 1)

        self.table_RefreshDB_Button_2 = QPushButton(self.tab_58)
        self.table_RefreshDB_Button_2.setObjectName(u"table_RefreshDB_Button_2")

        self.gridLayout_43.addWidget(self.table_RefreshDB_Button_2, 2, 0, 1, 1)

        self.DB_Query_2 = QLineEdit(self.tab_58)
        self.DB_Query_2.setObjectName(u"DB_Query_2")

        self.gridLayout_43.addWidget(self.DB_Query_2, 1, 0, 1, 2)

        self.table_SQLDB_2 = QTableWidget(self.tab_58)
        self.table_SQLDB_2.setObjectName(u"table_SQLDB_2")

        self.gridLayout_43.addWidget(self.table_SQLDB_2, 0, 0, 1, 2)

        self.text_PortScan_tab_2.addTab(self.tab_58, "")
        self.tab_59 = QWidget()
        self.tab_59.setObjectName(u"tab_59")
        self.c2_systemshell = QTextEdit(self.tab_59)
        self.c2_systemshell.setObjectName(u"c2_systemshell")
        self.c2_systemshell.setEnabled(True)
        self.c2_systemshell.setGeometry(QRect(10, 10, 929, 487))
        self.c2_systemshell.setFont(font2)
        self.c2_systemshell.setStyleSheet(u"background-color: rgb(29, 29, 29);")
        self.c2_systemshell.setReadOnly(True)
        self.c2_systemshell_input = QLineEdit(self.tab_59)
        self.c2_systemshell_input.setObjectName(u"c2_systemshell_input")
        self.c2_systemshell_input.setGeometry(QRect(10, 496, 861, 31))
        self.c2_systemshell_input.setStyleSheet(u"background-color: rgb(29, 29, 29);")
        self.c2_systemshell_send = QPushButton(self.tab_59)
        self.c2_systemshell_send.setObjectName(u"c2_systemshell_send")
        self.c2_systemshell_send.setEnabled(True)
        self.c2_systemshell_send.setGeometry(QRect(881, 500, 61, 27))
        self.text_PortScan_tab_2.addTab(self.tab_59, "")
        self.textEdit_25 = QTextEdit(self.tab_53)
        self.textEdit_25.setObjectName(u"textEdit_25")
        self.textEdit_25.setGeometry(QRect(70, 20, 951, 161))
        self.tabWidget.addTab(self.tab_53, "")
        self.tab_38 = QWidget()
        self.tab_38.setObjectName(u"tab_38")
        self.gridLayout_29 = QGridLayout(self.tab_38)
        self.gridLayout_29.setObjectName(u"gridLayout_29")
        self.tabWidget_5 = QTabWidget(self.tab_38)
        self.tabWidget_5.setObjectName(u"tabWidget_5")
        self.tab_39 = QWidget()
        self.tab_39.setObjectName(u"tab_39")
        self.gridLayout_30 = QGridLayout(self.tab_39)
        self.gridLayout_30.setObjectName(u"gridLayout_30")
        self.lineEdit_17 = QLineEdit(self.tab_39)
        self.lineEdit_17.setObjectName(u"lineEdit_17")

        self.gridLayout_30.addWidget(self.lineEdit_17, 3, 1, 1, 1)

        self.label_70 = QLabel(self.tab_39)
        self.label_70.setObjectName(u"label_70")

        self.gridLayout_30.addWidget(self.label_70, 3, 0, 1, 1)

        self.label_67 = QLabel(self.tab_39)
        self.label_67.setObjectName(u"label_67")

        self.gridLayout_30.addWidget(self.label_67, 0, 0, 2, 1)

        self.label_69 = QLabel(self.tab_39)
        self.label_69.setObjectName(u"label_69")

        self.gridLayout_30.addWidget(self.label_69, 2, 2, 1, 1)

        self.label_68 = QLabel(self.tab_39)
        self.label_68.setObjectName(u"label_68")

        self.gridLayout_30.addWidget(self.label_68, 2, 0, 1, 1)

        self.lineEdit_14 = QLineEdit(self.tab_39)
        self.lineEdit_14.setObjectName(u"lineEdit_14")

        self.gridLayout_30.addWidget(self.lineEdit_14, 0, 1, 2, 1)

        self.portscan_start_6 = QPushButton(self.tab_39)
        self.portscan_start_6.setObjectName(u"portscan_start_6")

        self.gridLayout_30.addWidget(self.portscan_start_6, 3, 3, 1, 2)

        self.lineEdit_15 = QLineEdit(self.tab_39)
        self.lineEdit_15.setObjectName(u"lineEdit_15")

        self.gridLayout_30.addWidget(self.lineEdit_15, 2, 1, 1, 1)

        self.dashboard_osint_keyword_2 = QLineEdit(self.tab_39)
        self.dashboard_osint_keyword_2.setObjectName(u"dashboard_osint_keyword_2")

        self.gridLayout_30.addWidget(self.dashboard_osint_keyword_2, 0, 3, 1, 1)

        self.lineEdit_16 = QLineEdit(self.tab_39)
        self.lineEdit_16.setObjectName(u"lineEdit_16")

        self.gridLayout_30.addWidget(self.lineEdit_16, 1, 3, 2, 1)

        self.scrollArea_4 = QScrollArea(self.tab_39)
        self.scrollArea_4.setObjectName(u"scrollArea_4")
        self.scrollArea_4.setWidgetResizable(True)
        self.scrollAreaWidgetContents_4 = QWidget()
        self.scrollAreaWidgetContents_4.setObjectName(u"scrollAreaWidgetContents_4")
        self.scrollAreaWidgetContents_4.setGeometry(QRect(0, 0, 1282, 522))
        self.label_62 = QLabel(self.scrollAreaWidgetContents_4)
        self.label_62.setObjectName(u"label_62")
        self.label_62.setGeometry(QRect(10, 10, 91, 19))
        font3 = QFont()
        font3.setUnderline(True)
        self.label_62.setFont(font3)
        self.lineEdit_12 = QLineEdit(self.scrollAreaWidgetContents_4)
        self.lineEdit_12.setObjectName(u"lineEdit_12")
        self.lineEdit_12.setGeometry(QRect(10, 510, 113, 27))
        self.dashboard_reddit_onlycomments_2 = QCheckBox(self.scrollAreaWidgetContents_4)
        self.dashboard_reddit_onlycomments_2.setObjectName(u"dashboard_reddit_onlycomments_2")
        self.dashboard_reddit_onlycomments_2.setGeometry(QRect(140, 70, 140, 25))
        self.dashboard_reddit_onlycomments_2.setCheckable(True)
        self.dashboard_reddit_onlycomments_2.setChecked(False)
        self.combo_time_3 = QComboBox(self.scrollAreaWidgetContents_4)
        self.combo_time_3.addItem("")
        self.combo_time_3.addItem("")
        self.combo_time_3.addItem("")
        self.combo_time_3.addItem("")
        self.combo_time_3.addItem("")
        self.combo_time_3.setObjectName(u"combo_time_3")
        self.combo_time_3.setGeometry(QRect(15, 133, 123, 27))
        self.label_63 = QLabel(self.scrollAreaWidgetContents_4)
        self.label_63.setObjectName(u"label_63")
        self.label_63.setGeometry(QRect(15, 38, 123, 25))
        self.label_64 = QLabel(self.scrollAreaWidgetContents_4)
        self.label_64.setObjectName(u"label_64")
        self.label_64.setGeometry(QRect(15, 102, 123, 25))
        self.dashboard_reddit_onlyprofile_2 = QCheckBox(self.scrollAreaWidgetContents_4)
        self.dashboard_reddit_onlyprofile_2.setObjectName(u"dashboard_reddit_onlyprofile_2")
        self.dashboard_reddit_onlyprofile_2.setGeometry(QRect(140, 100, 140, 25))
        self.combo_sort_3 = QComboBox(self.scrollAreaWidgetContents_4)
        self.combo_sort_3.addItem("")
        self.combo_sort_3.addItem("")
        self.combo_sort_3.addItem("")
        self.combo_sort_3.addItem("")
        self.combo_sort_3.addItem("")
        self.combo_sort_3.setObjectName(u"combo_sort_3")
        self.combo_sort_3.setGeometry(QRect(15, 69, 123, 27))
        self.dashboard_reddit_downloadmedia_2 = QCheckBox(self.scrollAreaWidgetContents_4)
        self.dashboard_reddit_downloadmedia_2.setObjectName(u"dashboard_reddit_downloadmedia_2")
        self.dashboard_reddit_downloadmedia_2.setGeometry(QRect(140, 130, 170, 25))
        self.dashboard_reddit_downloadmedia_2.setChecked(True)
        self.line_15 = QFrame(self.scrollAreaWidgetContents_4)
        self.line_15.setObjectName(u"line_15")
        self.line_15.setGeometry(QRect(10, 230, 271, 21))
        self.line_15.setFrameShape(QFrame.HLine)
        self.line_15.setFrameShadow(QFrame.Sunken)
        self.dashboard_reddit_subreddit_2 = QLineEdit(self.scrollAreaWidgetContents_4)
        self.dashboard_reddit_subreddit_2.setObjectName(u"dashboard_reddit_subreddit_2")
        self.dashboard_reddit_subreddit_2.setGeometry(QRect(10, 200, 271, 27))
        self.label_65 = QLabel(self.scrollAreaWidgetContents_4)
        self.label_65.setObjectName(u"label_65")
        self.label_65.setGeometry(QRect(20, 170, 151, 25))
        self.line_16 = QFrame(self.scrollAreaWidgetContents_4)
        self.line_16.setObjectName(u"line_16")
        self.line_16.setGeometry(QRect(290, 20, 21, 221))
        self.line_16.setFrameShape(QFrame.VLine)
        self.line_16.setFrameShadow(QFrame.Sunken)
        self.dashboard_reddit_hideNSFW_2 = QCheckBox(self.scrollAreaWidgetContents_4)
        self.dashboard_reddit_hideNSFW_2.setObjectName(u"dashboard_reddit_hideNSFW_2")
        self.dashboard_reddit_hideNSFW_2.setGeometry(QRect(140, 40, 131, 25))
        self.lineEdit_13 = QLineEdit(self.scrollAreaWidgetContents_4)
        self.lineEdit_13.setObjectName(u"lineEdit_13")
        self.lineEdit_13.setGeometry(QRect(182, 380, 751, 27))
        self.scrollArea_4.setWidget(self.scrollAreaWidgetContents_4)

        self.gridLayout_30.addWidget(self.scrollArea_4, 5, 0, 1, 5)

        self.label_66 = QLabel(self.tab_39)
        self.label_66.setObjectName(u"label_66")

        self.gridLayout_30.addWidget(self.label_66, 0, 2, 1, 1)

        self.progressBar = QProgressBar(self.tab_39)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(24)

        self.gridLayout_30.addWidget(self.progressBar, 6, 0, 1, 4)

        self.tabWidget_5.addTab(self.tab_39, "")
        self.tab_40 = QWidget()
        self.tab_40.setObjectName(u"tab_40")
        self.tabWidget_5.addTab(self.tab_40, "")

        self.gridLayout_29.addWidget(self.tabWidget_5, 1, 0, 1, 1)

        self.tabWidget.addTab(self.tab_38, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.gridLayout_5 = QGridLayout(self.tab_4)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.osint_dork = QTabWidget(self.tab_4)
        self.osint_dork.setObjectName(u"osint_dork")
        self.tab_12 = QWidget()
        self.tab_12.setObjectName(u"tab_12")
        self.gridLayout_8 = QGridLayout(self.tab_12)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.label_7 = QLabel(self.tab_12)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_8.addWidget(self.label_7, 0, 0, 1, 1)

        self.dashboard_osint_keyword = QLineEdit(self.tab_12)
        self.dashboard_osint_keyword.setObjectName(u"dashboard_osint_keyword")

        self.gridLayout_8.addWidget(self.dashboard_osint_keyword, 0, 1, 1, 2)

        self.comboBox_3 = QComboBox(self.tab_12)
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.setObjectName(u"comboBox_3")

        self.gridLayout_8.addWidget(self.comboBox_3, 1, 1, 1, 1)

        self.scrollArea_2 = QScrollArea(self.tab_12)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 72, 16))
        self.label_11 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(10, 10, 66, 19))
        self.label_11.setFont(font3)
        self.lineEdit_6 = QLineEdit(self.scrollAreaWidgetContents_2)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        self.lineEdit_6.setGeometry(QRect(10, 510, 113, 27))
        self.dashboard_reddit_onlycomments = QCheckBox(self.scrollAreaWidgetContents_2)
        self.dashboard_reddit_onlycomments.setObjectName(u"dashboard_reddit_onlycomments")
        self.dashboard_reddit_onlycomments.setGeometry(QRect(140, 70, 140, 25))
        self.dashboard_reddit_onlycomments.setCheckable(True)
        self.dashboard_reddit_onlycomments.setChecked(False)
        self.combo_time_2 = QComboBox(self.scrollAreaWidgetContents_2)
        self.combo_time_2.addItem("")
        self.combo_time_2.addItem("")
        self.combo_time_2.addItem("")
        self.combo_time_2.addItem("")
        self.combo_time_2.addItem("")
        self.combo_time_2.setObjectName(u"combo_time_2")
        self.combo_time_2.setGeometry(QRect(15, 133, 123, 27))
        self.label_15 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(15, 38, 123, 25))
        self.label_17 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(15, 102, 123, 25))
        self.dashboard_reddit_onlyprofile = QCheckBox(self.scrollAreaWidgetContents_2)
        self.dashboard_reddit_onlyprofile.setObjectName(u"dashboard_reddit_onlyprofile")
        self.dashboard_reddit_onlyprofile.setGeometry(QRect(140, 100, 140, 25))
        self.combo_sort_2 = QComboBox(self.scrollAreaWidgetContents_2)
        self.combo_sort_2.addItem("")
        self.combo_sort_2.addItem("")
        self.combo_sort_2.addItem("")
        self.combo_sort_2.addItem("")
        self.combo_sort_2.addItem("")
        self.combo_sort_2.setObjectName(u"combo_sort_2")
        self.combo_sort_2.setGeometry(QRect(15, 69, 123, 27))
        self.dashboard_reddit_downloadmedia = QCheckBox(self.scrollAreaWidgetContents_2)
        self.dashboard_reddit_downloadmedia.setObjectName(u"dashboard_reddit_downloadmedia")
        self.dashboard_reddit_downloadmedia.setGeometry(QRect(140, 130, 170, 25))
        self.dashboard_reddit_downloadmedia.setChecked(True)
        self.line_3 = QFrame(self.scrollAreaWidgetContents_2)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setGeometry(QRect(10, 230, 271, 21))
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)
        self.dashboard_reddit_subreddit = QLineEdit(self.scrollAreaWidgetContents_2)
        self.dashboard_reddit_subreddit.setObjectName(u"dashboard_reddit_subreddit")
        self.dashboard_reddit_subreddit.setGeometry(QRect(10, 200, 271, 27))
        self.label_23 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setGeometry(QRect(20, 170, 151, 25))
        self.line_7 = QFrame(self.scrollAreaWidgetContents_2)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setGeometry(QRect(290, 20, 21, 221))
        self.line_7.setFrameShape(QFrame.VLine)
        self.line_7.setFrameShadow(QFrame.Sunken)
        self.dashboard_reddit_hideNSFW = QCheckBox(self.scrollAreaWidgetContents_2)
        self.dashboard_reddit_hideNSFW.setObjectName(u"dashboard_reddit_hideNSFW")
        self.dashboard_reddit_hideNSFW.setGeometry(QRect(140, 40, 131, 25))
        self.lineEdit_7 = QLineEdit(self.scrollAreaWidgetContents_2)
        self.lineEdit_7.setObjectName(u"lineEdit_7")
        self.lineEdit_7.setGeometry(QRect(182, 380, 751, 27))
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)

        self.gridLayout_8.addWidget(self.scrollArea_2, 2, 0, 1, 3)

        self.portscan_start_5 = QPushButton(self.tab_12)
        self.portscan_start_5.setObjectName(u"portscan_start_5")

        self.gridLayout_8.addWidget(self.portscan_start_5, 1, 2, 1, 1)

        self.label_24 = QLabel(self.tab_12)
        self.label_24.setObjectName(u"label_24")

        self.gridLayout_8.addWidget(self.label_24, 1, 0, 1, 1)

        self.progressBar_2 = QProgressBar(self.tab_12)
        self.progressBar_2.setObjectName(u"progressBar_2")
        self.progressBar_2.setValue(24)

        self.gridLayout_8.addWidget(self.progressBar_2, 3, 0, 1, 3)

        self.osint_dork.addTab(self.tab_12, "")
        self.tab_13 = QWidget()
        self.tab_13.setObjectName(u"tab_13")
        self.gridLayout_10 = QGridLayout(self.tab_13)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.osint_reddit_onlyprofile = QCheckBox(self.tab_13)
        self.osint_reddit_onlyprofile.setObjectName(u"osint_reddit_onlyprofile")

        self.gridLayout_10.addWidget(self.osint_reddit_onlyprofile, 8, 3, 1, 1)

        self.osint_reddit_search = QPushButton(self.tab_13)
        self.osint_reddit_search.setObjectName(u"osint_reddit_search")

        self.gridLayout_10.addWidget(self.osint_reddit_search, 9, 3, 1, 2)

        self.osint_reddit_keyword = QLineEdit(self.tab_13)
        self.osint_reddit_keyword.setObjectName(u"osint_reddit_keyword")

        self.gridLayout_10.addWidget(self.osint_reddit_keyword, 7, 1, 1, 1)

        self.label_10 = QLabel(self.tab_13)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_10.addWidget(self.label_10, 8, 2, 1, 1)

        self.combo_sort = QComboBox(self.tab_13)
        self.combo_sort.addItem("")
        self.combo_sort.addItem("")
        self.combo_sort.addItem("")
        self.combo_sort.addItem("")
        self.combo_sort.addItem("")
        self.combo_sort.setObjectName(u"combo_sort")

        self.gridLayout_10.addWidget(self.combo_sort, 7, 2, 1, 1)

        self.reddit_progressbar = QProgressBar(self.tab_13)
        self.reddit_progressbar.setObjectName(u"reddit_progressbar")
        self.reddit_progressbar.setValue(0)
        self.reddit_progressbar.setInvertedAppearance(False)

        self.gridLayout_10.addWidget(self.reddit_progressbar, 4, 1, 1, 4)

        self.checkBox_2 = QCheckBox(self.tab_13)
        self.checkBox_2.setObjectName(u"checkBox_2")
        self.checkBox_2.setChecked(False)
        self.checkBox_2.setTristate(False)

        self.gridLayout_10.addWidget(self.checkBox_2, 8, 4, 1, 1)

        self.DB_Query_osint_reddit = QLineEdit(self.tab_13)
        self.DB_Query_osint_reddit.setObjectName(u"DB_Query_osint_reddit")

        self.gridLayout_10.addWidget(self.DB_Query_osint_reddit, 1, 1, 1, 4)

        self.label_6 = QLabel(self.tab_13)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_10.addWidget(self.label_6, 6, 1, 1, 1)

        self.table_QueryDB_Button_osint_reddit = QPushButton(self.tab_13)
        self.table_QueryDB_Button_osint_reddit.setObjectName(u"table_QueryDB_Button_osint_reddit")

        self.gridLayout_10.addWidget(self.table_QueryDB_Button_osint_reddit, 2, 2, 2, 3)

        self.table_SQLDB_osint_reddit = QTableWidget(self.tab_13)
        self.table_SQLDB_osint_reddit.setObjectName(u"table_SQLDB_osint_reddit")

        self.gridLayout_10.addWidget(self.table_SQLDB_osint_reddit, 0, 1, 1, 4)

        self.osint_reddit_hideNSFW = QCheckBox(self.tab_13)
        self.osint_reddit_hideNSFW.setObjectName(u"osint_reddit_hideNSFW")

        self.gridLayout_10.addWidget(self.osint_reddit_hideNSFW, 6, 4, 1, 1)

        self.combo_time = QComboBox(self.tab_13)
        self.combo_time.addItem("")
        self.combo_time.addItem("")
        self.combo_time.addItem("")
        self.combo_time.addItem("")
        self.combo_time.addItem("")
        self.combo_time.setObjectName(u"combo_time")

        self.gridLayout_10.addWidget(self.combo_time, 9, 2, 1, 1)

        self.osint_reddit_downloadmedia = QCheckBox(self.tab_13)
        self.osint_reddit_downloadmedia.setObjectName(u"osint_reddit_downloadmedia")
        self.osint_reddit_downloadmedia.setChecked(True)

        self.gridLayout_10.addWidget(self.osint_reddit_downloadmedia, 7, 4, 1, 1)

        self.table_RefreshDB_Button_osint_reddit = QPushButton(self.tab_13)
        self.table_RefreshDB_Button_osint_reddit.setObjectName(u"table_RefreshDB_Button_osint_reddit")

        self.gridLayout_10.addWidget(self.table_RefreshDB_Button_osint_reddit, 2, 1, 2, 1)

        self.osint_reddit_onlycomments = QCheckBox(self.tab_13)
        self.osint_reddit_onlycomments.setObjectName(u"osint_reddit_onlycomments")
        self.osint_reddit_onlycomments.setCheckable(True)
        self.osint_reddit_onlycomments.setChecked(False)

        self.gridLayout_10.addWidget(self.osint_reddit_onlycomments, 7, 3, 1, 1)

        self.label_9 = QLabel(self.tab_13)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_10.addWidget(self.label_9, 6, 2, 1, 1)

        self.label_8 = QLabel(self.tab_13)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_10.addWidget(self.label_8, 8, 1, 1, 1)

        self.osint_reddit_subreddit = QLineEdit(self.tab_13)
        self.osint_reddit_subreddit.setObjectName(u"osint_reddit_subreddit")

        self.gridLayout_10.addWidget(self.osint_reddit_subreddit, 9, 1, 1, 1)

        self.line_8 = QFrame(self.tab_13)
        self.line_8.setObjectName(u"line_8")
        self.line_8.setFrameShape(QFrame.HLine)
        self.line_8.setFrameShadow(QFrame.Sunken)

        self.gridLayout_10.addWidget(self.line_8, 5, 1, 1, 4)

        self.osint_dork.addTab(self.tab_13, "")
        self.tab_18 = QWidget()
        self.tab_18.setObjectName(u"tab_18")
        self.gridLayout_20 = QGridLayout(self.tab_18)
        self.gridLayout_20.setObjectName(u"gridLayout_20")
        self.label_54 = QLabel(self.tab_18)
        self.label_54.setObjectName(u"label_54")

        self.gridLayout_20.addWidget(self.label_54, 0, 0, 1, 1)

        self.line_17 = QFrame(self.tab_18)
        self.line_17.setObjectName(u"line_17")
        self.line_17.setFrameShape(QFrame.VLine)
        self.line_17.setFrameShadow(QFrame.Sunken)

        self.gridLayout_20.addWidget(self.line_17, 0, 1, 7, 1)

        self.label_53 = QLabel(self.tab_18)
        self.label_53.setObjectName(u"label_53")

        self.gridLayout_20.addWidget(self.label_53, 0, 2, 1, 1)

        self.line_18 = QFrame(self.tab_18)
        self.line_18.setObjectName(u"line_18")
        self.line_18.setFrameShape(QFrame.VLine)
        self.line_18.setFrameShadow(QFrame.Sunken)

        self.gridLayout_20.addWidget(self.line_18, 0, 3, 7, 1)

        self.label_52 = QLabel(self.tab_18)
        self.label_52.setObjectName(u"label_52")

        self.gridLayout_20.addWidget(self.label_52, 0, 4, 1, 1)

        self.osint_dork_searchterm = QLineEdit(self.tab_18)
        self.osint_dork_searchterm.setObjectName(u"osint_dork_searchterm")

        self.gridLayout_20.addWidget(self.osint_dork_searchterm, 1, 0, 1, 1)

        self.osint_dork_intitle = QLineEdit(self.tab_18)
        self.osint_dork_intitle.setObjectName(u"osint_dork_intitle")

        self.gridLayout_20.addWidget(self.osint_dork_intitle, 1, 2, 1, 1)

        self.osint_dork_filetype = QLineEdit(self.tab_18)
        self.osint_dork_filetype.setObjectName(u"osint_dork_filetype")

        self.gridLayout_20.addWidget(self.osint_dork_filetype, 1, 4, 1, 1)

        self.label_50 = QLabel(self.tab_18)
        self.label_50.setObjectName(u"label_50")

        self.gridLayout_20.addWidget(self.label_50, 2, 0, 1, 1)

        self.label_51 = QLabel(self.tab_18)
        self.label_51.setObjectName(u"label_51")

        self.gridLayout_20.addWidget(self.label_51, 2, 2, 1, 1)

        self.osint_dork_keyword = QLineEdit(self.tab_18)
        self.osint_dork_keyword.setObjectName(u"osint_dork_keyword")

        self.gridLayout_20.addWidget(self.osint_dork_keyword, 3, 0, 1, 1)

        self.lineEdit_19 = QLineEdit(self.tab_18)
        self.lineEdit_19.setObjectName(u"lineEdit_19")

        self.gridLayout_20.addWidget(self.lineEdit_19, 3, 2, 1, 1)

        self.checkBox_21 = QCheckBox(self.tab_18)
        self.checkBox_21.setObjectName(u"checkBox_21")

        self.gridLayout_20.addWidget(self.checkBox_21, 4, 2, 1, 1)

        self.checkBox_19 = QCheckBox(self.tab_18)
        self.checkBox_19.setObjectName(u"checkBox_19")

        self.gridLayout_20.addWidget(self.checkBox_19, 5, 2, 1, 1)

        self.checkBox_20 = QCheckBox(self.tab_18)
        self.checkBox_20.setObjectName(u"checkBox_20")

        self.gridLayout_20.addWidget(self.checkBox_20, 6, 2, 1, 1)

        self.osint_dork_generate = QPushButton(self.tab_18)
        self.osint_dork_generate.setObjectName(u"osint_dork_generate")

        self.gridLayout_20.addWidget(self.osint_dork_generate, 7, 0, 1, 5)

        self.tabWidget_3 = QTabWidget(self.tab_18)
        self.tabWidget_3.setObjectName(u"tabWidget_3")
        self.tab_31 = QWidget()
        self.tab_31.setObjectName(u"tab_31")
        self.gridLayout_32 = QGridLayout(self.tab_31)
        self.gridLayout_32.setObjectName(u"gridLayout_32")
        self.osint_dork_output = QTextEdit(self.tab_31)
        self.osint_dork_output.setObjectName(u"osint_dork_output")

        self.gridLayout_32.addWidget(self.osint_dork_output, 0, 0, 1, 1)

        self.tabWidget_3.addTab(self.tab_31, "")
        self.tab_42 = QWidget()
        self.tab_42.setObjectName(u"tab_42")
        self.lineEdit_18 = QLineEdit(self.tab_42)
        self.lineEdit_18.setObjectName(u"lineEdit_18")
        self.lineEdit_18.setGeometry(QRect(380, 110, 671, 27))
        self.tabWidget_3.addTab(self.tab_42, "")

        self.gridLayout_20.addWidget(self.tabWidget_3, 8, 0, 1, 5)

        self.osint_dork.addTab(self.tab_18, "")
        self.tab_14 = QWidget()
        self.tab_14.setObjectName(u"tab_14")
        self.lineEdit_8 = QLineEdit(self.tab_14)
        self.lineEdit_8.setObjectName(u"lineEdit_8")
        self.lineEdit_8.setGeometry(QRect(150, 320, 751, 27))
        self.osint_dork.addTab(self.tab_14, "")

        self.gridLayout_5.addWidget(self.osint_dork, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab_4, "")
        self.tab_22 = QWidget()
        self.tab_22.setObjectName(u"tab_22")
        self.gridLayout_17 = QGridLayout(self.tab_22)
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.tabWidget_8 = QTabWidget(self.tab_22)
        self.tabWidget_8.setObjectName(u"tabWidget_8")
        self.tab_24 = QWidget()
        self.tab_24.setObjectName(u"tab_24")
        self.gridLayout_22 = QGridLayout(self.tab_24)
        self.gridLayout_22.setObjectName(u"gridLayout_22")
        self.label_16 = QLabel(self.tab_24)
        self.label_16.setObjectName(u"label_16")

        self.gridLayout_22.addWidget(self.label_16, 0, 0, 1, 1)

        self.comboBox_2 = QComboBox(self.tab_24)
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")

        self.gridLayout_22.addWidget(self.comboBox_2, 1, 0, 1, 1)

        self.portscan_start_4 = QPushButton(self.tab_24)
        self.portscan_start_4.setObjectName(u"portscan_start_4")

        self.gridLayout_22.addWidget(self.portscan_start_4, 1, 1, 1, 1)

        self.scrollArea = QScrollArea(self.tab_24)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 1395, 620))
        self.dashboard_portscan_IP = QLineEdit(self.scrollAreaWidgetContents)
        self.dashboard_portscan_IP.setObjectName(u"dashboard_portscan_IP")
        self.dashboard_portscan_IP.setGeometry(QRect(10, 40, 211, 27))
        self.dashboard_portscan_stealth_check = QCheckBox(self.scrollAreaWidgetContents)
        self.dashboard_portscan_stealth_check.setObjectName(u"dashboard_portscan_stealth_check")
        self.dashboard_portscan_stealth_check.setGeometry(QRect(100, 140, 100, 25))
        self.dashboard_portscan_stealth_check.setMaximumSize(QSize(100, 16777215))
        self.checkBox_6 = QCheckBox(self.scrollAreaWidgetContents)
        self.checkBox_6.setObjectName(u"checkBox_6")
        self.checkBox_6.setGeometry(QRect(100, 160, 100, 25))
        self.checkBox_6.setMaximumSize(QSize(100, 16777215))
        self.dashboard_portscan_standard_check = QCheckBox(self.scrollAreaWidgetContents)
        self.dashboard_portscan_standard_check.setObjectName(u"dashboard_portscan_standard_check")
        self.dashboard_portscan_standard_check.setGeometry(QRect(10, 139, 100, 25))
        self.dashboard_portscan_standard_check.setMaximumSize(QSize(100, 16777215))
        self.dashboard_portscan_extraport = QLineEdit(self.scrollAreaWidgetContents)
        self.dashboard_portscan_extraport.setObjectName(u"dashboard_portscan_extraport")
        self.dashboard_portscan_extraport.setGeometry(QRect(10, 106, 211, 27))
        self.dashboard_portscan_maxport = QLineEdit(self.scrollAreaWidgetContents)
        self.dashboard_portscan_maxport.setObjectName(u"dashboard_portscan_maxport")
        self.dashboard_portscan_maxport.setGeometry(QRect(120, 75, 101, 27))
        self.dashboard_portscan_fast_check = QCheckBox(self.scrollAreaWidgetContents)
        self.dashboard_portscan_fast_check.setObjectName(u"dashboard_portscan_fast_check")
        self.dashboard_portscan_fast_check.setGeometry(QRect(10, 160, 100, 25))
        self.dashboard_portscan_fast_check.setMaximumSize(QSize(100, 16777215))
        self.dashboard_portscan_minport = QLineEdit(self.scrollAreaWidgetContents)
        self.dashboard_portscan_minport.setObjectName(u"dashboard_portscan_minport")
        self.dashboard_portscan_minport.setGeometry(QRect(10, 75, 101, 27))
        self.label_21 = QLabel(self.scrollAreaWidgetContents)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setGeometry(QRect(10, 10, 66, 19))
        self.line_4 = QFrame(self.scrollAreaWidgetContents)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setGeometry(QRect(10, 200, 211, 31))
        self.line_4.setFrameShape(QFrame.HLine)
        self.line_4.setFrameShadow(QFrame.Sunken)
        self.dashboard_dnsName = QLineEdit(self.scrollAreaWidgetContents)
        self.dashboard_dnsName.setObjectName(u"dashboard_dnsName")
        self.dashboard_dnsName.setGeometry(QRect(240, 80, 211, 27))
        self.label_22 = QLabel(self.scrollAreaWidgetContents)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setGeometry(QRect(240, 10, 91, 19))
        self.line_6 = QFrame(self.scrollAreaWidgetContents)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setGeometry(QRect(220, 10, 16, 211))
        self.line_6.setFrameShape(QFrame.VLine)
        self.line_6.setFrameShadow(QFrame.Sunken)
        self.line_5 = QFrame(self.scrollAreaWidgetContents)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setGeometry(QRect(240, 200, 211, 31))
        self.line_5.setFrameShape(QFrame.HLine)
        self.line_5.setFrameShadow(QFrame.Sunken)
        self.lineEdit_9 = QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_9.setObjectName(u"lineEdit_9")
        self.lineEdit_9.setGeometry(QRect(140, 370, 751, 27))
        self.label_38 = QLabel(self.scrollAreaWidgetContents)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setGeometry(QRect(240, 50, 111, 19))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout_22.addWidget(self.scrollArea, 2, 0, 1, 2)

        self.progressBar_8 = QProgressBar(self.tab_24)
        self.progressBar_8.setObjectName(u"progressBar_8")
        self.progressBar_8.setValue(24)

        self.gridLayout_22.addWidget(self.progressBar_8, 3, 0, 1, 2)

        self.tabWidget_8.addTab(self.tab_24, "")
        self.tab_23 = QWidget()
        self.tab_23.setObjectName(u"tab_23")
        self.gridLayout_18 = QGridLayout(self.tab_23)
        self.gridLayout_18.setObjectName(u"gridLayout_18")
        self.line = QFrame(self.tab_23)
        self.line.setObjectName(u"line")
        self.line.setMinimumSize(QSize(5, 0))
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridLayout_18.addWidget(self.line, 0, 6, 15, 1)

        self.portscan_fast_timeout = QComboBox(self.tab_23)
        self.portscan_fast_timeout.addItem("")
        self.portscan_fast_timeout.addItem("")
        self.portscan_fast_timeout.addItem("")
        self.portscan_fast_timeout.addItem("")
        self.portscan_fast_timeout.addItem("")
        self.portscan_fast_timeout.setObjectName(u"portscan_fast_timeout")

        self.gridLayout_18.addWidget(self.portscan_fast_timeout, 12, 0, 1, 1)

        self.stealth_bar = QProgressBar(self.tab_23)
        self.stealth_bar.setObjectName(u"stealth_bar")
        self.stealth_bar.setValue(88)

        self.gridLayout_18.addWidget(self.stealth_bar, 1, 7, 1, 1)

        self.line_14 = QFrame(self.tab_23)
        self.line_14.setObjectName(u"line_14")
        self.line_14.setFrameShape(QFrame.HLine)
        self.line_14.setFrameShadow(QFrame.Sunken)

        self.gridLayout_18.addWidget(self.line_14, 7, 0, 1, 4)

        self.portscan_delay = QComboBox(self.tab_23)
        self.portscan_delay.addItem("")
        self.portscan_delay.addItem("")
        self.portscan_delay.addItem("")
        self.portscan_delay.addItem("")
        self.portscan_delay.addItem("")
        self.portscan_delay.setObjectName(u"portscan_delay")

        self.gridLayout_18.addWidget(self.portscan_delay, 12, 1, 1, 3)

        self.line_13 = QFrame(self.tab_23)
        self.line_13.setObjectName(u"line_13")
        self.line_13.setFrameShape(QFrame.HLine)
        self.line_13.setFrameShadow(QFrame.Sunken)

        self.gridLayout_18.addWidget(self.line_13, 10, 0, 1, 4)

        self.tabWidget_9 = QTabWidget(self.tab_23)
        self.tabWidget_9.setObjectName(u"tabWidget_9")
        self.tab_25 = QWidget()
        self.tab_25.setObjectName(u"tab_25")
        self.gridLayout_19 = QGridLayout(self.tab_25)
        self.gridLayout_19.setObjectName(u"gridLayout_19")
        self.DB_Query_scanning_portscan = QLineEdit(self.tab_25)
        self.DB_Query_scanning_portscan.setObjectName(u"DB_Query_scanning_portscan")

        self.gridLayout_19.addWidget(self.DB_Query_scanning_portscan, 1, 0, 1, 2)

        self.table_RefreshDB_Button_scanning_portscan = QPushButton(self.tab_25)
        self.table_RefreshDB_Button_scanning_portscan.setObjectName(u"table_RefreshDB_Button_scanning_portscan")

        self.gridLayout_19.addWidget(self.table_RefreshDB_Button_scanning_portscan, 2, 0, 1, 1)

        self.scanning_portscan_db = QTableWidget(self.tab_25)
        self.scanning_portscan_db.setObjectName(u"scanning_portscan_db")

        self.gridLayout_19.addWidget(self.scanning_portscan_db, 0, 0, 1, 2)

        self.table_QueryDB_Button_scanning_portscan = QPushButton(self.tab_25)
        self.table_QueryDB_Button_scanning_portscan.setObjectName(u"table_QueryDB_Button_scanning_portscan")

        self.gridLayout_19.addWidget(self.table_QueryDB_Button_scanning_portscan, 2, 1, 1, 1)

        self.tabWidget_9.addTab(self.tab_25, "")
        self.tab_26 = QWidget()
        self.tab_26.setObjectName(u"tab_26")
        self.tabWidget_9.addTab(self.tab_26, "")

        self.gridLayout_18.addWidget(self.tabWidget_9, 15, 0, 1, 8)

        self.portscan_stealth_check = QCheckBox(self.tab_23)
        self.portscan_stealth_check.setObjectName(u"portscan_stealth_check")
        self.portscan_stealth_check.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_18.addWidget(self.portscan_stealth_check, 8, 1, 1, 1)

        self.portscan_standard_check = QCheckBox(self.tab_23)
        self.portscan_standard_check.setObjectName(u"portscan_standard_check")
        self.portscan_standard_check.setMaximumSize(QSize(16777215, 16777215))
        self.portscan_standard_check.setChecked(True)

        self.gridLayout_18.addWidget(self.portscan_standard_check, 8, 0, 1, 1)

        self.portscan_fast_check = QCheckBox(self.tab_23)
        self.portscan_fast_check.setObjectName(u"portscan_fast_check")
        self.portscan_fast_check.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_18.addWidget(self.portscan_fast_check, 9, 0, 1, 1)

        self.label_61 = QLabel(self.tab_23)
        self.label_61.setObjectName(u"label_61")

        self.gridLayout_18.addWidget(self.label_61, 11, 0, 1, 1)

        self.portscan_IP = QLineEdit(self.tab_23)
        self.portscan_IP.setObjectName(u"portscan_IP")

        self.gridLayout_18.addWidget(self.portscan_IP, 1, 0, 1, 4)

        self.line_9 = QFrame(self.tab_23)
        self.line_9.setObjectName(u"line_9")
        self.line_9.setFrameShape(QFrame.HLine)
        self.line_9.setFrameShadow(QFrame.Sunken)

        self.gridLayout_18.addWidget(self.line_9, 14, 0, 1, 5)

        self.checkBox_4 = QCheckBox(self.tab_23)
        self.checkBox_4.setObjectName(u"checkBox_4")
        self.checkBox_4.setMaximumSize(QSize(200, 16777215))

        self.gridLayout_18.addWidget(self.checkBox_4, 9, 1, 1, 1)

        self.portscan_minport = QLineEdit(self.tab_23)
        self.portscan_minport.setObjectName(u"portscan_minport")

        self.gridLayout_18.addWidget(self.portscan_minport, 2, 0, 2, 3)

        self.label_13 = QLabel(self.tab_23)
        self.label_13.setObjectName(u"label_13")

        self.gridLayout_18.addWidget(self.label_13, 0, 7, 1, 1)

        self.portscan_extraport = QLineEdit(self.tab_23)
        self.portscan_extraport.setObjectName(u"portscan_extraport")

        self.gridLayout_18.addWidget(self.portscan_extraport, 5, 0, 2, 4)

        self.portscan_maxport = QLineEdit(self.tab_23)
        self.portscan_maxport.setObjectName(u"portscan_maxport")

        self.gridLayout_18.addWidget(self.portscan_maxport, 2, 3, 2, 1)

        self.portscan_start = QPushButton(self.tab_23)
        self.portscan_start.setObjectName(u"portscan_start")

        self.gridLayout_18.addWidget(self.portscan_start, 13, 0, 1, 4)

        self.portscan_1_1024 = QRadioButton(self.tab_23)
        self.portscan_1_1024.setObjectName(u"portscan_1_1024")
        self.portscan_1_1024.setChecked(True)

        self.gridLayout_18.addWidget(self.portscan_1_1024, 4, 0, 1, 1)

        self.portscan_1_10000 = QRadioButton(self.tab_23)
        self.portscan_1_10000.setObjectName(u"portscan_1_10000")

        self.gridLayout_18.addWidget(self.portscan_1_10000, 4, 1, 1, 1)

        self.portscan_1_65535 = QRadioButton(self.tab_23)
        self.portscan_1_65535.setObjectName(u"portscan_1_65535")

        self.gridLayout_18.addWidget(self.portscan_1_65535, 4, 2, 1, 1)

        self.label_60 = QLabel(self.tab_23)
        self.label_60.setObjectName(u"label_60")

        self.gridLayout_18.addWidget(self.label_60, 11, 1, 1, 1)

        self.tabWidget_13 = QTabWidget(self.tab_23)
        self.tabWidget_13.setObjectName(u"tabWidget_13")
        self.tab_61 = QWidget()
        self.tab_61.setObjectName(u"tab_61")
        self.gridLayout_45 = QGridLayout(self.tab_61)
        self.gridLayout_45.setObjectName(u"gridLayout_45")
        self.portscan_liveports_browser = QTextEdit(self.tab_61)
        self.portscan_liveports_browser.setObjectName(u"portscan_liveports_browser")

        self.gridLayout_45.addWidget(self.portscan_liveports_browser, 0, 0, 1, 1)

        self.tabWidget_13.addTab(self.tab_61, "")
        self.tab_62 = QWidget()
        self.tab_62.setObjectName(u"tab_62")
        self.tabWidget_13.addTab(self.tab_62, "")

        self.gridLayout_18.addWidget(self.tabWidget_13, 2, 7, 13, 1)

        self.tabWidget_8.addTab(self.tab_23, "")
        self.tab_16 = QWidget()
        self.tab_16.setObjectName(u"tab_16")
        self.gridLayout_13 = QGridLayout(self.tab_16)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.label_30 = QLabel(self.tab_16)
        self.label_30.setObjectName(u"label_30")
        font4 = QFont()
        font4.setPointSize(10)
        font4.setUnderline(False)
        self.label_30.setFont(font4)

        self.gridLayout_13.addWidget(self.label_30, 6, 0, 1, 1)

        self.scanning_dns_query = QLineEdit(self.tab_16)
        self.scanning_dns_query.setObjectName(u"scanning_dns_query")

        self.gridLayout_13.addWidget(self.scanning_dns_query, 0, 0, 1, 2)

        self.dns_TXT_table = QTableWidget(self.tab_16)
        self.dns_TXT_table.setObjectName(u"dns_TXT_table")

        self.gridLayout_13.addWidget(self.dns_TXT_table, 3, 1, 1, 1)

        self.dns_MX_table = QTableWidget(self.tab_16)
        self.dns_MX_table.setObjectName(u"dns_MX_table")

        self.gridLayout_13.addWidget(self.dns_MX_table, 7, 0, 1, 1)

        self.label_28 = QLabel(self.tab_16)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setFont(font4)

        self.gridLayout_13.addWidget(self.label_28, 4, 0, 1, 1)

        self.dns_Reverse_table = QTableWidget(self.tab_16)
        self.dns_Reverse_table.setObjectName(u"dns_Reverse_table")

        self.gridLayout_13.addWidget(self.dns_Reverse_table, 9, 0, 1, 1)

        self.scanning_dns_lookup = QPushButton(self.tab_16)
        self.scanning_dns_lookup.setObjectName(u"scanning_dns_lookup")

        self.gridLayout_13.addWidget(self.scanning_dns_lookup, 1, 1, 1, 1)

        self.label_29 = QLabel(self.tab_16)
        self.label_29.setObjectName(u"label_29")
        font5 = QFont()
        font5.setPointSize(10)
        self.label_29.setFont(font5)

        self.gridLayout_13.addWidget(self.label_29, 4, 1, 1, 1)

        self.dns_CNAME_table = QTableWidget(self.tab_16)
        self.dns_CNAME_table.setObjectName(u"dns_CNAME_table")

        self.gridLayout_13.addWidget(self.dns_CNAME_table, 5, 0, 1, 1)

        self.comboBox = QComboBox(self.tab_16)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")

        self.gridLayout_13.addWidget(self.comboBox, 1, 0, 1, 1)

        self.label_31 = QLabel(self.tab_16)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setFont(font4)

        self.gridLayout_13.addWidget(self.label_31, 8, 0, 1, 1)

        self.dns_a_table = QTableWidget(self.tab_16)
        self.dns_a_table.setObjectName(u"dns_a_table")

        self.gridLayout_13.addWidget(self.dns_a_table, 3, 0, 1, 1)

        self.label_26 = QLabel(self.tab_16)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setMaximumSize(QSize(16777215, 15))
        self.label_26.setFont(font5)

        self.gridLayout_13.addWidget(self.label_26, 2, 0, 1, 1)

        self.scanning_dns_A_4 = QTextEdit(self.tab_16)
        self.scanning_dns_A_4.setObjectName(u"scanning_dns_A_4")

        self.gridLayout_13.addWidget(self.scanning_dns_A_4, 7, 1, 1, 1)

        self.label_27 = QLabel(self.tab_16)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setFont(font5)

        self.gridLayout_13.addWidget(self.label_27, 2, 1, 1, 1)

        self.dns_NS_table = QTableWidget(self.tab_16)
        self.dns_NS_table.setObjectName(u"dns_NS_table")

        self.gridLayout_13.addWidget(self.dns_NS_table, 5, 1, 1, 1)

        self.test_table = QTableWidget(self.tab_16)
        self.test_table.setObjectName(u"test_table")

        self.gridLayout_13.addWidget(self.test_table, 9, 1, 1, 1)

        self.tabWidget_8.addTab(self.tab_16, "")

        self.gridLayout_17.addWidget(self.tabWidget_8, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab_22, "")
        self.tab_41 = QWidget()
        self.tab_41.setObjectName(u"tab_41")
        self.gridLayout_31 = QGridLayout(self.tab_41)
        self.gridLayout_31.setObjectName(u"gridLayout_31")
        self.tabWidget_6 = QTabWidget(self.tab_41)
        self.tabWidget_6.setObjectName(u"tabWidget_6")
        self.webdir_bf = QWidget()
        self.webdir_bf.setObjectName(u"webdir_bf")
        self.gridLayout_16 = QGridLayout(self.webdir_bf)
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.bruteforce_delay = QDoubleSpinBox(self.webdir_bf)
        self.bruteforce_delay.setObjectName(u"bruteforce_delay")
        self.bruteforce_delay.setValue(1.000000000000000)

        self.gridLayout_16.addWidget(self.bruteforce_delay, 7, 4, 1, 1)

        self.bruteforce_pass_browse = QPushButton(self.webdir_bf)
        self.bruteforce_pass_browse.setObjectName(u"bruteforce_pass_browse")

        self.gridLayout_16.addWidget(self.bruteforce_pass_browse, 4, 3, 1, 1)

        self.label_143 = QLabel(self.webdir_bf)
        self.label_143.setObjectName(u"label_143")
        self.label_143.setMaximumSize(QSize(200, 15))

        self.gridLayout_16.addWidget(self.label_143, 6, 4, 1, 2)

        self.bruteforce_livetries = QLineEdit(self.webdir_bf)
        self.bruteforce_livetries.setObjectName(u"bruteforce_livetries")

        self.gridLayout_16.addWidget(self.bruteforce_livetries, 3, 4, 1, 1)

        self.label_145 = QLabel(self.webdir_bf)
        self.label_145.setObjectName(u"label_145")
        self.label_145.setMaximumSize(QSize(16777215, 15))

        self.gridLayout_16.addWidget(self.label_145, 3, 0, 1, 1)

        self.bruteforce_batchsize = QSpinBox(self.webdir_bf)
        self.bruteforce_batchsize.setObjectName(u"bruteforce_batchsize")
        self.bruteforce_batchsize.setMaximum(100000)
        self.bruteforce_batchsize.setValue(10)

        self.gridLayout_16.addWidget(self.bruteforce_batchsize, 2, 3, 1, 1)

        self.bruteforce_user_browse = QPushButton(self.webdir_bf)
        self.bruteforce_user_browse.setObjectName(u"bruteforce_user_browse")

        self.gridLayout_16.addWidget(self.bruteforce_user_browse, 4, 1, 1, 1)

        self.bruteforce_port = QLineEdit(self.webdir_bf)
        self.bruteforce_port.setObjectName(u"bruteforce_port")

        self.gridLayout_16.addWidget(self.bruteforce_port, 1, 2, 1, 2)

        self.bruteforce_target = QLineEdit(self.webdir_bf)
        self.bruteforce_target.setObjectName(u"bruteforce_target")

        self.gridLayout_16.addWidget(self.bruteforce_target, 1, 0, 1, 2)

        self.label_148 = QLabel(self.webdir_bf)
        self.label_148.setObjectName(u"label_148")
        self.label_148.setMaximumSize(QSize(16777215, 15))

        self.gridLayout_16.addWidget(self.label_148, 0, 0, 1, 2)

        self.bruteforce_stop = QPushButton(self.webdir_bf)
        self.bruteforce_stop.setObjectName(u"bruteforce_stop")

        self.gridLayout_16.addWidget(self.bruteforce_stop, 11, 4, 1, 1)

        self.label_71 = QLabel(self.webdir_bf)
        self.label_71.setObjectName(u"label_71")

        self.gridLayout_16.addWidget(self.label_71, 2, 2, 1, 1)

        self.bruteforce_start = QPushButton(self.webdir_bf)
        self.bruteforce_start.setObjectName(u"bruteforce_start")

        self.gridLayout_16.addWidget(self.bruteforce_start, 10, 4, 1, 1)

        self.bruteforce_threads = QSpinBox(self.webdir_bf)
        self.bruteforce_threads.setObjectName(u"bruteforce_threads")
        self.bruteforce_threads.setValue(10)

        self.gridLayout_16.addWidget(self.bruteforce_threads, 9, 4, 1, 1)

        self.bruteforce_progressbar = QProgressBar(self.webdir_bf)
        self.bruteforce_progressbar.setObjectName(u"bruteforce_progressbar")
        self.bruteforce_progressbar.setValue(0)

        self.gridLayout_16.addWidget(self.bruteforce_progressbar, 1, 4, 1, 1)

        self.bruteforce_passdir = QLineEdit(self.webdir_bf)
        self.bruteforce_passdir.setObjectName(u"bruteforce_passdir")

        self.gridLayout_16.addWidget(self.bruteforce_passdir, 4, 2, 1, 1)

        self.comboBox_5 = QComboBox(self.webdir_bf)
        self.comboBox_5.addItem("")
        self.comboBox_5.setObjectName(u"comboBox_5")

        self.gridLayout_16.addWidget(self.comboBox_5, 4, 4, 1, 1)

        self.label_55 = QLabel(self.webdir_bf)
        self.label_55.setObjectName(u"label_55")
        self.label_55.setMinimumSize(QSize(0, 0))
        self.label_55.setMaximumSize(QSize(16777215, 15))

        self.gridLayout_16.addWidget(self.label_55, 8, 4, 1, 2)

        self.bruteforce_panel = QTabWidget(self.webdir_bf)
        self.bruteforce_panel.setObjectName(u"bruteforce_panel")
        self.bruteforce_panel.setMaximumSize(QSize(16777215, 16777215))
        self.tab_46 = QWidget()
        self.tab_46.setObjectName(u"tab_46")
        self.gridLayout_33 = QGridLayout(self.tab_46)
        self.gridLayout_33.setObjectName(u"gridLayout_33")
        self.bruteforce_goodcreds = QTextEdit(self.tab_46)
        self.bruteforce_goodcreds.setObjectName(u"bruteforce_goodcreds")
        self.bruteforce_goodcreds.setMaximumSize(QSize(1677700, 16777215))

        self.gridLayout_33.addWidget(self.bruteforce_goodcreds, 0, 0, 1, 1)

        self.bruteforce_panel.addTab(self.tab_46, "")
        self.tab_47 = QWidget()
        self.tab_47.setObjectName(u"tab_47")
        self.gridLayout_34 = QGridLayout(self.tab_47)
        self.gridLayout_34.setObjectName(u"gridLayout_34")
        self.bruteforce_currentbatch = QTextEdit(self.tab_47)
        self.bruteforce_currentbatch.setObjectName(u"bruteforce_currentbatch")

        self.gridLayout_34.addWidget(self.bruteforce_currentbatch, 0, 0, 1, 1)

        self.bruteforce_panel.addTab(self.tab_47, "")
        self.tab_51 = QWidget()
        self.tab_51.setObjectName(u"tab_51")
        self.gridLayout_38 = QGridLayout(self.tab_51)
        self.gridLayout_38.setObjectName(u"gridLayout_38")
        self.bruteforce_errlog = QTextEdit(self.tab_51)
        self.bruteforce_errlog.setObjectName(u"bruteforce_errlog")

        self.gridLayout_38.addWidget(self.bruteforce_errlog, 0, 0, 1, 1)

        self.bruteforce_panel.addTab(self.tab_51, "")

        self.gridLayout_16.addWidget(self.bruteforce_panel, 5, 4, 1, 1)

        self.bruteforce_protocol = QComboBox(self.webdir_bf)
        self.bruteforce_protocol.addItem("")
        self.bruteforce_protocol.addItem("")
        self.bruteforce_protocol.addItem("")
        self.bruteforce_protocol.addItem("")
        self.bruteforce_protocol.addItem("")
        self.bruteforce_protocol.addItem("")
        self.bruteforce_protocol.setObjectName(u"bruteforce_protocol")

        self.gridLayout_16.addWidget(self.bruteforce_protocol, 2, 0, 1, 2)

        self.label_142 = QLabel(self.webdir_bf)
        self.label_142.setObjectName(u"label_142")
        self.label_142.setMaximumSize(QSize(100, 16777215))

        self.gridLayout_16.addWidget(self.label_142, 0, 2, 1, 1)

        self.label_150 = QLabel(self.webdir_bf)
        self.label_150.setObjectName(u"label_150")

        self.gridLayout_16.addWidget(self.label_150, 0, 4, 1, 1)

        self.bruteforce_userdir = QLineEdit(self.webdir_bf)
        self.bruteforce_userdir.setObjectName(u"bruteforce_userdir")

        self.gridLayout_16.addWidget(self.bruteforce_userdir, 4, 0, 1, 1)

        self.label_147 = QLabel(self.webdir_bf)
        self.label_147.setObjectName(u"label_147")
        self.label_147.setMaximumSize(QSize(16777215, 15))

        self.gridLayout_16.addWidget(self.label_147, 3, 2, 1, 1)

        self.label_149 = QLabel(self.webdir_bf)
        self.label_149.setObjectName(u"label_149")

        self.gridLayout_16.addWidget(self.label_149, 2, 4, 1, 1)

        self.tabWidget_14 = QTabWidget(self.webdir_bf)
        self.tabWidget_14.setObjectName(u"tabWidget_14")
        self.tab_87 = QWidget()
        self.tab_87.setObjectName(u"tab_87")
        self.gridLayout_62 = QGridLayout(self.tab_87)
        self.gridLayout_62.setObjectName(u"gridLayout_62")
        self.DB_Query_scanning_bruteforce = QLineEdit(self.tab_87)
        self.DB_Query_scanning_bruteforce.setObjectName(u"DB_Query_scanning_bruteforce")

        self.gridLayout_62.addWidget(self.DB_Query_scanning_bruteforce, 1, 0, 1, 2)

        self.scanning_bruteforce_refresh = QPushButton(self.tab_87)
        self.scanning_bruteforce_refresh.setObjectName(u"scanning_bruteforce_refresh")

        self.gridLayout_62.addWidget(self.scanning_bruteforce_refresh, 2, 0, 1, 1)

        self.scanning_bruteforce_db = QTableWidget(self.tab_87)
        self.scanning_bruteforce_db.setObjectName(u"scanning_bruteforce_db")

        self.gridLayout_62.addWidget(self.scanning_bruteforce_db, 0, 0, 1, 2)

        self.scanning_bruteforce_query = QPushButton(self.tab_87)
        self.scanning_bruteforce_query.setObjectName(u"scanning_bruteforce_query")

        self.gridLayout_62.addWidget(self.scanning_bruteforce_query, 2, 1, 1, 1)

        self.tabWidget_14.addTab(self.tab_87, "")
        self.tab_44 = QWidget()
        self.tab_44.setObjectName(u"tab_44")
        self.gridLayout_37 = QGridLayout(self.tab_44)
        self.gridLayout_37.setObjectName(u"gridLayout_37")
        self.lineEdit_21 = QLineEdit(self.tab_44)
        self.lineEdit_21.setObjectName(u"lineEdit_21")

        self.gridLayout_37.addWidget(self.lineEdit_21, 2, 2, 1, 1)

        self.bruteforce_download_seclist_topshort = QPushButton(self.tab_44)
        self.bruteforce_download_seclist_topshort.setObjectName(u"bruteforce_download_seclist_topshort")
        font6 = QFont()
        font6.setStrikeOut(False)
        self.bruteforce_download_seclist_topshort.setFont(font6)
        self.bruteforce_download_seclist_topshort.setAutoDefault(False)
        self.bruteforce_download_seclist_topshort.setFlat(False)

        self.gridLayout_37.addWidget(self.bruteforce_download_seclist_topshort, 3, 1, 1, 1)

        self.bruteforce_download_seclist_defaults = QPushButton(self.tab_44)
        self.bruteforce_download_seclist_defaults.setObjectName(u"bruteforce_download_seclist_defaults")

        self.gridLayout_37.addWidget(self.bruteforce_download_seclist_defaults, 2, 3, 1, 1)

        self.lineEdit_23 = QLineEdit(self.tab_44)
        self.lineEdit_23.setObjectName(u"lineEdit_23")

        self.gridLayout_37.addWidget(self.lineEdit_23, 3, 0, 1, 1)

        self.label_74 = QLabel(self.tab_44)
        self.label_74.setObjectName(u"label_74")
        self.label_74.setMaximumSize(QSize(16777215, 20))
        font7 = QFont()
        font7.setBold(True)
        font7.setUnderline(True)
        self.label_74.setFont(font7)

        self.gridLayout_37.addWidget(self.label_74, 1, 0, 1, 1)

        self.lineEdit_20 = QLineEdit(self.tab_44)
        self.lineEdit_20.setObjectName(u"lineEdit_20")

        self.gridLayout_37.addWidget(self.lineEdit_20, 4, 2, 1, 1)

        self.bruteforce_download_seclist_top10mil_usernames = QPushButton(self.tab_44)
        self.bruteforce_download_seclist_top10mil_usernames.setObjectName(u"bruteforce_download_seclist_top10mil_usernames")
        self.bruteforce_download_seclist_top10mil_usernames.setFont(font6)
        self.bruteforce_download_seclist_top10mil_usernames.setAutoDefault(False)
        self.bruteforce_download_seclist_top10mil_usernames.setFlat(False)

        self.gridLayout_37.addWidget(self.bruteforce_download_seclist_top10mil_usernames, 2, 1, 1, 1)

        self.bruteforce_download_seclist_top10mil = QPushButton(self.tab_44)
        self.bruteforce_download_seclist_top10mil.setObjectName(u"bruteforce_download_seclist_top10mil")

        self.gridLayout_37.addWidget(self.bruteforce_download_seclist_top10mil, 3, 3, 1, 1)

        self.lineEdit_24 = QLineEdit(self.tab_44)
        self.lineEdit_24.setObjectName(u"lineEdit_24")

        self.gridLayout_37.addWidget(self.lineEdit_24, 3, 2, 1, 1)

        self.bruteforce_download_ignis_1M = QPushButton(self.tab_44)
        self.bruteforce_download_ignis_1M.setObjectName(u"bruteforce_download_ignis_1M")

        self.gridLayout_37.addWidget(self.bruteforce_download_ignis_1M, 4, 3, 1, 1)

        self.lineEdit_22 = QLineEdit(self.tab_44)
        self.lineEdit_22.setObjectName(u"lineEdit_22")

        self.gridLayout_37.addWidget(self.lineEdit_22, 2, 0, 1, 1)

        self.label_73 = QLabel(self.tab_44)
        self.label_73.setObjectName(u"label_73")
        self.label_73.setFont(font7)

        self.gridLayout_37.addWidget(self.label_73, 0, 2, 1, 1)

        self.tabWidget_14.addTab(self.tab_44, "")
        self.lineEdit_23.raise_()
        self.lineEdit_22.raise_()
        self.bruteforce_download_seclist_topshort.raise_()
        self.bruteforce_download_seclist_top10mil_usernames.raise_()
        self.bruteforce_download_seclist_defaults.raise_()
        self.lineEdit_21.raise_()
        self.bruteforce_download_seclist_top10mil.raise_()
        self.lineEdit_20.raise_()
        self.lineEdit_24.raise_()
        self.bruteforce_download_ignis_1M.raise_()
        self.label_73.raise_()
        self.label_74.raise_()
        self.tab_45 = QWidget()
        self.tab_45.setObjectName(u"tab_45")
        self.tabWidget_14.addTab(self.tab_45, "")

        self.gridLayout_16.addWidget(self.tabWidget_14, 5, 0, 7, 4)

        self.tabWidget_6.addTab(self.webdir_bf, "")
        self.tab_43 = QWidget()
        self.tab_43.setObjectName(u"tab_43")
        self.gridLayout_98 = QGridLayout(self.tab_43)
        self.gridLayout_98.setObjectName(u"gridLayout_98")
        self.bruteforce_fuzz_delay = QDoubleSpinBox(self.tab_43)
        self.bruteforce_fuzz_delay.setObjectName(u"bruteforce_fuzz_delay")
        self.bruteforce_fuzz_delay.setValue(1.000000000000000)

        self.gridLayout_98.addWidget(self.bruteforce_fuzz_delay, 13, 5, 1, 1)

        self.bruteforce_fuzz_url = QTextEdit(self.tab_43)
        self.bruteforce_fuzz_url.setObjectName(u"bruteforce_fuzz_url")

        self.gridLayout_98.addWidget(self.bruteforce_fuzz_url, 1, 0, 4, 5)

        self.label_161 = QLabel(self.tab_43)
        self.label_161.setObjectName(u"label_161")
        self.label_161.setMaximumSize(QSize(16777215, 20))

        self.gridLayout_98.addWidget(self.label_161, 5, 0, 1, 1)

        self.bruteforce_fuzz_progressbar = QProgressBar(self.tab_43)
        self.bruteforce_fuzz_progressbar.setObjectName(u"bruteforce_fuzz_progressbar")
        self.bruteforce_fuzz_progressbar.setValue(0)

        self.gridLayout_98.addWidget(self.bruteforce_fuzz_progressbar, 1, 5, 1, 1)

        self.bruteforce_fuzz_livetries = QLineEdit(self.tab_43)
        self.bruteforce_fuzz_livetries.setObjectName(u"bruteforce_fuzz_livetries")

        self.gridLayout_98.addWidget(self.bruteforce_fuzz_livetries, 3, 5, 1, 1)

        self.bruteforce_fuzz_wordlistdir = QLineEdit(self.tab_43)
        self.bruteforce_fuzz_wordlistdir.setObjectName(u"bruteforce_fuzz_wordlistdir")

        self.gridLayout_98.addWidget(self.bruteforce_fuzz_wordlistdir, 6, 0, 1, 1)

        self.bruteforce_fuzz_wordlist_browse = QPushButton(self.tab_43)
        self.bruteforce_fuzz_wordlist_browse.setObjectName(u"bruteforce_fuzz_wordlist_browse")

        self.gridLayout_98.addWidget(self.bruteforce_fuzz_wordlist_browse, 6, 1, 1, 1)

        self.bruteforce_fuzz_start = QPushButton(self.tab_43)
        self.bruteforce_fuzz_start.setObjectName(u"bruteforce_fuzz_start")

        self.gridLayout_98.addWidget(self.bruteforce_fuzz_start, 16, 5, 1, 1)

        self.bruteforce_fuzz_batchsize = QSpinBox(self.tab_43)
        self.bruteforce_fuzz_batchsize.setObjectName(u"bruteforce_fuzz_batchsize")
        self.bruteforce_fuzz_batchsize.setMaximum(100000)
        self.bruteforce_fuzz_batchsize.setValue(10)

        self.gridLayout_98.addWidget(self.bruteforce_fuzz_batchsize, 8, 3, 1, 1)

        self.label_170 = QLabel(self.tab_43)
        self.label_170.setObjectName(u"label_170")
        self.label_170.setMaximumSize(QSize(16777215, 25))

        self.gridLayout_98.addWidget(self.label_170, 0, 0, 1, 2)

        self.bruteforce_fuzz_stop = QPushButton(self.tab_43)
        self.bruteforce_fuzz_stop.setObjectName(u"bruteforce_fuzz_stop")

        self.gridLayout_98.addWidget(self.bruteforce_fuzz_stop, 17, 5, 1, 1)

        self.label_160 = QLabel(self.tab_43)
        self.label_160.setObjectName(u"label_160")

        self.gridLayout_98.addWidget(self.label_160, 0, 5, 1, 1)

        self.label_168 = QLabel(self.tab_43)
        self.label_168.setObjectName(u"label_168")
        self.label_168.setMaximumSize(QSize(200, 15))

        self.gridLayout_98.addWidget(self.label_168, 12, 5, 1, 1)

        self.bruteforce_fuzz_threads = QSpinBox(self.tab_43)
        self.bruteforce_fuzz_threads.setObjectName(u"bruteforce_fuzz_threads")
        self.bruteforce_fuzz_threads.setValue(10)

        self.gridLayout_98.addWidget(self.bruteforce_fuzz_threads, 15, 5, 1, 1)

        self.label_163 = QLabel(self.tab_43)
        self.label_163.setObjectName(u"label_163")
        self.label_163.setMaximumSize(QSize(16777215, 15))

        self.gridLayout_98.addWidget(self.label_163, 2, 5, 1, 1)

        self.bruteforce_fuzz_showfullurl_option = QCheckBox(self.tab_43)
        self.bruteforce_fuzz_showfullurl_option.setObjectName(u"bruteforce_fuzz_showfullurl_option")

        self.gridLayout_98.addWidget(self.bruteforce_fuzz_showfullurl_option, 7, 3, 1, 1)

        self.label_171 = QLabel(self.tab_43)
        self.label_171.setObjectName(u"label_171")
        self.label_171.setMaximumSize(QSize(100, 16777215))

        self.gridLayout_98.addWidget(self.label_171, 7, 0, 1, 1)

        self.checkBox_43 = QCheckBox(self.tab_43)
        self.checkBox_43.setObjectName(u"checkBox_43")

        self.gridLayout_98.addWidget(self.checkBox_43, 7, 2, 1, 1)

        self.label_159 = QLabel(self.tab_43)
        self.label_159.setObjectName(u"label_159")
        self.label_159.setMinimumSize(QSize(0, 0))
        self.label_159.setMaximumSize(QSize(16777215, 15))

        self.gridLayout_98.addWidget(self.label_159, 14, 5, 1, 1)

        self.bruteforce_fuzz_port = QLineEdit(self.tab_43)
        self.bruteforce_fuzz_port.setObjectName(u"bruteforce_fuzz_port")

        self.gridLayout_98.addWidget(self.bruteforce_fuzz_port, 8, 0, 1, 1)

        self.bruteforce_fuzz_panel = QTabWidget(self.tab_43)
        self.bruteforce_fuzz_panel.setObjectName(u"bruteforce_fuzz_panel")
        self.bruteforce_fuzz_panel.setMaximumSize(QSize(1677215, 16777215))
        self.tab_130 = QWidget()
        self.tab_130.setObjectName(u"tab_130")
        self.gridLayout_95 = QGridLayout(self.tab_130)
        self.gridLayout_95.setObjectName(u"gridLayout_95")
        self.bruteforce_fuzz_gooddir_gui = QTextEdit(self.tab_130)
        self.bruteforce_fuzz_gooddir_gui.setObjectName(u"bruteforce_fuzz_gooddir_gui")
        self.bruteforce_fuzz_gooddir_gui.setMaximumSize(QSize(1677700, 16777215))

        self.gridLayout_95.addWidget(self.bruteforce_fuzz_gooddir_gui, 0, 0, 1, 1)

        self.bruteforce_fuzz_panel.addTab(self.tab_130, "")
        self.tab_131 = QWidget()
        self.tab_131.setObjectName(u"tab_131")
        self.gridLayout_96 = QGridLayout(self.tab_131)
        self.gridLayout_96.setObjectName(u"gridLayout_96")
        self.bruteforce_fuzz_currentbatch = QTextEdit(self.tab_131)
        self.bruteforce_fuzz_currentbatch.setObjectName(u"bruteforce_fuzz_currentbatch")

        self.gridLayout_96.addWidget(self.bruteforce_fuzz_currentbatch, 0, 0, 1, 1)

        self.bruteforce_fuzz_panel.addTab(self.tab_131, "")
        self.tab_132 = QWidget()
        self.tab_132.setObjectName(u"tab_132")
        self.gridLayout_97 = QGridLayout(self.tab_132)
        self.gridLayout_97.setObjectName(u"gridLayout_97")
        self.bruteforce_fuzz_errlog = QTextEdit(self.tab_132)
        self.bruteforce_fuzz_errlog.setObjectName(u"bruteforce_fuzz_errlog")

        self.gridLayout_97.addWidget(self.bruteforce_fuzz_errlog, 0, 0, 1, 1)

        self.bruteforce_fuzz_panel.addTab(self.tab_132, "")

        self.gridLayout_98.addWidget(self.bruteforce_fuzz_panel, 4, 5, 8, 1)

        self.label_169 = QLabel(self.tab_43)
        self.label_169.setObjectName(u"label_169")

        self.gridLayout_98.addWidget(self.label_169, 8, 1, 1, 1)

        self.tabWidget_29 = QTabWidget(self.tab_43)
        self.tabWidget_29.setObjectName(u"tabWidget_29")
        self.tab_127 = QWidget()
        self.tab_127.setObjectName(u"tab_127")
        self.gridLayout_93 = QGridLayout(self.tab_127)
        self.gridLayout_93.setObjectName(u"gridLayout_93")
        self.DB_Query_scanning_bruteforce_4 = QLineEdit(self.tab_127)
        self.DB_Query_scanning_bruteforce_4.setObjectName(u"DB_Query_scanning_bruteforce_4")

        self.gridLayout_93.addWidget(self.DB_Query_scanning_bruteforce_4, 1, 0, 1, 2)

        self.scanning_bruteforce_refresh_4 = QPushButton(self.tab_127)
        self.scanning_bruteforce_refresh_4.setObjectName(u"scanning_bruteforce_refresh_4")

        self.gridLayout_93.addWidget(self.scanning_bruteforce_refresh_4, 2, 0, 1, 1)

        self.scanning_bruteforce_db_4 = QTableWidget(self.tab_127)
        self.scanning_bruteforce_db_4.setObjectName(u"scanning_bruteforce_db_4")

        self.gridLayout_93.addWidget(self.scanning_bruteforce_db_4, 0, 0, 1, 2)

        self.scanning_bruteforce_query_4 = QPushButton(self.tab_127)
        self.scanning_bruteforce_query_4.setObjectName(u"scanning_bruteforce_query_4")

        self.gridLayout_93.addWidget(self.scanning_bruteforce_query_4, 2, 1, 1, 1)

        self.tabWidget_29.addTab(self.tab_127, "")
        self.tab_128 = QWidget()
        self.tab_128.setObjectName(u"tab_128")
        self.gridLayout_94 = QGridLayout(self.tab_128)
        self.gridLayout_94.setObjectName(u"gridLayout_94")
        self.label_167 = QLabel(self.tab_128)
        self.label_167.setObjectName(u"label_167")
        self.label_167.setMaximumSize(QSize(16777215, 15))
        self.label_167.setFont(font7)

        self.gridLayout_94.addWidget(self.label_167, 0, 0, 1, 1)

        self.label_166 = QLabel(self.tab_128)
        self.label_166.setObjectName(u"label_166")
        self.label_166.setFont(font7)

        self.gridLayout_94.addWidget(self.label_166, 0, 2, 1, 1)

        self.lineEdit_56 = QLineEdit(self.tab_128)
        self.lineEdit_56.setObjectName(u"lineEdit_56")

        self.gridLayout_94.addWidget(self.lineEdit_56, 1, 0, 1, 1)

        self.bruteforce_download_seclist_top10mil_usernames_4 = QPushButton(self.tab_128)
        self.bruteforce_download_seclist_top10mil_usernames_4.setObjectName(u"bruteforce_download_seclist_top10mil_usernames_4")
        self.bruteforce_download_seclist_top10mil_usernames_4.setFont(font6)
        self.bruteforce_download_seclist_top10mil_usernames_4.setAutoDefault(False)
        self.bruteforce_download_seclist_top10mil_usernames_4.setFlat(False)

        self.gridLayout_94.addWidget(self.bruteforce_download_seclist_top10mil_usernames_4, 1, 1, 1, 1)

        self.lineEdit_55 = QLineEdit(self.tab_128)
        self.lineEdit_55.setObjectName(u"lineEdit_55")

        self.gridLayout_94.addWidget(self.lineEdit_55, 1, 2, 1, 1)

        self.bruteforce_download_seclist_defaults_4 = QPushButton(self.tab_128)
        self.bruteforce_download_seclist_defaults_4.setObjectName(u"bruteforce_download_seclist_defaults_4")

        self.gridLayout_94.addWidget(self.bruteforce_download_seclist_defaults_4, 1, 3, 1, 1)

        self.lineEdit_58 = QLineEdit(self.tab_128)
        self.lineEdit_58.setObjectName(u"lineEdit_58")

        self.gridLayout_94.addWidget(self.lineEdit_58, 2, 0, 1, 1)

        self.bruteforce_download_seclist_topshort_4 = QPushButton(self.tab_128)
        self.bruteforce_download_seclist_topshort_4.setObjectName(u"bruteforce_download_seclist_topshort_4")
        self.bruteforce_download_seclist_topshort_4.setFont(font6)
        self.bruteforce_download_seclist_topshort_4.setAutoDefault(False)
        self.bruteforce_download_seclist_topshort_4.setFlat(False)

        self.gridLayout_94.addWidget(self.bruteforce_download_seclist_topshort_4, 2, 1, 1, 1)

        self.lineEdit_57 = QLineEdit(self.tab_128)
        self.lineEdit_57.setObjectName(u"lineEdit_57")

        self.gridLayout_94.addWidget(self.lineEdit_57, 2, 2, 1, 1)

        self.bruteforce_download_seclist_top10mil_4 = QPushButton(self.tab_128)
        self.bruteforce_download_seclist_top10mil_4.setObjectName(u"bruteforce_download_seclist_top10mil_4")

        self.gridLayout_94.addWidget(self.bruteforce_download_seclist_top10mil_4, 2, 3, 1, 1)

        self.lineEdit_54 = QLineEdit(self.tab_128)
        self.lineEdit_54.setObjectName(u"lineEdit_54")

        self.gridLayout_94.addWidget(self.lineEdit_54, 3, 2, 1, 1)

        self.bruteforce_download_ignis_1M_4 = QPushButton(self.tab_128)
        self.bruteforce_download_ignis_1M_4.setObjectName(u"bruteforce_download_ignis_1M_4")

        self.gridLayout_94.addWidget(self.bruteforce_download_ignis_1M_4, 3, 3, 1, 1)

        self.tabWidget_29.addTab(self.tab_128, "")
        self.tab_129 = QWidget()
        self.tab_129.setObjectName(u"tab_129")
        self.gridLayout_44 = QGridLayout(self.tab_129)
        self.gridLayout_44.setObjectName(u"gridLayout_44")
        self.label_49 = QLabel(self.tab_129)
        self.label_49.setObjectName(u"label_49")

        self.gridLayout_44.addWidget(self.label_49, 0, 0, 1, 1)

        self.label_72 = QLabel(self.tab_129)
        self.label_72.setObjectName(u"label_72")

        self.gridLayout_44.addWidget(self.label_72, 0, 1, 1, 1)

        self.bruteforce_fuzz_validresponsecode = QTextEdit(self.tab_129)
        self.bruteforce_fuzz_validresponsecode.setObjectName(u"bruteforce_fuzz_validresponsecode")

        self.gridLayout_44.addWidget(self.bruteforce_fuzz_validresponsecode, 1, 0, 1, 1)

        self.bruteforce_fuzz_validresponsecode_2 = QTextEdit(self.tab_129)
        self.bruteforce_fuzz_validresponsecode_2.setObjectName(u"bruteforce_fuzz_validresponsecode_2")

        self.gridLayout_44.addWidget(self.bruteforce_fuzz_validresponsecode_2, 1, 1, 1, 1)

        self.comboBox_6 = QComboBox(self.tab_129)
        self.comboBox_6.setObjectName(u"comboBox_6")

        self.gridLayout_44.addWidget(self.comboBox_6, 2, 0, 1, 2)

        self.tabWidget_29.addTab(self.tab_129, "")
        self.tab_60 = QWidget()
        self.tab_60.setObjectName(u"tab_60")
        self.label_75 = QLabel(self.tab_60)
        self.label_75.setObjectName(u"label_75")
        self.label_75.setGeometry(QRect(440, 10, 191, 19))
        self.label_75.setFont(font3)
        self.lineEdit_25 = QLineEdit(self.tab_60)
        self.lineEdit_25.setObjectName(u"lineEdit_25")
        self.lineEdit_25.setGeometry(QRect(12, 70, 131, 27))
        self.label_76 = QLabel(self.tab_60)
        self.label_76.setObjectName(u"label_76")
        self.label_76.setGeometry(QRect(10, 50, 221, 19))
        self.radioButton_4 = QRadioButton(self.tab_60)
        self.radioButton_4.setObjectName(u"radioButton_4")
        self.radioButton_4.setGeometry(QRect(10, 40, 171, 25))
        self.radioButton_5 = QRadioButton(self.tab_60)
        self.radioButton_5.setObjectName(u"radioButton_5")
        self.radioButton_5.setGeometry(QRect(10, 10, 161, 25))
        self.radioButton_6 = QRadioButton(self.tab_60)
        self.radioButton_6.setObjectName(u"radioButton_6")
        self.radioButton_6.setGeometry(QRect(10, 110, 171, 25))
        self.radioButton_6.setChecked(True)
        self.lineEdit_26 = QLineEdit(self.tab_60)
        self.lineEdit_26.setObjectName(u"lineEdit_26")
        self.lineEdit_26.setGeometry(QRect(12, 140, 131, 27))
        self.bruteforce_download_seclist_top10mil_usernames_5 = QPushButton(self.tab_60)
        self.bruteforce_download_seclist_top10mil_usernames_5.setObjectName(u"bruteforce_download_seclist_top10mil_usernames_5")
        self.bruteforce_download_seclist_top10mil_usernames_5.setGeometry(QRect(150, 70, 80, 27))
        self.bruteforce_download_seclist_top10mil_usernames_5.setFont(font6)
        self.bruteforce_download_seclist_top10mil_usernames_5.setAutoDefault(False)
        self.bruteforce_download_seclist_top10mil_usernames_5.setFlat(False)
        self.checkBox_22 = QCheckBox(self.tab_60)
        self.checkBox_22.setObjectName(u"checkBox_22")
        self.checkBox_22.setGeometry(QRect(440, 50, 141, 25))
        self.lineEdit_27 = QLineEdit(self.tab_60)
        self.lineEdit_27.setObjectName(u"lineEdit_27")
        self.lineEdit_27.setGeometry(QRect(590, 50, 241, 27))
        self.label_77 = QLabel(self.tab_60)
        self.label_77.setObjectName(u"label_77")
        self.label_77.setGeometry(QRect(760, 310, 81, 19))
        font8 = QFont()
        font8.setPointSize(6)
        self.label_77.setFont(font8)
        self.tabWidget_29.addTab(self.tab_60, "")

        self.gridLayout_98.addWidget(self.tabWidget_29, 9, 0, 9, 5)

        self.tabWidget_6.addTab(self.tab_43, "")

        self.gridLayout_31.addWidget(self.tabWidget_6, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab_41, "")
        self.tab_6 = QWidget()
        self.tab_6.setObjectName(u"tab_6")
        self.gridLayout_7 = QGridLayout(self.tab_6)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.table_SQLDB_main = QTableWidget(self.tab_6)
        self.table_SQLDB_main.setObjectName(u"table_SQLDB_main")

        self.gridLayout_7.addWidget(self.table_SQLDB_main, 0, 0, 1, 2)

        self.DB_Query_main = QLineEdit(self.tab_6)
        self.DB_Query_main.setObjectName(u"DB_Query_main")

        self.gridLayout_7.addWidget(self.DB_Query_main, 1, 0, 1, 2)

        self.table_RefreshDB_Button_main = QPushButton(self.tab_6)
        self.table_RefreshDB_Button_main.setObjectName(u"table_RefreshDB_Button_main")

        self.gridLayout_7.addWidget(self.table_RefreshDB_Button_main, 2, 0, 1, 1)

        self.table_QueryDB_Button_main = QPushButton(self.tab_6)
        self.table_QueryDB_Button_main.setObjectName(u"table_QueryDB_Button_main")

        self.gridLayout_7.addWidget(self.table_QueryDB_Button_main, 2, 1, 1, 1)

        self.tabWidget.addTab(self.tab_6, "")
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.gridLayout_6 = QGridLayout(self.tab_5)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.tabWidget_2 = QTabWidget(self.tab_5)
        self.tabWidget_2.setObjectName(u"tabWidget_2")
        self.tab_7 = QWidget()
        self.tab_7.setObjectName(u"tab_7")
        self.gridLayout_11 = QGridLayout(self.tab_7)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.label_2 = QLabel(self.tab_7)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_11.addWidget(self.label_2, 0, 0, 1, 1)

        self.radioButton = QRadioButton(self.tab_7)
        self.radioButton.setObjectName(u"radioButton")

        self.gridLayout_11.addWidget(self.radioButton, 0, 1, 2, 1)

        self.lineEdit = QLineEdit(self.tab_7)
        self.lineEdit.setObjectName(u"lineEdit")

        self.gridLayout_11.addWidget(self.lineEdit, 1, 0, 2, 1)

        self.radioButton_2 = QRadioButton(self.tab_7)
        self.radioButton_2.setObjectName(u"radioButton_2")

        self.gridLayout_11.addWidget(self.radioButton_2, 2, 1, 2, 1)

        self.label_3 = QLabel(self.tab_7)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_11.addWidget(self.label_3, 3, 0, 2, 1)

        self.radioButton_3 = QRadioButton(self.tab_7)
        self.radioButton_3.setObjectName(u"radioButton_3")

        self.gridLayout_11.addWidget(self.radioButton_3, 4, 1, 2, 1)

        self.lineEdit_2 = QLineEdit(self.tab_7)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.gridLayout_11.addWidget(self.lineEdit_2, 5, 0, 1, 1)

        self.tabWidget_2.addTab(self.tab_7, "")
        self.tab_9 = QWidget()
        self.tab_9.setObjectName(u"tab_9")
        self.tabWidget_2.addTab(self.tab_9, "")
        self.tab_8 = QWidget()
        self.tab_8.setObjectName(u"tab_8")
        self.gridLayout_12 = QGridLayout(self.tab_8)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.tabWidget_4 = QTabWidget(self.tab_8)
        self.tabWidget_4.setObjectName(u"tabWidget_4")
        self.tabWidget_4.setLayoutDirection(Qt.LeftToRight)
        self.tabWidget_4.setTabPosition(QTabWidget.West)
        self.tab_10 = QWidget()
        self.tab_10.setObjectName(u"tab_10")
        self.lineEdit_3 = QLineEdit(self.tab_10)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(10, 30, 271, 27))
        self.label_4 = QLabel(self.tab_10)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(10, 10, 66, 19))
        self.lineEdit_4 = QLineEdit(self.tab_10)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setGeometry(QRect(10, 120, 271, 27))
        self.label_5 = QLabel(self.tab_10)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(10, 100, 321, 19))
        self.tabWidget_4.addTab(self.tab_10, "")
        self.tab_11 = QWidget()
        self.tab_11.setObjectName(u"tab_11")
        self.tabWidget_4.addTab(self.tab_11, "")

        self.gridLayout_12.addWidget(self.tabWidget_4, 0, 0, 1, 1)

        self.tabWidget_2.addTab(self.tab_8, "")
        self.tab_17 = QWidget()
        self.tab_17.setObjectName(u"tab_17")
        self.comboBox_4 = QComboBox(self.tab_17)
        self.comboBox_4.setObjectName(u"comboBox_4")
        self.comboBox_4.setGeometry(QRect(10, 70, 181, 27))
        self.label_32 = QLabel(self.tab_17)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setGeometry(QRect(10, 30, 66, 19))
        self.pushButton = QPushButton(self.tab_17)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(100, 110, 87, 27))
        self.tabWidget_2.addTab(self.tab_17, "")
        self.tab_37 = QWidget()
        self.tab_37.setObjectName(u"tab_37")
        self.gridLayout_28 = QGridLayout(self.tab_37)
        self.gridLayout_28.setObjectName(u"gridLayout_28")
        self.settings_edit = QTextEdit(self.tab_37)
        self.settings_edit.setObjectName(u"settings_edit")

        self.gridLayout_28.addWidget(self.settings_edit, 0, 0, 1, 2)

        self.settings_reload = QPushButton(self.tab_37)
        self.settings_reload.setObjectName(u"settings_reload")

        self.gridLayout_28.addWidget(self.settings_reload, 1, 0, 1, 1)

        self.settings_write = QPushButton(self.tab_37)
        self.settings_write.setObjectName(u"settings_write")

        self.gridLayout_28.addWidget(self.settings_write, 1, 1, 1, 1)

        self.tabWidget_2.addTab(self.tab_37, "")

        self.gridLayout_6.addWidget(self.tabWidget_2, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab_5, "")
        self.tab_27 = QWidget()
        self.tab_27.setObjectName(u"tab_27")
        self.gridLayout_25 = QGridLayout(self.tab_27)
        self.gridLayout_25.setObjectName(u"gridLayout_25")
        self.tabWidget_10 = QTabWidget(self.tab_27)
        self.tabWidget_10.setObjectName(u"tabWidget_10")
        self.tab_33 = QWidget()
        self.tab_33.setObjectName(u"tab_33")
        self.gridLayout_24 = QGridLayout(self.tab_33)
        self.gridLayout_24.setObjectName(u"gridLayout_24")
        self.table_RefreshDB_Button_performance2 = QPushButton(self.tab_33)
        self.table_RefreshDB_Button_performance2.setObjectName(u"table_RefreshDB_Button_performance2")

        self.gridLayout_24.addWidget(self.table_RefreshDB_Button_performance2, 21, 0, 1, 1)

        self.line_10 = QFrame(self.tab_33)
        self.line_10.setObjectName(u"line_10")
        self.line_10.setFrameShape(QFrame.HLine)
        self.line_10.setFrameShadow(QFrame.Sunken)

        self.gridLayout_24.addWidget(self.line_10, 7, 0, 1, 1)

        self.label_44 = QLabel(self.tab_33)
        self.label_44.setObjectName(u"label_44")

        self.gridLayout_24.addWidget(self.label_44, 10, 0, 1, 1)

        self.performance_lcd_download = QLCDNumber(self.tab_33)
        self.performance_lcd_download.setObjectName(u"performance_lcd_download")
        self.performance_lcd_download.setFrameShape(QFrame.Panel)
        self.performance_lcd_download.setFrameShadow(QFrame.Sunken)
        self.performance_lcd_download.setDigitCount(5)
        self.performance_lcd_download.setProperty("value", 0.000000000000000)

        self.gridLayout_24.addWidget(self.performance_lcd_download, 11, 3, 1, 2)

        self.label_39 = QLabel(self.tab_33)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setFont(font2)

        self.gridLayout_24.addWidget(self.label_39, 0, 0, 1, 1)

        self.label_40 = QLabel(self.tab_33)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setFont(font3)

        self.gridLayout_24.addWidget(self.label_40, 3, 3, 1, 1)

        self.progressBar_19 = QProgressBar(self.tab_33)
        self.progressBar_19.setObjectName(u"progressBar_19")
        self.progressBar_19.setValue(0)

        self.gridLayout_24.addWidget(self.progressBar_19, 2, 0, 1, 1)

        self.label_18 = QLabel(self.tab_33)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setFont(font2)

        self.gridLayout_24.addWidget(self.label_18, 0, 2, 1, 2)

        self.label_78 = QLabel(self.tab_33)
        self.label_78.setObjectName(u"label_78")
        self.label_78.setMaximumSize(QSize(16777215, 20))
        self.label_78.setFont(font2)

        self.gridLayout_24.addWidget(self.label_78, 15, 3, 1, 2)

        self.performance_seconds = QLineEdit(self.tab_33)
        self.performance_seconds.setObjectName(u"performance_seconds")
        self.performance_seconds.setMaximumSize(QSize(200, 16777215))

        self.gridLayout_24.addWidget(self.performance_seconds, 16, 3, 1, 1)

        self.label_79 = QLabel(self.tab_33)
        self.label_79.setObjectName(u"label_79")

        self.gridLayout_24.addWidget(self.label_79, 16, 4, 1, 1)

        self.label_41 = QLabel(self.tab_33)
        self.label_41.setObjectName(u"label_41")

        self.gridLayout_24.addWidget(self.label_41, 4, 0, 1, 1)

        self.line_12 = QFrame(self.tab_33)
        self.line_12.setObjectName(u"line_12")
        self.line_12.setFrameShape(QFrame.VLine)
        self.line_12.setFrameShadow(QFrame.Sunken)

        self.gridLayout_24.addWidget(self.line_12, 0, 1, 22, 1)

        self.performance_lcd_ping = QLCDNumber(self.tab_33)
        self.performance_lcd_ping.setObjectName(u"performance_lcd_ping")

        self.gridLayout_24.addWidget(self.performance_lcd_ping, 5, 3, 1, 2)

        self.label_43 = QLabel(self.tab_33)
        self.label_43.setObjectName(u"label_43")

        self.gridLayout_24.addWidget(self.label_43, 1, 4, 1, 1)

        self.progressBar_20 = QProgressBar(self.tab_33)
        self.progressBar_20.setObjectName(u"progressBar_20")
        self.progressBar_20.setValue(0)

        self.gridLayout_24.addWidget(self.progressBar_20, 9, 0, 1, 1)

        self.label_48 = QLabel(self.tab_33)
        self.label_48.setObjectName(u"label_48")

        self.gridLayout_24.addWidget(self.label_48, 12, 0, 1, 1)

        self.label_46 = QLabel(self.tab_33)
        self.label_46.setObjectName(u"label_46")

        self.gridLayout_24.addWidget(self.label_46, 7, 3, 1, 1)

        self.label_20 = QLabel(self.tab_33)
        self.label_20.setObjectName(u"label_20")

        self.gridLayout_24.addWidget(self.label_20, 15, 0, 1, 1)

        self.other_performance_cpuall = QProgressBar(self.tab_33)
        self.other_performance_cpuall.setObjectName(u"other_performance_cpuall")
        self.other_performance_cpuall.setValue(24)

        self.gridLayout_24.addWidget(self.other_performance_cpuall, 11, 0, 1, 1)

        self.label_33 = QLabel(self.tab_33)
        self.label_33.setObjectName(u"label_33")

        self.gridLayout_24.addWidget(self.label_33, 1, 3, 1, 1)

        self.other_performance_ramall = QProgressBar(self.tab_33)
        self.other_performance_ramall.setObjectName(u"other_performance_ramall")
        self.other_performance_ramall.setValue(24)

        self.gridLayout_24.addWidget(self.other_performance_ramall, 5, 0, 1, 1)

        self.table_SQLDB_performance_error2 = QTableWidget(self.tab_33)
        self.table_SQLDB_performance_error2.setObjectName(u"table_SQLDB_performance_error2")

        self.gridLayout_24.addWidget(self.table_SQLDB_performance_error2, 18, 0, 1, 1)

        self.line_19 = QFrame(self.tab_33)
        self.line_19.setObjectName(u"line_19")
        self.line_19.setFrameShape(QFrame.HLine)
        self.line_19.setFrameShadow(QFrame.Sunken)

        self.gridLayout_24.addWidget(self.line_19, 14, 3, 1, 2)

        self.performance_benchmark_button = QPushButton(self.tab_33)
        self.performance_benchmark_button.setObjectName(u"performance_benchmark_button")

        self.gridLayout_24.addWidget(self.performance_benchmark_button, 17, 3, 1, 1)

        self.performance_speedtest = QPushButton(self.tab_33)
        self.performance_speedtest.setObjectName(u"performance_speedtest")

        self.gridLayout_24.addWidget(self.performance_speedtest, 13, 3, 1, 2)

        self.label_47 = QLabel(self.tab_33)
        self.label_47.setObjectName(u"label_47")

        self.gridLayout_24.addWidget(self.label_47, 8, 0, 1, 1)

        self.label_42 = QLabel(self.tab_33)
        self.label_42.setObjectName(u"label_42")

        self.gridLayout_24.addWidget(self.label_42, 10, 3, 1, 1)

        self.line_11 = QFrame(self.tab_33)
        self.line_11.setObjectName(u"line_11")
        self.line_11.setFrameShape(QFrame.VLine)
        self.line_11.setFrameShadow(QFrame.Sunken)

        self.gridLayout_24.addWidget(self.line_11, 0, 5, 15, 1)

        self.lineEdit_11 = QLineEdit(self.tab_33)
        self.lineEdit_11.setObjectName(u"lineEdit_11")

        self.gridLayout_24.addWidget(self.lineEdit_11, 13, 0, 1, 1)

        self.label_45 = QLabel(self.tab_33)
        self.label_45.setObjectName(u"label_45")

        self.gridLayout_24.addWidget(self.label_45, 1, 0, 1, 1)

        self.label_19 = QLabel(self.tab_33)
        self.label_19.setObjectName(u"label_19")

        self.gridLayout_24.addWidget(self.label_19, 4, 3, 1, 1)

        self.performance_lcd_upload = QLCDNumber(self.tab_33)
        self.performance_lcd_upload.setObjectName(u"performance_lcd_upload")
        self.performance_lcd_upload.setFrameShape(QFrame.Panel)
        self.performance_lcd_upload.setFrameShadow(QFrame.Sunken)
        self.performance_lcd_upload.setDigitCount(5)
        self.performance_lcd_upload.setProperty("value", 0.000000000000000)

        self.gridLayout_24.addWidget(self.performance_lcd_upload, 9, 3, 1, 2)

        self.tabWidget_10.addTab(self.tab_33, "")
        self.tab_52 = QWidget()
        self.tab_52.setObjectName(u"tab_52")
        self.gridLayout_55 = QGridLayout(self.tab_52)
        self.gridLayout_55.setObjectName(u"gridLayout_55")
        self.line_20 = QFrame(self.tab_52)
        self.line_20.setObjectName(u"line_20")
        self.line_20.setFrameShape(QFrame.VLine)
        self.line_20.setFrameShadow(QFrame.Sunken)

        self.gridLayout_55.addWidget(self.line_20, 8, 1, 1, 1)

        self.other_cpu_performance = QGraphicsView(self.tab_52)
        self.other_cpu_performance.setObjectName(u"other_cpu_performance")
        self.other_cpu_performance.setMinimumSize(QSize(0, 100))
        self.other_cpu_performance.setMaximumSize(QSize(16777215, 100))

        self.gridLayout_55.addWidget(self.other_cpu_performance, 1, 0, 1, 2)

        self.label_14 = QLabel(self.tab_52)
        self.label_14.setObjectName(u"label_14")

        self.gridLayout_55.addWidget(self.label_14, 0, 0, 1, 1)

        self.tabWidget_16 = QTabWidget(self.tab_52)
        self.tabWidget_16.setObjectName(u"tabWidget_16")
        self.tab_75 = QWidget()
        self.tab_75.setObjectName(u"tab_75")
        self.gridLayout_54 = QGridLayout(self.tab_75)
        self.gridLayout_54.setObjectName(u"gridLayout_54")
        self.label_84 = QLabel(self.tab_75)
        self.label_84.setObjectName(u"label_84")

        self.gridLayout_54.addWidget(self.label_84, 4, 0, 2, 1)

        self.performance_lcd_upload_2 = QLCDNumber(self.tab_75)
        self.performance_lcd_upload_2.setObjectName(u"performance_lcd_upload_2")
        self.performance_lcd_upload_2.setFrameShape(QFrame.Panel)
        self.performance_lcd_upload_2.setFrameShadow(QFrame.Sunken)
        self.performance_lcd_upload_2.setDigitCount(5)
        self.performance_lcd_upload_2.setProperty("value", 0.000000000000000)

        self.gridLayout_54.addWidget(self.performance_lcd_upload_2, 9, 0, 1, 2)

        self.label_85 = QLabel(self.tab_75)
        self.label_85.setObjectName(u"label_85")
        self.label_85.setFont(font)

        self.gridLayout_54.addWidget(self.label_85, 3, 0, 1, 1)

        self.performance_seconds_5 = QLineEdit(self.tab_75)
        self.performance_seconds_5.setObjectName(u"performance_seconds_5")
        self.performance_seconds_5.setMaximumSize(QSize(19777, 16777215))

        self.gridLayout_54.addWidget(self.performance_seconds_5, 8, 3, 1, 1)

        self.label_121 = QLabel(self.tab_75)
        self.label_121.setObjectName(u"label_121")

        self.gridLayout_54.addWidget(self.label_121, 8, 4, 1, 1)

        self.line_22 = QFrame(self.tab_75)
        self.line_22.setObjectName(u"line_22")
        self.line_22.setFrameShape(QFrame.VLine)
        self.line_22.setFrameShadow(QFrame.Sunken)

        self.gridLayout_54.addWidget(self.line_22, 0, 7, 14, 1)

        self.line_21 = QFrame(self.tab_75)
        self.line_21.setObjectName(u"line_21")
        self.line_21.setFrameShape(QFrame.VLine)
        self.line_21.setFrameShadow(QFrame.Sunken)

        self.gridLayout_54.addWidget(self.line_21, 0, 5, 14, 1)

        self.textEdit_29 = QTextEdit(self.tab_75)
        self.textEdit_29.setObjectName(u"textEdit_29")

        self.gridLayout_54.addWidget(self.textEdit_29, 0, 6, 14, 1)

        self.label_91 = QLabel(self.tab_75)
        self.label_91.setObjectName(u"label_91")
        font9 = QFont()
        font9.setUnderline(True)
        font9.setKerning(True)
        self.label_91.setFont(font9)

        self.gridLayout_54.addWidget(self.label_91, 0, 3, 2, 1)

        self.line_30 = QFrame(self.tab_75)
        self.line_30.setObjectName(u"line_30")
        self.line_30.setFrameShape(QFrame.VLine)
        self.line_30.setFrameShadow(QFrame.Sunken)

        self.gridLayout_54.addWidget(self.line_30, 1, 2, 13, 1)

        self.checkBox_23 = QCheckBox(self.tab_75)
        self.checkBox_23.setObjectName(u"checkBox_23")

        self.gridLayout_54.addWidget(self.checkBox_23, 3, 3, 1, 2)

        self.performance_lcd_ping_2 = QLCDNumber(self.tab_75)
        self.performance_lcd_ping_2.setObjectName(u"performance_lcd_ping_2")

        self.gridLayout_54.addWidget(self.performance_lcd_ping_2, 6, 0, 1, 2)

        self.label_83 = QLabel(self.tab_75)
        self.label_83.setObjectName(u"label_83")

        self.gridLayout_54.addWidget(self.label_83, 1, 1, 1, 1)

        self.label_82 = QLabel(self.tab_75)
        self.label_82.setObjectName(u"label_82")

        self.gridLayout_54.addWidget(self.label_82, 3, 1, 1, 1)

        self.performance_seconds_2 = QLineEdit(self.tab_75)
        self.performance_seconds_2.setObjectName(u"performance_seconds_2")
        self.performance_seconds_2.setMaximumSize(QSize(19777, 16777215))

        self.gridLayout_54.addWidget(self.performance_seconds_2, 4, 3, 1, 1)

        self.checkBox_24 = QCheckBox(self.tab_75)
        self.checkBox_24.setObjectName(u"checkBox_24")

        self.gridLayout_54.addWidget(self.checkBox_24, 6, 3, 1, 1)

        self.textEdit_23 = QTextEdit(self.tab_75)
        self.textEdit_23.setObjectName(u"textEdit_23")

        self.gridLayout_54.addWidget(self.textEdit_23, 0, 8, 14, 1)

        self.label_90 = QLabel(self.tab_75)
        self.label_90.setObjectName(u"label_90")

        self.gridLayout_54.addWidget(self.label_90, 4, 4, 1, 1)

        self.performance_lcd_download_2 = QLCDNumber(self.tab_75)
        self.performance_lcd_download_2.setObjectName(u"performance_lcd_download_2")
        self.performance_lcd_download_2.setFrameShape(QFrame.Panel)
        self.performance_lcd_download_2.setFrameShadow(QFrame.Sunken)
        self.performance_lcd_download_2.setDigitCount(5)
        self.performance_lcd_download_2.setProperty("value", 0.000000000000000)

        self.gridLayout_54.addWidget(self.performance_lcd_download_2, 12, 0, 1, 2)

        self.label_86 = QLabel(self.tab_75)
        self.label_86.setObjectName(u"label_86")
        self.label_86.setFont(font3)

        self.gridLayout_54.addWidget(self.label_86, 0, 0, 2, 1)

        self.label_88 = QLabel(self.tab_75)
        self.label_88.setObjectName(u"label_88")

        self.gridLayout_54.addWidget(self.label_88, 7, 0, 2, 1)

        self.label_87 = QLabel(self.tab_75)
        self.label_87.setObjectName(u"label_87")

        self.gridLayout_54.addWidget(self.label_87, 10, 0, 2, 1)

        self.performance_speedtest_2 = QPushButton(self.tab_75)
        self.performance_speedtest_2.setObjectName(u"performance_speedtest_2")

        self.gridLayout_54.addWidget(self.performance_speedtest_2, 13, 0, 1, 2)

        self.performance_benchmark_button_2 = QPushButton(self.tab_75)
        self.performance_benchmark_button_2.setObjectName(u"performance_benchmark_button_2")

        self.gridLayout_54.addWidget(self.performance_benchmark_button_2, 13, 3, 1, 2)

        self.tabWidget_16.addTab(self.tab_75, "")
        self.tab_76 = QWidget()
        self.tab_76.setObjectName(u"tab_76")
        self.gridLayout_56 = QGridLayout(self.tab_76)
        self.gridLayout_56.setObjectName(u"gridLayout_56")
        self.table_SQLDB_performance_error = QTableWidget(self.tab_76)
        self.table_SQLDB_performance_error.setObjectName(u"table_SQLDB_performance_error")

        self.gridLayout_56.addWidget(self.table_SQLDB_performance_error, 0, 0, 1, 1)

        self.table_RefreshDB_Button_performance = QPushButton(self.tab_76)
        self.table_RefreshDB_Button_performance.setObjectName(u"table_RefreshDB_Button_performance")

        self.gridLayout_56.addWidget(self.table_RefreshDB_Button_performance, 1, 0, 1, 1)

        self.tabWidget_16.addTab(self.tab_76, "")
        self.tab_77 = QWidget()
        self.tab_77.setObjectName(u"tab_77")
        self.lineEdit_10 = QLineEdit(self.tab_77)
        self.lineEdit_10.setObjectName(u"lineEdit_10")
        self.lineEdit_10.setGeometry(QRect(10, 30, 361, 27))
        self.label_89 = QLabel(self.tab_77)
        self.label_89.setObjectName(u"label_89")
        self.label_89.setGeometry(QRect(10, 10, 171, 19))
        self.label_122 = QLabel(self.tab_77)
        self.label_122.setObjectName(u"label_122")
        self.label_122.setGeometry(QRect(10, 70, 171, 19))
        self.comboBox_7 = QComboBox(self.tab_77)
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.setObjectName(u"comboBox_7")
        self.comboBox_7.setGeometry(QRect(10, 100, 361, 27))
        self.tabWidget_16.addTab(self.tab_77, "")

        self.gridLayout_55.addWidget(self.tabWidget_16, 6, 0, 1, 1)

        self.label_80 = QLabel(self.tab_52)
        self.label_80.setObjectName(u"label_80")

        self.gridLayout_55.addWidget(self.label_80, 2, 0, 1, 1)

        self.other_ram_performance = QGraphicsView(self.tab_52)
        self.other_ram_performance.setObjectName(u"other_ram_performance")
        self.other_ram_performance.setMinimumSize(QSize(0, 100))
        self.other_ram_performance.setMaximumSize(QSize(16777215, 100))

        self.gridLayout_55.addWidget(self.other_ram_performance, 3, 0, 1, 2)

        self.label_81 = QLabel(self.tab_52)
        self.label_81.setObjectName(u"label_81")

        self.gridLayout_55.addWidget(self.label_81, 4, 0, 1, 1)

        self.testgraph_3 = QGraphicsView(self.tab_52)
        self.testgraph_3.setObjectName(u"testgraph_3")
        self.testgraph_3.setMinimumSize(QSize(0, 100))
        self.testgraph_3.setMaximumSize(QSize(16777215, 100))

        self.gridLayout_55.addWidget(self.testgraph_3, 5, 0, 1, 2)

        self.tabWidget_10.addTab(self.tab_52, "")
        self.tab_28 = QWidget()
        self.tab_28.setObjectName(u"tab_28")
        self.gridLayout_26 = QGridLayout(self.tab_28)
        self.gridLayout_26.setObjectName(u"gridLayout_26")
        self.tabWidget_11 = QTabWidget(self.tab_28)
        self.tabWidget_11.setObjectName(u"tabWidget_11")
        self.tab_29 = QWidget()
        self.tab_29.setObjectName(u"tab_29")
        self.tabWidget_11.addTab(self.tab_29, "")
        self.tab_30 = QWidget()
        self.tab_30.setObjectName(u"tab_30")
        self.gridLayout_21 = QGridLayout(self.tab_30)
        self.gridLayout_21.setObjectName(u"gridLayout_21")
        self.tabWidget_12 = QTabWidget(self.tab_30)
        self.tabWidget_12.setObjectName(u"tabWidget_12")
        self.tabWidget_12.setTabPosition(QTabWidget.West)
        self.tab_34 = QWidget()
        self.tab_34.setObjectName(u"tab_34")
        self.gridLayout_23 = QGridLayout(self.tab_34)
        self.gridLayout_23.setObjectName(u"gridLayout_23")
        self.textEdit_5 = QTextEdit(self.tab_34)
        self.textEdit_5.setObjectName(u"textEdit_5")

        self.gridLayout_23.addWidget(self.textEdit_5, 0, 0, 1, 1)

        self.tabWidget_12.addTab(self.tab_34, "")
        self.tab_35 = QWidget()
        self.tab_35.setObjectName(u"tab_35")
        self.tabWidget_12.addTab(self.tab_35, "")

        self.gridLayout_21.addWidget(self.tabWidget_12, 0, 0, 1, 1)

        self.tabWidget_11.addTab(self.tab_30, "")
        self.tab_48 = QWidget()
        self.tab_48.setObjectName(u"tab_48")
        self.gridLayout_36 = QGridLayout(self.tab_48)
        self.gridLayout_36.setObjectName(u"gridLayout_36")
        self.tabWidget_15 = QTabWidget(self.tab_48)
        self.tabWidget_15.setObjectName(u"tabWidget_15")
        self.tabWidget_15.setTabPosition(QTabWidget.West)
        self.tab_49 = QWidget()
        self.tab_49.setObjectName(u"tab_49")
        self.gridLayout_35 = QGridLayout(self.tab_49)
        self.gridLayout_35.setObjectName(u"gridLayout_35")
        self.textEdit_21 = QTextEdit(self.tab_49)
        self.textEdit_21.setObjectName(u"textEdit_21")

        self.gridLayout_35.addWidget(self.textEdit_21, 0, 0, 1, 1)

        self.tabWidget_15.addTab(self.tab_49, "")
        self.tab_50 = QWidget()
        self.tab_50.setObjectName(u"tab_50")
        self.gridLayout_46 = QGridLayout(self.tab_50)
        self.gridLayout_46.setObjectName(u"gridLayout_46")
        self.textEdit_22 = QTextEdit(self.tab_50)
        self.textEdit_22.setObjectName(u"textEdit_22")

        self.gridLayout_46.addWidget(self.textEdit_22, 0, 0, 1, 1)

        self.tabWidget_15.addTab(self.tab_50, "")

        self.gridLayout_36.addWidget(self.tabWidget_15, 0, 0, 1, 1)

        self.tabWidget_11.addTab(self.tab_48, "")

        self.gridLayout_26.addWidget(self.tabWidget_11, 0, 0, 1, 1)

        self.tabWidget_10.addTab(self.tab_28, "")

        self.gridLayout_25.addWidget(self.tabWidget_10, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab_27, "")
        self.tab_20 = QWidget()
        self.tab_20.setObjectName(u"tab_20")
        self.gridLayout_9 = QGridLayout(self.tab_20)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.tabWidget_7 = QTabWidget(self.tab_20)
        self.tabWidget_7.setObjectName(u"tabWidget_7")
        self.tab_21 = QWidget()
        self.tab_21.setObjectName(u"tab_21")
        self.gridLayout_14 = QGridLayout(self.tab_21)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.textEdit_3 = QTextEdit(self.tab_21)
        self.textEdit_3.setObjectName(u"textEdit_3")

        self.gridLayout_14.addWidget(self.textEdit_3, 0, 0, 1, 1)

        self.tabWidget_7.addTab(self.tab_21, "")
        self.tab_19 = QWidget()
        self.tab_19.setObjectName(u"tab_19")
        self.gridLayout_15 = QGridLayout(self.tab_19)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.label_12 = QLabel(self.tab_19)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout_15.addWidget(self.label_12, 0, 0, 1, 1)

        self.textEdit_4 = QTextEdit(self.tab_19)
        self.textEdit_4.setObjectName(u"textEdit_4")

        self.gridLayout_15.addWidget(self.textEdit_4, 1, 1, 1, 1)

        self.tabWidget_7.addTab(self.tab_19, "")
        self.tab_32 = QWidget()
        self.tab_32.setObjectName(u"tab_32")
        self.label_25 = QLabel(self.tab_32)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setGeometry(QRect(20, 40, 201, 19))
        self.label_34 = QLabel(self.tab_32)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setGeometry(QRect(20, 140, 261, 19))
        self.label_35 = QLabel(self.tab_32)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setGeometry(QRect(20, 170, 101, 19))
        self.label_36 = QLabel(self.tab_32)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setGeometry(QRect(20, 200, 101, 19))
        self.label_37 = QLabel(self.tab_32)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setGeometry(QRect(20, 230, 131, 19))
        self.textEdit = QTextEdit(self.tab_32)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(260, 230, 621, 311))
        self.progressBar_17 = QProgressBar(self.tab_32)
        self.progressBar_17.setObjectName(u"progressBar_17")
        self.progressBar_17.setGeometry(QRect(140, 600, 781, 23))
        self.progressBar_17.setAutoFillBackground(False)
        self.progressBar_17.setMaximum(100)
        self.progressBar_17.setValue(75)
        self.tabWidget_7.addTab(self.tab_32, "")
        self.tab_36 = QWidget()
        self.tab_36.setObjectName(u"tab_36")
        self.gridLayout_27 = QGridLayout(self.tab_36)
        self.gridLayout_27.setObjectName(u"gridLayout_27")
        self.label_59 = QLabel(self.tab_36)
        self.label_59.setObjectName(u"label_59")

        self.gridLayout_27.addWidget(self.label_59, 0, 0, 1, 1)

        self.scrollArea_3 = QScrollArea(self.tab_36)
        self.scrollArea_3.setObjectName(u"scrollArea_3")
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 1282, 635))
        self.label_56 = QLabel(self.scrollAreaWidgetContents_3)
        self.label_56.setObjectName(u"label_56")
        self.label_56.setGeometry(QRect(9, 152, 59, 19))
        self.checkBox_18 = QCheckBox(self.scrollAreaWidgetContents_3)
        self.checkBox_18.setObjectName(u"checkBox_18")
        self.checkBox_18.setGeometry(QRect(521, 500, 119, 25))
        self.checkBox_13 = QCheckBox(self.scrollAreaWidgetContents_3)
        self.checkBox_13.setObjectName(u"checkBox_13")
        self.checkBox_13.setGeometry(QRect(521, 326, 119, 25))
        self.checkBox_7 = QCheckBox(self.scrollAreaWidgetContents_3)
        self.checkBox_7.setObjectName(u"checkBox_7")
        self.checkBox_7.setGeometry(QRect(692, 152, 172, 25))
        self.checkBox_8 = QCheckBox(self.scrollAreaWidgetContents_3)
        self.checkBox_8.setObjectName(u"checkBox_8")
        self.checkBox_8.setGeometry(QRect(870, 152, 149, 25))
        self.checkBox_15 = QCheckBox(self.scrollAreaWidgetContents_3)
        self.checkBox_15.setObjectName(u"checkBox_15")
        self.checkBox_15.setGeometry(QRect(180, 500, 123, 25))
        self.checkBox_16 = QCheckBox(self.scrollAreaWidgetContents_3)
        self.checkBox_16.setObjectName(u"checkBox_16")
        self.checkBox_16.setGeometry(QRect(351, 500, 83, 25))
        self.label_57 = QLabel(self.scrollAreaWidgetContents_3)
        self.label_57.setObjectName(u"label_57")
        self.label_57.setGeometry(QRect(9, 326, 92, 19))
        self.checkBox_5 = QCheckBox(self.scrollAreaWidgetContents_3)
        self.checkBox_5.setObjectName(u"checkBox_5")
        self.checkBox_5.setGeometry(QRect(521, 152, 119, 25))
        self.label_58 = QLabel(self.scrollAreaWidgetContents_3)
        self.label_58.setObjectName(u"label_58")
        self.label_58.setGeometry(QRect(9, 500, 71, 19))
        self.checkBox_9 = QCheckBox(self.scrollAreaWidgetContents_3)
        self.checkBox_9.setObjectName(u"checkBox_9")
        self.checkBox_9.setGeometry(QRect(692, 326, 172, 25))
        self.checkBox_3 = QCheckBox(self.scrollAreaWidgetContents_3)
        self.checkBox_3.setObjectName(u"checkBox_3")
        self.checkBox_3.setGeometry(QRect(351, 152, 83, 25))
        self.checkBox_3.setChecked(True)
        self.checkBox_10 = QCheckBox(self.scrollAreaWidgetContents_3)
        self.checkBox_10.setObjectName(u"checkBox_10")
        self.checkBox_10.setGeometry(QRect(180, 326, 123, 25))
        self.checkBox_17 = QCheckBox(self.scrollAreaWidgetContents_3)
        self.checkBox_17.setObjectName(u"checkBox_17")
        self.checkBox_17.setGeometry(QRect(870, 500, 149, 25))
        self.checkBox_11 = QCheckBox(self.scrollAreaWidgetContents_3)
        self.checkBox_11.setObjectName(u"checkBox_11")
        self.checkBox_11.setGeometry(QRect(351, 326, 83, 25))
        self.checkBox_12 = QCheckBox(self.scrollAreaWidgetContents_3)
        self.checkBox_12.setObjectName(u"checkBox_12")
        self.checkBox_12.setGeometry(QRect(870, 326, 149, 25))
        self.checkBox = QCheckBox(self.scrollAreaWidgetContents_3)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setGeometry(QRect(180, 152, 123, 25))
        self.checkBox.setChecked(True)
        self.checkBox_14 = QCheckBox(self.scrollAreaWidgetContents_3)
        self.checkBox_14.setObjectName(u"checkBox_14")
        self.checkBox_14.setGeometry(QRect(692, 500, 172, 25))
        self.textEdit_2 = QTextEdit(self.scrollAreaWidgetContents_3)
        self.textEdit_2.setObjectName(u"textEdit_2")
        self.textEdit_2.setGeometry(QRect(140, 180, 171, 131))
        self.textEdit_6 = QTextEdit(self.scrollAreaWidgetContents_3)
        self.textEdit_6.setObjectName(u"textEdit_6")
        self.textEdit_6.setGeometry(QRect(330, 180, 171, 131))
        self.textEdit_7 = QTextEdit(self.scrollAreaWidgetContents_3)
        self.textEdit_7.setObjectName(u"textEdit_7")
        self.textEdit_7.setGeometry(QRect(510, 180, 171, 131))
        self.textEdit_8 = QTextEdit(self.scrollAreaWidgetContents_3)
        self.textEdit_8.setObjectName(u"textEdit_8")
        self.textEdit_8.setGeometry(QRect(690, 180, 171, 131))
        self.textEdit_9 = QTextEdit(self.scrollAreaWidgetContents_3)
        self.textEdit_9.setObjectName(u"textEdit_9")
        self.textEdit_9.setGeometry(QRect(870, 180, 171, 131))
        self.textEdit_10 = QTextEdit(self.scrollAreaWidgetContents_3)
        self.textEdit_10.setObjectName(u"textEdit_10")
        self.textEdit_10.setGeometry(QRect(150, 350, 171, 131))
        self.textEdit_11 = QTextEdit(self.scrollAreaWidgetContents_3)
        self.textEdit_11.setObjectName(u"textEdit_11")
        self.textEdit_11.setGeometry(QRect(330, 350, 171, 131))
        self.textEdit_12 = QTextEdit(self.scrollAreaWidgetContents_3)
        self.textEdit_12.setObjectName(u"textEdit_12")
        self.textEdit_12.setGeometry(QRect(510, 350, 171, 131))
        self.textEdit_13 = QTextEdit(self.scrollAreaWidgetContents_3)
        self.textEdit_13.setObjectName(u"textEdit_13")
        self.textEdit_13.setGeometry(QRect(690, 350, 171, 131))
        self.textEdit_14 = QTextEdit(self.scrollAreaWidgetContents_3)
        self.textEdit_14.setObjectName(u"textEdit_14")
        self.textEdit_14.setGeometry(QRect(870, 350, 171, 131))
        self.textEdit_15 = QTextEdit(self.scrollAreaWidgetContents_3)
        self.textEdit_15.setObjectName(u"textEdit_15")
        self.textEdit_15.setGeometry(QRect(860, 530, 171, 131))
        self.textEdit_16 = QTextEdit(self.scrollAreaWidgetContents_3)
        self.textEdit_16.setObjectName(u"textEdit_16")
        self.textEdit_16.setGeometry(QRect(320, 530, 171, 131))
        self.textEdit_17 = QTextEdit(self.scrollAreaWidgetContents_3)
        self.textEdit_17.setObjectName(u"textEdit_17")
        self.textEdit_17.setGeometry(QRect(680, 530, 171, 131))
        self.textEdit_18 = QTextEdit(self.scrollAreaWidgetContents_3)
        self.textEdit_18.setObjectName(u"textEdit_18")
        self.textEdit_18.setGeometry(QRect(500, 530, 171, 131))
        self.textEdit_19 = QTextEdit(self.scrollAreaWidgetContents_3)
        self.textEdit_19.setObjectName(u"textEdit_19")
        self.textEdit_19.setGeometry(QRect(140, 530, 171, 131))
        self.textEdit_20 = QTextEdit(self.scrollAreaWidgetContents_3)
        self.textEdit_20.setObjectName(u"textEdit_20")
        self.textEdit_20.setGeometry(QRect(0, 170, 131, 131))
        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_3)

        self.gridLayout_27.addWidget(self.scrollArea_3, 1, 0, 1, 1)

        self.tabWidget_7.addTab(self.tab_36, "")
        self.tab_15 = QWidget()
        self.tab_15.setObjectName(u"tab_15")
        self.tabWidget_7.addTab(self.tab_15, "")

        self.gridLayout_9.addWidget(self.tabWidget_7, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab_20, "")

        self.gridLayout_4.addWidget(self.tabWidget, 0, 0, 1, 1)

        LogecC3.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(LogecC3)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1346, 24))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuTarget = QMenu(self.menubar)
        self.menuTarget.setObjectName(u"menuTarget")
        self.menu_Target_SpawnShell = QMenu(self.menuTarget)
        self.menu_Target_SpawnShell.setObjectName(u"menu_Target_SpawnShell")
        self.menu_Target_PythonShells = QMenu(self.menu_Target_SpawnShell)
        self.menu_Target_PythonShells.setObjectName(u"menu_Target_PythonShells")
        self.action_Target_Perl_binbash = QMenu(self.menu_Target_SpawnShell)
        self.action_Target_Perl_binbash.setObjectName(u"action_Target_Perl_binbash")
        self.menuRuby_Shells = QMenu(self.menu_Target_SpawnShell)
        self.menuRuby_Shells.setObjectName(u"menuRuby_Shells")
        self.menu_Target_Destruction = QMenu(self.menuTarget)
        self.menu_Target_Destruction.setObjectName(u"menu_Target_Destruction")
        self.menu_Target_Encryption = QMenu(self.menu_Target_Destruction)
        self.menu_Target_Encryption.setObjectName(u"menu_Target_Encryption")
        self.menu_Target_Info = QMenu(self.menuTarget)
        self.menu_Target_Info.setObjectName(u"menu_Target_Info")
        self.menu_GettingStarted = QMenu(self.menubar)
        self.menu_GettingStarted.setObjectName(u"menu_GettingStarted")
        self.menuExternal_Target = QMenu(self.menubar)
        self.menuExternal_Target.setObjectName(u"menuExternal_Target")
        self.menuExploits = QMenu(self.menuExternal_Target)
        self.menuExploits.setObjectName(u"menuExploits")
        self.menuWindows = QMenu(self.menuExploits)
        self.menuWindows.setObjectName(u"menuWindows")
        self.menuSMB = QMenu(self.menuWindows)
        self.menuSMB.setObjectName(u"menuSMB")
        self.menuEnumeration = QMenu(self.menuExternal_Target)
        self.menuEnumeration.setObjectName(u"menuEnumeration")
        self.menuData = QMenu(self.menubar)
        self.menuData.setObjectName(u"menuData")
        self.menuSQL_Shortcuts = QMenu(self.menuData)
        self.menuSQL_Shortcuts.setObjectName(u"menuSQL_Shortcuts")
        LogecC3.setMenuBar(self.menubar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuTarget.menuAction())
        self.menubar.addAction(self.menuExternal_Target.menuAction())
        self.menubar.addAction(self.menuData.menuAction())
        self.menubar.addAction(self.menu_GettingStarted.menuAction())
        self.menuFile.addAction(self.actionDEBUG)
        self.menuTarget.addAction(self.action_Target_Listen)
        self.menuTarget.addAction(self.menu_Target_Info.menuAction())
        self.menuTarget.addAction(self.menu_Target_SpawnShell.menuAction())
        self.menuTarget.addAction(self.menu_Target_Destruction.menuAction())
        self.menu_Target_SpawnShell.addSeparator()
        self.menu_Target_SpawnShell.addAction(self.actionLanguage)
        self.menu_Target_SpawnShell.addSeparator()
        self.menu_Target_SpawnShell.addAction(self.menu_Target_PythonShells.menuAction())
        self.menu_Target_SpawnShell.addAction(self.action_Target_Perl_binbash.menuAction())
        self.menu_Target_SpawnShell.addAction(self.menuRuby_Shells.menuAction())
        self.menu_Target_PythonShells.addAction(self.action_Target_Python_binbash)
        self.menu_Target_PythonShells.addAction(self.action_Target_Python_win)
        self.action_Target_Perl_binbash.addAction(self.action_Perl)
        self.menuRuby_Shells.addAction(self.action_Target_Ruby_NonInteractive)
        self.menu_Target_Destruction.addAction(self.menu_Target_Encryption.menuAction())
        self.menu_Target_Encryption.addAction(self.actionEncrypt_Files)
        self.menu_Target_Info.addAction(self.actionNetInfo)
        self.menu_GettingStarted.addAction(self.GettingStarted_Readme)
        self.menu_GettingStarted.addAction(self.actionRead_Me_webview)
        self.menuExternal_Target.addAction(self.menuEnumeration.menuAction())
        self.menuExternal_Target.addAction(self.menuExploits.menuAction())
        self.menuExploits.addAction(self.menuWindows.menuAction())
        self.menuExploits.addAction(self.actionLinux)
        self.menuExploits.addAction(self.actionOther)
        self.menuWindows.addAction(self.menuSMB.menuAction())
        self.menuSMB.addAction(self.actionCVE_2017_0144_Eternal_Blue)
        self.menuEnumeration.addAction(self.actionPort_Scan)
        self.menuData.addAction(self.menuSQL_Shortcuts.menuAction())
        self.menuSQL_Shortcuts.addAction(self.actionHelp_Menu_DB)
        self.menuSQL_Shortcuts.addAction(self.actionError_DB)
        self.menuSQL_Shortcuts.addAction(self.actionTables_DB_2)
        self.menuSQL_Shortcuts.addSeparator()
        self.menuSQL_Shortcuts.addAction(self.actionPortScan_DB_3)
        self.menuSQL_Shortcuts.addAction(self.actionOther_More_Cool_DB)

        self.retranslateUi(LogecC3)

        self.tabWidget.setCurrentIndex(8)
        self.text_PortScan_tab.setCurrentIndex(0)
        self.bruteforce_panel_2.setCurrentIndex(0)
        self.text_PortScan_tab_2.setCurrentIndex(2)
        self.tabWidget_5.setCurrentIndex(0)
        self.osint_dork.setCurrentIndex(2)
        self.tabWidget_3.setCurrentIndex(1)
        self.tabWidget_8.setCurrentIndex(1)
        self.tabWidget_9.setCurrentIndex(0)
        self.tabWidget_6.setCurrentIndex(1)
        self.bruteforce_panel.setCurrentIndex(0)
        self.tabWidget_14.setCurrentIndex(1)
        self.bruteforce_download_seclist_topshort.setDefault(False)
        self.bruteforce_download_seclist_top10mil_usernames.setDefault(False)
        self.bruteforce_fuzz_panel.setCurrentIndex(0)
        self.tabWidget_29.setCurrentIndex(3)
        self.bruteforce_download_seclist_top10mil_usernames_4.setDefault(False)
        self.bruteforce_download_seclist_topshort_4.setDefault(False)
        self.bruteforce_download_seclist_top10mil_usernames_5.setDefault(False)
        self.tabWidget_2.setCurrentIndex(2)
        self.tabWidget_4.setCurrentIndex(1)
        self.tabWidget_10.setCurrentIndex(1)
        self.tabWidget_16.setCurrentIndex(2)
        self.tabWidget_11.setCurrentIndex(2)
        self.tabWidget_12.setCurrentIndex(1)
        self.tabWidget_15.setCurrentIndex(1)
        self.tabWidget_7.setCurrentIndex(3)


        QMetaObject.connectSlotsByName(LogecC3)
    # setupUi

    def retranslateUi(self, LogecC3):
        LogecC3.setWindowTitle(QCoreApplication.translate("LogecC3", u"MainWindow", None))
        self.action_Target_Listen.setText(QCoreApplication.translate("LogecC3", u"Listen for connection", None))
        self.actionBash.setText(QCoreApplication.translate("LogecC3", u"/bin/bash", None))
        self.action_bin_sh.setText(QCoreApplication.translate("LogecC3", u"/bin/sh", None))
        self.action_Target_Python_binbash.setText(QCoreApplication.translate("LogecC3", u"Python Linux Shell", None))
        self.action_Target_Python_binsh.setText(QCoreApplication.translate("LogecC3", u"Windows Shell", None))
        self.action_Perl.setText(QCoreApplication.translate("LogecC3", u"Pearl Linux Shell", None))
        self.actionShell_Type.setText(QCoreApplication.translate("LogecC3", u"Shell Type", None))
        self.actionLanguage.setText(QCoreApplication.translate("LogecC3", u"Language", None))
        self.actionDisable_Firewall.setText(QCoreApplication.translate("LogecC3", u"Disable Firewall", None))
        self.GettingStarted_Readme.setText(QCoreApplication.translate("LogecC3", u"Read Me! (To shell tab)", None))
        self.menu_Data_Download.setText(QCoreApplication.translate("LogecC3", u"Download Files from Target", None))
        self.menu_Data_Upload.setText(QCoreApplication.translate("LogecC3", u"Upload Files to Target", None))
        self.action_Target_Ruby_NonInteractive.setText(QCoreApplication.translate("LogecC3", u"Linx Ruby Shell (Non-interactive)", None))
        self.actionEncrypt_Files.setText(QCoreApplication.translate("LogecC3", u"Encrypt Files", None))
        self.actionLinux.setText(QCoreApplication.translate("LogecC3", u"Linux", None))
        self.actionOther.setText(QCoreApplication.translate("LogecC3", u"Other", None))
        self.actionCVE_2017_0144_Eternal_Blue.setText(QCoreApplication.translate("LogecC3", u"CVE-2017-0144: Eternal Blue", None))
        self.action_Target_Python_win.setText(QCoreApplication.translate("LogecC3", u"Python Windows Shell", None))
        self.actionDEBUG.setText(QCoreApplication.translate("LogecC3", u"DEBUG", None))
        self.actionRead_Me_webview.setText(QCoreApplication.translate("LogecC3", u"Read Me! (webview)", None))
        self.actionNetInfo.setText(QCoreApplication.translate("LogecC3", u"NetInfo", None))
        self.actionPortScan_DB.setText(QCoreApplication.translate("LogecC3", u"PortScan DB", None))
        self.actionPortScan_DB_2.setText(QCoreApplication.translate("LogecC3", u"PortScan DB", None))
        self.actionHelp_DB.setText(QCoreApplication.translate("LogecC3", u"Help DB", None))
        self.actionTables_DB.setText(QCoreApplication.translate("LogecC3", u"Tables DB", None))
        self.actionHelp_Menu_DB.setText(QCoreApplication.translate("LogecC3", u"Help Menu DB", None))
        self.actionTables_DB_2.setText(QCoreApplication.translate("LogecC3", u"Tables DB", None))
        self.actionPortScan_DB_3.setText(QCoreApplication.translate("LogecC3", u"PortScan DB", None))
        self.actionOther_More_Cool_DB.setText(QCoreApplication.translate("LogecC3", u"Other More Cool DB", None))
        self.actionPort_Scan.setText(QCoreApplication.translate("LogecC3", u"Port Scan", None))
        self.actionError_DB.setText(QCoreApplication.translate("LogecC3", u"Error DB", None))
        self.status_data_IPADDR.setText(QCoreApplication.translate("LogecC3", u"N/A", None))
        self.label.setText(QCoreApplication.translate("LogecC3", u"send '!quit' to disconnect", None))
        self.status_label_IPADDR.setText(QCoreApplication.translate("LogecC3", u"External IP:", None))
        self.status_label_OS.setText(QCoreApplication.translate("LogecC3", u"OS:", None))
        self.status_Connected.setText(QCoreApplication.translate("LogecC3", u"Connection: Disconnected", None))
        self.status_data_HOSTNAME.setText(QCoreApplication.translate("LogecC3", u"N/A", None))
        self.status_label_HOSTNAME.setText(QCoreApplication.translate("LogecC3", u"HostName:", None))
#if QT_CONFIG(tooltip)
        self.text_PortScan_tab.setToolTip(QCoreApplication.translate("LogecC3", u"Enter", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.text_PortScan_tab.setWhatsThis(QCoreApplication.translate("LogecC3", u"Enter", None))
#endif // QT_CONFIG(whatsthis)
#if QT_CONFIG(tooltip)
        self.text_Program_Output.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.text_Program_Output.setPlaceholderText(QCoreApplication.translate("LogecC3", u"Results from command will show up here", None))
#if QT_CONFIG(tooltip)
        self.shell_input.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.shell_input.setPlaceholderText(QCoreApplication.translate("LogecC3", u"Enter Command Here!", None))
#if QT_CONFIG(tooltip)
        self.shell_input_enter.setToolTip(QCoreApplication.translate("LogecC3", u"Hit the Enter Key", None))
#endif // QT_CONFIG(tooltip)
        self.shell_input_enter.setText(QCoreApplication.translate("LogecC3", u"-->> Send <<-- ", None))
        self.text_PortScan_tab.setTabText(self.text_PortScan_tab.indexOf(self.tab), QCoreApplication.translate("LogecC3", u"Shell", None))
#if QT_CONFIG(tooltip)
        self.table_QueryDB_Button.setToolTip(QCoreApplication.translate("LogecC3", u"Run a query on the DB", None))
#endif // QT_CONFIG(tooltip)
        self.table_QueryDB_Button.setText(QCoreApplication.translate("LogecC3", u"-->> Query DB <<--", None))
#if QT_CONFIG(tooltip)
        self.table_RefreshDB_Button.setToolTip(QCoreApplication.translate("LogecC3", u"Refresh the Database, updating values from the SQLITE DB file", None))
#endif // QT_CONFIG(tooltip)
        self.table_RefreshDB_Button.setText(QCoreApplication.translate("LogecC3", u"-->> Refresh DB <<--", None))
        self.DB_Query.setText("")
        self.DB_Query.setPlaceholderText(QCoreApplication.translate("LogecC3", u"Enter SQL Query! Type !_help for help! ", None))
        self.text_PortScan_tab.setTabText(self.text_PortScan_tab.indexOf(self.tab_2), QCoreApplication.translate("LogecC3", u"Local DB", None))
        self.status_data_OS.setText(QCoreApplication.translate("LogecC3", u"N/A", None))
        self.lineEdit_5.setText(QCoreApplication.translate("LogecC3", u"Font for the left is lato regular, it's not bad. might switch everyhting to it", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("LogecC3", u"Main/C2", None))
        self.bruteforce_currentbatch_2.setHtml(QCoreApplication.translate("LogecC3", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Cantarell'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">IP: 51.16.91.8:7331 | User: Root | Length 41m 31s</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">IP: 51.16.91.8:7331 | User: Root | Length 41m 31s</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style"
                        "=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">IP: 51.16.91.8:7331 | User: Root | Length 41m 31s</p></body></html>", None))
        self.bruteforce_panel_2.setTabText(self.bruteforce_panel_2.indexOf(self.tab_55), QCoreApplication.translate("LogecC3", u"Clients", None))
        self.bruteforce_goodcreds_2.setHtml(QCoreApplication.translate("LogecC3", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Cantarell'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.bruteforce_panel_2.setTabText(self.bruteforce_panel_2.indexOf(self.tab_54), QCoreApplication.translate("LogecC3", u"Connection Details", None))
        self.bruteforce_errlog_2.setHtml(QCoreApplication.translate("LogecC3", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Cantarell'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.bruteforce_panel_2.setTabText(self.bruteforce_panel_2.indexOf(self.tab_56), QCoreApplication.translate("LogecC3", u"Log (0)", None))
#if QT_CONFIG(tooltip)
        self.text_PortScan_tab_2.setToolTip(QCoreApplication.translate("LogecC3", u"Enter", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.text_PortScan_tab_2.setWhatsThis(QCoreApplication.translate("LogecC3", u"Enter", None))
#endif // QT_CONFIG(whatsthis)
#if QT_CONFIG(tooltip)
        self.text_Program_Output_2.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.text_Program_Output_2.setHtml(QCoreApplication.translate("LogecC3", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Cantarell'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.text_Program_Output_2.setPlaceholderText(QCoreApplication.translate("LogecC3", u"root@127.0.0.1> ", None))
#if QT_CONFIG(tooltip)
        self.shell_input_2.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.shell_input_2.setPlaceholderText(QCoreApplication.translate("LogecC3", u"Enter Command Here!", None))
#if QT_CONFIG(tooltip)
        self.shell_input_enter_2.setToolTip(QCoreApplication.translate("LogecC3", u"Hit the Enter Key", None))
#endif // QT_CONFIG(tooltip)
        self.shell_input_enter_2.setText(QCoreApplication.translate("LogecC3", u"-->> Send <<-- ", None))
        self.text_PortScan_tab_2.setTabText(self.text_PortScan_tab_2.indexOf(self.tab_57), QCoreApplication.translate("LogecC3", u"RemoteShell", None))
#if QT_CONFIG(tooltip)
        self.table_QueryDB_Button_2.setToolTip(QCoreApplication.translate("LogecC3", u"Run a query on the DB", None))
#endif // QT_CONFIG(tooltip)
        self.table_QueryDB_Button_2.setText(QCoreApplication.translate("LogecC3", u"-->> Query DB <<--", None))
#if QT_CONFIG(tooltip)
        self.table_RefreshDB_Button_2.setToolTip(QCoreApplication.translate("LogecC3", u"Refresh the Database, updating values from the SQLITE DB file", None))
#endif // QT_CONFIG(tooltip)
        self.table_RefreshDB_Button_2.setText(QCoreApplication.translate("LogecC3", u"-->> Refresh DB <<--", None))
        self.DB_Query_2.setText("")
        self.DB_Query_2.setPlaceholderText(QCoreApplication.translate("LogecC3", u"Enter SQL Query! Type !_help for help! ", None))
        self.text_PortScan_tab_2.setTabText(self.text_PortScan_tab_2.indexOf(self.tab_58), QCoreApplication.translate("LogecC3", u"Local DB", None))
#if QT_CONFIG(tooltip)
        self.c2_systemshell.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.c2_systemshell.setHtml(QCoreApplication.translate("LogecC3", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Cantarell'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.c2_systemshell.setPlaceholderText(QCoreApplication.translate("LogecC3", u"root@127.0.0.1> ", None))
#if QT_CONFIG(tooltip)
        self.c2_systemshell_input.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.c2_systemshell_input.setPlaceholderText(QCoreApplication.translate("LogecC3", u"Enter Command Here!", None))
#if QT_CONFIG(tooltip)
        self.c2_systemshell_send.setToolTip(QCoreApplication.translate("LogecC3", u"Hit the Enter Key", None))
#endif // QT_CONFIG(tooltip)
        self.c2_systemshell_send.setText(QCoreApplication.translate("LogecC3", u"-->> Send <<-- ", None))
        self.text_PortScan_tab_2.setTabText(self.text_PortScan_tab_2.indexOf(self.tab_59), QCoreApplication.translate("LogecC3", u"LocalShell", None))
        self.textEdit_25.setHtml(QCoreApplication.translate("LogecC3", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Cantarell'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Fira Code';\">Adding a menu bar in here</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Fira Code';\"><br /><br />from PyQt5.QtWidgets import QApplication, QMainWindow, QMenuBar, QTabWidget, QWidget</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Fira Code';\"><br /></p>\n"
"<p style=\" margin-to"
                        "p:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Fira Code';\">app = QApplication([])</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Fira Code';\">window = QMainWindow()</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Fira Code';\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Fira Code';\">menu_bar = QMenuBar()</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Fira Code';\">file_menu = menu_bar.addMenu(&quot;File&quot;)</span></p>\n"
"<p style=\"-qt-paragraph-type:emp"
                        "ty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Fira Code';\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Fira Code';\">tab_widget = QTabWidget()</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Fira Code';\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Fira Code';\">tab1 = QWidget()</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Fira Code';\">tab1.setLayout(menu_bar)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -q"
                        "t-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Fira Code';\">tab_widget.addTab(tab1, &quot;Tab 1&quot;)</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Fira Code';\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Fira Code';\">window.setCentralWidget(tab_widget)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Fira Code';\">window.show()</span></p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_53), QCoreApplication.translate("LogecC3", u"C2New", None))
        self.label_70.setText(QCoreApplication.translate("LogecC3", u"Other?", None))
        self.label_67.setText(QCoreApplication.translate("LogecC3", u"Username", None))
        self.label_69.setText(QCoreApplication.translate("LogecC3", u"DC-IP", None))
        self.label_68.setText(QCoreApplication.translate("LogecC3", u"Password", None))
        self.lineEdit_14.setPlaceholderText(QCoreApplication.translate("LogecC3", u"AldersonE", None))
        self.portscan_start_6.setText(QCoreApplication.translate("LogecC3", u"-->> Start <<--", None))
        self.lineEdit_15.setPlaceholderText(QCoreApplication.translate("LogecC3", u"MR.Rob3t", None))
        self.dashboard_osint_keyword_2.setPlaceholderText(QCoreApplication.translate("LogecC3", u"AllSafe", None))
        self.lineEdit_16.setText("")
        self.lineEdit_16.setPlaceholderText(QCoreApplication.translate("LogecC3", u"Optional", None))
        self.label_62.setText(QCoreApplication.translate("LogecC3", u"Kerberoast", None))
        self.lineEdit_12.setText(QCoreApplication.translate("LogecC3", u"Length", None))
#if QT_CONFIG(tooltip)
        self.dashboard_reddit_onlycomments_2.setToolTip(QCoreApplication.translate("LogecC3", u"Search ONLY for comments with \"KEYWORD\" in the text", None))
#endif // QT_CONFIG(tooltip)
        self.dashboard_reddit_onlycomments_2.setText(QCoreApplication.translate("LogecC3", u"Comment Search", None))
        self.combo_time_3.setItemText(0, QCoreApplication.translate("LogecC3", u"All", None))
        self.combo_time_3.setItemText(1, QCoreApplication.translate("LogecC3", u"Year", None))
        self.combo_time_3.setItemText(2, QCoreApplication.translate("LogecC3", u"Month", None))
        self.combo_time_3.setItemText(3, QCoreApplication.translate("LogecC3", u"Day", None))
        self.combo_time_3.setItemText(4, QCoreApplication.translate("LogecC3", u"Hour", None))

        self.label_63.setText(QCoreApplication.translate("LogecC3", u"SortBy", None))
        self.label_64.setText(QCoreApplication.translate("LogecC3", u"Time", None))
#if QT_CONFIG(tooltip)
        self.dashboard_reddit_onlyprofile_2.setToolTip(QCoreApplication.translate("LogecC3", u"Search for a user profile, enter the username in \"keyword\"", None))
#endif // QT_CONFIG(tooltip)
        self.dashboard_reddit_onlyprofile_2.setText(QCoreApplication.translate("LogecC3", u"Profile Search", None))
        self.combo_sort_3.setItemText(0, QCoreApplication.translate("LogecC3", u"Hot", None))
        self.combo_sort_3.setItemText(1, QCoreApplication.translate("LogecC3", u"Top", None))
        self.combo_sort_3.setItemText(2, QCoreApplication.translate("LogecC3", u"New", None))
        self.combo_sort_3.setItemText(3, QCoreApplication.translate("LogecC3", u"Controversial", None))
        self.combo_sort_3.setItemText(4, QCoreApplication.translate("LogecC3", u"Comments", None))

#if QT_CONFIG(tooltip)
        self.dashboard_reddit_downloadmedia_2.setToolTip(QCoreApplication.translate("LogecC3", u"Download Images/Videos associated with the posts searched", None))
#endif // QT_CONFIG(tooltip)
        self.dashboard_reddit_downloadmedia_2.setText(QCoreApplication.translate("LogecC3", u"Download Media", None))
        self.dashboard_reddit_subreddit_2.setPlaceholderText(QCoreApplication.translate("LogecC3", u"r/technology", None))
        self.label_65.setText(QCoreApplication.translate("LogecC3", u"Subreddit (Optional)", None))
        self.dashboard_reddit_hideNSFW_2.setText(QCoreApplication.translate("LogecC3", u"Hide NSFW", None))
        self.lineEdit_13.setText(QCoreApplication.translate("LogecC3", u"Non Functional", None))
        self.label_66.setText(QCoreApplication.translate("LogecC3", u"Domain", None))
        self.tabWidget_5.setTabText(self.tabWidget_5.indexOf(self.tab_39), QCoreApplication.translate("LogecC3", u"DashBoard", None))
        self.tabWidget_5.setTabText(self.tabWidget_5.indexOf(self.tab_40), QCoreApplication.translate("LogecC3", u"Kerberoast", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_38), QCoreApplication.translate("LogecC3", u"AD", None))
        self.label_7.setText(QCoreApplication.translate("LogecC3", u"Keyword(s) ", None))
        self.dashboard_osint_keyword.setPlaceholderText(QCoreApplication.translate("LogecC3", u"Windows", None))
        self.comboBox_3.setItemText(0, QCoreApplication.translate("LogecC3", u"Everything (Grabs everything, all possible boxes are checked)", None))
        self.comboBox_3.setItemText(1, QCoreApplication.translate("LogecC3", u"Username (pulls data with specific username in it)", None))
        self.comboBox_3.setItemText(2, QCoreApplication.translate("LogecC3", u"Everythign Keyword (grabs wverything based off of specific keyword)", None))
        self.comboBox_3.setItemText(3, QCoreApplication.translate("LogecC3", u"Custom (Nothing checked, up to user)", None))

        self.label_11.setText(QCoreApplication.translate("LogecC3", u"Reddit", None))
        self.lineEdit_6.setText(QCoreApplication.translate("LogecC3", u"Length", None))
#if QT_CONFIG(tooltip)
        self.dashboard_reddit_onlycomments.setToolTip(QCoreApplication.translate("LogecC3", u"Search ONLY for comments with \"KEYWORD\" in the text", None))
#endif // QT_CONFIG(tooltip)
        self.dashboard_reddit_onlycomments.setText(QCoreApplication.translate("LogecC3", u"Comment Search", None))
        self.combo_time_2.setItemText(0, QCoreApplication.translate("LogecC3", u"All", None))
        self.combo_time_2.setItemText(1, QCoreApplication.translate("LogecC3", u"Year", None))
        self.combo_time_2.setItemText(2, QCoreApplication.translate("LogecC3", u"Month", None))
        self.combo_time_2.setItemText(3, QCoreApplication.translate("LogecC3", u"Day", None))
        self.combo_time_2.setItemText(4, QCoreApplication.translate("LogecC3", u"Hour", None))

        self.label_15.setText(QCoreApplication.translate("LogecC3", u"SortBy", None))
        self.label_17.setText(QCoreApplication.translate("LogecC3", u"Time", None))
#if QT_CONFIG(tooltip)
        self.dashboard_reddit_onlyprofile.setToolTip(QCoreApplication.translate("LogecC3", u"Search for a user profile, enter the username in \"keyword\"", None))
#endif // QT_CONFIG(tooltip)
        self.dashboard_reddit_onlyprofile.setText(QCoreApplication.translate("LogecC3", u"Profile Search", None))
        self.combo_sort_2.setItemText(0, QCoreApplication.translate("LogecC3", u"Hot", None))
        self.combo_sort_2.setItemText(1, QCoreApplication.translate("LogecC3", u"Top", None))
        self.combo_sort_2.setItemText(2, QCoreApplication.translate("LogecC3", u"New", None))
        self.combo_sort_2.setItemText(3, QCoreApplication.translate("LogecC3", u"Controversial", None))
        self.combo_sort_2.setItemText(4, QCoreApplication.translate("LogecC3", u"Comments", None))

#if QT_CONFIG(tooltip)
        self.dashboard_reddit_downloadmedia.setToolTip(QCoreApplication.translate("LogecC3", u"Download Images/Videos associated with the posts searched", None))
#endif // QT_CONFIG(tooltip)
        self.dashboard_reddit_downloadmedia.setText(QCoreApplication.translate("LogecC3", u"Download Media", None))
        self.dashboard_reddit_subreddit.setPlaceholderText(QCoreApplication.translate("LogecC3", u"r/technology", None))
        self.label_23.setText(QCoreApplication.translate("LogecC3", u"Subreddit (Optional)", None))
        self.dashboard_reddit_hideNSFW.setText(QCoreApplication.translate("LogecC3", u"Hide NSFW", None))
        self.lineEdit_7.setText(QCoreApplication.translate("LogecC3", u"Non Functional", None))
        self.portscan_start_5.setText(QCoreApplication.translate("LogecC3", u"-->> Start <<--", None))
        self.label_24.setText(QCoreApplication.translate("LogecC3", u"Preset", None))
        self.osint_dork.setTabText(self.osint_dork.indexOf(self.tab_12), QCoreApplication.translate("LogecC3", u"Dashboard", None))
#if QT_CONFIG(tooltip)
        self.osint_reddit_onlyprofile.setToolTip(QCoreApplication.translate("LogecC3", u"Search for a user profile, enter the username in \"keyword\"", None))
#endif // QT_CONFIG(tooltip)
        self.osint_reddit_onlyprofile.setText(QCoreApplication.translate("LogecC3", u"Profile Search", None))
        self.osint_reddit_search.setText(QCoreApplication.translate("LogecC3", u"-->> Search <<--", None))
        self.osint_reddit_keyword.setPlaceholderText(QCoreApplication.translate("LogecC3", u"Windows", None))
        self.label_10.setText(QCoreApplication.translate("LogecC3", u"Time", None))
        self.combo_sort.setItemText(0, QCoreApplication.translate("LogecC3", u"Hot", None))
        self.combo_sort.setItemText(1, QCoreApplication.translate("LogecC3", u"Top", None))
        self.combo_sort.setItemText(2, QCoreApplication.translate("LogecC3", u"New", None))
        self.combo_sort.setItemText(3, QCoreApplication.translate("LogecC3", u"Controversial", None))
        self.combo_sort.setItemText(4, QCoreApplication.translate("LogecC3", u"Comments", None))

#if QT_CONFIG(tooltip)
        self.checkBox_2.setToolTip(QCoreApplication.translate("LogecC3", u"Add/append results to previous results", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.checkBox_2.setStatusTip("")
#endif // QT_CONFIG(statustip)
        self.checkBox_2.setText(QCoreApplication.translate("LogecC3", u"Append Results to DB", None))
        self.DB_Query_osint_reddit.setPlaceholderText(QCoreApplication.translate("LogecC3", u"SELECT * FROM RedditResults", None))
        self.label_6.setText(QCoreApplication.translate("LogecC3", u"Keyword (required)", None))
#if QT_CONFIG(tooltip)
        self.table_QueryDB_Button_osint_reddit.setToolTip(QCoreApplication.translate("LogecC3", u"Run a query on the DB", None))
#endif // QT_CONFIG(tooltip)
        self.table_QueryDB_Button_osint_reddit.setText(QCoreApplication.translate("LogecC3", u"-->> Query DB <<--", None))
        self.osint_reddit_hideNSFW.setText(QCoreApplication.translate("LogecC3", u"Hide NSFW", None))
        self.combo_time.setItemText(0, QCoreApplication.translate("LogecC3", u"All", None))
        self.combo_time.setItemText(1, QCoreApplication.translate("LogecC3", u"Year", None))
        self.combo_time.setItemText(2, QCoreApplication.translate("LogecC3", u"Month", None))
        self.combo_time.setItemText(3, QCoreApplication.translate("LogecC3", u"Day", None))
        self.combo_time.setItemText(4, QCoreApplication.translate("LogecC3", u"Hour", None))

#if QT_CONFIG(tooltip)
        self.osint_reddit_downloadmedia.setToolTip(QCoreApplication.translate("LogecC3", u"Download Images/Videos associated with the posts searched", None))
#endif // QT_CONFIG(tooltip)
        self.osint_reddit_downloadmedia.setText(QCoreApplication.translate("LogecC3", u"Download Media", None))
#if QT_CONFIG(tooltip)
        self.table_RefreshDB_Button_osint_reddit.setToolTip(QCoreApplication.translate("LogecC3", u"Refresh the Database, updating values from the SQLITE DB file", None))
#endif // QT_CONFIG(tooltip)
        self.table_RefreshDB_Button_osint_reddit.setText(QCoreApplication.translate("LogecC3", u"-->> Refresh DB <<--", None))
#if QT_CONFIG(tooltip)
        self.osint_reddit_onlycomments.setToolTip(QCoreApplication.translate("LogecC3", u"Search ONLY for comments with \"KEYWORD\" in the text", None))
#endif // QT_CONFIG(tooltip)
        self.osint_reddit_onlycomments.setText(QCoreApplication.translate("LogecC3", u"Comment Search", None))
        self.label_9.setText(QCoreApplication.translate("LogecC3", u"SortBy", None))
        self.label_8.setText(QCoreApplication.translate("LogecC3", u"Subreddit (Optional)", None))
        self.osint_reddit_subreddit.setPlaceholderText(QCoreApplication.translate("LogecC3", u"r/technology", None))
        self.osint_dork.setTabText(self.osint_dork.indexOf(self.tab_13), QCoreApplication.translate("LogecC3", u"Reddit", None))
        self.label_54.setText(QCoreApplication.translate("LogecC3", u"Search Term", None))
        self.label_53.setText(QCoreApplication.translate("LogecC3", u"In Title", None))
        self.label_52.setText(QCoreApplication.translate("LogecC3", u"FileType", None))
        self.label_50.setText(QCoreApplication.translate("LogecC3", u"Keyword", None))
        self.label_51.setText(QCoreApplication.translate("LogecC3", u"Site", None))
        self.checkBox_21.setText(QCoreApplication.translate("LogecC3", u"Search For Link", None))
        self.checkBox_19.setText(QCoreApplication.translate("LogecC3", u"Related/Similar Sites", None))
        self.checkBox_20.setText(QCoreApplication.translate("LogecC3", u"Show Cached Content", None))
        self.osint_dork_generate.setText(QCoreApplication.translate("LogecC3", u"Generate", None))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_31), QCoreApplication.translate("LogecC3", u"Results", None))
        self.lineEdit_18.setText(QCoreApplication.translate("LogecC3", u"Put a DB view (or multiple) of a table in the DB with cheathssset google dorks", None))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_42), QCoreApplication.translate("LogecC3", u"CheatSheet", None))
        self.osint_dork.setTabText(self.osint_dork.indexOf(self.tab_18), QCoreApplication.translate("LogecC3", u"DorkGen", None))
        self.lineEdit_8.setText(QCoreApplication.translate("LogecC3", u"Non Functional", None))
        self.osint_dork.setTabText(self.osint_dork.indexOf(self.tab_14), QCoreApplication.translate("LogecC3", u"VideoCams(use qwebview)", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QCoreApplication.translate("LogecC3", u"Osint", None))
        self.label_16.setText(QCoreApplication.translate("LogecC3", u"Preset", None))
        self.comboBox_2.setItemText(0, QCoreApplication.translate("LogecC3", u"WebScan (Nikto, dirbuster)", None))
        self.comboBox_2.setItemText(1, QCoreApplication.translate("LogecC3", u"Full Scan (Everything, portscan first)", None))

        self.portscan_start_4.setText(QCoreApplication.translate("LogecC3", u"-->> Start <<--", None))
        self.dashboard_portscan_IP.setPlaceholderText(QCoreApplication.translate("LogecC3", u"8.8.8.8", None))
        self.dashboard_portscan_stealth_check.setText(QCoreApplication.translate("LogecC3", u"Stealth", None))
        self.checkBox_6.setText(QCoreApplication.translate("LogecC3", u"Other2", None))
        self.dashboard_portscan_standard_check.setText(QCoreApplication.translate("LogecC3", u"Standard", None))
        self.dashboard_portscan_extraport.setPlaceholderText(QCoreApplication.translate("LogecC3", u"80, 443", None))
        self.dashboard_portscan_maxport.setPlaceholderText(QCoreApplication.translate("LogecC3", u"1024", None))
        self.dashboard_portscan_fast_check.setText(QCoreApplication.translate("LogecC3", u"Fast", None))
        self.dashboard_portscan_minport.setPlaceholderText(QCoreApplication.translate("LogecC3", u"1", None))
        self.label_21.setText(QCoreApplication.translate("LogecC3", u"PortScan", None))
        self.dashboard_dnsName.setPlaceholderText(QCoreApplication.translate("LogecC3", u"8.8.8.8", None))
        self.label_22.setText(QCoreApplication.translate("LogecC3", u"DNS Lookup", None))
        self.lineEdit_9.setText(QCoreApplication.translate("LogecC3", u"Non Functional", None))
        self.label_38.setText(QCoreApplication.translate("LogecC3", u"IP/Name", None))
        self.tabWidget_8.setTabText(self.tabWidget_8.indexOf(self.tab_24), QCoreApplication.translate("LogecC3", u"DashBoard", None))
        self.portscan_fast_timeout.setItemText(0, QCoreApplication.translate("LogecC3", u"Normal Speed (1 Second Timeout)", None))
        self.portscan_fast_timeout.setItemText(1, QCoreApplication.translate("LogecC3", u"Light Speed (.5 Second Timeout)", None))
        self.portscan_fast_timeout.setItemText(2, QCoreApplication.translate("LogecC3", u"Ridiculous Speed (.25 Second Timeout)", None))
        self.portscan_fast_timeout.setItemText(3, QCoreApplication.translate("LogecC3", u"Ludicrous Speed (.1 Second Timeout)", None))
        self.portscan_fast_timeout.setItemText(4, QCoreApplication.translate("LogecC3", u"Plaid (.01 Second Timeout)", None))

        self.portscan_delay.setItemText(0, QCoreApplication.translate("LogecC3", u"None", None))
        self.portscan_delay.setItemText(1, QCoreApplication.translate("LogecC3", u".001-.1", None))
        self.portscan_delay.setItemText(2, QCoreApplication.translate("LogecC3", u".1-1.0", None))
        self.portscan_delay.setItemText(3, QCoreApplication.translate("LogecC3", u"1.0-5.0", None))
        self.portscan_delay.setItemText(4, "")

        self.DB_Query_scanning_portscan.setText("")
        self.DB_Query_scanning_portscan.setPlaceholderText(QCoreApplication.translate("LogecC3", u"Enter SQL Query! Type !_help for help! ", None))
#if QT_CONFIG(tooltip)
        self.table_RefreshDB_Button_scanning_portscan.setToolTip(QCoreApplication.translate("LogecC3", u"Refresh the Database, updating values from the SQLITE DB file", None))
#endif // QT_CONFIG(tooltip)
        self.table_RefreshDB_Button_scanning_portscan.setText(QCoreApplication.translate("LogecC3", u"-->> Refresh DB <<--", None))
#if QT_CONFIG(tooltip)
        self.table_QueryDB_Button_scanning_portscan.setToolTip(QCoreApplication.translate("LogecC3", u"Run a query on the DB", None))
#endif // QT_CONFIG(tooltip)
        self.table_QueryDB_Button_scanning_portscan.setText(QCoreApplication.translate("LogecC3", u"-->> Query DB <<--", None))
        self.tabWidget_9.setTabText(self.tabWidget_9.indexOf(self.tab_25), QCoreApplication.translate("LogecC3", u"LocalDB", None))
        self.tabWidget_9.setTabText(self.tabWidget_9.indexOf(self.tab_26), QCoreApplication.translate("LogecC3", u"ProgressBars", None))
        self.portscan_stealth_check.setText(QCoreApplication.translate("LogecC3", u"Stealth (Scapy)", None))
        self.portscan_standard_check.setText(QCoreApplication.translate("LogecC3", u"Standard (Telnet)", None))
        self.portscan_fast_check.setText(QCoreApplication.translate("LogecC3", u"???", None))
        self.label_61.setText(QCoreApplication.translate("LogecC3", u"Speed", None))
        self.portscan_IP.setPlaceholderText(QCoreApplication.translate("LogecC3", u"8.8.8.8", None))
        self.checkBox_4.setText(QCoreApplication.translate("LogecC3", u"???", None))
        self.portscan_minport.setText(QCoreApplication.translate("LogecC3", u"1", None))
        self.portscan_minport.setPlaceholderText(QCoreApplication.translate("LogecC3", u"1", None))
        self.label_13.setText(QCoreApplication.translate("LogecC3", u"192.168.0.1 Stealth 1-100, 80, 631", None))
        self.portscan_extraport.setPlaceholderText(QCoreApplication.translate("LogecC3", u"80, 443", None))
        self.portscan_maxport.setText(QCoreApplication.translate("LogecC3", u"1024", None))
        self.portscan_maxport.setPlaceholderText(QCoreApplication.translate("LogecC3", u"1024", None))
        self.portscan_start.setText(QCoreApplication.translate("LogecC3", u"-->> Start Scan <<--", None))
        self.portscan_1_1024.setText(QCoreApplication.translate("LogecC3", u"1-1024", None))
        self.portscan_1_10000.setText(QCoreApplication.translate("LogecC3", u"1-10,000", None))
        self.portscan_1_65535.setText(QCoreApplication.translate("LogecC3", u"1-65535 ", None))
        self.label_60.setText(QCoreApplication.translate("LogecC3", u"Random Delay (S)", None))
        self.tabWidget_13.setTabText(self.tabWidget_13.indexOf(self.tab_61), QCoreApplication.translate("LogecC3", u"Open Ports", None))
        self.tabWidget_13.setTabText(self.tabWidget_13.indexOf(self.tab_62), QCoreApplication.translate("LogecC3", u"Tab 2", None))
        self.tabWidget_8.setTabText(self.tabWidget_8.indexOf(self.tab_23), QCoreApplication.translate("LogecC3", u"PortScan", None))
        self.label_30.setText(QCoreApplication.translate("LogecC3", u"MX", None))
        self.scanning_dns_query.setText(QCoreApplication.translate("LogecC3", u"google.com", None))
        self.scanning_dns_query.setPlaceholderText(QCoreApplication.translate("LogecC3", u"Enter URL/IP", None))
        self.label_28.setText(QCoreApplication.translate("LogecC3", u"CNAME", None))
        self.scanning_dns_lookup.setText(QCoreApplication.translate("LogecC3", u"-->> Lookup <<--", None))
        self.label_29.setText(QCoreApplication.translate("LogecC3", u"NS", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("LogecC3", u"All Records", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("LogecC3", u"MX", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("LogecC3", u"Cname", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("LogecC3", u"A (IP)", None))

        self.label_31.setText(QCoreApplication.translate("LogecC3", u"Reverse Lookup", None))
        self.label_26.setText(QCoreApplication.translate("LogecC3", u"A Record", None))
        self.label_27.setText(QCoreApplication.translate("LogecC3", u"TXT ", None))
        self.tabWidget_8.setTabText(self.tabWidget_8.indexOf(self.tab_16), QCoreApplication.translate("LogecC3", u"DNS Lookup", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_22), QCoreApplication.translate("LogecC3", u"Scanning/Enumeration", None))
#if QT_CONFIG(accessibility)
        self.tabWidget_6.setAccessibleName("")
#endif // QT_CONFIG(accessibility)
        self.bruteforce_pass_browse.setText(QCoreApplication.translate("LogecC3", u"Browse", None))
        self.label_143.setText(QCoreApplication.translate("LogecC3", u"Delay (Up to X seconds)", None))
        self.label_145.setText(QCoreApplication.translate("LogecC3", u"Username Directory", None))
        self.bruteforce_user_browse.setText(QCoreApplication.translate("LogecC3", u"Browse", None))
        self.bruteforce_target.setText(QCoreApplication.translate("LogecC3", u"127.0.0.1", None))
        self.label_148.setText(QCoreApplication.translate("LogecC3", u"Target IP/Hostname", None))
        self.bruteforce_stop.setText(QCoreApplication.translate("LogecC3", u"-->> Stop Bruteforce <<--", None))
        self.label_71.setText(QCoreApplication.translate("LogecC3", u"Batch Size (May not need)", None))
        self.bruteforce_start.setText(QCoreApplication.translate("LogecC3", u"-->> Start Bruteforce <<--", None))
        self.bruteforce_passdir.setText(QCoreApplication.translate("LogecC3", u"/home/kali/Documents/passlist", None))
        self.comboBox_5.setItemText(0, QCoreApplication.translate("LogecC3", u"Aggresive (Batch size: 100, Threads: 100, Delay: 1 Sec)", None))

        self.label_55.setText(QCoreApplication.translate("LogecC3", u"Threads", None))
        self.bruteforce_goodcreds.setHtml(QCoreApplication.translate("LogecC3", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Cantarell'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.bruteforce_panel.setTabText(self.bruteforce_panel.indexOf(self.tab_46), QCoreApplication.translate("LogecC3", u"Successful (0)", None))
        self.bruteforce_currentbatch.setHtml(QCoreApplication.translate("LogecC3", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Cantarell'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">('1', '78')</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">('1', '79')</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">('1', '81')</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">('1', '82')</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">('1"
                        "', '83')</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">('1', '84')</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">('1', '85')</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">('1', '86')</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">('1', '87')</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">('1', '88')</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.bruteforce_panel.setTabText(self.bruteforce_panel.indexOf(self.tab_47), QCoreApplication.translate("LogecC3", u"Current Batch (0/0)", None))
        self.bruteforce_errlog.setHtml(QCoreApplication.translate("LogecC3", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Cantarell'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.bruteforce_panel.setTabText(self.bruteforce_panel.indexOf(self.tab_51), QCoreApplication.translate("LogecC3", u"Log (0)", None))
        self.bruteforce_protocol.setItemText(0, QCoreApplication.translate("LogecC3", u"FTP", None))
        self.bruteforce_protocol.setItemText(1, QCoreApplication.translate("LogecC3", u"SSH", None))
        self.bruteforce_protocol.setItemText(2, QCoreApplication.translate("LogecC3", u"SQL", None))
        self.bruteforce_protocol.setItemText(3, QCoreApplication.translate("LogecC3", u"SMB", None))
        self.bruteforce_protocol.setItemText(4, QCoreApplication.translate("LogecC3", u"HTTP", None))
        self.bruteforce_protocol.setItemText(5, QCoreApplication.translate("LogecC3", u"HTTPS", None))

        self.label_142.setText(QCoreApplication.translate("LogecC3", u"Port (Optional)", None))
        self.label_150.setText(QCoreApplication.translate("LogecC3", u"Progress", None))
        self.bruteforce_userdir.setText(QCoreApplication.translate("LogecC3", u"/home/kali/Documents/userlist", None))
        self.label_147.setText(QCoreApplication.translate("LogecC3", u"Password Directory", None))
        self.label_149.setText(QCoreApplication.translate("LogecC3", u"Current Attempts:", None))
        self.DB_Query_scanning_bruteforce.setText("")
        self.DB_Query_scanning_bruteforce.setPlaceholderText(QCoreApplication.translate("LogecC3", u"Enter SQL Query! Type !_help for help! ", None))
#if QT_CONFIG(tooltip)
        self.scanning_bruteforce_refresh.setToolTip(QCoreApplication.translate("LogecC3", u"Refresh the Database, updating values from the SQLITE DB file", None))
#endif // QT_CONFIG(tooltip)
        self.scanning_bruteforce_refresh.setText(QCoreApplication.translate("LogecC3", u"-->> Refresh DB <<--", None))
#if QT_CONFIG(tooltip)
        self.scanning_bruteforce_query.setToolTip(QCoreApplication.translate("LogecC3", u"Run a query on the DB", None))
#endif // QT_CONFIG(tooltip)
        self.scanning_bruteforce_query.setText(QCoreApplication.translate("LogecC3", u"-->> Query DB <<--", None))
        self.tabWidget_14.setTabText(self.tabWidget_14.indexOf(self.tab_87), QCoreApplication.translate("LogecC3", u"LocalDB", None))
        self.lineEdit_21.setText(QCoreApplication.translate("LogecC3", u"SecList Default Passwords", None))
        self.bruteforce_download_seclist_topshort.setText(QCoreApplication.translate("LogecC3", u"Download", None))
        self.bruteforce_download_seclist_defaults.setText(QCoreApplication.translate("LogecC3", u"Download", None))
        self.lineEdit_23.setText(QCoreApplication.translate("LogecC3", u"SecList Top Usernames (Short List)", None))
        self.label_74.setText(QCoreApplication.translate("LogecC3", u"Usernames", None))
        self.lineEdit_20.setText(QCoreApplication.translate("LogecC3", u"Ignis 1m Public Passwords", None))
        self.bruteforce_download_seclist_top10mil_usernames.setText(QCoreApplication.translate("LogecC3", u"Download", None))
        self.bruteforce_download_seclist_top10mil.setText(QCoreApplication.translate("LogecC3", u"Download", None))
        self.lineEdit_24.setText(QCoreApplication.translate("LogecC3", u"SecList Top 10 Million Passwords", None))
        self.bruteforce_download_ignis_1M.setText(QCoreApplication.translate("LogecC3", u"Download", None))
        self.lineEdit_22.setText(QCoreApplication.translate("LogecC3", u"SecList 10mil Usernames", None))
        self.label_73.setText(QCoreApplication.translate("LogecC3", u"Passwords", None))
        self.tabWidget_14.setTabText(self.tabWidget_14.indexOf(self.tab_44), QCoreApplication.translate("LogecC3", u"Wordlists", None))
        self.tabWidget_14.setTabText(self.tabWidget_14.indexOf(self.tab_45), QCoreApplication.translate("LogecC3", u"FileBrowser", None))
        self.tabWidget_6.setTabText(self.tabWidget_6.indexOf(self.webdir_bf), QCoreApplication.translate("LogecC3", u"Credentials", None))
        self.bruteforce_fuzz_url.setHtml(QCoreApplication.translate("LogecC3", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Cantarell'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">http://127.0.0.1/FUZZ</p></body></html>", None))
        self.label_161.setText(QCoreApplication.translate("LogecC3", u"Wordlist Dir", None))
        self.bruteforce_fuzz_wordlistdir.setText(QCoreApplication.translate("LogecC3", u"Modules/General/Bruteforce/Wordlists/SecList-top1-short-usernames", None))
        self.bruteforce_fuzz_wordlist_browse.setText(QCoreApplication.translate("LogecC3", u"Browse", None))
        self.bruteforce_fuzz_start.setText(QCoreApplication.translate("LogecC3", u"-->> Start Bruteforce <<--", None))
        self.label_170.setText(QCoreApplication.translate("LogecC3", u"Target URL", None))
        self.bruteforce_fuzz_stop.setText(QCoreApplication.translate("LogecC3", u"-->> Stop Bruteforce <<--", None))
        self.label_160.setText(QCoreApplication.translate("LogecC3", u"Progress", None))
        self.label_168.setText(QCoreApplication.translate("LogecC3", u"Delay (Up to X seconds)", None))
        self.label_163.setText(QCoreApplication.translate("LogecC3", u"Current Attempts:", None))
        self.bruteforce_fuzz_showfullurl_option.setText(QCoreApplication.translate("LogecC3", u"Show Full URL", None))
        self.label_171.setText(QCoreApplication.translate("LogecC3", u"Port (Optional)", None))
        self.checkBox_43.setText(QCoreApplication.translate("LogecC3", u"Options", None))
        self.label_159.setText(QCoreApplication.translate("LogecC3", u"Threads", None))
        self.bruteforce_fuzz_gooddir_gui.setHtml(QCoreApplication.translate("LogecC3", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Cantarell'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.bruteforce_fuzz_panel.setTabText(self.bruteforce_fuzz_panel.indexOf(self.tab_130), QCoreApplication.translate("LogecC3", u"Successful (0)", None))
        self.bruteforce_fuzz_currentbatch.setHtml(QCoreApplication.translate("LogecC3", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Cantarell'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">('1', '78')</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">('1', '79')</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">('1', '81')</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">('1', '82')</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">('1"
                        "', '83')</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">('1', '84')</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">('1', '85')</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">('1', '86')</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">('1', '87')</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">('1', '88')</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.bruteforce_fuzz_panel.setTabText(self.bruteforce_fuzz_panel.indexOf(self.tab_131), QCoreApplication.translate("LogecC3", u"Current Batch (0/0)", None))
        self.bruteforce_fuzz_errlog.setHtml(QCoreApplication.translate("LogecC3", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Cantarell'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.bruteforce_fuzz_panel.setTabText(self.bruteforce_fuzz_panel.indexOf(self.tab_132), QCoreApplication.translate("LogecC3", u"Log (0)", None))
        self.label_169.setText(QCoreApplication.translate("LogecC3", u"Batch Size ", None))
        self.DB_Query_scanning_bruteforce_4.setText("")
        self.DB_Query_scanning_bruteforce_4.setPlaceholderText(QCoreApplication.translate("LogecC3", u"Enter SQL Query! Type !_help for help! ", None))
#if QT_CONFIG(tooltip)
        self.scanning_bruteforce_refresh_4.setToolTip(QCoreApplication.translate("LogecC3", u"Refresh the Database, updating values from the SQLITE DB file", None))
#endif // QT_CONFIG(tooltip)
        self.scanning_bruteforce_refresh_4.setText(QCoreApplication.translate("LogecC3", u"-->> Refresh DB <<--", None))
#if QT_CONFIG(tooltip)
        self.scanning_bruteforce_query_4.setToolTip(QCoreApplication.translate("LogecC3", u"Run a query on the DB", None))
#endif // QT_CONFIG(tooltip)
        self.scanning_bruteforce_query_4.setText(QCoreApplication.translate("LogecC3", u"-->> Query DB <<--", None))
        self.tabWidget_29.setTabText(self.tabWidget_29.indexOf(self.tab_127), QCoreApplication.translate("LogecC3", u"LocalDB", None))
        self.label_167.setText(QCoreApplication.translate("LogecC3", u"Usernames", None))
        self.label_166.setText(QCoreApplication.translate("LogecC3", u"Passwords", None))
        self.lineEdit_56.setText(QCoreApplication.translate("LogecC3", u"SecList 10mil Usernames", None))
        self.bruteforce_download_seclist_top10mil_usernames_4.setText(QCoreApplication.translate("LogecC3", u"Download", None))
        self.lineEdit_55.setText(QCoreApplication.translate("LogecC3", u"SecList Default Passwords", None))
        self.bruteforce_download_seclist_defaults_4.setText(QCoreApplication.translate("LogecC3", u"Download", None))
        self.lineEdit_58.setText(QCoreApplication.translate("LogecC3", u"SecList Top Usernames (Short List)", None))
        self.bruteforce_download_seclist_topshort_4.setText(QCoreApplication.translate("LogecC3", u"Download", None))
        self.lineEdit_57.setText(QCoreApplication.translate("LogecC3", u"SecList Top 10 Million Passwords", None))
        self.bruteforce_download_seclist_top10mil_4.setText(QCoreApplication.translate("LogecC3", u"Download", None))
        self.lineEdit_54.setText(QCoreApplication.translate("LogecC3", u"Ignis 1m Public Passwords", None))
        self.bruteforce_download_ignis_1M_4.setText(QCoreApplication.translate("LogecC3", u"Download", None))
        self.tabWidget_29.setTabText(self.tabWidget_29.indexOf(self.tab_128), QCoreApplication.translate("LogecC3", u"Wordlists", None))
        self.label_49.setText(QCoreApplication.translate("LogecC3", u"Success Code", None))
        self.label_72.setText(QCoreApplication.translate("LogecC3", u"Characters to ignore (Not implemented)", None))
        self.bruteforce_fuzz_validresponsecode.setHtml(QCoreApplication.translate("LogecC3", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Cantarell'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">200, 500</p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.bruteforce_fuzz_validresponsecode_2.setToolTip(QCoreApplication.translate("LogecC3", u"Handy for characters with anything allowed after them, such as '#' or '?'", None))
#endif // QT_CONFIG(tooltip)
        self.bruteforce_fuzz_validresponsecode_2.setHtml(QCoreApplication.translate("LogecC3", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Cantarell'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"># , ?</p></body></html>", None))
        self.bruteforce_fuzz_validresponsecode_2.setPlaceholderText("")
        self.tabWidget_29.setTabText(self.tabWidget_29.indexOf(self.tab_129), QCoreApplication.translate("LogecC3", u"Quick Tweaks", None))
        self.label_75.setText(QCoreApplication.translate("LogecC3", u"Custom Headers", None))
        self.label_76.setText("")
        self.radioButton_4.setText(QCoreApplication.translate("LogecC3", u"User Agents wordlist", None))
        self.radioButton_5.setText(QCoreApplication.translate("LogecC3", u"Random User Agent", None))
        self.radioButton_6.setText(QCoreApplication.translate("LogecC3", u"Fixed User Agent", None))
        self.lineEdit_26.setText(QCoreApplication.translate("LogecC3", u"l33tHecker", None))
        self.bruteforce_download_seclist_top10mil_usernames_5.setText(QCoreApplication.translate("LogecC3", u"Browse", None))
        self.checkBox_22.setText(QCoreApplication.translate("LogecC3", u"x-content-length:", None))
        self.lineEdit_27.setText(QCoreApplication.translate("LogecC3", u"0", None))
        self.label_77.setText(QCoreApplication.translate("LogecC3", u"> Get Fucked WAF < ", None))
        self.tabWidget_29.setTabText(self.tabWidget_29.indexOf(self.tab_60), QCoreApplication.translate("LogecC3", u"Evasion", None))
        self.tabWidget_6.setTabText(self.tabWidget_6.indexOf(self.tab_43), QCoreApplication.translate("LogecC3", u"WebFuzzer", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_41), QCoreApplication.translate("LogecC3", u"BruteForce", None))
        self.DB_Query_main.setText("")
        self.DB_Query_main.setPlaceholderText(QCoreApplication.translate("LogecC3", u"Enter SQL Query! Type !_help for help! ", None))
#if QT_CONFIG(tooltip)
        self.table_RefreshDB_Button_main.setToolTip(QCoreApplication.translate("LogecC3", u"Refresh the Database, updating values from the SQLITE DB file", None))
#endif // QT_CONFIG(tooltip)
        self.table_RefreshDB_Button_main.setText(QCoreApplication.translate("LogecC3", u"-->> Refresh DB <<--", None))
#if QT_CONFIG(tooltip)
        self.table_QueryDB_Button_main.setToolTip(QCoreApplication.translate("LogecC3", u"Run a query on the DB", None))
#endif // QT_CONFIG(tooltip)
        self.table_QueryDB_Button_main.setText(QCoreApplication.translate("LogecC3", u"-->> Query DB <<--", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), QCoreApplication.translate("LogecC3", u"LocalDB", None))
        self.label_2.setText(QCoreApplication.translate("LogecC3", u"Client Port", None))
        self.radioButton.setText(QCoreApplication.translate("LogecC3", u"RadioButton", None))
        self.lineEdit.setText(QCoreApplication.translate("LogecC3", u"5064", None))
        self.radioButton_2.setText(QCoreApplication.translate("LogecC3", u"RadioButton", None))
        self.label_3.setText(QCoreApplication.translate("LogecC3", u"Client IP", None))
        self.radioButton_3.setText(QCoreApplication.translate("LogecC3", u"RadioButton", None))
        self.lineEdit_2.setText(QCoreApplication.translate("LogecC3", u"206.16.8.14", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_7), QCoreApplication.translate("LogecC3", u"C2 Settings", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_9), QCoreApplication.translate("LogecC3", u"Scanning Settings", None))
        self.label_4.setText(QCoreApplication.translate("LogecC3", u"API Key", None))
        self.lineEdit_4.setText("")
        self.lineEdit_4.setPlaceholderText(QCoreApplication.translate("LogecC3", u"/home/user/Documents/RedditMedia", None))
        self.label_5.setText(QCoreApplication.translate("LogecC3", u"Media Download (Absolute) Path", None))
        self.tabWidget_4.setTabText(self.tabWidget_4.indexOf(self.tab_10), QCoreApplication.translate("LogecC3", u"Reddit", None))
        self.tabWidget_4.setTabText(self.tabWidget_4.indexOf(self.tab_11), QCoreApplication.translate("LogecC3", u"Tab 2", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_8), QCoreApplication.translate("LogecC3", u"OsintSettings", None))
        self.label_32.setText(QCoreApplication.translate("LogecC3", u"Theme", None))
        self.pushButton.setText(QCoreApplication.translate("LogecC3", u"Apply", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_17), QCoreApplication.translate("LogecC3", u"Appearance", None))
        self.settings_edit.setHtml(QCoreApplication.translate("LogecC3", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Cantarell'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.settings_reload.setText(QCoreApplication.translate("LogecC3", u"-->> Reload <<--", None))
        self.settings_write.setText(QCoreApplication.translate("LogecC3", u"-->> Write <<--", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_37), QCoreApplication.translate("LogecC3", u"Settings", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), QCoreApplication.translate("LogecC3", u"Settings", None))
        self.table_RefreshDB_Button_performance2.setText(QCoreApplication.translate("LogecC3", u"-->> Refresh DB <<--", None))
        self.label_44.setText(QCoreApplication.translate("LogecC3", u"System CPU Usage:", None))
        self.label_39.setText(QCoreApplication.translate("LogecC3", u"CPU/RAM Specs", None))
        self.label_40.setText(QCoreApplication.translate("LogecC3", u"SpeedTest", None))
        self.label_18.setText(QCoreApplication.translate("LogecC3", u"Network Specs", None))
        self.label_78.setText(QCoreApplication.translate("LogecC3", u"Benchmark (Count to 10 million)", None))
        self.performance_seconds.setText(QCoreApplication.translate("LogecC3", u"6.16", None))
        self.label_79.setText(QCoreApplication.translate("LogecC3", u"Seconds", None))
        self.label_41.setText(QCoreApplication.translate("LogecC3", u"System Ram Usage: ", None))
        self.label_43.setText(QCoreApplication.translate("LogecC3", u"Local IP:", None))
        self.label_48.setText(QCoreApplication.translate("LogecC3", u"Process ID (PID)", None))
        self.label_46.setText(QCoreApplication.translate("LogecC3", u"Upload (MBPS)", None))
        self.label_20.setText(QCoreApplication.translate("LogecC3", u"Error Log", None))
        self.label_33.setText(QCoreApplication.translate("LogecC3", u"External IP: ", None))
        self.performance_benchmark_button.setText(QCoreApplication.translate("LogecC3", u"Start Benchmark", None))
        self.performance_speedtest.setText(QCoreApplication.translate("LogecC3", u"Run SpeedTest", None))
        self.label_47.setText(QCoreApplication.translate("LogecC3", u"Program CPU Usage:", None))
        self.label_42.setText(QCoreApplication.translate("LogecC3", u"Download (MBPS)", None))
        self.lineEdit_11.setText(QCoreApplication.translate("LogecC3", u"1234", None))
        self.label_45.setText(QCoreApplication.translate("LogecC3", u"Program Ram Usage:", None))
        self.label_19.setText(QCoreApplication.translate("LogecC3", u"Ping (MS)", None))
        self.tabWidget_10.setTabText(self.tabWidget_10.indexOf(self.tab_33), QCoreApplication.translate("LogecC3", u"Performance/Health", None))
        self.label_14.setText(QCoreApplication.translate("LogecC3", u"System CPU Usage", None))
        self.label_84.setText(QCoreApplication.translate("LogecC3", u"Ping (MS)", None))
        self.label_85.setText(QCoreApplication.translate("LogecC3", u"SpeedTest", None))
        self.performance_seconds_5.setText(QCoreApplication.translate("LogecC3", u"6.16", None))
        self.label_121.setText(QCoreApplication.translate("LogecC3", u"Seconds", None))
        self.textEdit_29.setHtml(QCoreApplication.translate("LogecC3", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Cantarell'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Process List?</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.label_91.setText(QCoreApplication.translate("LogecC3", u"Benchmarks", None))
        self.checkBox_23.setText(QCoreApplication.translate("LogecC3", u"Count to 10 Million", None))
        self.label_83.setText(QCoreApplication.translate("LogecC3", u"External IP:  123.456.111.333", None))
        self.label_82.setText(QCoreApplication.translate("LogecC3", u"Local IP: 123.456.444.222", None))
        self.performance_seconds_2.setText(QCoreApplication.translate("LogecC3", u"6.16", None))
        self.checkBox_24.setText(QCoreApplication.translate("LogecC3", u"Some Fancy Benchmark or math", None))
        self.textEdit_23.setHtml(QCoreApplication.translate("LogecC3", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Cantarell'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Something else?</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.label_90.setText(QCoreApplication.translate("LogecC3", u"Seconds", None))
        self.label_86.setText(QCoreApplication.translate("LogecC3", u"Network Specs", None))
        self.label_88.setText(QCoreApplication.translate("LogecC3", u"Upload (MBPS)", None))
        self.label_87.setText(QCoreApplication.translate("LogecC3", u"Download (MBPS)", None))
        self.performance_speedtest_2.setText(QCoreApplication.translate("LogecC3", u"Run SpeedTest", None))
        self.performance_benchmark_button_2.setText(QCoreApplication.translate("LogecC3", u"Start Benchmark", None))
        self.tabWidget_16.setTabText(self.tabWidget_16.indexOf(self.tab_75), QCoreApplication.translate("LogecC3", u"Benchmarks And Processes", None))
        self.table_RefreshDB_Button_performance.setText(QCoreApplication.translate("LogecC3", u"-->> Refresh DB <<--", None))
        self.tabWidget_16.setTabText(self.tabWidget_16.indexOf(self.tab_76), QCoreApplication.translate("LogecC3", u"Error List", None))
        self.lineEdit_10.setText(QCoreApplication.translate("LogecC3", u"1", None))
        self.label_89.setText(QCoreApplication.translate("LogecC3", u"Graph Refresh (Seconds)", None))
        self.label_122.setText(QCoreApplication.translate("LogecC3", u"Graph Color ", None))
        self.comboBox_7.setItemText(0, QCoreApplication.translate("LogecC3", u"Red", None))
        self.comboBox_7.setItemText(1, QCoreApplication.translate("LogecC3", u"Green", None))
        self.comboBox_7.setItemText(2, QCoreApplication.translate("LogecC3", u"Blue", None))
        self.comboBox_7.setItemText(3, QCoreApplication.translate("LogecC3", u"Yellow", None))
        self.comboBox_7.setItemText(4, QCoreApplication.translate("LogecC3", u"White", None))

        self.tabWidget_16.setTabText(self.tabWidget_16.indexOf(self.tab_77), QCoreApplication.translate("LogecC3", u"Page", None))
        self.label_80.setText(QCoreApplication.translate("LogecC3", u"System Ram Usage", None))
        self.label_81.setText(QCoreApplication.translate("LogecC3", u"Program Ram Usage", None))
        self.tabWidget_10.setTabText(self.tabWidget_10.indexOf(self.tab_52), QCoreApplication.translate("LogecC3", u"Performance2", None))
        self.tabWidget_11.setTabText(self.tabWidget_11.indexOf(self.tab_29), QCoreApplication.translate("LogecC3", u"Tab 1", None))
        self.textEdit_5.setHtml(QCoreApplication.translate("LogecC3", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Cantarell'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">&quot;Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.&quot;</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right"
                        ":0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">&quot;At vero eos et accusamus et iusto odio dignissimos ducimus qui blanditiis praesentium voluptatum deleniti atque corrupti quos dolores et quas molestias excepturi sint occaecati cupiditate non provident, similique sunt in culpa qui officia deserunt mollitia animi, id est laborum et dolorum fuga. Et harum quidem rerum facilis est et expedita distinctio. Nam libero tempore, cum soluta nobis est eligendi optio cumque nihil impedit quo minus id quod maxime placeat facere possimus, omnis voluptas assumenda est, omnis dolor repellendus. Temporibus autem quibusdam et aut officiis debitis aut rerum necessitatibus saepe eveniet ut et voluptates repudiandae sint et molestiae non recusandae. Itaque earum rerum hic tenetur a sapiente delectus, ut aut reiciendis voluptatibus maiores alias consequatur aut perferendis doloribus asperiores rep"
                        "ellat.&quot;</p></body></html>", None))
        self.tabWidget_12.setTabText(self.tabWidget_12.indexOf(self.tab_34), QCoreApplication.translate("LogecC3", u"Reddit", None))
        self.tabWidget_12.setTabText(self.tabWidget_12.indexOf(self.tab_35), QCoreApplication.translate("LogecC3", u"Tab 2", None))
        self.tabWidget_11.setTabText(self.tabWidget_11.indexOf(self.tab_30), QCoreApplication.translate("LogecC3", u"OSINT", None))
        self.textEdit_21.setHtml(QCoreApplication.translate("LogecC3", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Cantarell'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Bruteforce:</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Services:</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">FTP: Seems to work well at a random delay of 1 second, any shorter and you get 'too many connections from this IP address'</p>"
                        "\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">SSH: You're gonna have to take this one really slow, SSH hates repeated attempts to log in, and will start spitting errors if you go to fast</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">How it works:</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:"
                        "0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Connections:</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">	There are various libs used for the connections:</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">		SSH: Paramiko</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">		FTP: ftplib</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Bruteforcing:</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">	To save memory &amp; disk space, the requests are issued in batches. For example, if you have a wordlist with 100 "
                        "lines, and a batch size of 10, it will use the first 10 lines to brute force, then when completed the next ten,  etc. This greatly cuts down on memory for parallel tasks, as it (Thread Pool Executor) releases the memory once each batch is done.</p></body></html>", None))
        self.tabWidget_15.setTabText(self.tabWidget_15.indexOf(self.tab_49), QCoreApplication.translate("LogecC3", u"Bruteforce", None))
        self.textEdit_22.setHtml(QCoreApplication.translate("LogecC3", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Cantarell'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" text-decoration: underline;\">Database: </span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">This database works differently than the rest (Save for the reddit DB). The others store all current, and past data gathered by the tool, but for the fuzzer, it only stores your most recent fuzz (One entry per atte"
                        "mpt). The rationale is that you may be fuzzing hundreds, if not thousands of URL's, and a per-attempt entry makes it easier to sort through with SQL queries. </p></body></html>", None))
        self.tabWidget_15.setTabText(self.tabWidget_15.indexOf(self.tab_50), QCoreApplication.translate("LogecC3", u"Fuzzer", None))
        self.tabWidget_11.setTabText(self.tabWidget_11.indexOf(self.tab_48), QCoreApplication.translate("LogecC3", u"Bruteforce", None))
        self.tabWidget_10.setTabText(self.tabWidget_10.indexOf(self.tab_28), QCoreApplication.translate("LogecC3", u"Guide", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_27), QCoreApplication.translate("LogecC3", u"Other", None))
        self.textEdit_3.setHtml(QCoreApplication.translate("LogecC3", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Cantarell'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">An easy connect to at least openvpn, have a config file location input, location of openvpn executable, and have it open in its own thread</p></body></html>", None))
        self.tabWidget_7.setTabText(self.tabWidget_7.indexOf(self.tab_21), QCoreApplication.translate("LogecC3", u"VPN", None))
        self.label_12.setText(QCoreApplication.translate("LogecC3", u"HTML files", None))
        self.textEdit_4.setHtml(QCoreApplication.translate("LogecC3", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Cantarell'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">A quick way to spin up a simple flask webserver, have options for port, IP to put it on, html files (and a default fake page), and make it on its own thread</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">also do popup to take files from fielsystem if possible</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; mar"
                        "gin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">can have preview of site in this tab too</p></body></html>", None))
        self.tabWidget_7.setTabText(self.tabWidget_7.indexOf(self.tab_19), QCoreApplication.translate("LogecC3", u"FlaskWebSErver", None))
        self.label_25.setText(QCoreApplication.translate("LogecC3", u"Current Risk Level", None))
        self.label_34.setText(QCoreApplication.translate("LogecC3", u"# of Events that most likely had/were:", None))
        self.label_35.setText(QCoreApplication.translate("LogecC3", u"SIEM Alert: 3", None))
        self.label_36.setText(QCoreApplication.translate("LogecC3", u"Logged: 41", None))
        self.label_37.setText(QCoreApplication.translate("LogecC3", u"No Detection: 2", None))
        self.textEdit.setHtml(QCoreApplication.translate("LogecC3", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Cantarell'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">THe idea here is to assign a risk level to each function, and feed it to this plugin. if something (such as running mimikatz) is most likely alerted/high risk, it gets a +1 to the alerted feild in the list, same as down the stack</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Overall, from those scores, a &quot;Risk somewo"
                        "rd&quot; is created on how risky your operations are, aka how likely you are to get caught. Higher is worse/more likely.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">long term it would be great if the C2 could give feedback on if an alert happened or not but that's a pipe dream<br /><br /><br />for the progress bar, each level =  total levels/100, and each level has a diff color (green to start, red to finish) s lets say there are 4 levels, 75% would be level 3 % a deep orange/redish if possible</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.tabWidget_7.setTabText(self.tabWidget_7.indexOf(self.tab_32), QCoreApplication.translate("LogecC3", u"Risk Report", None))
        self.label_59.setText(QCoreApplication.translate("LogecC3", u"Dev Tracker for current modules", None))
        self.label_56.setText(QCoreApplication.translate("LogecC3", u"Portscan", None))
        self.checkBox_18.setText(QCoreApplication.translate("LogecC3", u"Fully Built out", None))
        self.checkBox_13.setText(QCoreApplication.translate("LogecC3", u"Fully Built out", None))
        self.checkBox_7.setText(QCoreApplication.translate("LogecC3", u"Optimized/cleaned up", None))
        self.checkBox_8.setText(QCoreApplication.translate("LogecC3", u"File in correct spot", None))
        self.checkBox_15.setText(QCoreApplication.translate("LogecC3", u"Error Handling", None))
        self.checkBox_16.setText(QCoreApplication.translate("LogecC3", u"Working", None))
        self.label_57.setText(QCoreApplication.translate("LogecC3", u"Reddit OSINT", None))
        self.checkBox_5.setText(QCoreApplication.translate("LogecC3", u"Fully Built out", None))
        self.label_58.setText(QCoreApplication.translate("LogecC3", u"Bruteforce", None))
        self.checkBox_9.setText(QCoreApplication.translate("LogecC3", u"Optimized/cleaned up", None))
        self.checkBox_3.setText(QCoreApplication.translate("LogecC3", u"Working", None))
        self.checkBox_10.setText(QCoreApplication.translate("LogecC3", u"Error Handling", None))
        self.checkBox_17.setText(QCoreApplication.translate("LogecC3", u"File in correct spot", None))
        self.checkBox_11.setText(QCoreApplication.translate("LogecC3", u"Working", None))
        self.checkBox_12.setText(QCoreApplication.translate("LogecC3", u"File in correct spot", None))
        self.checkBox.setText(QCoreApplication.translate("LogecC3", u"Error Handling", None))
        self.checkBox_14.setText(QCoreApplication.translate("LogecC3", u"Optimized/cleaned up", None))
        self.textEdit_2.setHtml(QCoreApplication.translate("LogecC3", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Cantarell'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Mostly done, need to catch any other possibel errors</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Gonna be a bigger task than expected, as I need to use Qthreads and or signals to get a connector accross saying an error ocured</p></body></html>", None))
        self.textEdit_6.setHtml(QCoreApplication.translate("LogecC3", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Cantarell'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.textEdit_7.setHtml(QCoreApplication.translate("LogecC3", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Cantarell'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.textEdit_8.setHtml(QCoreApplication.translate("LogecC3", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Cantarell'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Optimized with executor, and failry cleaned up</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Need to do one more pass with cleaning commetns etc</p></body></html>", None))
        self.textEdit_9.setHtml(QCoreApplication.translate("LogecC3", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Cantarell'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.textEdit_10.setHtml(QCoreApplication.translate("LogecC3", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Cantarell'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.textEdit_11.setHtml(QCoreApplication.translate("LogecC3", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Cantarell'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Works, need to get subreddit function properly up and going though</p></body></html>", None))
        self.textEdit_12.setHtml(QCoreApplication.translate("LogecC3", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Cantarell'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.textEdit_13.setHtml(QCoreApplication.translate("LogecC3", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Cantarell'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.textEdit_14.setHtml(QCoreApplication.translate("LogecC3", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Cantarell'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.textEdit_15.setHtml(QCoreApplication.translate("LogecC3", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Cantarell'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.textEdit_16.setHtml(QCoreApplication.translate("LogecC3", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Cantarell'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Current Error: DB not in same thread :(</p></body></html>", None))
        self.textEdit_17.setHtml(QCoreApplication.translate("LogecC3", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Cantarell'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.textEdit_18.setHtml(QCoreApplication.translate("LogecC3", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Cantarell'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.textEdit_19.setHtml(QCoreApplication.translate("LogecC3", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Cantarell'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.textEdit_20.setHtml(QCoreApplication.translate("LogecC3", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Cantarell'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Integrate some C, (do the scanning with C) nmap is kicking my ass interms of speed</p></body></html>", None))
        self.tabWidget_7.setTabText(self.tabWidget_7.indexOf(self.tab_36), QCoreApplication.translate("LogecC3", u"Dev Track", None))
        self.tabWidget_7.setTabText(self.tabWidget_7.indexOf(self.tab_15), QCoreApplication.translate("LogecC3", u"SQL Injection?", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_20), QCoreApplication.translate("LogecC3", u"Ideas/POC", None))
        self.menuFile.setTitle(QCoreApplication.translate("LogecC3", u"File", None))
        self.menuTarget.setTitle(QCoreApplication.translate("LogecC3", u"Client", None))
        self.menu_Target_SpawnShell.setTitle(QCoreApplication.translate("LogecC3", u"Spawn Shell", None))
        self.menu_Target_PythonShells.setTitle(QCoreApplication.translate("LogecC3", u"Python Shells", None))
        self.action_Target_Perl_binbash.setTitle(QCoreApplication.translate("LogecC3", u"Perl Shells", None))
        self.menuRuby_Shells.setTitle(QCoreApplication.translate("LogecC3", u"Ruby Shells", None))
        self.menu_Target_Destruction.setTitle(QCoreApplication.translate("LogecC3", u"Destruction", None))
        self.menu_Target_Encryption.setTitle(QCoreApplication.translate("LogecC3", u"Encryption", None))
        self.menu_Target_Info.setTitle(QCoreApplication.translate("LogecC3", u"Target Info", None))
        self.menu_GettingStarted.setTitle(QCoreApplication.translate("LogecC3", u"Getting Started", None))
        self.menuExternal_Target.setTitle(QCoreApplication.translate("LogecC3", u"External Target", None))
        self.menuExploits.setTitle(QCoreApplication.translate("LogecC3", u"Exploits", None))
        self.menuWindows.setTitle(QCoreApplication.translate("LogecC3", u"Windows", None))
        self.menuSMB.setTitle(QCoreApplication.translate("LogecC3", u"SMB", None))
        self.menuEnumeration.setTitle(QCoreApplication.translate("LogecC3", u"Enumeration", None))
        self.menuData.setTitle(QCoreApplication.translate("LogecC3", u"Data", None))
        self.menuSQL_Shortcuts.setTitle(QCoreApplication.translate("LogecC3", u"SQL Shortcuts", None))
    # retranslateUi

