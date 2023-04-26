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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QCheckBox, QComboBox,
    QDoubleSpinBox, QFrame, QGraphicsView, QGridLayout,
    QGroupBox, QHBoxLayout, QHeaderView, QLCDNumber,
    QLabel, QLayout, QLineEdit, QMainWindow,
    QMenu, QMenuBar, QProgressBar, QPushButton,
    QRadioButton, QScrollArea, QSizePolicy, QSpinBox,
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
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setEnabled(True)
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setTabPosition(QTabWidget.North)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setMovable(True)
        self.tabWidget.setTabBarAutoHide(False)
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
        self.gridLayout_29 = QGridLayout(self.c2_gui_groupbox_options)
        self.gridLayout_29.setObjectName(u"gridLayout_29")
        self.bruteforce_panel_2 = QTabWidget(self.c2_gui_groupbox_options)
        self.bruteforce_panel_2.setObjectName(u"bruteforce_panel_2")
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

        self.tabWidget.addTab(self.c2_tab, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.gridLayout_5 = QGridLayout(self.tab_4)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.osint_reddit_tab = QTabWidget(self.tab_4)
        self.osint_reddit_tab.setObjectName(u"osint_reddit_tab")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.gridLayout_10 = QGridLayout(self.tab_2)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.groupBox_2 = QGroupBox(self.tab_2)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.gridLayout_2 = QGridLayout(self.groupBox_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.table_SQLDB_osint_reddit = QTableWidget(self.groupBox_2)
        self.table_SQLDB_osint_reddit.setObjectName(u"table_SQLDB_osint_reddit")
        self.table_SQLDB_osint_reddit.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.table_SQLDB_osint_reddit.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)

        self.gridLayout_2.addWidget(self.table_SQLDB_osint_reddit, 0, 0, 1, 2)

        self.DB_Query_osint_reddit = QLineEdit(self.groupBox_2)
        self.DB_Query_osint_reddit.setObjectName(u"DB_Query_osint_reddit")

        self.gridLayout_2.addWidget(self.DB_Query_osint_reddit, 1, 0, 1, 2)

        self.table_RefreshDB_Button_osint_reddit = QPushButton(self.groupBox_2)
        self.table_RefreshDB_Button_osint_reddit.setObjectName(u"table_RefreshDB_Button_osint_reddit")

        self.gridLayout_2.addWidget(self.table_RefreshDB_Button_osint_reddit, 2, 0, 1, 1)

        self.table_QueryDB_Button_osint_reddit = QPushButton(self.groupBox_2)
        self.table_QueryDB_Button_osint_reddit.setObjectName(u"table_QueryDB_Button_osint_reddit")

        self.gridLayout_2.addWidget(self.table_QueryDB_Button_osint_reddit, 2, 1, 1, 1)


        self.gridLayout_10.addWidget(self.groupBox_2, 0, 0, 1, 1)

        self.osint_reddit_searchbox = QGroupBox(self.tab_2)
        self.osint_reddit_searchbox.setObjectName(u"osint_reddit_searchbox")
        self.gridLayout_3 = QGridLayout(self.osint_reddit_searchbox)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_42 = QLabel(self.osint_reddit_searchbox)
        self.label_42.setObjectName(u"label_42")

        self.gridLayout_3.addWidget(self.label_42, 0, 0, 1, 1)

        self.label_20 = QLabel(self.osint_reddit_searchbox)
        self.label_20.setObjectName(u"label_20")

        self.gridLayout_3.addWidget(self.label_20, 0, 1, 1, 1)

        self.label_40 = QLabel(self.osint_reddit_searchbox)
        self.label_40.setObjectName(u"label_40")

        self.gridLayout_3.addWidget(self.label_40, 0, 2, 1, 1)

        self.label_33 = QLabel(self.osint_reddit_searchbox)
        self.label_33.setObjectName(u"label_33")

        self.gridLayout_3.addWidget(self.label_33, 0, 3, 1, 1)

        self.osint_reddit_keyword = QLineEdit(self.osint_reddit_searchbox)
        self.osint_reddit_keyword.setObjectName(u"osint_reddit_keyword")

        self.gridLayout_3.addWidget(self.osint_reddit_keyword, 1, 0, 1, 1)

        self.combo_sort = QComboBox(self.osint_reddit_searchbox)
        self.combo_sort.addItem("")
        self.combo_sort.addItem("")
        self.combo_sort.addItem("")
        self.combo_sort.addItem("")
        self.combo_sort.addItem("")
        self.combo_sort.setObjectName(u"combo_sort")

        self.gridLayout_3.addWidget(self.combo_sort, 1, 1, 1, 1)

        self.osint_reddit_onlypost = QRadioButton(self.osint_reddit_searchbox)
        self.osint_reddit_onlypost.setObjectName(u"osint_reddit_onlypost")
        self.osint_reddit_onlypost.setChecked(True)

        self.gridLayout_3.addWidget(self.osint_reddit_onlypost, 1, 2, 1, 1)

        self.osint_reddit_hideNSFW = QCheckBox(self.osint_reddit_searchbox)
        self.osint_reddit_hideNSFW.setObjectName(u"osint_reddit_hideNSFW")

        self.gridLayout_3.addWidget(self.osint_reddit_hideNSFW, 1, 3, 1, 1)

        self.line_10 = QFrame(self.osint_reddit_searchbox)
        self.line_10.setObjectName(u"line_10")
        self.line_10.setFrameShape(QFrame.HLine)
        self.line_10.setFrameShadow(QFrame.Sunken)

        self.gridLayout_3.addWidget(self.line_10, 2, 0, 1, 1)

        self.label_41 = QLabel(self.osint_reddit_searchbox)
        self.label_41.setObjectName(u"label_41")

        self.gridLayout_3.addWidget(self.label_41, 3, 0, 1, 1)

        self.label_43 = QLabel(self.osint_reddit_searchbox)
        self.label_43.setObjectName(u"label_43")

        self.gridLayout_3.addWidget(self.label_43, 3, 1, 1, 1)

        self.osint_reddit_onlycomments = QRadioButton(self.osint_reddit_searchbox)
        self.osint_reddit_onlycomments.setObjectName(u"osint_reddit_onlycomments")

        self.gridLayout_3.addWidget(self.osint_reddit_onlycomments, 3, 2, 1, 1)

        self.osint_reddit_downloadmedia = QCheckBox(self.osint_reddit_searchbox)
        self.osint_reddit_downloadmedia.setObjectName(u"osint_reddit_downloadmedia")
        self.osint_reddit_downloadmedia.setChecked(True)

        self.gridLayout_3.addWidget(self.osint_reddit_downloadmedia, 3, 3, 2, 1)

        self.osint_reddit_searchurl = QLineEdit(self.osint_reddit_searchbox)
        self.osint_reddit_searchurl.setObjectName(u"osint_reddit_searchurl")
        self.osint_reddit_searchurl.setReadOnly(True)

        self.gridLayout_3.addWidget(self.osint_reddit_searchurl, 4, 0, 1, 1)

        self.combo_time = QComboBox(self.osint_reddit_searchbox)
        self.combo_time.addItem("")
        self.combo_time.addItem("")
        self.combo_time.addItem("")
        self.combo_time.addItem("")
        self.combo_time.addItem("")
        self.combo_time.setObjectName(u"combo_time")

        self.gridLayout_3.addWidget(self.combo_time, 4, 1, 1, 1)

        self.osint_reddit_onlysubreddit = QRadioButton(self.osint_reddit_searchbox)
        self.osint_reddit_onlysubreddit.setObjectName(u"osint_reddit_onlysubreddit")

        self.gridLayout_3.addWidget(self.osint_reddit_onlysubreddit, 4, 2, 1, 1)

        self.label_39 = QLabel(self.osint_reddit_searchbox)
        self.label_39.setObjectName(u"label_39")

        self.gridLayout_3.addWidget(self.label_39, 5, 0, 1, 1)

        self.osint_reddit_onlyprofile = QRadioButton(self.osint_reddit_searchbox)
        self.osint_reddit_onlyprofile.setObjectName(u"osint_reddit_onlyprofile")

        self.gridLayout_3.addWidget(self.osint_reddit_onlyprofile, 5, 2, 1, 1)

        self.checkBox_29 = QCheckBox(self.osint_reddit_searchbox)
        self.checkBox_29.setObjectName(u"checkBox_29")
        self.checkBox_29.setChecked(False)
        self.checkBox_29.setTristate(False)

        self.gridLayout_3.addWidget(self.checkBox_29, 5, 3, 1, 1)

        self.osint_reddit_search = QPushButton(self.osint_reddit_searchbox)
        self.osint_reddit_search.setObjectName(u"osint_reddit_search")

        self.gridLayout_3.addWidget(self.osint_reddit_search, 6, 1, 1, 3)


        self.gridLayout_10.addWidget(self.osint_reddit_searchbox, 1, 0, 1, 1)

        self.osint_reddit_gui_hide_search = QCheckBox(self.tab_2)
        self.osint_reddit_gui_hide_search.setObjectName(u"osint_reddit_gui_hide_search")

        self.gridLayout_10.addWidget(self.osint_reddit_gui_hide_search, 2, 0, 1, 1)

        self.osint_reddit_tab.addTab(self.tab_2, "")

        self.gridLayout_5.addWidget(self.osint_reddit_tab, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab_4, "")
        self.tab_22 = QWidget()
        self.tab_22.setObjectName(u"tab_22")
        self.gridLayout_17 = QGridLayout(self.tab_22)
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.tabWidget_8 = QTabWidget(self.tab_22)
        self.tabWidget_8.setObjectName(u"tabWidget_8")
        self.tab_63 = QWidget()
        self.tab_63.setObjectName(u"tab_63")
        self.gridLayout_47 = QGridLayout(self.tab_63)
        self.gridLayout_47.setObjectName(u"gridLayout_47")
        self.scrollArea_5 = QScrollArea(self.tab_63)
        self.scrollArea_5.setObjectName(u"scrollArea_5")
        self.scrollArea_5.setWidgetResizable(True)
        self.scrollAreaWidgetContents_5 = QWidget()
        self.scrollAreaWidgetContents_5.setObjectName(u"scrollAreaWidgetContents_5")
        self.scrollAreaWidgetContents_5.setGeometry(QRect(0, 0, 1515, 742))
        self.bashbuild_toolBox = QToolBox(self.scrollAreaWidgetContents_5)
        self.bashbuild_toolBox.setObjectName(u"bashbuild_toolBox")
        self.bashbuild_toolBox.setGeometry(QRect(0, 0, 241, 651))
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.page_4.setGeometry(QRect(0, 0, 92, 78))
        self.gridLayout_48 = QGridLayout(self.page_4)
        self.gridLayout_48.setObjectName(u"gridLayout_48")
        self.textEdit_24 = QTextEdit(self.page_4)
        self.textEdit_24.setObjectName(u"textEdit_24")

        self.gridLayout_48.addWidget(self.textEdit_24, 0, 0, 1, 1)

        self.bashbuild_toolBox.addItem(self.page_4, u"Quick Guide")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.page.setGeometry(QRect(0, 0, 100, 30))
        self.bashbuild_dnsenum = QCheckBox(self.page)
        self.bashbuild_dnsenum.setObjectName(u"bashbuild_dnsenum")
        self.bashbuild_dnsenum.setGeometry(QRect(10, 0, 92, 25))
        self.bashbuild_toolBox.addItem(self.page, u"DNS")
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.page_3.setGeometry(QRect(0, 0, 100, 30))
        self.bashbuild_nmap = QCheckBox(self.page_3)
        self.bashbuild_nmap.setObjectName(u"bashbuild_nmap")
        self.bashbuild_nmap.setGeometry(QRect(10, 20, 92, 25))
        self.bashbuild_toolBox.addItem(self.page_3, u"PortScan")
        self.page_6 = QWidget()
        self.page_6.setObjectName(u"page_6")
        self.page_6.setGeometry(QRect(0, 0, 241, 453))
        self.checkBox_25 = QCheckBox(self.page_6)
        self.checkBox_25.setObjectName(u"checkBox_25")
        self.checkBox_25.setGeometry(QRect(10, 10, 181, 25))
        self.checkBox_26 = QCheckBox(self.page_6)
        self.checkBox_26.setObjectName(u"checkBox_26")
        self.checkBox_26.setGeometry(QRect(10, 40, 181, 25))
        self.checkBox_27 = QCheckBox(self.page_6)
        self.checkBox_27.setObjectName(u"checkBox_27")
        self.checkBox_27.setGeometry(QRect(10, 70, 181, 25))
        self.checkBox_28 = QCheckBox(self.page_6)
        self.checkBox_28.setObjectName(u"checkBox_28")
        self.checkBox_28.setGeometry(QRect(10, 100, 181, 25))
        self.bashbuild_toolBox.addItem(self.page_6, u"Local")
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.page_2.setGeometry(QRect(0, 0, 100, 30))
        self.bashbuild_diagnostic = QCheckBox(self.page_2)
        self.bashbuild_diagnostic.setObjectName(u"bashbuild_diagnostic")
        self.bashbuild_diagnostic.setGeometry(QRect(10, 10, 201, 25))
        self.bashbuild_diagnostic.setChecked(True)
        self.bashbuild_installpackages = QCheckBox(self.page_2)
        self.bashbuild_installpackages.setObjectName(u"bashbuild_installpackages")
        self.bashbuild_installpackages.setGeometry(QRect(10, 40, 211, 25))
        self.bashbuild_installpackages.setChecked(True)
        self.bashbuild_toolBox.addItem(self.page_2, u"Other")
        self.page_5 = QWidget()
        self.page_5.setObjectName(u"page_5")
        self.page_5.setGeometry(QRect(0, 0, 92, 78))
        self.gridLayout_49 = QGridLayout(self.page_5)
        self.gridLayout_49.setObjectName(u"gridLayout_49")
        self.textEdit_26 = QTextEdit(self.page_5)
        self.textEdit_26.setObjectName(u"textEdit_26")

        self.gridLayout_49.addWidget(self.textEdit_26, 0, 0, 1, 1)

        self.bashbuild_toolBox.addItem(self.page_5, u"Overview")
        self.bashbuild_textoutput = QTextEdit(self.scrollAreaWidgetContents_5)
        self.bashbuild_textoutput.setObjectName(u"bashbuild_textoutput")
        self.bashbuild_textoutput.setGeometry(QRect(240, 10, 1031, 601))
        self.bashbuilder_generate = QPushButton(self.scrollAreaWidgetContents_5)
        self.bashbuilder_generate.setObjectName(u"bashbuilder_generate")
        self.bashbuilder_generate.setGeometry(QRect(780, 620, 491, 27))
        self.pushButton_3 = QPushButton(self.scrollAreaWidgetContents_5)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(240, 620, 261, 27))
        self.pushButton_4 = QPushButton(self.scrollAreaWidgetContents_5)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(510, 620, 261, 27))
        self.scrollArea_5.setWidget(self.scrollAreaWidgetContents_5)

        self.gridLayout_47.addWidget(self.scrollArea_5, 0, 0, 1, 1)

        self.tabWidget_8.addTab(self.tab_63, "")
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
        self.stealth_bar.setValue(0)

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
        font3 = QFont()
        font3.setPointSize(10)
        font3.setUnderline(False)
        self.label_30.setFont(font3)

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
        self.label_28.setFont(font3)

        self.gridLayout_13.addWidget(self.label_28, 4, 0, 1, 1)

        self.dns_Reverse_table = QTableWidget(self.tab_16)
        self.dns_Reverse_table.setObjectName(u"dns_Reverse_table")

        self.gridLayout_13.addWidget(self.dns_Reverse_table, 9, 0, 1, 1)

        self.scanning_dns_lookup = QPushButton(self.tab_16)
        self.scanning_dns_lookup.setObjectName(u"scanning_dns_lookup")

        self.gridLayout_13.addWidget(self.scanning_dns_lookup, 1, 1, 1, 1)

        self.label_29 = QLabel(self.tab_16)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setFont(font3)

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
        self.label_31.setFont(font3)

        self.gridLayout_13.addWidget(self.label_31, 8, 0, 1, 1)

        self.dns_a_table = QTableWidget(self.tab_16)
        self.dns_a_table.setObjectName(u"dns_a_table")

        self.gridLayout_13.addWidget(self.dns_a_table, 3, 0, 1, 1)

        self.label_26 = QLabel(self.tab_16)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setMaximumSize(QSize(16777215, 15))
        self.label_26.setFont(font3)

        self.gridLayout_13.addWidget(self.label_26, 2, 0, 1, 1)

        self.label_27 = QLabel(self.tab_16)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setFont(font3)

        self.gridLayout_13.addWidget(self.label_27, 2, 1, 1, 1)

        self.dns_NS_table = QTableWidget(self.tab_16)
        self.dns_NS_table.setObjectName(u"dns_NS_table")

        self.gridLayout_13.addWidget(self.dns_NS_table, 5, 1, 1, 1)

        self.scanning_dns_A_4 = QTextEdit(self.tab_16)
        self.scanning_dns_A_4.setObjectName(u"scanning_dns_A_4")

        self.gridLayout_13.addWidget(self.scanning_dns_A_4, 7, 1, 3, 1)

        self.label = QLabel(self.tab_16)
        self.label.setObjectName(u"label")

        self.gridLayout_13.addWidget(self.label, 6, 1, 1, 1)

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
        font4 = QFont()
        font4.setUnderline(False)
        font4.setStrikeOut(False)
        self.bruteforce_download_seclist_topshort.setFont(font4)
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
        font5 = QFont()
        font5.setBold(True)
        font5.setUnderline(True)
        self.label_74.setFont(font5)

        self.gridLayout_37.addWidget(self.label_74, 1, 0, 1, 1)

        self.lineEdit_20 = QLineEdit(self.tab_44)
        self.lineEdit_20.setObjectName(u"lineEdit_20")

        self.gridLayout_37.addWidget(self.lineEdit_20, 4, 2, 1, 1)

        self.bruteforce_download_seclist_top10mil_usernames = QPushButton(self.tab_44)
        self.bruteforce_download_seclist_top10mil_usernames.setObjectName(u"bruteforce_download_seclist_top10mil_usernames")
        self.bruteforce_download_seclist_top10mil_usernames.setFont(font4)
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
        self.label_73.setFont(font5)

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
        self.DB_Query_scanning_bruteforce_fuzzer = QLineEdit(self.tab_127)
        self.DB_Query_scanning_bruteforce_fuzzer.setObjectName(u"DB_Query_scanning_bruteforce_fuzzer")

        self.gridLayout_93.addWidget(self.DB_Query_scanning_bruteforce_fuzzer, 1, 0, 1, 2)

        self.scanning_bruteforce_fuzzer_refresh = QPushButton(self.tab_127)
        self.scanning_bruteforce_fuzzer_refresh.setObjectName(u"scanning_bruteforce_fuzzer_refresh")

        self.gridLayout_93.addWidget(self.scanning_bruteforce_fuzzer_refresh, 2, 0, 1, 1)

        self.scanning_bruteforce_fuzzer_db = QTableWidget(self.tab_127)
        self.scanning_bruteforce_fuzzer_db.setObjectName(u"scanning_bruteforce_fuzzer_db")

        self.gridLayout_93.addWidget(self.scanning_bruteforce_fuzzer_db, 0, 0, 1, 2)

        self.scanning_bruteforce_fuzzer_query = QPushButton(self.tab_127)
        self.scanning_bruteforce_fuzzer_query.setObjectName(u"scanning_bruteforce_fuzzer_query")

        self.gridLayout_93.addWidget(self.scanning_bruteforce_fuzzer_query, 2, 1, 1, 1)

        self.tabWidget_29.addTab(self.tab_127, "")
        self.tab_128 = QWidget()
        self.tab_128.setObjectName(u"tab_128")
        self.gridLayout_94 = QGridLayout(self.tab_128)
        self.gridLayout_94.setObjectName(u"gridLayout_94")
        self.label_167 = QLabel(self.tab_128)
        self.label_167.setObjectName(u"label_167")
        self.label_167.setMaximumSize(QSize(16777215, 15))
        self.label_167.setFont(font5)

        self.gridLayout_94.addWidget(self.label_167, 0, 0, 1, 1)

        self.label_166 = QLabel(self.tab_128)
        self.label_166.setObjectName(u"label_166")
        self.label_166.setFont(font5)

        self.gridLayout_94.addWidget(self.label_166, 0, 2, 1, 1)

        self.lineEdit_56 = QLineEdit(self.tab_128)
        self.lineEdit_56.setObjectName(u"lineEdit_56")

        self.gridLayout_94.addWidget(self.lineEdit_56, 1, 0, 1, 1)

        self.bruteforce_download_seclist_top10mil_usernames_4 = QPushButton(self.tab_128)
        self.bruteforce_download_seclist_top10mil_usernames_4.setObjectName(u"bruteforce_download_seclist_top10mil_usernames_4")
        self.bruteforce_download_seclist_top10mil_usernames_4.setFont(font4)
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
        self.bruteforce_download_seclist_topshort_4.setFont(font4)
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
        font6 = QFont()
        font6.setUnderline(True)
        self.label_75.setFont(font6)
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
        self.bruteforce_download_seclist_top10mil_usernames_5.setFont(font4)
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
        font7 = QFont()
        font7.setPointSize(6)
        font7.setUnderline(False)
        self.label_77.setFont(font7)
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
        self.tab_37 = QWidget()
        self.tab_37.setObjectName(u"tab_37")
        self.gridLayout_28 = QGridLayout(self.tab_37)
        self.gridLayout_28.setObjectName(u"gridLayout_28")
        self.settings_edit = QTextEdit(self.tab_37)
        self.settings_edit.setObjectName(u"settings_edit")
        font8 = QFont()
        self.settings_edit.setFont(font8)

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

        self.tabWidget.addTab(self.tab_5, "")
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
        self.label_86.setFont(font6)

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
        self.page_7.setGeometry(QRect(0, 0, 1517, 678))
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
        self.gridLayout_67 = QGridLayout()
        self.gridLayout_67.setObjectName(u"gridLayout_67")
        self.lineEdit_88 = QLineEdit(self.tab_8)
        self.lineEdit_88.setObjectName(u"lineEdit_88")

        self.gridLayout_67.addWidget(self.lineEdit_88, 2, 0, 1, 1)

        self.lineEdit_89 = QLineEdit(self.tab_8)
        self.lineEdit_89.setObjectName(u"lineEdit_89")

        self.gridLayout_67.addWidget(self.lineEdit_89, 1, 0, 1, 1)

        self.lineEdit_90 = QLineEdit(self.tab_8)
        self.lineEdit_90.setObjectName(u"lineEdit_90")

        self.gridLayout_67.addWidget(self.lineEdit_90, 3, 0, 1, 1)

        self.bruteforce_download_seclist_top10mil_22 = QPushButton(self.tab_8)
        self.bruteforce_download_seclist_top10mil_22.setObjectName(u"bruteforce_download_seclist_top10mil_22")

        self.gridLayout_67.addWidget(self.bruteforce_download_seclist_top10mil_22, 3, 1, 1, 1)

        self.bruteforce_download_seclist_defaults_13 = QPushButton(self.tab_8)
        self.bruteforce_download_seclist_defaults_13.setObjectName(u"bruteforce_download_seclist_defaults_13")

        self.gridLayout_67.addWidget(self.bruteforce_download_seclist_defaults_13, 1, 1, 1, 1)

        self.bruteforce_download_seclist_top10mil_23 = QPushButton(self.tab_8)
        self.bruteforce_download_seclist_top10mil_23.setObjectName(u"bruteforce_download_seclist_top10mil_23")

        self.gridLayout_67.addWidget(self.bruteforce_download_seclist_top10mil_23, 2, 1, 1, 1)

        self.label_6 = QLabel(self.tab_8)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_67.addWidget(self.label_6, 0, 0, 1, 1)


        self.gridLayout_66.addLayout(self.gridLayout_67, 0, 0, 1, 1)

        self.gridLayout_68 = QGridLayout()
        self.gridLayout_68.setObjectName(u"gridLayout_68")
        self.lineEdit_91 = QLineEdit(self.tab_8)
        self.lineEdit_91.setObjectName(u"lineEdit_91")

        self.gridLayout_68.addWidget(self.lineEdit_91, 3, 0, 1, 1)

        self.bruteforce_download_seclist_top10mil_24 = QPushButton(self.tab_8)
        self.bruteforce_download_seclist_top10mil_24.setObjectName(u"bruteforce_download_seclist_top10mil_24")

        self.gridLayout_68.addWidget(self.bruteforce_download_seclist_top10mil_24, 3, 1, 1, 1)

        self.lineEdit_92 = QLineEdit(self.tab_8)
        self.lineEdit_92.setObjectName(u"lineEdit_92")

        self.gridLayout_68.addWidget(self.lineEdit_92, 1, 0, 1, 1)

        self.bruteforce_download_seclist_top10mil_25 = QPushButton(self.tab_8)
        self.bruteforce_download_seclist_top10mil_25.setObjectName(u"bruteforce_download_seclist_top10mil_25")

        self.gridLayout_68.addWidget(self.bruteforce_download_seclist_top10mil_25, 2, 1, 1, 1)

        self.bruteforce_download_seclist_defaults_14 = QPushButton(self.tab_8)
        self.bruteforce_download_seclist_defaults_14.setObjectName(u"bruteforce_download_seclist_defaults_14")

        self.gridLayout_68.addWidget(self.bruteforce_download_seclist_defaults_14, 1, 1, 1, 1)

        self.lineEdit_93 = QLineEdit(self.tab_8)
        self.lineEdit_93.setObjectName(u"lineEdit_93")

        self.gridLayout_68.addWidget(self.lineEdit_93, 2, 0, 1, 1)

        self.label_8 = QLabel(self.tab_8)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_68.addWidget(self.label_8, 0, 0, 1, 1)


        self.gridLayout_66.addLayout(self.gridLayout_68, 1, 0, 1, 1)

        self.gridLayout_69 = QGridLayout()
        self.gridLayout_69.setObjectName(u"gridLayout_69")
        self.lineEdit_94 = QLineEdit(self.tab_8)
        self.lineEdit_94.setObjectName(u"lineEdit_94")

        self.gridLayout_69.addWidget(self.lineEdit_94, 1, 0, 1, 1)

        self.bruteforce_download_seclist_top10mil_26 = QPushButton(self.tab_8)
        self.bruteforce_download_seclist_top10mil_26.setObjectName(u"bruteforce_download_seclist_top10mil_26")

        self.gridLayout_69.addWidget(self.bruteforce_download_seclist_top10mil_26, 3, 1, 1, 1)

        self.bruteforce_download_seclist_top10mil_27 = QPushButton(self.tab_8)
        self.bruteforce_download_seclist_top10mil_27.setObjectName(u"bruteforce_download_seclist_top10mil_27")

        self.gridLayout_69.addWidget(self.bruteforce_download_seclist_top10mil_27, 2, 1, 1, 1)

        self.lineEdit_95 = QLineEdit(self.tab_8)
        self.lineEdit_95.setObjectName(u"lineEdit_95")

        self.gridLayout_69.addWidget(self.lineEdit_95, 2, 0, 1, 1)

        self.bruteforce_download_seclist_defaults_15 = QPushButton(self.tab_8)
        self.bruteforce_download_seclist_defaults_15.setObjectName(u"bruteforce_download_seclist_defaults_15")

        self.gridLayout_69.addWidget(self.bruteforce_download_seclist_defaults_15, 1, 1, 1, 1)

        self.lineEdit_96 = QLineEdit(self.tab_8)
        self.lineEdit_96.setObjectName(u"lineEdit_96")

        self.gridLayout_69.addWidget(self.lineEdit_96, 3, 0, 1, 1)

        self.label_9 = QLabel(self.tab_8)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_69.addWidget(self.label_9, 0, 0, 1, 1)


        self.gridLayout_66.addLayout(self.gridLayout_69, 0, 1, 1, 1)

        self.gridLayout_70 = QGridLayout()
        self.gridLayout_70.setObjectName(u"gridLayout_70")
        self.bruteforce_download_seclist_defaults_16 = QPushButton(self.tab_8)
        self.bruteforce_download_seclist_defaults_16.setObjectName(u"bruteforce_download_seclist_defaults_16")

        self.gridLayout_70.addWidget(self.bruteforce_download_seclist_defaults_16, 1, 1, 1, 1)

        self.lineEdit_97 = QLineEdit(self.tab_8)
        self.lineEdit_97.setObjectName(u"lineEdit_97")

        self.gridLayout_70.addWidget(self.lineEdit_97, 2, 0, 1, 1)

        self.lineEdit_98 = QLineEdit(self.tab_8)
        self.lineEdit_98.setObjectName(u"lineEdit_98")

        self.gridLayout_70.addWidget(self.lineEdit_98, 3, 0, 1, 1)

        self.bruteforce_download_seclist_top10mil_28 = QPushButton(self.tab_8)
        self.bruteforce_download_seclist_top10mil_28.setObjectName(u"bruteforce_download_seclist_top10mil_28")

        self.gridLayout_70.addWidget(self.bruteforce_download_seclist_top10mil_28, 3, 1, 1, 1)

        self.bruteforce_download_seclist_top10mil_29 = QPushButton(self.tab_8)
        self.bruteforce_download_seclist_top10mil_29.setObjectName(u"bruteforce_download_seclist_top10mil_29")

        self.gridLayout_70.addWidget(self.bruteforce_download_seclist_top10mil_29, 2, 1, 1, 1)

        self.lineEdit_99 = QLineEdit(self.tab_8)
        self.lineEdit_99.setObjectName(u"lineEdit_99")

        self.gridLayout_70.addWidget(self.lineEdit_99, 1, 0, 1, 1)

        self.label_10 = QLabel(self.tab_8)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_70.addWidget(self.label_10, 0, 0, 1, 1)


        self.gridLayout_66.addLayout(self.gridLayout_70, 1, 1, 1, 1)


        self.gridLayout_58.addLayout(self.gridLayout_66, 0, 0, 1, 1)

        self.tabWidget_5.addTab(self.tab_8, "")
        self.tab_10 = QWidget()
        self.tab_10.setObjectName(u"tab_10")
        self.gridLayout_76 = QGridLayout(self.tab_10)
        self.gridLayout_76.setObjectName(u"gridLayout_76")
        self.gridLayout_71 = QGridLayout()
        self.gridLayout_71.setObjectName(u"gridLayout_71")
        self.other_content_directory_layout_SecList = QGridLayout()
        self.other_content_directory_layout_SecList.setObjectName(u"other_content_directory_layout_SecList")
        self.other_content_directory_layout_SecList_placeholder_button = QPushButton(self.tab_10)
        self.other_content_directory_layout_SecList_placeholder_button.setObjectName(u"other_content_directory_layout_SecList_placeholder_button")
        self.other_content_directory_layout_SecList_placeholder_button.setEnabled(False)

        self.other_content_directory_layout_SecList.addWidget(self.other_content_directory_layout_SecList_placeholder_button, 2, 1, 1, 1)

        self.other_content_directory_layout_SecList_placeholder = QLineEdit(self.tab_10)
        self.other_content_directory_layout_SecList_placeholder.setObjectName(u"other_content_directory_layout_SecList_placeholder")
        self.other_content_directory_layout_SecList_placeholder.setEnabled(False)

        self.other_content_directory_layout_SecList.addWidget(self.other_content_directory_layout_SecList_placeholder, 2, 0, 1, 1)

        self.label_18 = QLabel(self.tab_10)
        self.label_18.setObjectName(u"label_18")

        self.other_content_directory_layout_SecList.addWidget(self.label_18, 1, 0, 1, 1)


        self.gridLayout_71.addLayout(self.other_content_directory_layout_SecList, 0, 0, 1, 1)

        self.other_content_directory_layout_WeakPasswords = QGridLayout()
        self.other_content_directory_layout_WeakPasswords.setObjectName(u"other_content_directory_layout_WeakPasswords")
        self.other_content_directory_layout_WeakPasswords_placeholder_button = QPushButton(self.tab_10)
        self.other_content_directory_layout_WeakPasswords_placeholder_button.setObjectName(u"other_content_directory_layout_WeakPasswords_placeholder_button")
        self.other_content_directory_layout_WeakPasswords_placeholder_button.setEnabled(False)

        self.other_content_directory_layout_WeakPasswords.addWidget(self.other_content_directory_layout_WeakPasswords_placeholder_button, 1, 1, 1, 1)

        self.label_19 = QLabel(self.tab_10)
        self.label_19.setObjectName(u"label_19")

        self.other_content_directory_layout_WeakPasswords.addWidget(self.label_19, 0, 0, 1, 1)

        self.other_content_directory_layout_WeakPasswords_placeholder = QLineEdit(self.tab_10)
        self.other_content_directory_layout_WeakPasswords_placeholder.setObjectName(u"other_content_directory_layout_WeakPasswords_placeholder")
        self.other_content_directory_layout_WeakPasswords_placeholder.setEnabled(False)

        self.other_content_directory_layout_WeakPasswords.addWidget(self.other_content_directory_layout_WeakPasswords_placeholder, 1, 0, 1, 1)


        self.gridLayout_71.addLayout(self.other_content_directory_layout_WeakPasswords, 1, 0, 1, 1)

        self.other_content_directory_layout_DefaultPasswords = QGridLayout()
        self.other_content_directory_layout_DefaultPasswords.setObjectName(u"other_content_directory_layout_DefaultPasswords")
        self.other_content_directory_layout_DefaultPasswords_placeholder_button = QPushButton(self.tab_10)
        self.other_content_directory_layout_DefaultPasswords_placeholder_button.setObjectName(u"other_content_directory_layout_DefaultPasswords_placeholder_button")
        self.other_content_directory_layout_DefaultPasswords_placeholder_button.setEnabled(False)

        self.other_content_directory_layout_DefaultPasswords.addWidget(self.other_content_directory_layout_DefaultPasswords_placeholder_button, 1, 1, 1, 1)

        self.label_32 = QLabel(self.tab_10)
        self.label_32.setObjectName(u"label_32")

        self.other_content_directory_layout_DefaultPasswords.addWidget(self.label_32, 0, 0, 1, 1)

        self.other_content_directory_layout_DefaultPasswords_placeholder = QLineEdit(self.tab_10)
        self.other_content_directory_layout_DefaultPasswords_placeholder.setObjectName(u"other_content_directory_layout_DefaultPasswords_placeholder")
        self.other_content_directory_layout_DefaultPasswords_placeholder.setEnabled(False)

        self.other_content_directory_layout_DefaultPasswords.addWidget(self.other_content_directory_layout_DefaultPasswords_placeholder, 1, 0, 1, 1)


        self.gridLayout_71.addLayout(self.other_content_directory_layout_DefaultPasswords, 0, 1, 1, 1)

        self.other_content_directory_layout_LeakedPasswords = QGridLayout()
        self.other_content_directory_layout_LeakedPasswords.setObjectName(u"other_content_directory_layout_LeakedPasswords")
        self.label_44 = QLabel(self.tab_10)
        self.label_44.setObjectName(u"label_44")

        self.other_content_directory_layout_LeakedPasswords.addWidget(self.label_44, 0, 0, 1, 1)

        self.other_content_directory_layout_LeakedPasswords_placeholder = QLineEdit(self.tab_10)
        self.other_content_directory_layout_LeakedPasswords_placeholder.setObjectName(u"other_content_directory_layout_LeakedPasswords_placeholder")
        self.other_content_directory_layout_LeakedPasswords_placeholder.setEnabled(False)

        self.other_content_directory_layout_LeakedPasswords.addWidget(self.other_content_directory_layout_LeakedPasswords_placeholder, 1, 0, 1, 1)

        self.other_content_directory_layout_LeakedPasswords_placeholder_button = QPushButton(self.tab_10)
        self.other_content_directory_layout_LeakedPasswords_placeholder_button.setObjectName(u"other_content_directory_layout_LeakedPasswords_placeholder_button")
        self.other_content_directory_layout_LeakedPasswords_placeholder_button.setEnabled(False)

        self.other_content_directory_layout_LeakedPasswords.addWidget(self.other_content_directory_layout_LeakedPasswords_placeholder_button, 1, 1, 1, 1)


        self.gridLayout_71.addLayout(self.other_content_directory_layout_LeakedPasswords, 1, 1, 1, 1)


        self.gridLayout_76.addLayout(self.gridLayout_71, 0, 0, 1, 1)

        self.tabWidget_5.addTab(self.tab_10, "")
        self.tab_9 = QWidget()
        self.tab_9.setObjectName(u"tab_9")
        self.gridLayout_57 = QGridLayout(self.tab_9)
        self.gridLayout_57.setObjectName(u"gridLayout_57")
        self.gridLayout_59 = QGridLayout()
        self.gridLayout_59.setObjectName(u"gridLayout_59")
        self.gridLayout_60 = QGridLayout()
        self.gridLayout_60.setObjectName(u"gridLayout_60")
        self.lineEdit_75 = QLineEdit(self.tab_9)
        self.lineEdit_75.setObjectName(u"lineEdit_75")

        self.gridLayout_60.addWidget(self.lineEdit_75, 2, 0, 1, 1)

        self.lineEdit_73 = QLineEdit(self.tab_9)
        self.lineEdit_73.setObjectName(u"lineEdit_73")

        self.gridLayout_60.addWidget(self.lineEdit_73, 1, 0, 1, 1)

        self.lineEdit_74 = QLineEdit(self.tab_9)
        self.lineEdit_74.setObjectName(u"lineEdit_74")

        self.gridLayout_60.addWidget(self.lineEdit_74, 3, 0, 1, 1)

        self.bruteforce_download_seclist_top10mil_12 = QPushButton(self.tab_9)
        self.bruteforce_download_seclist_top10mil_12.setObjectName(u"bruteforce_download_seclist_top10mil_12")

        self.gridLayout_60.addWidget(self.bruteforce_download_seclist_top10mil_12, 3, 1, 1, 1)

        self.bruteforce_download_seclist_defaults_8 = QPushButton(self.tab_9)
        self.bruteforce_download_seclist_defaults_8.setObjectName(u"bruteforce_download_seclist_defaults_8")

        self.gridLayout_60.addWidget(self.bruteforce_download_seclist_defaults_8, 1, 1, 1, 1)

        self.bruteforce_download_seclist_top10mil_13 = QPushButton(self.tab_9)
        self.bruteforce_download_seclist_top10mil_13.setObjectName(u"bruteforce_download_seclist_top10mil_13")

        self.gridLayout_60.addWidget(self.bruteforce_download_seclist_top10mil_13, 2, 1, 1, 1)

        self.label_2 = QLabel(self.tab_9)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_60.addWidget(self.label_2, 0, 0, 1, 1)


        self.gridLayout_59.addLayout(self.gridLayout_60, 0, 0, 1, 1)

        self.gridLayout_63 = QGridLayout()
        self.gridLayout_63.setObjectName(u"gridLayout_63")
        self.lineEdit_80 = QLineEdit(self.tab_9)
        self.lineEdit_80.setObjectName(u"lineEdit_80")

        self.gridLayout_63.addWidget(self.lineEdit_80, 3, 0, 1, 1)

        self.bruteforce_download_seclist_top10mil_16 = QPushButton(self.tab_9)
        self.bruteforce_download_seclist_top10mil_16.setObjectName(u"bruteforce_download_seclist_top10mil_16")

        self.gridLayout_63.addWidget(self.bruteforce_download_seclist_top10mil_16, 3, 1, 1, 1)

        self.lineEdit_79 = QLineEdit(self.tab_9)
        self.lineEdit_79.setObjectName(u"lineEdit_79")

        self.gridLayout_63.addWidget(self.lineEdit_79, 1, 0, 1, 1)

        self.bruteforce_download_seclist_top10mil_17 = QPushButton(self.tab_9)
        self.bruteforce_download_seclist_top10mil_17.setObjectName(u"bruteforce_download_seclist_top10mil_17")

        self.gridLayout_63.addWidget(self.bruteforce_download_seclist_top10mil_17, 2, 1, 1, 1)

        self.bruteforce_download_seclist_defaults_10 = QPushButton(self.tab_9)
        self.bruteforce_download_seclist_defaults_10.setObjectName(u"bruteforce_download_seclist_defaults_10")

        self.gridLayout_63.addWidget(self.bruteforce_download_seclist_defaults_10, 1, 1, 1, 1)

        self.lineEdit_81 = QLineEdit(self.tab_9)
        self.lineEdit_81.setObjectName(u"lineEdit_81")

        self.gridLayout_63.addWidget(self.lineEdit_81, 2, 0, 1, 1)

        self.label_4 = QLabel(self.tab_9)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_63.addWidget(self.label_4, 0, 0, 1, 1)


        self.gridLayout_59.addLayout(self.gridLayout_63, 1, 0, 1, 1)

        self.gridLayout_64 = QGridLayout()
        self.gridLayout_64.setObjectName(u"gridLayout_64")
        self.lineEdit_82 = QLineEdit(self.tab_9)
        self.lineEdit_82.setObjectName(u"lineEdit_82")

        self.gridLayout_64.addWidget(self.lineEdit_82, 1, 0, 1, 1)

        self.bruteforce_download_seclist_top10mil_18 = QPushButton(self.tab_9)
        self.bruteforce_download_seclist_top10mil_18.setObjectName(u"bruteforce_download_seclist_top10mil_18")

        self.gridLayout_64.addWidget(self.bruteforce_download_seclist_top10mil_18, 3, 1, 1, 1)

        self.bruteforce_download_seclist_top10mil_19 = QPushButton(self.tab_9)
        self.bruteforce_download_seclist_top10mil_19.setObjectName(u"bruteforce_download_seclist_top10mil_19")

        self.gridLayout_64.addWidget(self.bruteforce_download_seclist_top10mil_19, 2, 1, 1, 1)

        self.lineEdit_84 = QLineEdit(self.tab_9)
        self.lineEdit_84.setObjectName(u"lineEdit_84")

        self.gridLayout_64.addWidget(self.lineEdit_84, 2, 0, 1, 1)

        self.bruteforce_download_seclist_defaults_11 = QPushButton(self.tab_9)
        self.bruteforce_download_seclist_defaults_11.setObjectName(u"bruteforce_download_seclist_defaults_11")

        self.gridLayout_64.addWidget(self.bruteforce_download_seclist_defaults_11, 1, 1, 1, 1)

        self.lineEdit_83 = QLineEdit(self.tab_9)
        self.lineEdit_83.setObjectName(u"lineEdit_83")

        self.gridLayout_64.addWidget(self.lineEdit_83, 3, 0, 1, 1)

        self.label_3 = QLabel(self.tab_9)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_64.addWidget(self.label_3, 0, 0, 1, 1)


        self.gridLayout_59.addLayout(self.gridLayout_64, 0, 1, 1, 1)

        self.gridLayout_65 = QGridLayout()
        self.gridLayout_65.setObjectName(u"gridLayout_65")
        self.bruteforce_download_seclist_defaults_12 = QPushButton(self.tab_9)
        self.bruteforce_download_seclist_defaults_12.setObjectName(u"bruteforce_download_seclist_defaults_12")

        self.gridLayout_65.addWidget(self.bruteforce_download_seclist_defaults_12, 1, 1, 1, 1)

        self.lineEdit_87 = QLineEdit(self.tab_9)
        self.lineEdit_87.setObjectName(u"lineEdit_87")

        self.gridLayout_65.addWidget(self.lineEdit_87, 2, 0, 1, 1)

        self.lineEdit_86 = QLineEdit(self.tab_9)
        self.lineEdit_86.setObjectName(u"lineEdit_86")

        self.gridLayout_65.addWidget(self.lineEdit_86, 3, 0, 1, 1)

        self.bruteforce_download_seclist_top10mil_20 = QPushButton(self.tab_9)
        self.bruteforce_download_seclist_top10mil_20.setObjectName(u"bruteforce_download_seclist_top10mil_20")

        self.gridLayout_65.addWidget(self.bruteforce_download_seclist_top10mil_20, 3, 1, 1, 1)

        self.bruteforce_download_seclist_top10mil_21 = QPushButton(self.tab_9)
        self.bruteforce_download_seclist_top10mil_21.setObjectName(u"bruteforce_download_seclist_top10mil_21")

        self.gridLayout_65.addWidget(self.bruteforce_download_seclist_top10mil_21, 2, 1, 1, 1)

        self.lineEdit_85 = QLineEdit(self.tab_9)
        self.lineEdit_85.setObjectName(u"lineEdit_85")

        self.gridLayout_65.addWidget(self.lineEdit_85, 1, 0, 1, 1)

        self.label_5 = QLabel(self.tab_9)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_65.addWidget(self.label_5, 0, 0, 1, 1)


        self.gridLayout_59.addLayout(self.gridLayout_65, 1, 1, 1, 1)


        self.gridLayout_57.addLayout(self.gridLayout_59, 0, 0, 1, 1)

        self.tabWidget_5.addTab(self.tab_9, "")

        self.gridLayout_53.addWidget(self.tabWidget_5, 0, 0, 1, 1)

        self.toolBox.addItem(self.page_7, u"Wordlists")
        self.page_8 = QWidget()
        self.page_8.setObjectName(u"page_8")
        self.page_8.setGeometry(QRect(0, 0, 100, 30))
        self.toolBox.addItem(self.page_8, u"Other - Not Yet Occupied")

        self.gridLayout_52.addWidget(self.toolBox, 0, 0, 1, 1)

        self.tabWidget_10.addTab(self.tab_7, "")

        self.gridLayout_25.addWidget(self.tabWidget_10, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab_27, "")

        self.gridLayout_4.addWidget(self.tabWidget, 0, 0, 1, 1)

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

        self.tabWidget.setCurrentIndex(0)
        self.bruteforce_panel_2.setCurrentIndex(2)
        self.c2_shell_tab.setCurrentIndex(0)
        self.osint_reddit_tab.setCurrentIndex(0)
        self.tabWidget_8.setCurrentIndex(0)
        self.bashbuild_toolBox.setCurrentIndex(3)
        self.tabWidget_9.setCurrentIndex(0)
        self.tabWidget_6.setCurrentIndex(1)
        self.bruteforce_panel.setCurrentIndex(0)
        self.tabWidget_14.setCurrentIndex(0)
        self.bruteforce_download_seclist_topshort.setDefault(False)
        self.bruteforce_download_seclist_top10mil_usernames.setDefault(False)
        self.bruteforce_fuzz_panel.setCurrentIndex(0)
        self.tabWidget_29.setCurrentIndex(1)
        self.bruteforce_download_seclist_top10mil_usernames_4.setDefault(False)
        self.bruteforce_download_seclist_topshort_4.setDefault(False)
        self.bruteforce_download_seclist_top10mil_usernames_5.setDefault(False)
        self.tabWidget_2.setCurrentIndex(0)
        self.tabWidget_10.setCurrentIndex(2)
        self.tabWidget_16.setCurrentIndex(0)
        self.tabWidget_11.setCurrentIndex(2)
        self.tabWidget_12.setCurrentIndex(1)
        self.tabWidget_15.setCurrentIndex(1)
        self.toolBox.setCurrentIndex(0)
        self.tabWidget_5.setCurrentIndex(1)


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
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.c2_tab), QCoreApplication.translate("LogecC3", u"C2", None))
        self.groupBox_2.setTitle("")
        self.DB_Query_osint_reddit.setPlaceholderText(QCoreApplication.translate("LogecC3", u"SELECT * FROM RedditResults", None))
