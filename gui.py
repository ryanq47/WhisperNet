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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFrame,
    QGraphicsView, QGridLayout, QGroupBox, QHBoxLayout,
    QHeaderView, QLCDNumber, QLabel, QLayout,
    QLineEdit, QMainWindow, QMenu, QMenuBar,
    QPushButton, QSizePolicy, QSpacerItem, QSpinBox,
    QTabWidget, QTableWidget, QTableWidgetItem, QTextEdit,
    QToolBox, QWidget)

class Ui_LogecC3(object):
    def setupUi(self, LogecC3):
        if not LogecC3.objectName():
            LogecC3.setObjectName(u"LogecC3")
        LogecC3.setWindowModality(Qt.NonModal)
        LogecC3.setEnabled(True)
        LogecC3.resize(1579, 888)
        LogecC3.setMinimumSize(QSize(850, 688))
        LogecC3.setMaximumSize(QSize(10000, 10000))
        font = QFont()
        font.setUnderline(False)
        LogecC3.setFont(font)
        LogecC3.setAcceptDrops(False)
        icon = QIcon()
        icon.addFile(u"../../Documents/Screenshot_2023-04-30_01-44-21.png", QSize(), QIcon.Normal, QIcon.Off)
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
        self.actionRELOAD = QAction(LogecC3)
        self.actionRELOAD.setObjectName(u"actionRELOAD")
        self.actionSave_Project = QAction(LogecC3)
        self.actionSave_Project.setObjectName(u"actionSave_Project")
        self.actionSaveAs_Project = QAction(LogecC3)
        self.actionSaveAs_Project.setObjectName(u"actionSaveAs_Project")
        self.actionOpen_Project = QAction(LogecC3)
        self.actionOpen_Project.setObjectName(u"actionOpen_Project")
        self.actionExit = QAction(LogecC3)
        self.actionExit.setObjectName(u"actionExit")
        self.centralwidget = QWidget(LogecC3)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_4 = QGridLayout(self.centralwidget)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.main_tab_widget = QTabWidget(self.centralwidget)
        self.main_tab_widget.setObjectName(u"main_tab_widget")
        self.main_tab_widget.setEnabled(True)
        self.main_tab_widget.setLayoutDirection(Qt.LeftToRight)
        self.main_tab_widget.setAutoFillBackground(False)
        self.main_tab_widget.setStyleSheet(u"")
        self.main_tab_widget.setTabPosition(QTabWidget.North)
        self.main_tab_widget.setTabShape(QTabWidget.Rounded)
        self.main_tab_widget.setTabsClosable(False)
        self.main_tab_widget.setMovable(True)
        self.main_tab_widget.setTabBarAutoHide(False)
        self.c2_tab = QWidget()
        self.c2_tab.setObjectName(u"c2_tab")
        self.gridLayout_40 = QGridLayout(self.c2_tab)
        self.gridLayout_40.setObjectName(u"gridLayout_40")
        self.c2_gui_hide_clients = QCheckBox(self.c2_tab)
        self.c2_gui_hide_clients.setObjectName(u"c2_gui_hide_clients")

        self.gridLayout_40.addWidget(self.c2_gui_hide_clients, 0, 0, 1, 1)

        self.c2_gui_hide_shells = QCheckBox(self.c2_tab)
        self.c2_gui_hide_shells.setObjectName(u"c2_gui_hide_shells")

        self.gridLayout_40.addWidget(self.c2_gui_hide_shells, 0, 1, 1, 1)

        self.c2_gui_hide_options = QCheckBox(self.c2_tab)
        self.c2_gui_hide_options.setObjectName(u"c2_gui_hide_options")

        self.gridLayout_40.addWidget(self.c2_gui_hide_options, 0, 2, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.c2_gui_groupbox_clients = QGroupBox(self.c2_tab)
        self.c2_gui_groupbox_clients.setObjectName(u"c2_gui_groupbox_clients")
        self.c2_gui_groupbox_clients.setStyleSheet(u"border:0")
        self.c2_gui_groupbox_clients.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)
        self.gridLayout_12 = QGridLayout(self.c2_gui_groupbox_clients)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.gridLayout_12.setSizeConstraint(QLayout.SetNoConstraint)
        self.c2_gui_groupbox_client_table = QTableWidget(self.c2_gui_groupbox_clients)
        self.c2_gui_groupbox_client_table.setObjectName(u"c2_gui_groupbox_client_table")

        self.gridLayout_12.addWidget(self.c2_gui_groupbox_client_table, 0, 0, 1, 1)


        self.horizontalLayout.addWidget(self.c2_gui_groupbox_clients)

        self.c2_gui_groupbox_options = QGroupBox(self.c2_tab)
        self.c2_gui_groupbox_options.setObjectName(u"c2_gui_groupbox_options")
        self.c2_gui_groupbox_options.setStyleSheet(u"border:0")
        self.gridLayout_29 = QGridLayout(self.c2_gui_groupbox_options)
        self.gridLayout_29.setObjectName(u"gridLayout_29")
        self.bruteforce_panel_2 = QTabWidget(self.c2_gui_groupbox_options)
        self.bruteforce_panel_2.setObjectName(u"bruteforce_panel_2")
        self.bruteforce_panel_2.setStyleSheet(u"border:0")
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
        self.tab_33 = QWidget()
        self.tab_33.setObjectName(u"tab_33")
        self.gridLayout_24 = QGridLayout(self.tab_33)
        self.gridLayout_24.setObjectName(u"gridLayout_24")
        self.c2_server_username = QLineEdit(self.tab_33)
        self.c2_server_username.setObjectName(u"c2_server_username")

        self.gridLayout_24.addWidget(self.c2_server_username, 1, 0, 1, 2)

        self.c2_disconnect_button = QPushButton(self.tab_33)
        self.c2_disconnect_button.setObjectName(u"c2_disconnect_button")

        self.gridLayout_24.addWidget(self.c2_disconnect_button, 3, 0, 1, 1)

        self.c2_server_port = QLineEdit(self.tab_33)
        self.c2_server_port.setObjectName(u"c2_server_port")

        self.gridLayout_24.addWidget(self.c2_server_port, 0, 1, 1, 1)

        self.c2_server_ip = QLineEdit(self.tab_33)
        self.c2_server_ip.setObjectName(u"c2_server_ip")

        self.gridLayout_24.addWidget(self.c2_server_ip, 0, 0, 1, 1)

        self.c2_status_label = QLabel(self.tab_33)
        self.c2_status_label.setObjectName(u"c2_status_label")

        self.gridLayout_24.addWidget(self.c2_status_label, 4, 0, 1, 2)

        self.c2_server_password = QLineEdit(self.tab_33)
        self.c2_server_password.setObjectName(u"c2_server_password")

        self.gridLayout_24.addWidget(self.c2_server_password, 2, 0, 1, 2)

        self.c2_connect_button = QPushButton(self.tab_33)
        self.c2_connect_button.setObjectName(u"c2_connect_button")

        self.gridLayout_24.addWidget(self.c2_connect_button, 3, 1, 1, 1)

        self.bruteforce_panel_2.addTab(self.tab_33, "")
        self.tab_53 = QWidget()
        self.tab_53.setObjectName(u"tab_53")
        self.gridLayout_51 = QGridLayout(self.tab_53)
        self.gridLayout_51.setObjectName(u"gridLayout_51")
        self.c2_start_server_local = QPushButton(self.tab_53)
        self.c2_start_server_local.setObjectName(u"c2_start_server_local")

        self.gridLayout_51.addWidget(self.c2_start_server_local, 2, 1, 1, 1)

        self.c2_server_log_local = QTextEdit(self.tab_53)
        self.c2_server_log_local.setObjectName(u"c2_server_log_local")

        self.gridLayout_51.addWidget(self.c2_server_log_local, 3, 0, 1, 2)

        self.c2_server_password_local = QLineEdit(self.tab_53)
        self.c2_server_password_local.setObjectName(u"c2_server_password_local")
        self.c2_server_password_local.setInputMethodHints(Qt.ImhSensitiveData)

        self.gridLayout_51.addWidget(self.c2_server_password_local, 1, 0, 1, 2)

        self.c2_server_port_local = QLineEdit(self.tab_53)
        self.c2_server_port_local.setObjectName(u"c2_server_port_local")

        self.gridLayout_51.addWidget(self.c2_server_port_local, 0, 1, 1, 1)

        self.c2_stop_server_local = QPushButton(self.tab_53)
        self.c2_stop_server_local.setObjectName(u"c2_stop_server_local")

        self.gridLayout_51.addWidget(self.c2_stop_server_local, 2, 0, 1, 1)

        self.c2_server_ip_local = QLineEdit(self.tab_53)
        self.c2_server_ip_local.setObjectName(u"c2_server_ip_local")

        self.gridLayout_51.addWidget(self.c2_server_ip_local, 0, 0, 1, 1)

        self.bruteforce_panel_2.addTab(self.tab_53, "")

        self.gridLayout_29.addWidget(self.bruteforce_panel_2, 0, 0, 1, 1)


        self.horizontalLayout.addWidget(self.c2_gui_groupbox_options)


        self.gridLayout_40.addLayout(self.horizontalLayout, 1, 0, 1, 3)

        self.c2_gui_groupbox_shells = QGroupBox(self.c2_tab)
        self.c2_gui_groupbox_shells.setObjectName(u"c2_gui_groupbox_shells")
        self.c2_gui_groupbox_shells.setStyleSheet(u"border:0")
        self.gridLayout_30 = QGridLayout(self.c2_gui_groupbox_shells)
        self.gridLayout_30.setObjectName(u"gridLayout_30")
        self.c2_shell_tab = QTabWidget(self.c2_gui_groupbox_shells)
        self.c2_shell_tab.setObjectName(u"c2_shell_tab")
        self.c2_shell_tab.setMinimumSize(QSize(0, 400))
        self.tab_57 = QWidget()
        self.tab_57.setObjectName(u"tab_57")
        self.gridLayout_42 = QGridLayout(self.tab_57)
        self.gridLayout_42.setObjectName(u"gridLayout_42")
        self.c2_servershell = QTextEdit(self.tab_57)
        self.c2_servershell.setObjectName(u"c2_servershell")
        self.c2_servershell.setEnabled(True)
        font1 = QFont()
        font1.setFamilies([u"Monospace"])
        font1.setPointSize(9)
        font1.setUnderline(False)
        self.c2_servershell.setFont(font1)
        self.c2_servershell.setStyleSheet(u"background-color: rgb(29, 29, 29);")
        self.c2_servershell.setReadOnly(False)

        self.gridLayout_42.addWidget(self.c2_servershell, 0, 0, 1, 2)

        self.c2_servershell_send = QPushButton(self.tab_57)
        self.c2_servershell_send.setObjectName(u"c2_servershell_send")
        self.c2_servershell_send.setEnabled(True)

        self.gridLayout_42.addWidget(self.c2_servershell_send, 1, 1, 1, 1)

        self.c2_servershell_input = QLineEdit(self.tab_57)
        self.c2_servershell_input.setObjectName(u"c2_servershell_input")
        font2 = QFont()
        font2.setFamilies([u"DejaVu Sans Mono"])
        font2.setPointSize(9)
        font2.setUnderline(False)
        self.c2_servershell_input.setFont(font2)
        self.c2_servershell_input.setStyleSheet(u"background-color: rgb(29, 29, 29);")

        self.gridLayout_42.addWidget(self.c2_servershell_input, 1, 0, 1, 1)

        self.c2_shell_tab.addTab(self.tab_57, "")
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

        self.c2_shell_tab.addTab(self.tab_58, "")
        self.tab_59 = QWidget()
        self.tab_59.setObjectName(u"tab_59")
        self.gridLayout_50 = QGridLayout(self.tab_59)
        self.gridLayout_50.setObjectName(u"gridLayout_50")
        self.c2_systemshell = QTextEdit(self.tab_59)
        self.c2_systemshell.setObjectName(u"c2_systemshell")
        self.c2_systemshell.setEnabled(True)
        self.c2_systemshell.setFont(font1)
        self.c2_systemshell.setStyleSheet(u"background-color: rgb(29, 29, 29);")
        self.c2_systemshell.setReadOnly(True)

        self.gridLayout_50.addWidget(self.c2_systemshell, 0, 0, 1, 2)

        self.c2_systemshell_input = QLineEdit(self.tab_59)
        self.c2_systemshell_input.setObjectName(u"c2_systemshell_input")
        self.c2_systemshell_input.setFont(font2)
        self.c2_systemshell_input.setStyleSheet(u"background-color: rgb(29, 29, 29);")

        self.gridLayout_50.addWidget(self.c2_systemshell_input, 1, 0, 1, 1)

        self.c2_systemshell_send = QPushButton(self.tab_59)
        self.c2_systemshell_send.setObjectName(u"c2_systemshell_send")
        self.c2_systemshell_send.setEnabled(True)

        self.gridLayout_50.addWidget(self.c2_systemshell_send, 1, 1, 1, 1)

        self.c2_shell_tab.addTab(self.tab_59, "")

        self.gridLayout_30.addWidget(self.c2_shell_tab, 0, 0, 1, 1)


        self.gridLayout_40.addWidget(self.c2_gui_groupbox_shells, 2, 0, 1, 3)

        self.main_tab_widget.addTab(self.c2_tab, "")
        self.tab_22 = QWidget()
        self.tab_22.setObjectName(u"tab_22")
        self.gridLayout_17 = QGridLayout(self.tab_22)
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.tabWidget_8 = QTabWidget(self.tab_22)
        self.tabWidget_8.setObjectName(u"tabWidget_8")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.gridLayout_8 = QGridLayout(self.tab)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.exploitandvuln_search_button = QPushButton(self.tab)
        self.exploitandvuln_search_button.setObjectName(u"exploitandvuln_search_button")
        self.exploitandvuln_search_button.setStyleSheet(u"")

        self.gridLayout_8.addWidget(self.exploitandvuln_search_button, 2, 0, 1, 2)

        self.exploitandvuln_search = QLineEdit(self.tab)
        self.exploitandvuln_search.setObjectName(u"exploitandvuln_search")

        self.gridLayout_8.addWidget(self.exploitandvuln_search, 1, 0, 1, 2)

        self.exploitandvuln_tableview = QTableWidget(self.tab)
        self.exploitandvuln_tableview.setObjectName(u"exploitandvuln_tableview")

        self.gridLayout_8.addWidget(self.exploitandvuln_tableview, 0, 0, 1, 1)

        self.tabWidget_8.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.gridLayout_2 = QGridLayout(self.tab_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.agentbuilder_compilation_log = QTextEdit(self.tab_2)
        self.agentbuilder_compilation_log.setObjectName(u"agentbuilder_compilation_log")

        self.gridLayout_2.addWidget(self.agentbuilder_compilation_log, 0, 1, 1, 1)

        self.agentbuilder_toolbox = QToolBox(self.tab_2)
        self.agentbuilder_toolbox.setObjectName(u"agentbuilder_toolbox")
        self.page_22 = QWidget()
        self.page_22.setObjectName(u"page_22")
        self.page_22.setGeometry(QRect(0, 0, 756, 645))
        self.gridLayout_11 = QGridLayout(self.page_22)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.gridLayout_10 = QGridLayout()
        self.gridLayout_10.setObjectName(u"gridLayout_10")

        self.gridLayout_11.addLayout(self.gridLayout_10, 5, 0, 1, 2)

        self.verticalSpacer_2 = QSpacerItem(20, 286, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_11.addItem(self.verticalSpacer_2, 6, 1, 1, 1)

        self.line_2 = QFrame(self.page_22)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.gridLayout_11.addWidget(self.line_2, 2, 0, 2, 2)

        self.verticalSpacer = QSpacerItem(20, 286, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_11.addItem(self.verticalSpacer, 6, 0, 1, 1)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.lineEdit_2 = QLineEdit(self.page_22)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.gridLayout_3.addWidget(self.lineEdit_2, 4, 0, 1, 1)

        self.label_10 = QLabel(self.page_22)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_3.addWidget(self.label_10, 3, 0, 1, 1)

        self.lineEdit = QLineEdit(self.page_22)
        self.lineEdit.setObjectName(u"lineEdit")

        self.gridLayout_3.addWidget(self.lineEdit, 2, 0, 1, 1)

        self.label_7 = QLabel(self.page_22)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_3.addWidget(self.label_7, 1, 0, 1, 1)

        self.label_13 = QLabel(self.page_22)
        self.label_13.setObjectName(u"label_13")
        font3 = QFont()
        self.label_13.setFont(font3)
        self.label_13.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label_13, 0, 0, 1, 1)


        self.gridLayout_11.addLayout(self.gridLayout_3, 0, 0, 1, 2)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.pushButton_2 = QPushButton(self.page_22)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.horizontalLayout_2.addWidget(self.pushButton_2)

        self.pushButton = QPushButton(self.page_22)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout_2.addWidget(self.pushButton)


        self.gridLayout_11.addLayout(self.horizontalLayout_2, 7, 0, 1, 2)

        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.label_12 = QLabel(self.page_22)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout_5.addWidget(self.label_12, 3, 2, 1, 1)

        self.lineEdit_6 = QLineEdit(self.page_22)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        self.lineEdit_6.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_5.addWidget(self.lineEdit_6, 6, 2, 1, 1)

        self.label = QLabel(self.page_22)
        self.label.setObjectName(u"label")

        self.gridLayout_5.addWidget(self.label, 1, 0, 1, 1)

        self.pushButton_5 = QPushButton(self.page_22)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setMaximumSize(QSize(75, 16777215))

        self.gridLayout_5.addWidget(self.pushButton_5, 6, 1, 1, 1)

        self.label_15 = QLabel(self.page_22)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setFont(font3)
        self.label_15.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.label_15, 0, 0, 1, 3)

        self.lineEdit_3 = QLineEdit(self.page_22)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.gridLayout_5.addWidget(self.lineEdit_3, 2, 0, 1, 1)

        self.lineEdit_4 = QLineEdit(self.page_22)
        self.lineEdit_4.setObjectName(u"lineEdit_4")

        self.gridLayout_5.addWidget(self.lineEdit_4, 6, 0, 1, 1)

        self.label_11 = QLabel(self.page_22)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout_5.addWidget(self.label_11, 3, 0, 1, 1)

        self.label_37 = QLabel(self.page_22)
        self.label_37.setObjectName(u"label_37")

        self.gridLayout_5.addWidget(self.label_37, 1, 2, 1, 1)

        self.spinBox_2 = QSpinBox(self.page_22)
        self.spinBox_2.setObjectName(u"spinBox_2")
        self.spinBox_2.setMinimum(1)
        self.spinBox_2.setMaximum(5000)
        self.spinBox_2.setValue(60)

        self.gridLayout_5.addWidget(self.spinBox_2, 2, 2, 1, 1)


        self.gridLayout_11.addLayout(self.gridLayout_5, 4, 0, 1, 2)

        self.agentbuilder_toolbox.addItem(self.page_22, u"C")
        self.page_13 = QWidget()
        self.page_13.setObjectName(u"page_13")
        self.page_13.setGeometry(QRect(0, 0, 756, 645))
        self.gridLayout_15 = QGridLayout(self.page_13)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.gridLayout_14 = QGridLayout()
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.lineEdit_11 = QLineEdit(self.page_13)
        self.lineEdit_11.setObjectName(u"lineEdit_11")

        self.gridLayout_14.addWidget(self.lineEdit_11, 4, 0, 1, 1)

        self.label_24 = QLabel(self.page_13)
        self.label_24.setObjectName(u"label_24")

        self.gridLayout_14.addWidget(self.label_24, 3, 0, 1, 1)

        self.lineEdit_12 = QLineEdit(self.page_13)
        self.lineEdit_12.setObjectName(u"lineEdit_12")

        self.gridLayout_14.addWidget(self.lineEdit_12, 2, 0, 1, 1)

        self.label_25 = QLabel(self.page_13)
        self.label_25.setObjectName(u"label_25")

        self.gridLayout_14.addWidget(self.label_25, 1, 0, 1, 1)

        self.label_26 = QLabel(self.page_13)
        self.label_26.setObjectName(u"label_26")
        font4 = QFont()
        font4.setUnderline(True)
        self.label_26.setFont(font4)
        self.label_26.setAlignment(Qt.AlignCenter)

        self.gridLayout_14.addWidget(self.label_26, 0, 0, 1, 1)


        self.gridLayout_15.addLayout(self.gridLayout_14, 0, 0, 1, 2)

        self.verticalSpacer_3 = QSpacerItem(20, 294, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_15.addItem(self.verticalSpacer_3, 3, 0, 1, 1)

        self.line_3 = QFrame(self.page_13)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.gridLayout_15.addWidget(self.line_3, 1, 0, 1, 2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.pushButton_6 = QPushButton(self.page_13)
        self.pushButton_6.setObjectName(u"pushButton_6")

        self.horizontalLayout_3.addWidget(self.pushButton_6)

        self.pushButton_7 = QPushButton(self.page_13)
        self.pushButton_7.setObjectName(u"pushButton_7")

        self.horizontalLayout_3.addWidget(self.pushButton_7)


        self.gridLayout_15.addLayout(self.horizontalLayout_3, 4, 0, 1, 2)

        self.verticalSpacer_4 = QSpacerItem(20, 294, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_15.addItem(self.verticalSpacer_4, 3, 1, 1, 1)

        self.gridLayout_13 = QGridLayout()
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.label_16 = QLabel(self.page_13)
        self.label_16.setObjectName(u"label_16")

        self.gridLayout_13.addWidget(self.label_16, 3, 2, 1, 1)

        self.pushButton_8 = QPushButton(self.page_13)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setMaximumSize(QSize(75, 16777215))

        self.gridLayout_13.addWidget(self.pushButton_8, 6, 1, 1, 1)

        self.label_17 = QLabel(self.page_13)
        self.label_17.setObjectName(u"label_17")

        self.gridLayout_13.addWidget(self.label_17, 1, 0, 1, 1)

        self.lineEdit_8 = QLineEdit(self.page_13)
        self.lineEdit_8.setObjectName(u"lineEdit_8")

        self.gridLayout_13.addWidget(self.lineEdit_8, 2, 0, 1, 1)

        self.lineEdit_7 = QLineEdit(self.page_13)
        self.lineEdit_7.setObjectName(u"lineEdit_7")
        self.lineEdit_7.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_13.addWidget(self.lineEdit_7, 6, 2, 1, 1)

        self.label_20 = QLabel(self.page_13)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setFont(font3)
        self.label_20.setAlignment(Qt.AlignCenter)

        self.gridLayout_13.addWidget(self.label_20, 0, 0, 1, 3)

        self.label_23 = QLabel(self.page_13)
        self.label_23.setObjectName(u"label_23")

        self.gridLayout_13.addWidget(self.label_23, 3, 0, 1, 1)

        self.lineEdit_9 = QLineEdit(self.page_13)
        self.lineEdit_9.setObjectName(u"lineEdit_9")

        self.gridLayout_13.addWidget(self.lineEdit_9, 6, 0, 1, 1)


        self.gridLayout_15.addLayout(self.gridLayout_13, 2, 0, 1, 2)

        self.agentbuilder_toolbox.addItem(self.page_13, u"C#")
        self.page_9 = QWidget()
        self.page_9.setObjectName(u"page_9")
        self.page_9.setGeometry(QRect(0, 0, 756, 645))
        self.gridLayout_19 = QGridLayout(self.page_9)
        self.gridLayout_19.setObjectName(u"gridLayout_19")
        self.gridLayout_16 = QGridLayout()
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.agentbuilder_toolbox_python_ip = QLineEdit(self.page_9)
        self.agentbuilder_toolbox_python_ip.setObjectName(u"agentbuilder_toolbox_python_ip")

        self.gridLayout_16.addWidget(self.agentbuilder_toolbox_python_ip, 2, 0, 1, 1)

        self.agentbuilder_toolbox_python_port = QLineEdit(self.page_9)
        self.agentbuilder_toolbox_python_port.setObjectName(u"agentbuilder_toolbox_python_port")

        self.gridLayout_16.addWidget(self.agentbuilder_toolbox_python_port, 4, 0, 1, 1)

        self.label_29 = QLabel(self.page_9)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setFont(font4)
        self.label_29.setAlignment(Qt.AlignCenter)

        self.gridLayout_16.addWidget(self.label_29, 0, 0, 1, 2)

        self.label_28 = QLabel(self.page_9)
        self.label_28.setObjectName(u"label_28")

        self.gridLayout_16.addWidget(self.label_28, 1, 0, 1, 1)

        self.label_27 = QLabel(self.page_9)
        self.label_27.setObjectName(u"label_27")

        self.gridLayout_16.addWidget(self.label_27, 3, 0, 1, 1)

        self.spinBox = QSpinBox(self.page_9)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setMinimum(1)
        self.spinBox.setMaximum(999999999)
        self.spinBox.setValue(60)

        self.gridLayout_16.addWidget(self.spinBox, 4, 1, 1, 1)

        self.label_38 = QLabel(self.page_9)
        self.label_38.setObjectName(u"label_38")

        self.gridLayout_16.addWidget(self.label_38, 3, 1, 1, 1)

        self.lineEdit_13 = QLineEdit(self.page_9)
        self.lineEdit_13.setObjectName(u"lineEdit_13")

        self.gridLayout_16.addWidget(self.lineEdit_13, 2, 1, 1, 1)


        self.gridLayout_19.addLayout(self.gridLayout_16, 0, 0, 1, 2)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.agentbuilder_toolbox_python_copy_to_clipboard = QPushButton(self.page_9)
        self.agentbuilder_toolbox_python_copy_to_clipboard.setObjectName(u"agentbuilder_toolbox_python_copy_to_clipboard")

        self.horizontalLayout_4.addWidget(self.agentbuilder_toolbox_python_copy_to_clipboard)

        self.agentbuilder_toolbox_python_save_to_file = QPushButton(self.page_9)
        self.agentbuilder_toolbox_python_save_to_file.setObjectName(u"agentbuilder_toolbox_python_save_to_file")

        self.horizontalLayout_4.addWidget(self.agentbuilder_toolbox_python_save_to_file)

        self.agentbuilder_toolbox_python_compile_button = QPushButton(self.page_9)
        self.agentbuilder_toolbox_python_compile_button.setObjectName(u"agentbuilder_toolbox_python_compile_button")

        self.horizontalLayout_4.addWidget(self.agentbuilder_toolbox_python_compile_button)


        self.gridLayout_19.addLayout(self.horizontalLayout_4, 3, 0, 1, 2)

        self.verticalSpacer_6 = QSpacerItem(20, 303, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_19.addItem(self.verticalSpacer_6, 2, 1, 1, 1)

        self.verticalSpacer_5 = QSpacerItem(20, 303, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_19.addItem(self.verticalSpacer_5, 2, 0, 1, 1)

        self.gridLayout_18 = QGridLayout()
        self.gridLayout_18.setObjectName(u"gridLayout_18")
        self.agentbuilder_toolbox_python_compile_savedir_browse = QPushButton(self.page_9)
        self.agentbuilder_toolbox_python_compile_savedir_browse.setObjectName(u"agentbuilder_toolbox_python_compile_savedir_browse")
        self.agentbuilder_toolbox_python_compile_savedir_browse.setMaximumSize(QSize(75, 16777215))

        self.gridLayout_18.addWidget(self.agentbuilder_toolbox_python_compile_savedir_browse, 7, 1, 1, 1)

        self.label_31 = QLabel(self.page_9)
        self.label_31.setObjectName(u"label_31")

        self.gridLayout_18.addWidget(self.label_31, 2, 0, 1, 1)

        self.label_30 = QLabel(self.page_9)
        self.label_30.setObjectName(u"label_30")

        self.gridLayout_18.addWidget(self.label_30, 4, 2, 1, 1)

        self.agentbuilder_toolbox_python_compile_flags = QLineEdit(self.page_9)
        self.agentbuilder_toolbox_python_compile_flags.setObjectName(u"agentbuilder_toolbox_python_compile_flags")

        self.gridLayout_18.addWidget(self.agentbuilder_toolbox_python_compile_flags, 3, 0, 1, 1)

        self.agentbuilder_toolbox_python_compile_savename = QLineEdit(self.page_9)
        self.agentbuilder_toolbox_python_compile_savename.setObjectName(u"agentbuilder_toolbox_python_compile_savename")
        self.agentbuilder_toolbox_python_compile_savename.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_18.addWidget(self.agentbuilder_toolbox_python_compile_savename, 7, 2, 1, 1)

        self.label_33 = QLabel(self.page_9)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setFont(font3)
        self.label_33.setAlignment(Qt.AlignCenter)

        self.gridLayout_18.addWidget(self.label_33, 0, 0, 1, 3)

        self.agentbuilder_toolbox_python_compile_savedir = QLineEdit(self.page_9)
        self.agentbuilder_toolbox_python_compile_savedir.setObjectName(u"agentbuilder_toolbox_python_compile_savedir")

        self.gridLayout_18.addWidget(self.agentbuilder_toolbox_python_compile_savedir, 7, 0, 1, 1)

        self.label_35 = QLabel(self.page_9)
        self.label_35.setObjectName(u"label_35")

        self.gridLayout_18.addWidget(self.label_35, 4, 0, 1, 1)

        self.label_36 = QLabel(self.page_9)
        self.label_36.setObjectName(u"label_36")

        self.gridLayout_18.addWidget(self.label_36, 2, 2, 1, 1)

        self.agentbuilder_toolbox_python_compile_timeout = QSpinBox(self.page_9)
        self.agentbuilder_toolbox_python_compile_timeout.setObjectName(u"agentbuilder_toolbox_python_compile_timeout")
        self.agentbuilder_toolbox_python_compile_timeout.setMinimum(1)
        self.agentbuilder_toolbox_python_compile_timeout.setMaximum(5000)
        self.agentbuilder_toolbox_python_compile_timeout.setValue(120)

        self.gridLayout_18.addWidget(self.agentbuilder_toolbox_python_compile_timeout, 3, 2, 1, 1)


        self.gridLayout_19.addLayout(self.gridLayout_18, 1, 0, 1, 2)

        self.agentbuilder_toolbox.addItem(self.page_9, u"Python")

        self.gridLayout_2.addWidget(self.agentbuilder_toolbox, 0, 0, 1, 1)

        self.tabWidget_8.addTab(self.tab_2, "")

        self.gridLayout_17.addWidget(self.tabWidget_8, 0, 0, 1, 1)

        self.main_tab_widget.addTab(self.tab_22, "")
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

        self.main_tab_widget.addTab(self.tab_6, "")
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.gridLayout_6 = QGridLayout(self.tab_5)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.tabWidget_2 = QTabWidget(self.tab_5)
        self.tabWidget_2.setObjectName(u"tabWidget_2")
        self.tab_37 = QWidget()
        self.tab_37.setObjectName(u"tab_37")
        self.gridLayout_28 = QGridLayout(self.tab_37)
        self.gridLayout_28.setObjectName(u"gridLayout_28")
        self.settings_edit = QTextEdit(self.tab_37)
        self.settings_edit.setObjectName(u"settings_edit")
        self.settings_edit.setFont(font3)

        self.gridLayout_28.addWidget(self.settings_edit, 0, 0, 1, 3)

        self.settings_reload = QPushButton(self.tab_37)
        self.settings_reload.setObjectName(u"settings_reload")

        self.gridLayout_28.addWidget(self.settings_reload, 2, 1, 1, 1)

        self.program_reload = QPushButton(self.tab_37)
        self.program_reload.setObjectName(u"program_reload")

        self.gridLayout_28.addWidget(self.program_reload, 2, 0, 1, 1)

        self.settings_write = QPushButton(self.tab_37)
        self.settings_write.setObjectName(u"settings_write")

        self.gridLayout_28.addWidget(self.settings_write, 2, 2, 1, 1)

        self.lineEdit_5 = QLineEdit(self.tab_37)
        self.lineEdit_5.setObjectName(u"lineEdit_5")

        self.gridLayout_28.addWidget(self.lineEdit_5, 1, 0, 1, 3)

        self.tabWidget_2.addTab(self.tab_37, "")

        self.gridLayout_6.addWidget(self.tabWidget_2, 0, 0, 1, 1)

        self.main_tab_widget.addTab(self.tab_5, "")
        self.tab_27 = QWidget()
        self.tab_27.setObjectName(u"tab_27")
        self.gridLayout_25 = QGridLayout(self.tab_27)
        self.gridLayout_25.setObjectName(u"gridLayout_25")
        self.tabWidget_10 = QTabWidget(self.tab_27)
        self.tabWidget_10.setObjectName(u"tabWidget_10")
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

        self.performance_lcd_upload = QLCDNumber(self.tab_75)
        self.performance_lcd_upload.setObjectName(u"performance_lcd_upload")
        self.performance_lcd_upload.setFrameShape(QFrame.Panel)
        self.performance_lcd_upload.setFrameShadow(QFrame.Sunken)
        self.performance_lcd_upload.setDigitCount(5)
        self.performance_lcd_upload.setProperty("value", 0.000000000000000)

        self.gridLayout_54.addWidget(self.performance_lcd_upload, 9, 0, 1, 2)

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
        font5 = QFont()
        font5.setUnderline(True)
        font5.setKerning(True)
        self.label_91.setFont(font5)

        self.gridLayout_54.addWidget(self.label_91, 0, 3, 2, 1)

        self.line_30 = QFrame(self.tab_75)
        self.line_30.setObjectName(u"line_30")
        self.line_30.setFrameShape(QFrame.VLine)
        self.line_30.setFrameShadow(QFrame.Sunken)

        self.gridLayout_54.addWidget(self.line_30, 1, 2, 13, 1)

        self.checkBox_23 = QCheckBox(self.tab_75)
        self.checkBox_23.setObjectName(u"checkBox_23")

        self.gridLayout_54.addWidget(self.checkBox_23, 3, 3, 1, 2)

        self.performance_lcd_ping = QLCDNumber(self.tab_75)
        self.performance_lcd_ping.setObjectName(u"performance_lcd_ping")

        self.gridLayout_54.addWidget(self.performance_lcd_ping, 6, 0, 1, 2)

        self.label_83 = QLabel(self.tab_75)
        self.label_83.setObjectName(u"label_83")

        self.gridLayout_54.addWidget(self.label_83, 1, 1, 1, 1)

        self.label_82 = QLabel(self.tab_75)
        self.label_82.setObjectName(u"label_82")

        self.gridLayout_54.addWidget(self.label_82, 3, 1, 1, 1)

        self.performance_seconds = QLineEdit(self.tab_75)
        self.performance_seconds.setObjectName(u"performance_seconds")
        self.performance_seconds.setMaximumSize(QSize(19777, 16777215))

        self.gridLayout_54.addWidget(self.performance_seconds, 4, 3, 1, 1)

        self.checkBox_24 = QCheckBox(self.tab_75)
        self.checkBox_24.setObjectName(u"checkBox_24")

        self.gridLayout_54.addWidget(self.checkBox_24, 6, 3, 1, 1)

        self.textEdit_23 = QTextEdit(self.tab_75)
        self.textEdit_23.setObjectName(u"textEdit_23")

        self.gridLayout_54.addWidget(self.textEdit_23, 0, 8, 14, 1)

        self.label_90 = QLabel(self.tab_75)
        self.label_90.setObjectName(u"label_90")

        self.gridLayout_54.addWidget(self.label_90, 4, 4, 1, 1)

        self.performance_lcd_download = QLCDNumber(self.tab_75)
        self.performance_lcd_download.setObjectName(u"performance_lcd_download")
        self.performance_lcd_download.setFrameShape(QFrame.Panel)
        self.performance_lcd_download.setFrameShadow(QFrame.Sunken)
        self.performance_lcd_download.setDigitCount(5)
        self.performance_lcd_download.setProperty("value", 0.000000000000000)

        self.gridLayout_54.addWidget(self.performance_lcd_download, 12, 0, 1, 2)

        self.label_86 = QLabel(self.tab_75)
        self.label_86.setObjectName(u"label_86")
        self.label_86.setFont(font4)

        self.gridLayout_54.addWidget(self.label_86, 0, 0, 2, 1)

        self.label_88 = QLabel(self.tab_75)
        self.label_88.setObjectName(u"label_88")

        self.gridLayout_54.addWidget(self.label_88, 7, 0, 2, 1)

        self.label_87 = QLabel(self.tab_75)
        self.label_87.setObjectName(u"label_87")

        self.gridLayout_54.addWidget(self.label_87, 10, 0, 2, 1)

        self.performance_speedtest = QPushButton(self.tab_75)
        self.performance_speedtest.setObjectName(u"performance_speedtest")

        self.gridLayout_54.addWidget(self.performance_speedtest, 13, 0, 1, 2)

        self.performance_benchmark_button = QPushButton(self.tab_75)
        self.performance_benchmark_button.setObjectName(u"performance_benchmark_button")

        self.gridLayout_54.addWidget(self.performance_benchmark_button, 13, 3, 1, 2)

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

        self.other_network_performance = QGraphicsView(self.tab_52)
        self.other_network_performance.setObjectName(u"other_network_performance")
        self.other_network_performance.setMinimumSize(QSize(0, 100))
        self.other_network_performance.setMaximumSize(QSize(16777215, 100))

        self.gridLayout_55.addWidget(self.other_network_performance, 5, 0, 1, 2)

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
        self.tab_7 = QWidget()
        self.tab_7.setObjectName(u"tab_7")
        self.gridLayout_52 = QGridLayout(self.tab_7)
        self.gridLayout_52.setObjectName(u"gridLayout_52")
        self.toolBox = QToolBox(self.tab_7)
        self.toolBox.setObjectName(u"toolBox")
        self.page_7 = QWidget()
        self.page_7.setObjectName(u"page_7")
        self.page_7.setGeometry(QRect(0, 0, 462, 187))
        self.gridLayout_53 = QGridLayout(self.page_7)
        self.gridLayout_53.setObjectName(u"gridLayout_53")
        self.tabWidget_5 = QTabWidget(self.page_7)
        self.tabWidget_5.setObjectName(u"tabWidget_5")
        self.tab_8 = QWidget()
        self.tab_8.setObjectName(u"tab_8")
        self.gridLayout_58 = QGridLayout(self.tab_8)
        self.gridLayout_58.setObjectName(u"gridLayout_58")
        self.gridLayout_66 = QGridLayout()
        self.gridLayout_66.setObjectName(u"gridLayout_66")
        self.other_content_usernames_layout_general = QGridLayout()
        self.other_content_usernames_layout_general.setObjectName(u"other_content_usernames_layout_general")
        self.label_6 = QLabel(self.tab_8)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.other_content_usernames_layout_general.addWidget(self.label_6, 0, 0, 1, 1)

        self.other_content_usernames_layout_general_button_placeholder = QPushButton(self.tab_8)
        self.other_content_usernames_layout_general_button_placeholder.setObjectName(u"other_content_usernames_layout_general_button_placeholder")
        self.other_content_usernames_layout_general_button_placeholder.setEnabled(False)

        self.other_content_usernames_layout_general.addWidget(self.other_content_usernames_layout_general_button_placeholder, 1, 1, 1, 1)

        self.other_content_usernames_layout_general_placeholder = QLineEdit(self.tab_8)
        self.other_content_usernames_layout_general_placeholder.setObjectName(u"other_content_usernames_layout_general_placeholder")
        self.other_content_usernames_layout_general_placeholder.setEnabled(False)
        self.other_content_usernames_layout_general_placeholder.setClearButtonEnabled(False)

        self.other_content_usernames_layout_general.addWidget(self.other_content_usernames_layout_general_placeholder, 1, 0, 1, 1)


        self.gridLayout_66.addLayout(self.other_content_usernames_layout_general, 0, 0, 1, 1)

        self.other_content_usernames_layout_default = QGridLayout()
        self.other_content_usernames_layout_default.setObjectName(u"other_content_usernames_layout_default")
        self.label_9 = QLabel(self.tab_8)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.other_content_usernames_layout_default.addWidget(self.label_9, 0, 0, 1, 1)

        self.other_content_usernames_layout_default_placeholder = QLineEdit(self.tab_8)
        self.other_content_usernames_layout_default_placeholder.setObjectName(u"other_content_usernames_layout_default_placeholder")
        self.other_content_usernames_layout_default_placeholder.setEnabled(False)

        self.other_content_usernames_layout_default.addWidget(self.other_content_usernames_layout_default_placeholder, 1, 0, 1, 1)

        self.other_content_usernames_layout_default_button_placeholder = QPushButton(self.tab_8)
        self.other_content_usernames_layout_default_button_placeholder.setObjectName(u"other_content_usernames_layout_default_button_placeholder")
        self.other_content_usernames_layout_default_button_placeholder.setEnabled(False)

        self.other_content_usernames_layout_default.addWidget(self.other_content_usernames_layout_default_button_placeholder, 1, 1, 1, 1)


        self.gridLayout_66.addLayout(self.other_content_usernames_layout_default, 0, 1, 1, 1)

        self.other_content_usernames_layout_other = QGridLayout()
        self.other_content_usernames_layout_other.setObjectName(u"other_content_usernames_layout_other")
        self.label_8 = QLabel(self.tab_8)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setAutoFillBackground(False)
        self.label_8.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.other_content_usernames_layout_other.addWidget(self.label_8, 0, 0, 1, 1)

        self.other_content_usernames_layout_other_placeholder = QLineEdit(self.tab_8)
        self.other_content_usernames_layout_other_placeholder.setObjectName(u"other_content_usernames_layout_other_placeholder")
        self.other_content_usernames_layout_other_placeholder.setEnabled(False)

        self.other_content_usernames_layout_other.addWidget(self.other_content_usernames_layout_other_placeholder, 1, 0, 1, 1)

        self.other_content_usernames_layout_other_button_placeholder = QPushButton(self.tab_8)
        self.other_content_usernames_layout_other_button_placeholder.setObjectName(u"other_content_usernames_layout_other_button_placeholder")
        self.other_content_usernames_layout_other_button_placeholder.setEnabled(False)

        self.other_content_usernames_layout_other.addWidget(self.other_content_usernames_layout_other_button_placeholder, 1, 1, 1, 1)


        self.gridLayout_66.addLayout(self.other_content_usernames_layout_other, 1, 0, 1, 2)


        self.gridLayout_58.addLayout(self.gridLayout_66, 0, 0, 1, 1)

        self.tabWidget_5.addTab(self.tab_8, "")
        self.tab_10 = QWidget()
        self.tab_10.setObjectName(u"tab_10")
        self.gridLayout_76 = QGridLayout(self.tab_10)
        self.gridLayout_76.setObjectName(u"gridLayout_76")
        self.gridLayout_71 = QGridLayout()
        self.gridLayout_71.setObjectName(u"gridLayout_71")
        self.other_content_password_layout_SecList = QGridLayout()
        self.other_content_password_layout_SecList.setObjectName(u"other_content_password_layout_SecList")
        self.other_content_password_layout_SecList_placeholder_button = QPushButton(self.tab_10)
        self.other_content_password_layout_SecList_placeholder_button.setObjectName(u"other_content_password_layout_SecList_placeholder_button")
        self.other_content_password_layout_SecList_placeholder_button.setEnabled(False)

        self.other_content_password_layout_SecList.addWidget(self.other_content_password_layout_SecList_placeholder_button, 2, 1, 1, 1)

        self.other_content_password_layout_SecList_placeholder = QLineEdit(self.tab_10)
        self.other_content_password_layout_SecList_placeholder.setObjectName(u"other_content_password_layout_SecList_placeholder")
        self.other_content_password_layout_SecList_placeholder.setEnabled(False)

        self.other_content_password_layout_SecList.addWidget(self.other_content_password_layout_SecList_placeholder, 2, 0, 1, 1)

        self.label_18 = QLabel(self.tab_10)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.other_content_password_layout_SecList.addWidget(self.label_18, 1, 0, 1, 1)


        self.gridLayout_71.addLayout(self.other_content_password_layout_SecList, 0, 0, 1, 1)

        self.other_content_password_layout_WeakPasswords = QGridLayout()
        self.other_content_password_layout_WeakPasswords.setObjectName(u"other_content_password_layout_WeakPasswords")
        self.other_content_password_layout_WeakPasswords_placeholder_button = QPushButton(self.tab_10)
        self.other_content_password_layout_WeakPasswords_placeholder_button.setObjectName(u"other_content_password_layout_WeakPasswords_placeholder_button")
        self.other_content_password_layout_WeakPasswords_placeholder_button.setEnabled(False)

        self.other_content_password_layout_WeakPasswords.addWidget(self.other_content_password_layout_WeakPasswords_placeholder_button, 1, 1, 1, 1)

        self.label_19 = QLabel(self.tab_10)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.other_content_password_layout_WeakPasswords.addWidget(self.label_19, 0, 0, 1, 1)

        self.other_content_password_layout_WeakPasswords_placeholder = QLineEdit(self.tab_10)
        self.other_content_password_layout_WeakPasswords_placeholder.setObjectName(u"other_content_password_layout_WeakPasswords_placeholder")
        self.other_content_password_layout_WeakPasswords_placeholder.setEnabled(False)

        self.other_content_password_layout_WeakPasswords.addWidget(self.other_content_password_layout_WeakPasswords_placeholder, 1, 0, 1, 1)


        self.gridLayout_71.addLayout(self.other_content_password_layout_WeakPasswords, 1, 0, 1, 1)

        self.other_content_password_layout_DefaultPasswords = QGridLayout()
        self.other_content_password_layout_DefaultPasswords.setObjectName(u"other_content_password_layout_DefaultPasswords")
        self.other_content_password_layout_DefaultPasswords_placeholder_button = QPushButton(self.tab_10)
        self.other_content_password_layout_DefaultPasswords_placeholder_button.setObjectName(u"other_content_password_layout_DefaultPasswords_placeholder_button")
        self.other_content_password_layout_DefaultPasswords_placeholder_button.setEnabled(False)

        self.other_content_password_layout_DefaultPasswords.addWidget(self.other_content_password_layout_DefaultPasswords_placeholder_button, 1, 1, 1, 1)

        self.label_32 = QLabel(self.tab_10)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.other_content_password_layout_DefaultPasswords.addWidget(self.label_32, 0, 0, 1, 1)

        self.other_content_password_layout_DefaultPasswords_placeholder = QLineEdit(self.tab_10)
        self.other_content_password_layout_DefaultPasswords_placeholder.setObjectName(u"other_content_password_layout_DefaultPasswords_placeholder")
        self.other_content_password_layout_DefaultPasswords_placeholder.setEnabled(False)

        self.other_content_password_layout_DefaultPasswords.addWidget(self.other_content_password_layout_DefaultPasswords_placeholder, 1, 0, 1, 1)


        self.gridLayout_71.addLayout(self.other_content_password_layout_DefaultPasswords, 0, 1, 1, 1)

        self.other_content_password_layout_LeakedPasswords = QGridLayout()
        self.other_content_password_layout_LeakedPasswords.setObjectName(u"other_content_password_layout_LeakedPasswords")
        self.label_44 = QLabel(self.tab_10)
        self.label_44.setObjectName(u"label_44")
        self.label_44.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.other_content_password_layout_LeakedPasswords.addWidget(self.label_44, 0, 0, 1, 1)

        self.other_content_password_layout_LeakedPasswords_placeholder = QLineEdit(self.tab_10)
        self.other_content_password_layout_LeakedPasswords_placeholder.setObjectName(u"other_content_password_layout_LeakedPasswords_placeholder")
        self.other_content_password_layout_LeakedPasswords_placeholder.setEnabled(False)

        self.other_content_password_layout_LeakedPasswords.addWidget(self.other_content_password_layout_LeakedPasswords_placeholder, 1, 0, 1, 1)

        self.other_content_password_layout_LeakedPasswords_placeholder_button = QPushButton(self.tab_10)
        self.other_content_password_layout_LeakedPasswords_placeholder_button.setObjectName(u"other_content_password_layout_LeakedPasswords_placeholder_button")
        self.other_content_password_layout_LeakedPasswords_placeholder_button.setEnabled(False)

        self.other_content_password_layout_LeakedPasswords.addWidget(self.other_content_password_layout_LeakedPasswords_placeholder_button, 1, 1, 1, 1)


        self.gridLayout_71.addLayout(self.other_content_password_layout_LeakedPasswords, 1, 1, 1, 1)


        self.gridLayout_76.addLayout(self.gridLayout_71, 0, 0, 1, 1)

        self.tabWidget_5.addTab(self.tab_10, "")
        self.tab_9 = QWidget()
        self.tab_9.setObjectName(u"tab_9")
        self.gridLayout_57 = QGridLayout(self.tab_9)
        self.gridLayout_57.setObjectName(u"gridLayout_57")
        self.gridLayout_59 = QGridLayout()
        self.gridLayout_59.setObjectName(u"gridLayout_59")
        self.other_content_directory_layout_general = QGridLayout()
        self.other_content_directory_layout_general.setObjectName(u"other_content_directory_layout_general")
        self.label_2 = QLabel(self.tab_9)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.other_content_directory_layout_general.addWidget(self.label_2, 0, 0, 1, 1)

        self.other_content_directory_layout_general_placeholder = QLineEdit(self.tab_9)
        self.other_content_directory_layout_general_placeholder.setObjectName(u"other_content_directory_layout_general_placeholder")
        self.other_content_directory_layout_general_placeholder.setEnabled(False)

        self.other_content_directory_layout_general.addWidget(self.other_content_directory_layout_general_placeholder, 1, 0, 1, 1)

        self.other_content_directory_layout_general_button_placeholder = QPushButton(self.tab_9)
        self.other_content_directory_layout_general_button_placeholder.setObjectName(u"other_content_directory_layout_general_button_placeholder")
        self.other_content_directory_layout_general_button_placeholder.setEnabled(False)

        self.other_content_directory_layout_general.addWidget(self.other_content_directory_layout_general_button_placeholder, 1, 1, 1, 1)


        self.gridLayout_59.addLayout(self.other_content_directory_layout_general, 0, 0, 1, 1)

        self.other_content_directory_layout_commonURL = QGridLayout()
        self.other_content_directory_layout_commonURL.setObjectName(u"other_content_directory_layout_commonURL")
        self.other_content_directory_layout_commonURL_placeholder = QLineEdit(self.tab_9)
        self.other_content_directory_layout_commonURL_placeholder.setObjectName(u"other_content_directory_layout_commonURL_placeholder")
        self.other_content_directory_layout_commonURL_placeholder.setEnabled(False)

        self.other_content_directory_layout_commonURL.addWidget(self.other_content_directory_layout_commonURL_placeholder, 1, 0, 1, 1)

        self.other_content_directory_layout_commonURL_button_placeholder = QPushButton(self.tab_9)
        self.other_content_directory_layout_commonURL_button_placeholder.setObjectName(u"other_content_directory_layout_commonURL_button_placeholder")
        self.other_content_directory_layout_commonURL_button_placeholder.setEnabled(False)

        self.other_content_directory_layout_commonURL.addWidget(self.other_content_directory_layout_commonURL_button_placeholder, 1, 1, 1, 1)

        self.label_4 = QLabel(self.tab_9)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.other_content_directory_layout_commonURL.addWidget(self.label_4, 0, 0, 1, 1)


        self.gridLayout_59.addLayout(self.other_content_directory_layout_commonURL, 1, 0, 1, 1)

        self.other_content_directory_layout_application = QGridLayout()
        self.other_content_directory_layout_application.setObjectName(u"other_content_directory_layout_application")
        self.other_content_directory_layout_application_button_placeholder = QPushButton(self.tab_9)
        self.other_content_directory_layout_application_button_placeholder.setObjectName(u"other_content_directory_layout_application_button_placeholder")
        self.other_content_directory_layout_application_button_placeholder.setEnabled(False)

        self.other_content_directory_layout_application.addWidget(self.other_content_directory_layout_application_button_placeholder, 1, 1, 1, 1)

        self.other_content_directory_layout_application_placeholder = QLineEdit(self.tab_9)
        self.other_content_directory_layout_application_placeholder.setObjectName(u"other_content_directory_layout_application_placeholder")
        self.other_content_directory_layout_application_placeholder.setEnabled(False)

        self.other_content_directory_layout_application.addWidget(self.other_content_directory_layout_application_placeholder, 1, 0, 1, 1)

        self.label_3 = QLabel(self.tab_9)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.other_content_directory_layout_application.addWidget(self.label_3, 0, 0, 1, 1)


        self.gridLayout_59.addLayout(self.other_content_directory_layout_application, 0, 1, 1, 1)

        self.other_content_directory_layout_other = QGridLayout()
        self.other_content_directory_layout_other.setObjectName(u"other_content_directory_layout_other")
        self.other_content_directory_layout_other_button_placeholder = QPushButton(self.tab_9)
        self.other_content_directory_layout_other_button_placeholder.setObjectName(u"other_content_directory_layout_other_button_placeholder")
        self.other_content_directory_layout_other_button_placeholder.setEnabled(False)

        self.other_content_directory_layout_other.addWidget(self.other_content_directory_layout_other_button_placeholder, 1, 1, 1, 1)

        self.label_5 = QLabel(self.tab_9)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.other_content_directory_layout_other.addWidget(self.label_5, 0, 0, 1, 1)

        self.other_content_directory_layout_other_placeholder = QLineEdit(self.tab_9)
        self.other_content_directory_layout_other_placeholder.setObjectName(u"other_content_directory_layout_other_placeholder")
        self.other_content_directory_layout_other_placeholder.setEnabled(False)

        self.other_content_directory_layout_other.addWidget(self.other_content_directory_layout_other_placeholder, 1, 0, 1, 1)


        self.gridLayout_59.addLayout(self.other_content_directory_layout_other, 1, 1, 1, 1)


        self.gridLayout_57.addLayout(self.gridLayout_59, 0, 0, 1, 1)

        self.tabWidget_5.addTab(self.tab_9, "")

        self.gridLayout_53.addWidget(self.tabWidget_5, 0, 0, 1, 1)

        self.toolBox.addItem(self.page_7, u"Wordlists")
        self.page_8 = QWidget()
        self.page_8.setObjectName(u"page_8")
        self.page_8.setGeometry(QRect(0, 0, 382, 134))
        self.gridLayout = QGridLayout(self.page_8)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout_72 = QGridLayout()
        self.gridLayout_72.setObjectName(u"gridLayout_72")
        self.other_content_exploit_layou_exploitdb = QGridLayout()
        self.other_content_exploit_layou_exploitdb.setObjectName(u"other_content_exploit_layou_exploitdb")
        self.other_content_exploit_layou_exploitdb_placeholder_button = QPushButton(self.page_8)
        self.other_content_exploit_layou_exploitdb_placeholder_button.setObjectName(u"other_content_exploit_layou_exploitdb_placeholder_button")
        self.other_content_exploit_layou_exploitdb_placeholder_button.setEnabled(False)

        self.other_content_exploit_layou_exploitdb.addWidget(self.other_content_exploit_layou_exploitdb_placeholder_button, 2, 1, 1, 1)

        self.other_content_exploit_layou_exploitdb_placeholder = QLineEdit(self.page_8)
        self.other_content_exploit_layou_exploitdb_placeholder.setObjectName(u"other_content_exploit_layou_exploitdb_placeholder")
        self.other_content_exploit_layou_exploitdb_placeholder.setEnabled(False)

        self.other_content_exploit_layou_exploitdb.addWidget(self.other_content_exploit_layou_exploitdb_placeholder, 2, 0, 1, 1)

        self.label_21 = QLabel(self.page_8)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.other_content_exploit_layou_exploitdb.addWidget(self.label_21, 1, 0, 1, 1)


        self.gridLayout_72.addLayout(self.other_content_exploit_layou_exploitdb, 0, 0, 1, 1)

        self.other_content_directory_layout_WeakPasswords_2 = QGridLayout()
        self.other_content_directory_layout_WeakPasswords_2.setObjectName(u"other_content_directory_layout_WeakPasswords_2")
        self.other_content_directory_layout_WeakPasswords_placeholder_button_2 = QPushButton(self.page_8)
        self.other_content_directory_layout_WeakPasswords_placeholder_button_2.setObjectName(u"other_content_directory_layout_WeakPasswords_placeholder_button_2")
        self.other_content_directory_layout_WeakPasswords_placeholder_button_2.setEnabled(False)

        self.other_content_directory_layout_WeakPasswords_2.addWidget(self.other_content_directory_layout_WeakPasswords_placeholder_button_2, 1, 1, 1, 1)

        self.label_22 = QLabel(self.page_8)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.other_content_directory_layout_WeakPasswords_2.addWidget(self.label_22, 0, 0, 1, 1)

        self.other_content_directory_layout_WeakPasswords_placeholder_2 = QLineEdit(self.page_8)
        self.other_content_directory_layout_WeakPasswords_placeholder_2.setObjectName(u"other_content_directory_layout_WeakPasswords_placeholder_2")
        self.other_content_directory_layout_WeakPasswords_placeholder_2.setEnabled(False)

        self.other_content_directory_layout_WeakPasswords_2.addWidget(self.other_content_directory_layout_WeakPasswords_placeholder_2, 1, 0, 1, 1)


        self.gridLayout_72.addLayout(self.other_content_directory_layout_WeakPasswords_2, 1, 0, 1, 1)

        self.other_content_directory_layout_DefaultPasswords_2 = QGridLayout()
        self.other_content_directory_layout_DefaultPasswords_2.setObjectName(u"other_content_directory_layout_DefaultPasswords_2")
        self.other_content_directory_layout_DefaultPasswords_placeholder_button_2 = QPushButton(self.page_8)
        self.other_content_directory_layout_DefaultPasswords_placeholder_button_2.setObjectName(u"other_content_directory_layout_DefaultPasswords_placeholder_button_2")
        self.other_content_directory_layout_DefaultPasswords_placeholder_button_2.setEnabled(False)

        self.other_content_directory_layout_DefaultPasswords_2.addWidget(self.other_content_directory_layout_DefaultPasswords_placeholder_button_2, 1, 1, 1, 1)

        self.label_34 = QLabel(self.page_8)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.other_content_directory_layout_DefaultPasswords_2.addWidget(self.label_34, 0, 0, 1, 1)

        self.other_content_directory_layout_DefaultPasswords_placeholder_2 = QLineEdit(self.page_8)
        self.other_content_directory_layout_DefaultPasswords_placeholder_2.setObjectName(u"other_content_directory_layout_DefaultPasswords_placeholder_2")
        self.other_content_directory_layout_DefaultPasswords_placeholder_2.setEnabled(False)

        self.other_content_directory_layout_DefaultPasswords_2.addWidget(self.other_content_directory_layout_DefaultPasswords_placeholder_2, 1, 0, 1, 1)


        self.gridLayout_72.addLayout(self.other_content_directory_layout_DefaultPasswords_2, 0, 1, 1, 1)

        self.other_content_directory_layout_LeakedPasswords_2 = QGridLayout()
        self.other_content_directory_layout_LeakedPasswords_2.setObjectName(u"other_content_directory_layout_LeakedPasswords_2")
        self.label_45 = QLabel(self.page_8)
        self.label_45.setObjectName(u"label_45")
        self.label_45.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.other_content_directory_layout_LeakedPasswords_2.addWidget(self.label_45, 0, 0, 1, 1)

        self.other_content_directory_layout_LeakedPasswords_placeholder_2 = QLineEdit(self.page_8)
        self.other_content_directory_layout_LeakedPasswords_placeholder_2.setObjectName(u"other_content_directory_layout_LeakedPasswords_placeholder_2")
        self.other_content_directory_layout_LeakedPasswords_placeholder_2.setEnabled(False)

        self.other_content_directory_layout_LeakedPasswords_2.addWidget(self.other_content_directory_layout_LeakedPasswords_placeholder_2, 1, 0, 1, 1)

        self.other_content_directory_layout_LeakedPasswords_placeholder_button_2 = QPushButton(self.page_8)
        self.other_content_directory_layout_LeakedPasswords_placeholder_button_2.setObjectName(u"other_content_directory_layout_LeakedPasswords_placeholder_button_2")
        self.other_content_directory_layout_LeakedPasswords_placeholder_button_2.setEnabled(False)

        self.other_content_directory_layout_LeakedPasswords_2.addWidget(self.other_content_directory_layout_LeakedPasswords_placeholder_button_2, 1, 1, 1, 1)


        self.gridLayout_72.addLayout(self.other_content_directory_layout_LeakedPasswords_2, 1, 1, 1, 1)


        self.gridLayout.addLayout(self.gridLayout_72, 0, 0, 1, 1)

        self.toolBox.addItem(self.page_8, u"Vulnerability Databases and Exploits")

        self.gridLayout_52.addWidget(self.toolBox, 0, 0, 1, 1)

        self.tabWidget_10.addTab(self.tab_7, "")

        self.gridLayout_25.addWidget(self.tabWidget_10, 0, 0, 1, 1)

        self.main_tab_widget.addTab(self.tab_27, "")

        self.gridLayout_4.addWidget(self.main_tab_widget, 0, 0, 1, 1)

        LogecC3.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(LogecC3)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1579, 24))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menu_GettingStarted = QMenu(self.menubar)
        self.menu_GettingStarted.setObjectName(u"menu_GettingStarted")
        LogecC3.setMenuBar(self.menubar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menu_GettingStarted.menuAction())
        self.menuFile.addAction(self.actionDEBUG)
        self.menuFile.addAction(self.actionRELOAD)
        self.menuFile.addAction(self.actionSave_Project)
        self.menuFile.addAction(self.actionSaveAs_Project)
        self.menuFile.addAction(self.actionOpen_Project)
        self.menuFile.addAction(self.actionExit)
        self.menu_GettingStarted.addAction(self.GettingStarted_Readme)
        self.menu_GettingStarted.addAction(self.actionRead_Me_webview)

        self.retranslateUi(LogecC3)

        self.main_tab_widget.setCurrentIndex(1)
        self.bruteforce_panel_2.setCurrentIndex(0)
        self.c2_shell_tab.setCurrentIndex(0)
        self.tabWidget_8.setCurrentIndex(1)
        self.agentbuilder_toolbox.setCurrentIndex(2)
        self.tabWidget_2.setCurrentIndex(0)
        self.tabWidget_10.setCurrentIndex(0)
        self.tabWidget_16.setCurrentIndex(0)
        self.tabWidget_11.setCurrentIndex(2)
        self.tabWidget_12.setCurrentIndex(1)
        self.tabWidget_15.setCurrentIndex(1)
        self.toolBox.setCurrentIndex(1)
        self.tabWidget_5.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(LogecC3)
    # setupUi

    def retranslateUi(self, LogecC3):
        LogecC3.setWindowTitle(QCoreApplication.translate("LogecC3", u"Logec-Suite", None))
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
        self.actionRELOAD.setText(QCoreApplication.translate("LogecC3", u"Reload - This has a mem leak so only use for dev", None))
#if QT_CONFIG(shortcut)
        self.actionRELOAD.setShortcut(QCoreApplication.translate("LogecC3", u"Ctrl+Alt+R", None))
#endif // QT_CONFIG(shortcut)
        self.actionSave_Project.setText(QCoreApplication.translate("LogecC3", u"Save Project", None))
#if QT_CONFIG(shortcut)
        self.actionSave_Project.setShortcut(QCoreApplication.translate("LogecC3", u"Ctrl+S", None))
#endif // QT_CONFIG(shortcut)
        self.actionSaveAs_Project.setText(QCoreApplication.translate("LogecC3", u"Save Project As...", None))
        self.actionOpen_Project.setText(QCoreApplication.translate("LogecC3", u"Open Project", None))
        self.actionExit.setText(QCoreApplication.translate("LogecC3", u"Exit", None))
        self.c2_gui_hide_clients.setText(QCoreApplication.translate("LogecC3", u"Hide Clients", None))
        self.c2_gui_hide_shells.setText(QCoreApplication.translate("LogecC3", u"Hide Shells", None))
        self.c2_gui_hide_options.setText(QCoreApplication.translate("LogecC3", u"Hide Options", None))
        self.c2_gui_groupbox_clients.setTitle("")
        self.c2_gui_groupbox_options.setTitle("")
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
        self.c2_server_username.setText(QCoreApplication.translate("LogecC3", u"ryan", None))
        self.c2_server_username.setPlaceholderText(QCoreApplication.translate("LogecC3", u"Username", None))
        self.c2_disconnect_button.setText(QCoreApplication.translate("LogecC3", u"Disconnect", None))
        self.c2_server_port.setText(QCoreApplication.translate("LogecC3", u"101", None))
        self.c2_server_port.setPlaceholderText(QCoreApplication.translate("LogecC3", u"Port", None))
        self.c2_server_ip.setText(QCoreApplication.translate("LogecC3", u"127.0.0.1", None))
        self.c2_server_ip.setPlaceholderText(QCoreApplication.translate("LogecC3", u"IP", None))
        self.c2_status_label.setText(QCoreApplication.translate("LogecC3", u"Status: Not Connected", None))
        self.c2_server_password.setText("")
        self.c2_server_password.setPlaceholderText(QCoreApplication.translate("LogecC3", u"Password (Converts to **  on de-select)", None))
        self.c2_connect_button.setText(QCoreApplication.translate("LogecC3", u"Connect", None))
        self.bruteforce_panel_2.setTabText(self.bruteforce_panel_2.indexOf(self.tab_33), QCoreApplication.translate("LogecC3", u"ServerLogin", None))
        self.c2_start_server_local.setText(QCoreApplication.translate("LogecC3", u"Start", None))
        self.c2_server_log_local.setHtml(QCoreApplication.translate("LogecC3", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Cantarell'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">If you'd like to spin up the server locally, you can do it here, or you can run the 'server.py' file</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">DevNote:</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">This is run via a traditional python t"
                        "hread instead of a QThread, so I don't have 2 versions of the server.py floating around. Logs will be displayed here, and the start/stop button works, but that's the extent of the itneraction from the GUI (Segfaults happen with regular threads talking to the QT event loop)</p></body></html>", None))
        self.c2_server_password_local.setPlaceholderText(QCoreApplication.translate("LogecC3", u"Password (Converts to **  on de-select)", None))
        self.c2_server_port_local.setPlaceholderText(QCoreApplication.translate("LogecC3", u"Port", None))
        self.c2_stop_server_local.setText(QCoreApplication.translate("LogecC3", u"Stop", None))
        self.c2_server_ip_local.setText(QCoreApplication.translate("LogecC3", u"0.0.0.0", None))
        self.c2_server_ip_local.setPlaceholderText(QCoreApplication.translate("LogecC3", u"IP", None))
        self.bruteforce_panel_2.setTabText(self.bruteforce_panel_2.indexOf(self.tab_53), QCoreApplication.translate("LogecC3", u"LocalServer", None))
        self.c2_gui_groupbox_shells.setTitle("")
#if QT_CONFIG(tooltip)
        self.c2_shell_tab.setToolTip(QCoreApplication.translate("LogecC3", u"Enter", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.c2_shell_tab.setWhatsThis(QCoreApplication.translate("LogecC3", u"Enter", None))
#endif // QT_CONFIG(whatsthis)
#if QT_CONFIG(tooltip)
        self.c2_servershell.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.c2_servershell.setHtml(QCoreApplication.translate("LogecC3", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Monospace'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Cantarell'; font-size:11pt;\"><br /></p></body></html>", None))
        self.c2_servershell.setPlaceholderText(QCoreApplication.translate("LogecC3", u"root@127.0.0.1> ", None))
#if QT_CONFIG(tooltip)
        self.c2_servershell_send.setToolTip(QCoreApplication.translate("LogecC3", u"Hit the Enter Key", None))
#endif // QT_CONFIG(tooltip)
        self.c2_servershell_send.setText(QCoreApplication.translate("LogecC3", u"-->> Send <<-- ", None))
#if QT_CONFIG(shortcut)
        self.c2_servershell_send.setShortcut(QCoreApplication.translate("LogecC3", u"Return", None))
#endif // QT_CONFIG(shortcut)
#if QT_CONFIG(tooltip)
        self.c2_servershell_input.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.c2_servershell_input.setPlaceholderText(QCoreApplication.translate("LogecC3", u"Enter Command Here!", None))
        self.c2_shell_tab.setTabText(self.c2_shell_tab.indexOf(self.tab_57), QCoreApplication.translate("LogecC3", u"RemoteShell", None))
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
        self.c2_shell_tab.setTabText(self.c2_shell_tab.indexOf(self.tab_58), QCoreApplication.translate("LogecC3", u"Local DB", None))
#if QT_CONFIG(tooltip)
        self.c2_systemshell.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.c2_systemshell.setHtml(QCoreApplication.translate("LogecC3", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Monospace'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Cantarell'; font-size:11pt;\"><br /></p></body></html>", None))
        self.c2_systemshell.setPlaceholderText(QCoreApplication.translate("LogecC3", u"$", None))
#if QT_CONFIG(tooltip)
        self.c2_systemshell_input.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.c2_systemshell_input.setPlaceholderText(QCoreApplication.translate("LogecC3", u"Enter Command Here!", None))
#if QT_CONFIG(tooltip)
        self.c2_systemshell_send.setToolTip(QCoreApplication.translate("LogecC3", u"Hit the Enter Key", None))
#endif // QT_CONFIG(tooltip)
        self.c2_systemshell_send.setText(QCoreApplication.translate("LogecC3", u"-->> Send <<-- ", None))
#if QT_CONFIG(shortcut)
        self.c2_systemshell_send.setShortcut(QCoreApplication.translate("LogecC3", u"Return", None))
#endif // QT_CONFIG(shortcut)
        self.c2_shell_tab.setTabText(self.c2_shell_tab.indexOf(self.tab_59), QCoreApplication.translate("LogecC3", u"LocalShell", None))
        self.main_tab_widget.setTabText(self.main_tab_widget.indexOf(self.c2_tab), QCoreApplication.translate("LogecC3", u"C2", None))
#if QT_CONFIG(tooltip)
        self.exploitandvuln_search_button.setToolTip(QCoreApplication.translate("LogecC3", u"Run a query on the DB", None))
#endif // QT_CONFIG(tooltip)
        self.exploitandvuln_search_button.setText(QCoreApplication.translate("LogecC3", u"-->> Query Exploit DB <<--", None))
        self.exploitandvuln_search.setText("")
        self.exploitandvuln_search.setPlaceholderText(QCoreApplication.translate("LogecC3", u"Enter search", None))
        self.tabWidget_8.setTabText(self.tabWidget_8.indexOf(self.tab), QCoreApplication.translate("LogecC3", u"ExploitAndVulnSearch", None))
        self.agentbuilder_compilation_log.setHtml(QCoreApplication.translate("LogecC3", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Cantarell'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" text-decoration: underline;\">Compilation Log</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">[*] Started compilation</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">[*] Compilation Successful</p></body></html>", None))
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("LogecC3", u"8080", None))
        self.label_10.setText(QCoreApplication.translate("LogecC3", u"Port", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("LogecC3", u"127.0.0.1", None))
        self.label_7.setText(QCoreApplication.translate("LogecC3", u"IP", None))
        self.label_13.setText(QCoreApplication.translate("LogecC3", u"Connection Options", None))
        self.pushButton_2.setText(QCoreApplication.translate("LogecC3", u"Copy code to clipboard", None))
        self.pushButton.setText(QCoreApplication.translate("LogecC3", u"Compile", None))
        self.label_12.setText(QCoreApplication.translate("LogecC3", u"Save Name", None))
        self.lineEdit_6.setText("")
        self.lineEdit_6.setPlaceholderText(QCoreApplication.translate("LogecC3", u"NotAMaliciousFile", None))
        self.label.setText(QCoreApplication.translate("LogecC3", u"Compile Flags", None))
        self.pushButton_5.setText(QCoreApplication.translate("LogecC3", u"Browse", None))
        self.label_15.setText(QCoreApplication.translate("LogecC3", u"Compile Options (GCC)", None))
        self.lineEdit_3.setPlaceholderText(QCoreApplication.translate("LogecC3", u"-Wall", None))
        self.lineEdit_4.setPlaceholderText(QCoreApplication.translate("LogecC3", u"/opt/payloads", None))
        self.label_11.setText(QCoreApplication.translate("LogecC3", u"Save Location", None))
#if QT_CONFIG(tooltip)
        self.label_37.setToolTip(QCoreApplication.translate("LogecC3", u"If the process takes longer than this value, kill. (due to this being a wrapper, this helps combat rogue processes)", None))
#endif // QT_CONFIG(tooltip)
        self.label_37.setText(QCoreApplication.translate("LogecC3", u"Process Timeout (Seconds)", None))
#if QT_CONFIG(tooltip)
        self.spinBox_2.setToolTip(QCoreApplication.translate("LogecC3", u"If the process takes longer than this value, kill. (due to this being a wrapper, this helps combat rogue processes)", None))
#endif // QT_CONFIG(tooltip)
        self.agentbuilder_toolbox.setItemText(self.agentbuilder_toolbox.indexOf(self.page_22), QCoreApplication.translate("LogecC3", u"C", None))
        self.lineEdit_11.setPlaceholderText(QCoreApplication.translate("LogecC3", u"8080", None))
        self.label_24.setText(QCoreApplication.translate("LogecC3", u"Port", None))
        self.lineEdit_12.setPlaceholderText(QCoreApplication.translate("LogecC3", u"127.0.0.1", None))
        self.label_25.setText(QCoreApplication.translate("LogecC3", u"IP", None))
        self.label_26.setText(QCoreApplication.translate("LogecC3", u"Connection Options", None))
        self.pushButton_6.setText(QCoreApplication.translate("LogecC3", u"Copy code to clipboard", None))
        self.pushButton_7.setText(QCoreApplication.translate("LogecC3", u"Compile", None))
        self.label_16.setText(QCoreApplication.translate("LogecC3", u"Save Name", None))
        self.pushButton_8.setText(QCoreApplication.translate("LogecC3", u"Browse", None))
        self.label_17.setText(QCoreApplication.translate("LogecC3", u"Compile Flags", None))
        self.lineEdit_8.setPlaceholderText(QCoreApplication.translate("LogecC3", u"-Wall", None))
        self.lineEdit_7.setText("")
        self.lineEdit_7.setPlaceholderText(QCoreApplication.translate("LogecC3", u"NotAMaliciousFile", None))
        self.label_20.setText(QCoreApplication.translate("LogecC3", u"Compile Options", None))
        self.label_23.setText(QCoreApplication.translate("LogecC3", u"Save Location", None))
        self.lineEdit_9.setPlaceholderText(QCoreApplication.translate("LogecC3", u"/opt/payloads", None))
        self.agentbuilder_toolbox.setItemText(self.agentbuilder_toolbox.indexOf(self.page_13), QCoreApplication.translate("LogecC3", u"C#", None))
        self.agentbuilder_toolbox_python_ip.setPlaceholderText(QCoreApplication.translate("LogecC3", u"127.0.0.1", None))
        self.agentbuilder_toolbox_python_port.setPlaceholderText(QCoreApplication.translate("LogecC3", u"8080", None))
        self.label_29.setText(QCoreApplication.translate("LogecC3", u"Connection Options", None))
        self.label_28.setText(QCoreApplication.translate("LogecC3", u"IP", None))
        self.label_27.setText(QCoreApplication.translate("LogecC3", u"Port", None))
        self.label_38.setText(QCoreApplication.translate("LogecC3", u"Initial Heartbeat interval (seconds)", None))
        self.agentbuilder_toolbox_python_copy_to_clipboard.setText(QCoreApplication.translate("LogecC3", u"Copy to Clipboard", None))
        self.agentbuilder_toolbox_python_save_to_file.setText(QCoreApplication.translate("LogecC3", u"Save to File", None))
        self.agentbuilder_toolbox_python_compile_button.setText(QCoreApplication.translate("LogecC3", u"Compile (Nuitka)", None))
        self.agentbuilder_toolbox_python_compile_savedir_browse.setText(QCoreApplication.translate("LogecC3", u"Browse", None))
        self.label_31.setText(QCoreApplication.translate("LogecC3", u"Compile Flags", None))
        self.label_30.setText(QCoreApplication.translate("LogecC3", u"Save Name", None))
        self.agentbuilder_toolbox_python_compile_flags.setPlaceholderText(QCoreApplication.translate("LogecC3", u"-Wall", None))
        self.agentbuilder_toolbox_python_compile_savename.setText("")
        self.agentbuilder_toolbox_python_compile_savename.setPlaceholderText(QCoreApplication.translate("LogecC3", u"NotAMaliciousFile", None))
        self.label_33.setText(QCoreApplication.translate("LogecC3", u"Compile Options (Nuitka)", None))
        self.agentbuilder_toolbox_python_compile_savedir.setPlaceholderText(QCoreApplication.translate("LogecC3", u"/opt/payloads", None))
        self.label_35.setText(QCoreApplication.translate("LogecC3", u"Save Location", None))
#if QT_CONFIG(tooltip)
        self.label_36.setToolTip(QCoreApplication.translate("LogecC3", u"If the process takes longer than this value, kill. (due to this being a wrapper, this helps combat rogue processes)", None))
#endif // QT_CONFIG(tooltip)
        self.label_36.setText(QCoreApplication.translate("LogecC3", u"Process Timeout (Seconds)", None))
#if QT_CONFIG(tooltip)
        self.agentbuilder_toolbox_python_compile_timeout.setToolTip(QCoreApplication.translate("LogecC3", u"If the process takes longer than this value, kill. (due to this being a wrapper, this helps combat rogue processes)", None))
#endif // QT_CONFIG(tooltip)
        self.agentbuilder_toolbox.setItemText(self.agentbuilder_toolbox.indexOf(self.page_9), QCoreApplication.translate("LogecC3", u"Python", None))
        self.tabWidget_8.setTabText(self.tabWidget_8.indexOf(self.tab_2), QCoreApplication.translate("LogecC3", u"Agent Builder", None))
        self.main_tab_widget.setTabText(self.main_tab_widget.indexOf(self.tab_22), QCoreApplication.translate("LogecC3", u"Payload Builder N Stuff", None))
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
        self.main_tab_widget.setTabText(self.main_tab_widget.indexOf(self.tab_6), QCoreApplication.translate("LogecC3", u"LocalDB", None))
        self.settings_edit.setHtml(QCoreApplication.translate("LogecC3", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Cantarell'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.settings_reload.setText(QCoreApplication.translate("LogecC3", u"-->> Reload File <<--", None))
        self.program_reload.setText(QCoreApplication.translate("LogecC3", u"-->> Reload Program <<--", None))
        self.settings_write.setText(QCoreApplication.translate("LogecC3", u"-->> Write FIle <<--", None))
        self.lineEdit_5.setPlaceholderText(QCoreApplication.translate("LogecC3", u"Status Bar (success, failure, etc)", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_37), QCoreApplication.translate("LogecC3", u"Settings", None))
        self.main_tab_widget.setTabText(self.main_tab_widget.indexOf(self.tab_5), QCoreApplication.translate("LogecC3", u"Settings", None))
#if QT_CONFIG(tooltip)
        self.other_cpu_performance.setToolTip(QCoreApplication.translate("LogecC3", u"If 'N/A' shows up for temp, then your OS cannot read the CPU Temp, most likely due to a virtual machine", None))
#endif // QT_CONFIG(tooltip)
        self.label_14.setText(QCoreApplication.translate("LogecC3", u"System CPU Usage", None))
        self.label_84.setText(QCoreApplication.translate("LogecC3", u"Ping (MS)", None))
        self.label_85.setText(QCoreApplication.translate("LogecC3", u"SpeedTest", None))
        self.performance_seconds_5.setText(QCoreApplication.translate("LogecC3", u"6.16", None))
        self.label_121.setText(QCoreApplication.translate("LogecC3", u"Seconds", None))
        self.textEdit_29.setHtml(QCoreApplication.translate("LogecC3", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Cantarell'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Process List? (for i in process create a list in list widget, + a right click menu that can kill a process (maybe have this window be all processes, the other be python specific?</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.label_91.setText(QCoreApplication.translate("LogecC3", u"Benchmarks", None))
        self.checkBox_23.setText(QCoreApplication.translate("LogecC3", u"Count to 10 Million (Single Thread)", None))
        self.label_83.setText(QCoreApplication.translate("LogecC3", u"External IP:  123.456.111.333", None))
        self.label_82.setText(QCoreApplication.translate("LogecC3", u"Local IP: 123.456.444.222", None))
        self.performance_seconds.setText(QCoreApplication.translate("LogecC3", u"6.16", None))
        self.checkBox_24.setText(QCoreApplication.translate("LogecC3", u"Multi Thread", None))
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
        self.performance_speedtest.setText(QCoreApplication.translate("LogecC3", u"Run SpeedTest", None))
        self.performance_benchmark_button.setText(QCoreApplication.translate("LogecC3", u"Start Benchmark", None))
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
        self.label_81.setText(QCoreApplication.translate("LogecC3", u"Network Traffic In/Out", None))
        self.tabWidget_10.setTabText(self.tabWidget_10.indexOf(self.tab_52), QCoreApplication.translate("LogecC3", u"Performance and Diagnostics", None))
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
        self.label_6.setText(QCoreApplication.translate("LogecC3", u"General", None))
        self.other_content_usernames_layout_general_button_placeholder.setText(QCoreApplication.translate("LogecC3", u"Download", None))
        self.other_content_usernames_layout_general_placeholder.setText(QCoreApplication.translate("LogecC3", u"Placeholder - if u see me then I screwed up my code :) consider it an easter egg", None))
        self.label_9.setText(QCoreApplication.translate("LogecC3", u"Default Usernames", None))
        self.other_content_usernames_layout_default_placeholder.setText(QCoreApplication.translate("LogecC3", u"Placeholder - if u see me then I screwed up my code :) consider it an easter egg", None))
        self.other_content_usernames_layout_default_button_placeholder.setText(QCoreApplication.translate("LogecC3", u"Download", None))
        self.label_8.setText(QCoreApplication.translate("LogecC3", u"Other", None))
        self.other_content_usernames_layout_other_placeholder.setText(QCoreApplication.translate("LogecC3", u"Placeholder - if u see me then I screwed up my code :) consider it an easter egg", None))
        self.other_content_usernames_layout_other_button_placeholder.setText(QCoreApplication.translate("LogecC3", u"Download", None))
        self.tabWidget_5.setTabText(self.tabWidget_5.indexOf(self.tab_8), QCoreApplication.translate("LogecC3", u"Usernames", None))
        self.other_content_password_layout_SecList_placeholder_button.setText(QCoreApplication.translate("LogecC3", u"Download", None))
        self.other_content_password_layout_SecList_placeholder.setText(QCoreApplication.translate("LogecC3", u"Placeholder - if u see me then I screwed up my code :) consider it an easter egg", None))
        self.label_18.setText(QCoreApplication.translate("LogecC3", u"Other/Fun", None))
        self.other_content_password_layout_WeakPasswords_placeholder_button.setText(QCoreApplication.translate("LogecC3", u"Download", None))
        self.label_19.setText(QCoreApplication.translate("LogecC3", u"Weak Passwords", None))
        self.other_content_password_layout_WeakPasswords_placeholder.setText(QCoreApplication.translate("LogecC3", u"SecList Default Passwords", None))
        self.other_content_password_layout_DefaultPasswords_placeholder_button.setText(QCoreApplication.translate("LogecC3", u"Download", None))
        self.label_32.setText(QCoreApplication.translate("LogecC3", u"Default Passwords", None))
        self.other_content_password_layout_DefaultPasswords_placeholder.setText(QCoreApplication.translate("LogecC3", u"SecList Default Passwords", None))
        self.label_44.setText(QCoreApplication.translate("LogecC3", u"Leaked Passwords", None))
        self.other_content_password_layout_LeakedPasswords_placeholder.setText(QCoreApplication.translate("LogecC3", u"SecList Default Passwords", None))
        self.other_content_password_layout_LeakedPasswords_placeholder_button.setText(QCoreApplication.translate("LogecC3", u"Download", None))
        self.tabWidget_5.setTabText(self.tabWidget_5.indexOf(self.tab_10), QCoreApplication.translate("LogecC3", u"Passwords", None))
        self.label_2.setText(QCoreApplication.translate("LogecC3", u"General", None))
        self.other_content_directory_layout_general_placeholder.setText(QCoreApplication.translate("LogecC3", u"SecList Top 10 Million Passwords", None))
        self.other_content_directory_layout_general_button_placeholder.setText(QCoreApplication.translate("LogecC3", u"Download", None))
        self.other_content_directory_layout_commonURL_placeholder.setText(QCoreApplication.translate("LogecC3", u"SecList Top 10 Million Passwords", None))
        self.other_content_directory_layout_commonURL_button_placeholder.setText(QCoreApplication.translate("LogecC3", u"Download", None))
        self.label_4.setText(QCoreApplication.translate("LogecC3", u"Common URL/I", None))
        self.other_content_directory_layout_application_button_placeholder.setText(QCoreApplication.translate("LogecC3", u"Download", None))
        self.other_content_directory_layout_application_placeholder.setText(QCoreApplication.translate("LogecC3", u"SecList Top 10 Million Passwords", None))
        self.label_3.setText(QCoreApplication.translate("LogecC3", u"Applications", None))
        self.other_content_directory_layout_other_button_placeholder.setText(QCoreApplication.translate("LogecC3", u"Download", None))
        self.label_5.setText(QCoreApplication.translate("LogecC3", u"Other", None))
        self.other_content_directory_layout_other_placeholder.setText(QCoreApplication.translate("LogecC3", u"SecList Top 10 Million Passwords", None))
        self.tabWidget_5.setTabText(self.tabWidget_5.indexOf(self.tab_9), QCoreApplication.translate("LogecC3", u"Directory", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_7), QCoreApplication.translate("LogecC3", u"Wordlists", None))
        self.other_content_exploit_layou_exploitdb_placeholder_button.setText(QCoreApplication.translate("LogecC3", u"Download", None))
        self.other_content_exploit_layou_exploitdb_placeholder.setText(QCoreApplication.translate("LogecC3", u"Placeholder - if u see me then I screwed up my code :) consider it an easter egg", None))
        self.label_21.setText(QCoreApplication.translate("LogecC3", u"ExploitDB", None))
        self.other_content_directory_layout_WeakPasswords_placeholder_button_2.setText(QCoreApplication.translate("LogecC3", u"Download", None))
        self.label_22.setText(QCoreApplication.translate("LogecC3", u"Coming Later", None))
        self.other_content_directory_layout_WeakPasswords_placeholder_2.setText(QCoreApplication.translate("LogecC3", u"SecList Default Passwords", None))
        self.other_content_directory_layout_DefaultPasswords_placeholder_button_2.setText(QCoreApplication.translate("LogecC3", u"Download", None))
        self.label_34.setText(QCoreApplication.translate("LogecC3", u"Coming Later", None))
        self.other_content_directory_layout_DefaultPasswords_placeholder_2.setText(QCoreApplication.translate("LogecC3", u"SecList Default Passwords", None))
        self.label_45.setText(QCoreApplication.translate("LogecC3", u"Coming Later", None))
        self.other_content_directory_layout_LeakedPasswords_placeholder_2.setText(QCoreApplication.translate("LogecC3", u"SecList Default Passwords", None))
        self.other_content_directory_layout_LeakedPasswords_placeholder_button_2.setText(QCoreApplication.translate("LogecC3", u"Download", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_8), QCoreApplication.translate("LogecC3", u"Vulnerability Databases and Exploits", None))
        self.tabWidget_10.setTabText(self.tabWidget_10.indexOf(self.tab_7), QCoreApplication.translate("LogecC3", u"Content", None))
        self.main_tab_widget.setTabText(self.main_tab_widget.indexOf(self.tab_27), QCoreApplication.translate("LogecC3", u"Other", None))
        self.menuFile.setTitle(QCoreApplication.translate("LogecC3", u"File", None))
        self.menu_GettingStarted.setTitle(QCoreApplication.translate("LogecC3", u"Getting Started", None))
    # retranslateUi