#if QT_CONFIG(tooltip)
        self.table_RefreshDB_Button_osint_reddit.setToolTip(QCoreApplication.translate("LogecC3", u"Refresh the Database, updating values from the SQLITE DB file", None))
#endif // QT_CONFIG(tooltip)
        self.table_RefreshDB_Button_osint_reddit.setText(QCoreApplication.translate("LogecC3", u"-->> Refresh DB <<--", None))
#if QT_CONFIG(tooltip)
        self.table_QueryDB_Button_osint_reddit.setToolTip(QCoreApplication.translate("LogecC3", u"Run a query on the DB", None))
#endif // QT_CONFIG(tooltip)
        self.table_QueryDB_Button_osint_reddit.setText(QCoreApplication.translate("LogecC3", u"-->> Query DB <<--", None))
        self.osint_reddit_searchbox.setTitle(QCoreApplication.translate("LogecC3", u"Search", None))
        self.label_42.setText(QCoreApplication.translate("LogecC3", u"Search  Term*", None))
        self.label_20.setText(QCoreApplication.translate("LogecC3", u"SortBy", None))
        self.label_40.setText(QCoreApplication.translate("LogecC3", u"Search for...", None))
        self.label_33.setText(QCoreApplication.translate("LogecC3", u"Other", None))
        self.osint_reddit_keyword.setPlaceholderText(QCoreApplication.translate("LogecC3", u"Windows", None))
        self.combo_sort.setItemText(0, QCoreApplication.translate("LogecC3", u"Hot", None))
        self.combo_sort.setItemText(1, QCoreApplication.translate("LogecC3", u"Top", None))
        self.combo_sort.setItemText(2, QCoreApplication.translate("LogecC3", u"New", None))
        self.combo_sort.setItemText(3, QCoreApplication.translate("LogecC3", u"Controversial", None))
        self.combo_sort.setItemText(4, QCoreApplication.translate("LogecC3", u"Comments", None))

        self.osint_reddit_onlypost.setText(QCoreApplication.translate("LogecC3", u"Posts", None))
        self.osint_reddit_hideNSFW.setText(QCoreApplication.translate("LogecC3", u"Hide NSFW", None))
        self.label_41.setText(QCoreApplication.translate("LogecC3", u"SearchURL", None))
        self.label_43.setText(QCoreApplication.translate("LogecC3", u"Time", None))
        self.osint_reddit_onlycomments.setText(QCoreApplication.translate("LogecC3", u"Comments", None))
#if QT_CONFIG(tooltip)
        self.osint_reddit_downloadmedia.setToolTip(QCoreApplication.translate("LogecC3", u"Download Images/Videos associated with the posts searched", None))
#endif // QT_CONFIG(tooltip)
        self.osint_reddit_downloadmedia.setText(QCoreApplication.translate("LogecC3", u"Download Media", None))
        self.combo_time.setItemText(0, QCoreApplication.translate("LogecC3", u"All", None))
        self.combo_time.setItemText(1, QCoreApplication.translate("LogecC3", u"Year", None))
        self.combo_time.setItemText(2, QCoreApplication.translate("LogecC3", u"Month", None))
        self.combo_time.setItemText(3, QCoreApplication.translate("LogecC3", u"Day", None))
        self.combo_time.setItemText(4, QCoreApplication.translate("LogecC3", u"Hour", None))

        self.osint_reddit_onlysubreddit.setText(QCoreApplication.translate("LogecC3", u"Subreddits", None))
        self.label_39.setText(QCoreApplication.translate("LogecC3", u"Items Found:", None))
        self.osint_reddit_onlyprofile.setText(QCoreApplication.translate("LogecC3", u"Profiles", None))
#if QT_CONFIG(tooltip)
        self.checkBox_29.setToolTip(QCoreApplication.translate("LogecC3", u"Add/append results to previous results", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.checkBox_29.setStatusTip("")
#endif // QT_CONFIG(statustip)
        self.checkBox_29.setText(QCoreApplication.translate("LogecC3", u"Append Results to DB", None))
        self.osint_reddit_search.setText(QCoreApplication.translate("LogecC3", u"-->> Search <<--", None))
        self.osint_reddit_gui_hide_search.setText(QCoreApplication.translate("LogecC3", u"Hide Search", None))
        self.osint_reddit_tab.setTabText(self.osint_reddit_tab.indexOf(self.tab_2), QCoreApplication.translate("LogecC3", u"Reddit Query", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QCoreApplication.translate("LogecC3", u"Osint", None))
        self.textEdit_24.setHtml(QCoreApplication.translate("LogecC3", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Cantarell'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Hey there!</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">This is a quick bash script builder, if you can click a button, you can build a script</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\""
                        " margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Each &quot;tab&quot; below this tab has a category, such as DNS, or Portscanning. Within each tab is a range of options for items related to that tab. Hit generate once you've selected the options you want, and tada a bash script customzied to what you need!</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Note, you'll enter your target IP &amp;Report name when you run the script, this allows for more flexibility that hardcoding it in </p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; m"
                        "argin-right:0px; -qt-block-indent:0; text-indent:0px;\">DevNote, set tabname to each selected, OR have a final overview tab that shows all selected stuff (put it in a list or something)</p></body></html>", None))
        self.bashbuild_toolBox.setItemText(self.bashbuild_toolBox.indexOf(self.page_4), QCoreApplication.translate("LogecC3", u"Quick Guide", None))
        self.bashbuild_dnsenum.setText(QCoreApplication.translate("LogecC3", u"DNSENUM", None))
        self.bashbuild_toolBox.setItemText(self.bashbuild_toolBox.indexOf(self.page), QCoreApplication.translate("LogecC3", u"DNS", None))
        self.bashbuild_nmap.setText(QCoreApplication.translate("LogecC3", u"NMAP", None))
        self.bashbuild_toolBox.setItemText(self.bashbuild_toolBox.indexOf(self.page_3), QCoreApplication.translate("LogecC3", u"PortScan", None))
        self.checkBox_25.setText(QCoreApplication.translate("LogecC3", u"Retrieve PASSWD file", None))
        self.checkBox_26.setText(QCoreApplication.translate("LogecC3", u"Retrieve SHADOW file", None))
        self.checkBox_27.setText(QCoreApplication.translate("LogecC3", u"Capture NETSTAT", None))
        self.checkBox_28.setText(QCoreApplication.translate("LogecC3", u"Capture Bash History", None))
        self.bashbuild_toolBox.setItemText(self.bashbuild_toolBox.indexOf(self.page_6), QCoreApplication.translate("LogecC3", u"Local", None))
        self.bashbuild_diagnostic.setText(QCoreApplication.translate("LogecC3", u"Enable Diagnostic Data", None))
#if QT_CONFIG(tooltip)
        self.bashbuild_installpackages.setToolTip(QCoreApplication.translate("LogecC3", u"Includes code to install packages. use --install when running the script", None))
#endif // QT_CONFIG(tooltip)
        self.bashbuild_installpackages.setText(QCoreApplication.translate("LogecC3", u"Install packages", None))
        self.bashbuild_toolBox.setItemText(self.bashbuild_toolBox.indexOf(self.page_2), QCoreApplication.translate("LogecC3", u"Other", None))
        self.textEdit_26.setHtml(QCoreApplication.translate("LogecC3", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Cantarell'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">PortScan:</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">	NMAP: On (turn green)</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">DNS:</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; "
                        "text-indent:0px;\">	DNSENUM: Off (turn red)</p></body></html>", None))
        self.bashbuild_toolBox.setItemText(self.bashbuild_toolBox.indexOf(self.page_5), QCoreApplication.translate("LogecC3", u"Overview", None))
        self.bashbuild_textoutput.setHtml(QCoreApplication.translate("LogecC3", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Cantarell'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">## Colors</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">RED=&quot;\\033[0;31m&quot;</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">BLUE=&quot;\\033[0;34m&quot;</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:"
                        "0px;\"><span style=\" font-size:10pt;\">GREEN=&quot;\\033[0;32m&quot;</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">YELLOW=&quot;\\033[0;33m&quot;</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">PURPLE=&quot;\\033[0;35m&quot;</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">GREY=&quot;\\033[0;37m&quot;</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">NC=&quot;\\033[0m&quot;</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10p"
                        "t;\">UNDERLINE=&quot;\\033[4m&quot;</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">NU=&quot;\\033[0m&quot;</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">printf &quot;${RED}Generated ${GREY}by ${BLUE}Logec-Suite${NC} &quot;</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">printf &quot;Enter a name for this"
                        " report and hit enter: &quot;</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">read NAME</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">printf &quot;Enter Target IP/FQDN and hit enter: &quot;</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">read IP</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px"
                        "; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">while [ $# -gt 0 ]; do</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">  case &quot;$1&quot; in</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">    --nmap-all)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">      nmap_all=true</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">      ;;</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style"
                        "=\" font-size:10pt;\">    --nmap-fast)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">      nmap_fast=true</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">      ;;</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">    --install)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">      install=true</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">      ;;</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin"
                        "-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">    *)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">      echo &quot;Unknown option: $1&quot;</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">      exit 1</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">      ;;</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">  esac</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\"> "
                        " shift</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">done</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">## Init Vars</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0p"
                        "x;\"><span style=\" font-size:10pt;\">## Current Dir</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">CURRENT_DIR_RAW=$(pwd)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">CURRENT_DIR=&quot;${CURRENT_DIR_RAW}/&quot;</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">#echo $CURRENT_DIR</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p style=\""
                        " margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">## Making reports dir</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">mkdir &quot;${CURRENT_DIR}Reports&quot;</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">##########</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">## Install</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:"
                        "0; text-indent:0px;\"><span style=\" font-size:10pt;\">##########</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">if [ &quot;$install&quot; = true ]; then</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">    sudo apt-get install ansi2html -y</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">    sudo apt-get install nmap -y</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">    sudo apt-get install dnsenum -y</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-ind"
                        "ent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">fi</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-bl"
                        "ock-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">printf &quot;${PURPLE}########## &lt;Portscan&gt; ##########${NC}\\n&quot; | tee -a Reports/$NAME</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">if [ &quot;$nmap_all&quot; = true ]; then</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; te"
                        "xt-indent:0px;\"><span style=\" font-size:10pt;\">    printf &quot;NMAP all selected... \\n&quot;</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">    sudo nmap ${IP} -sV -Pn -A -p- --script=vulners --script=ssh-auth-methods --script=smb-enum-shares,smb-ls --script=nfs-showmount --script=nfs-ls  | tee -a Reports/$NAME</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">elif [ &quot;$nmap_fast&quot; = true ]; then</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">    printf &quot;NMAP fast selected... \\n&quot;</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" fo"
                        "nt-size:10pt;\">    sudo nmap ${IP} -F | tee -a Reports/$NAME</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">else</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">    sudo nmap ${IP} | tee -a Reports/$NAME</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">fi</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">printf &quot;${PURPLE}########## &lt;/Portscan&gt; ########"
                        "##${NC}\\n&quot; | tee -a Reports/$NAME</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">printf &quot;${PURPLE}########## &lt;DNS&gt; ##########${NC}\\n&quot; | tee -a Reports/$NAME</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">printf &quot;</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">${UNDERLINE}DNS E"
                        "num:${NU}</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">&quot; | tee -a Reports/$NAME</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">dnsenum ${IP} | tee -a Reports/$NAME</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">printf &quot;${PURPLE}########## &lt;/DNS&gt; ##########${NC}\\n&quot; | tee -a Reports"
                        "/$NAME</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">printf &quot;\\n${GREEN}########## &lt;End of Report&gt; ##########${NC}\\n\\n&quot; | tee -a Reports/$NAME</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p></body></html>", None))
        self.bashbuilder_generate.setText(QCoreApplication.translate("LogecC3", u"-->> Generate <<--", None))
        self.pushButton_3.setText(QCoreApplication.translate("LogecC3", u"-->> Copy to Clipboard<<--", None))
        self.pushButton_4.setText(QCoreApplication.translate("LogecC3", u"-->> Save to File <<--", None))
        self.tabWidget_8.setTabText(self.tabWidget_8.indexOf(self.tab_63), QCoreApplication.translate("LogecC3", u"BashBuild", None))
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
        self.scanning_dns_A_4.setHtml(QCoreApplication.translate("LogecC3", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Cantarell'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">[Not Implemented]</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.label.setText(QCoreApplication.translate("LogecC3", u"Raw records", None))
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
        self.bruteforce_fuzz_wordlistdir.setText(QCoreApplication.translate("LogecC3", u"Modules/General/Bruteforce/dirlist", None))
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
        self.DB_Query_scanning_bruteforce_fuzzer.setText("")
        self.DB_Query_scanning_bruteforce_fuzzer.setPlaceholderText(QCoreApplication.translate("LogecC3", u"Enter SQL Query! Type !_help for help! ", None))
#if QT_CONFIG(tooltip)
        self.scanning_bruteforce_fuzzer_refresh.setToolTip(QCoreApplication.translate("LogecC3", u"Refresh the Database, updating values from the SQLITE DB file", None))
#endif // QT_CONFIG(tooltip)
        self.scanning_bruteforce_fuzzer_refresh.setText(QCoreApplication.translate("LogecC3", u"-->> Refresh DB <<--", None))
#if QT_CONFIG(tooltip)
        self.scanning_bruteforce_fuzzer_query.setToolTip(QCoreApplication.translate("LogecC3", u"Run a query on the DB", None))
#endif // QT_CONFIG(tooltip)
        self.scanning_bruteforce_fuzzer_query.setText(QCoreApplication.translate("LogecC3", u"-->> Query DB <<--", None))
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
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), QCoreApplication.translate("LogecC3", u"Settings", None))
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
        self.lineEdit_88.setText(QCoreApplication.translate("LogecC3", u"SecList Top 10 Million Passwords", None))
        self.lineEdit_89.setText(QCoreApplication.translate("LogecC3", u"SecList Default Passwords", None))
        self.lineEdit_90.setText(QCoreApplication.translate("LogecC3", u"SecList Top 10 Million Passwords", None))
        self.bruteforce_download_seclist_top10mil_22.setText(QCoreApplication.translate("LogecC3", u"Download", None))
        self.bruteforce_download_seclist_defaults_13.setText(QCoreApplication.translate("LogecC3", u"Download", None))
        self.bruteforce_download_seclist_top10mil_23.setText(QCoreApplication.translate("LogecC3", u"Download", None))
        self.label_6.setText(QCoreApplication.translate("LogecC3", u"SecList", None))
        self.lineEdit_91.setText(QCoreApplication.translate("LogecC3", u"SecList Top 10 Million Passwords", None))
        self.bruteforce_download_seclist_top10mil_24.setText(QCoreApplication.translate("LogecC3", u"Download", None))
        self.lineEdit_92.setText(QCoreApplication.translate("LogecC3", u"SecList Default Passwords", None))
        self.bruteforce_download_seclist_top10mil_25.setText(QCoreApplication.translate("LogecC3", u"Download", None))
        self.bruteforce_download_seclist_defaults_14.setText(QCoreApplication.translate("LogecC3", u"Download", None))
        self.lineEdit_93.setText(QCoreApplication.translate("LogecC3", u"SecList Top 10 Million Passwords", None))
        self.label_8.setText(QCoreApplication.translate("LogecC3", u"Other", None))
        self.lineEdit_94.setText(QCoreApplication.translate("LogecC3", u"SecList Default Passwords", None))
        self.bruteforce_download_seclist_top10mil_26.setText(QCoreApplication.translate("LogecC3", u"Download", None))
        self.bruteforce_download_seclist_top10mil_27.setText(QCoreApplication.translate("LogecC3", u"Download", None))
        self.lineEdit_95.setText(QCoreApplication.translate("LogecC3", u"SecList Top 10 Million Passwords", None))
        self.bruteforce_download_seclist_defaults_15.setText(QCoreApplication.translate("LogecC3", u"Download", None))
        self.lineEdit_96.setText(QCoreApplication.translate("LogecC3", u"SecList Top 10 Million Passwords", None))
        self.label_9.setText(QCoreApplication.translate("LogecC3", u"Default Usernames", None))
        self.bruteforce_download_seclist_defaults_16.setText(QCoreApplication.translate("LogecC3", u"Download", None))
        self.lineEdit_97.setText(QCoreApplication.translate("LogecC3", u"SecList Top 10 Million Passwords", None))
        self.lineEdit_98.setText(QCoreApplication.translate("LogecC3", u"SecList Top 10 Million Passwords", None))
        self.bruteforce_download_seclist_top10mil_28.setText(QCoreApplication.translate("LogecC3", u"Download", None))
        self.bruteforce_download_seclist_top10mil_29.setText(QCoreApplication.translate("LogecC3", u"Download", None))
        self.lineEdit_99.setText(QCoreApplication.translate("LogecC3", u"SecList Default Passwords", None))
        self.label_10.setText(QCoreApplication.translate("LogecC3", u"Other", None))
        self.tabWidget_5.setTabText(self.tabWidget_5.indexOf(self.tab_8), QCoreApplication.translate("LogecC3", u"Usernames", None))
        self.other_content_directory_layout_SecList_placeholder_button.setText(QCoreApplication.translate("LogecC3", u"Download", None))
        self.other_content_directory_layout_SecList_placeholder.setText(QCoreApplication.translate("LogecC3", u"Placeholder - if u see me then I screwed up my code :) consider it an easter egg", None))
        self.label_18.setText(QCoreApplication.translate("LogecC3", u"SecList", None))
        self.other_content_directory_layout_WeakPasswords_placeholder_button.setText(QCoreApplication.translate("LogecC3", u"Download", None))
        self.label_19.setText(QCoreApplication.translate("LogecC3", u"Weak Passwords", None))
        self.other_content_directory_layout_WeakPasswords_placeholder.setText(QCoreApplication.translate("LogecC3", u"SecList Default Passwords", None))
        self.other_content_directory_layout_DefaultPasswords_placeholder_button.setText(QCoreApplication.translate("LogecC3", u"Download", None))
        self.label_32.setText(QCoreApplication.translate("LogecC3", u"Default Passwords", None))
        self.other_content_directory_layout_DefaultPasswords_placeholder.setText(QCoreApplication.translate("LogecC3", u"SecList Default Passwords", None))
        self.label_44.setText(QCoreApplication.translate("LogecC3", u"Leaked Passwords", None))
        self.other_content_directory_layout_LeakedPasswords_placeholder.setText(QCoreApplication.translate("LogecC3", u"SecList Default Passwords", None))
        self.other_content_directory_layout_LeakedPasswords_placeholder_button.setText(QCoreApplication.translate("LogecC3", u"Download", None))
        self.tabWidget_5.setTabText(self.tabWidget_5.indexOf(self.tab_10), QCoreApplication.translate("LogecC3", u"Passwords", None))
        self.lineEdit_75.setText(QCoreApplication.translate("LogecC3", u"SecList Top 10 Million Passwords", None))
        self.lineEdit_73.setText(QCoreApplication.translate("LogecC3", u"SecList Default Passwords", None))
        self.lineEdit_74.setText(QCoreApplication.translate("LogecC3", u"SecList Top 10 Million Passwords", None))
        self.bruteforce_download_seclist_top10mil_12.setText(QCoreApplication.translate("LogecC3", u"Download", None))
        self.bruteforce_download_seclist_defaults_8.setText(QCoreApplication.translate("LogecC3", u"Download", None))
        self.bruteforce_download_seclist_top10mil_13.setText(QCoreApplication.translate("LogecC3", u"Download", None))
        self.label_2.setText(QCoreApplication.translate("LogecC3", u"SecList", None))
        self.lineEdit_80.setText(QCoreApplication.translate("LogecC3", u"SecList Top 10 Million Passwords", None))
        self.bruteforce_download_seclist_top10mil_16.setText(QCoreApplication.translate("LogecC3", u"Download", None))
        self.lineEdit_79.setText(QCoreApplication.translate("LogecC3", u"SecList Default Passwords", None))
        self.bruteforce_download_seclist_top10mil_17.setText(QCoreApplication.translate("LogecC3", u"Download", None))
        self.bruteforce_download_seclist_defaults_10.setText(QCoreApplication.translate("LogecC3", u"Download", None))
        self.lineEdit_81.setText(QCoreApplication.translate("LogecC3", u"SecList Top 10 Million Passwords", None))
        self.label_4.setText(QCoreApplication.translate("LogecC3", u"Weak Passwords", None))
        self.lineEdit_82.setText(QCoreApplication.translate("LogecC3", u"SecList Default Passwords", None))
        self.bruteforce_download_seclist_top10mil_18.setText(QCoreApplication.translate("LogecC3", u"Download", None))
        self.bruteforce_download_seclist_top10mil_19.setText(QCoreApplication.translate("LogecC3", u"Download", None))
        self.lineEdit_84.setText(QCoreApplication.translate("LogecC3", u"SecList Top 10 Million Passwords", None))
        self.bruteforce_download_seclist_defaults_11.setText(QCoreApplication.translate("LogecC3", u"Download", None))
        self.lineEdit_83.setText(QCoreApplication.translate("LogecC3", u"SecList Top 10 Million Passwords", None))
        self.label_3.setText(QCoreApplication.translate("LogecC3", u"Default Passwords", None))
        self.bruteforce_download_seclist_defaults_12.setText(QCoreApplication.translate("LogecC3", u"Download", None))
        self.lineEdit_87.setText(QCoreApplication.translate("LogecC3", u"SecList Top 10 Million Passwords", None))
        self.lineEdit_86.setText(QCoreApplication.translate("LogecC3", u"SecList Top 10 Million Passwords", None))
        self.bruteforce_download_seclist_top10mil_20.setText(QCoreApplication.translate("LogecC3", u"Download", None))
        self.bruteforce_download_seclist_top10mil_21.setText(QCoreApplication.translate("LogecC3", u"Download", None))
        self.lineEdit_85.setText(QCoreApplication.translate("LogecC3", u"SecList Default Passwords", None))
        self.label_5.setText(QCoreApplication.translate("LogecC3", u"Leaked Passwords", None))
        self.tabWidget_5.setTabText(self.tabWidget_5.indexOf(self.tab_9), QCoreApplication.translate("LogecC3", u"Directory", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_7), QCoreApplication.translate("LogecC3", u"Wordlists", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_8), QCoreApplication.translate("LogecC3", u"Other - Not Yet Occupied", None))
        self.tabWidget_10.setTabText(self.tabWidget_10.indexOf(self.tab_7), QCoreApplication.translate("LogecC3", u"Content", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_27), QCoreApplication.translate("LogecC3", u"Other", None))
        self.menuFile.setTitle(QCoreApplication.translate("LogecC3", u"File", None))
        self.menu_GettingStarted.setTitle(QCoreApplication.translate("LogecC3", u"Getting Started", None))
    # retranslateUi

