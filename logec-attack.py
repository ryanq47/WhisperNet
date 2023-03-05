#!/bin/python3

import sys
import os
import sqlite3

# Get the absolute path of the directory where the script is located
sys_path = os.path.dirname(os.path.abspath(sys.argv[0]))
print("Syspath:" + sys_path)

## pyqt singal needs to be moved to "signal"
from PySide6.QtCore import Qt, QObject, QThread, Signal, QFile, Slot, QThreadPool, QCoreApplication, QTimer
from PySide6 import QtWidgets
from PySide6.QtUiTools import loadUiType
from PySide6.QtGui import QIcon, QAction, QPen
from PySide6 import QtUiTools
from PySide6.QtSql import QSqlDatabase, QSqlTableModel, QSqlQuery
from PySide6.QtWidgets import (
    QMainWindow,
    QLabel,
    QMessageBox,
    QPushButton,
    QInputDialog,
    QTableView,
    QApplication,
    QTableWidget,
    QTableWidgetItem,
    QHeaderView,
    QFileDialog,
    QGraphicsScene,
    QGraphicsView,
    QGraphicsTextItem,
    QTabWidget,
    QTabBar,
    QMenuBar,
    QMenu
)

## Plugin path for sql driver (TLDR makes compiling easier by having a local copy)
plugin_path = 'plugins'
os.environ['QT_PLUGIN_PATH'] = plugin_path

# Add the path to the plugin directory
QCoreApplication.addLibraryPath(plugin_path)


import threading
import time
import webbrowser
import time
import json
from functools import partial

from agent.server import s_sock, s_action

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

from Modules.General.Bruteforce.bruteforce import Bruteforce, Fuzzer

from Modules.General.OSINT.dork import Dork

from Modules.General.SysShell.shell import Shell

from Modules.General.ScriptGen import ScriptGen

import Modules.General.utility as utility

import Modules.General.SaveFiles.fileops as fileops

from gui import Ui_LogecC3

class MyApp(QMainWindow, Ui_LogecC3):
    print("hi")
    def __init__(self, parent=None):
        ##### UI SETUP
        ## ELi5: Taking the imported gui.py and using that to make the gui n stuff
        super(MyApp, self).__init__(parent)
        self.setupUi(self)
        #####
        

        
        ##### Class Thread Manager:
        self.thread_manager = QThreadPool()
        #####
        
        ##### Project & settings Loading
        self.sql_global()
        self.settings_global()
        self.PF = fileops.SaveFiles()
        self.ProjectPath = None
        
        self.c2_layout()
        
        ##### Init Gui Settings:
        self.set_theme(self.settings['general']['theme'])
        
        ## Need to move this
        self.connected = False
        self.connected_list = []

        ## starting connections
        self.PID = os.getpid()

        self.startlist = 0
        ## A check to see if the program is on its first iteration, aka when run the first time.
        ## Handy for error messages, see the if statement in the DB section about empty queries

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
        

        ## File Menu ========================

        self.actionOpen_Project.triggered.connect(self.project_open)
        self.actionSave_Project.triggered.connect(self.project_save)
        self.actionSaveAs_Project.triggered.connect(self.project_saveAs)
        ## ========================================
        ## Shell (Depreacated, needs to be redone) ========================
        ## ========================================

        ## Sys Shell
        self.c2_systemshell_send.clicked.connect(self.sys_shell)
        self.c2_systemshell_input.setFocus()
        #self.c2_systemshell.textChanged.connect(self.sys_shell)
        

        ## debug:
        self.actionDEBUG.triggered.connect(self.DEBUG)
        self.actionRELOAD.triggered.connect(self.restart)

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

        ## == Osint Dork
        self.osint_dork_generate.clicked.connect(self.dork)

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

        self.portscan_start.clicked.connect(self.portscan)

        ## bruteforce
        self.bruteforce_start.clicked.connect(self.bruteforce)
        self.bruteforce_stop.clicked.connect(self.bruteforce_hardstop)
        self.bruteforce_user_browse.clicked.connect(partial(self.bf_browser_popup, "username"))
        self.bruteforce_pass_browse.clicked.connect(partial(self.bf_browser_popup, "password"))
        
        self.bruteforce_download_ignis_1M.clicked.connect(partial(self.bruteforce_download, "ignis-1M"))
        self.bruteforce_download_seclist_defaults.clicked.connect(partial(self.bruteforce_download, "seclist-defaults"))
        self.bruteforce_download_seclist_top10mil.clicked.connect(partial(self.bruteforce_download, "seclist-top10mil"))
        self.bruteforce_download_seclist_top10mil_usernames.clicked.connect(partial(self.bruteforce_download, "seclist-top10mil-usernames"))
        self.bruteforce_download_seclist_topshort.clicked.connect(partial(self.bruteforce_download, "seclist-top-short"))
        
        ## Bruteforce_fuzzer
        self.bruteforce_fuzz_start.clicked.connect(self.bruteforce_fuzzer)
        self.bruteforce_stop.clicked.connect(self.bruteforce_fuzz_hardstop)
        self.bruteforce_fuzz_wordlist_browse.clicked.connect(partial(self.bf_fuzz_browser_popup, "wordlistdir"))

        #== SQL bruteforce
        self.scanning_bruteforce_query.clicked.connect(
            lambda: self.custom_query('bruteforce_db')
        )
        self.scanning_bruteforce_query.setShortcut('Return')

        ## other
        # == BashBuikder
        self.bashbuilder_generate.clicked.connect(self.bash_builder)
        
        ## == Perf Tab
        
        ##### Performance Tab Inits
        self.other_cpu_scene = QGraphicsScene()
        self.other_cpu_performance.setScene(self.other_cpu_scene)
        #self.other_cpu_scene.setSceneRect(0, 0, 1000, 200)
        self.other_ram_scene = QGraphicsScene()
        self.other_ram_performance.setScene(self.other_ram_scene)
        
        self.other_network_scene = QGraphicsScene()
        self.other_network_performance.setScene(self.other_network_scene)
        
        self.cpu_data = []
        self.ram_data = []
        self.network_out_data = []
        self.network_in_data = []
        self.Perf = utility.Performance()
        self.x = 0
        self.draw_graph_refresh()
        #####
        
        ##### SQL Refresh
        self.table_RefreshDB_Button_performance.clicked.connect(
            lambda: self.custom_query('performance_error_db')
        )

        ## network speed test
        self.performance_speedtest.clicked.connect(
            self.performance_networkspeed
        )
        ## Benchmark
        self.performance_benchmark_button.clicked.connect(self.performance_benchmark)

        ## Settings
        self.settings_reload.clicked.connect(self.edit_settings)
        self.settings_write.clicked.connect(self.write_settings)
        self.program_reload.clicked.connect(self.restart)
        
        ## ========================================
        ## Init Values/Main Thread ================
        ## ========================================


        ## Object Instances ==================
        self.N = utility.Network()
        self.H = utility.Host()
        # self.P = Portscan()        self.bruteforce_user_browse.clicked.connect(self.browser_popup)

        ## Portscan Inits ==================
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

        ## SQL Inits =====================
        ## Setting the DB
        self.view = self.table_SQLDB

        ## Showing help table on startup
        self.DB_Query_main.setText('select * from Help')
        self.custom_query('main_db')

        self.DB_Query_osint_reddit.setText('SELECT * FROM RedditResults')
        self.custom_query('reddit_osint_db')

        self.DB_Query_scanning_portscan.setText('select * from PortScan')
        self.custom_query('scanning_portscan_db')

        self.DB_Query_scanning_bruteforce.setText('select * from "BRUTEFORCE-http"')
        self.custom_query('bruteforce_db')

        self.custom_query('performance_error_db')

        ## Other inits ==================
        
        ## Loading Settings
        self.edit_settings()

        ## Once loaded, setting startlist to 1
        self.startlist = self.startlist = 1

    ## ========================================
    ## Error, Checks & Debug ==================
    ## ========================================
        
    def restart(self): ## MEMORY LEAK !!
        # Restart the Python interpreter
        args = sys.argv[:]
        args.insert(0, sys.executable)
        self.close()
        sys.exit(os.spawnvp(os.P_WAIT, sys.executable, args))
        
    def DEBUG(self):
        self.client_connected()
        self.text_Program_Output.setText(
            'IN DEBUG MODE - NOT CONNECTED, THINGS WILL BREAK'
        )
        self.text_connections_output.setText(
            'IN DEBUG MODE - NOT CONNECTED, THINGS WILL BREAK'
        )

    ## Error handler
    def ERROR(self, error_list):#, severity, fix):
        Date = utility.Timestamp.UTC_Date()
        Time = utility.Timestamp.UTC_Time()
        
        error = error_list[0]
        severity = error_list[1]
        fix = error_list[2]

        QMessageBox.critical(
            None,
            ## Title
            'Error!',
            ## Actual Error
            f'SEVERITY: {severity} \nERRMSG: {error} \nFIX: {fix} \n',
        )
        #time.sleep(10)
        error_list = [severity, error, fix, Time, Date]
        
        self.db_error_write(error_list)

    def root_check(self, name):
        if os.getuid() != 0:
            self.ERROR([f"You are not running as root, note that {name} may not work as expected","Medium","Restart program as root"])

    ## ========================================
    ## Getting started tab ====================
    ## ========================================

    def getting_started(self):

        with open('Modules/GUI_System/gui_about', 'r') as f:
            welcome_message = f.read()
            self.text_Program_Output.setText(welcome_message)

    ## ========================================
    ## SQLDB Functions ========================
    ## ========================================

    ## This is where all the SQL Processing code is housed.

    def clear_db_table(self):
        self.view.clear()
        self.view.setRowCount(0)

    def refresh_db(self, _from):
        # removing old rows:
        self.clear_db_table()

        self.custom_query(_from)

    def custom_query(self, _from):
        ## Setting which QTable Object to output on
        if _from == 'c2_db':
            # self._from = "c2_db"
            self.view = self.table_SQLDB
            query_input_raw  = f'{self.DB_Query.text()}'

        ## To main db section
        elif _from == 'main_db':
            # self._from = "main_db"
            self.view = self.table_SQLDB_main
            query_input_raw  = f'{self.DB_Query_main.text()}'

        elif _from == 'reddit_osint_db':
            self.view = self.table_SQLDB_osint_reddit
            query_input_raw  = f'{self.DB_Query_osint_reddit.text()}'

        elif _from == 'scanning_portscan_db':
            self.view = self.scanning_portscan_db
            query_input_raw  = f'{self.DB_Query_scanning_portscan.text()} ORDER BY ScanDate DESC, ScanTime DESC'

        elif _from == 'performance_error_db':
            self.view = self.table_SQLDB_performance_error
            query_input_raw  = f'select * from Error ORDER BY Date DESC, Time DESC'

        elif _from == 'bruteforce_db':
            print("BF DB")
            self.view = self.scanning_bruteforce_db
            query_input_raw  = f'{self.DB_Query_scanning_bruteforce.text()} ORDER BY DATE DESC, TIME DESC'

        else: #query_input == '' and self.startlist != 0:
            query_input_raw  = ""
            self.view = ""
            self.ERROR(
                ['No Query Input Provided', 'Low', 'Enter an input to fix']
            )
        
        ## Shortcuts not working for some reason
        # Temp workaround
        query_input = query_input_raw
        '''
        if query_input_raw == '!_help':
            query_input = 'select * from Help'
        elif query_input_raw  == '!_tables':
            query_input == "select * from Tables"
        elif query_input_raw  == '!_error':
            query_input == "select * from Error ORDER BY Date DESC, Time DESC"
        elif '!_portscan' in query_input_raw :
            query_input == "select * from PortScan ORDER BY Date DESC, Time DESC"
        else:
            query_input = query_input_raw
        
        print(query_input)'''

        ## clearnig DB, and resetting from
        # _from = None
        self.clear_db_table()


            ## Getting query data 
        query = QSqlQuery(f'{query_input}') ##<< setting
            
            ## Connecting to DB for more data
        connection = sqlite3.connect(self.database_file)
        
        
        cursor = connection.execute(query_input) 
        names = list(map(lambda x: x[0], cursor.description))
        connection.close()
            
            ## init vars
        names_num = 0
        names_list = []
        query_num = 0
            
            # Loop for column names
        for i in names:
            names_list.append(i)
            names_num = names_num + 1
            
        self.view.setColumnCount(len(names_list))
        self.view.setHorizontalHeaderLabels(names_list)
            
            # Loop for data in each column
        while query.next():
            rows = self.view.rowCount()
            self.view.setRowCount(rows + 1)
                
            for i in range(0, len(names_list)):
                self.view.setItem(rows, i, QTableWidgetItem(query.value(i)))
                
            query_num = query_num + 1

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

## ========================================
## C2 Tab =================================
## ========================================

    # Eveything related to the C2 tab & functions

    ## ========================================
    ## System Shell ===========================
    ## ========================================
    
    ## A semi-interactive bash shell for the local system
    
    def c2_layout(self):
        self.c2_menuBar = QMenuBar()
        
        ## Options Tab ==================
        self.menuOptions = QMenu("Options", self.c2_menuBar)
        self.actionQuit = QAction('Quit', self)
        self.actionQuit.triggered.connect(self.close)

        self.menuOptions.addAction(self.actionQuit)
        self.c2_menuBar.addAction(self.menuOptions.menuAction())
        
        ## Client Tab ==================
        self.menuClient = QMenu("Client", self.c2_menuBar)
        self.actionStart_Listener = QAction('Start Listener', self)
        
        ## Adding actions to the bar
        self.menuClient.addAction(self.actionStart_Listener)
        self.c2_menuBar.addAction(self.menuClient.menuAction())
        
        ## Connect Actions:
        #self.actionStart_Listener.triggered.connect(self.listen) ## Stand in variable

        #WARN! TAB widget must have a layout!
        ##             ## Which tab
        self.tabWidget.widget(1).layout().setMenuBar(self.c2_menuBar)
    
    
    ## Gonna need some work, this currently creates one thread for each command
    def sys_shell(self):

        # The Enter key was pressed
        #print("Enter key pressed")
        input_list = [
                self.c2_systemshell_input.text()
                ]
            
        #self.sysshell_thread = QThread()
        self.sysshell_worker = Shell()
        #self.sysshell_worker.moveToThread(self.sysshell_thread)
        self.thread_manager.start(partial(self.sysshell_worker.shell_framework, input_list))
                
        ## Queing up the function to run (Slots n signals too)
        #print("Starting Shell Qthread")
                
        #Could be a lambda
        self.sysshell_worker.sys_out.connect(self.sys_shell_results)
    
    def sys_shell_results(self, results):
        try:
            self.c2_systemshell.setText(results)
            self.c2_systemshell_input.setText("")
        except Exception as e:
            print(e)

## ========================================
## Scanning/Enumeration ====================
## ========================================

## Everything related to scanning and enumeration

    ## ========================================
    ## PortScan Popup ========================
    ## ========================================

    def portscan(self, QObject):
        input_ip = self.portscan_IP.text()
        print(input_ip)

        try:
            ## setting bar to 0
            self.stealth_bar.setValue(0)

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
            
            timeout_mapping = {
            'Normal Speed (1 Second Timeout)': 1,
            'Light Speed (.5 Second Timeout)': 0.5,
            'Ridiculous Speed (.25 Second Timeout)': 0.25,
            'Ludicrous Speed (.1 Second Timeout)': 0.1,
            'Plaid (.01 Second Timeout)': 0.01
            }
            timeout = timeout_mapping.get(self.portscan_fast_timeout.currentText())
            
            delay_mapping = {
            'None': [0,0],
            '.001-.1': [.001,0.1],
            '.1-1.0': [.1,1],
            '1.0-5.0': [1,5],
            }
            delay = delay_mapping.get(self.portscan_delay.currentText())

            print(f'TIMOUT: {timeout}')
            
            print(f'DELAY: {delay}')       
            

            ## if clicked standard = true
            target_list = [ip, int(min_port), int(max_port), timeout, delay, extra_port]
            scantype_list = [
                standard,
                stealth,
                fast,
                #timeout,
            ]   ## timeout shoudl always be last

            #self.portscan_start.setText('-->> Scanning... <<--')
            self.portscan_worker = Portscan()
            self.thread_manager.start(partial(self.portscan_worker.scan_framework, target_list, scantype_list))

            self.portscan_worker.progress.connect(self.portscan_bar)
            self.portscan_worker.liveports.connect(self.portscan_liveports) #<< not getting triggered'''

            ## Getting results list & writing
            self.portscan_worker.results_list.connect(self.portscan_database_write)

            ## wiping live list
            self.portscan_liveports_browser.setText("")

        except ValueError as ve:
            self.ERROR([ve, "low", "Make sure all respective fields are filled"])

        except Exception as e:
            self.ERROR([e, "??", "Unkown Error - most likely a code issue (AKA Not your fault)"])
    
    def portscan_bar(self, status): ## I wonder if this dosen't work due to all the threads waiting to join back up? maybe portscanner writing the value to a tmp file would have to do it, or to the DB in a .hiddentable
        self.stealth_bar.setValue(status)
        if self.stealth_bar.value() == 99:
            self.stealth_bar.setValue(100)

    def portscan_liveports(self, ports):
        self.portscan_liveports_browser.setText("")
        #self.portscan_liveports_browser.setText(str(ports))
        for i in ports:
            self.portscan_liveports_browser.append(f"[+] {i}/tcp")

    def portscan_database_write(self, list):
        print("DB Triggered")
        try:
            cursor = self.sqliteConnection.cursor()
            
            ## Picked up this trick from chatGPT, basically each item coresponds to the number in list
            IP, PORT, SCANTYPE, SCANDATE, SCANTIME, RUNTIME, SCANNEDPORTS, DELAY = list
            
            sqlite_insert_query = f"""INSERT INTO PortScan (IP, PORT, ScanType, ScanDate, ScanTime, RunTime, ScannedPorts, Delay) 
            VALUES
            ({IP}, {str(PORT).replace("{","").replace("}","")}, '{SCANTYPE}', '{SCANDATE}', '{SCANTIME}', '{RUNTIME}', "{SCANNEDPORTS}", '{DELAY}')"""
            
            print(sqlite_insert_query)

            cursor.execute(sqlite_insert_query)
            self.sqliteConnection.commit()
            cursor.close()
            
        except Exception as e:
            self.ERROR([e, "Medium", "??"])
    
    ## ========================================
    ## Bash Builder ===========================
    ## ========================================
    
    ## A bash script builder
    
    def bash_builder(self):
        self.Script = ScriptGen.Script()
        
        ## Doing json here for expandability, rather than a list
        ## If the checks are checked, they return true. The scriptgen.py uses true & false
        ## for which blocks to build with
        print(self.bashbuild_diagnostic.isChecked())
        
        json_unpacked = {
            "DIAGNOSTIC":
                {
                    "diagnostic":self.bashbuild_diagnostic.isChecked(),
                    "installpackages":self.bashbuild_installpackages.isChecked()
                },
            
            
            "DNS":
                {
                    "dnsenum":self.bashbuild_dnsenum.isChecked(),
                    "whois":"false"
                },
            
            
            "PORTSCAN":
                {
                    "nmap":self.bashbuild_nmap.isChecked(),
                }
        }
        
        packed_json = json.dumps(json_unpacked)
        
        print(packed_json)
        
        self.Script.script_results.connect(self.bash_builder_display)
        
        ## Has to go last to grab signals n stiff
        self.Script.script_framework(packed_json)

    def bash_builder_display(self, final_script):
        print("triggered")
        self.bashbuild_textoutput.setText(final_script)

    ## ========================================
    ## DNS Lookup ===========================
    ## ========================================
    
    ## Quick DNS lookups
    
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
            self.ERROR([
                'No input for DNS',
                'Low',
                "Make sure the DNS field isn't empty",
            ])
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
                
                
## ========================================
## BruteForce Tab =========================
## ========================================

    ## ========================================
    ## BruteForce Creds =======================
    ## ========================================

    def bruteforce(self):
        
        try:
            target_list = [
                self.bruteforce_target.text(), 
                self.bruteforce_port.text(),
                self.bruteforce_protocol.currentText(),
                self.bruteforce_userdir.text(),
                self.bruteforce_passdir.text(),
                self.bruteforce_delay.value(),
                self.bruteforce_threads.value(),
                self.bruteforce_batchsize.value()
                ]
            
            # Bar to 0
            self.bruteforce_progressbar.setValue(0)
            
            
            self.bruteforce_worker = Bruteforce()
            self.thread_manager.start(partial(self.bruteforce_worker.bruteforce_framework, target_list))
            
            ##self.bruteforce_worker.finished.connect(self.bruteforce_worker.deleteLater)
            #self.bruteforce_worker.finished.connect(self.bruteforce_worker.thread.terminate)
            #self.bruteforce_worker.finished.connect(self.bruteforce_thread.deleteLater)
            
            #Error
            self.bruteforce_worker.module_error.connect(partial(self.ERROR, target_list))
            
            #errlog
            self.bruteforce_worker.errlog.connect(self.errlog_box)
            self.bruteforce_errlog.setText("")
            self.bruteforce_errlognum = 0
                    
            # Live attempts
            self.bruteforce_worker.live_attempts.connect(self.live_attempts_box)

            # Current Batch
            self.bruteforce_worker.current_batch.connect(self.batch_update)

            # Total batch
            self.bruteforce_worker.num_of_batches.connect(self.batch_total)

            # Progress
            self.bruteforce_worker.progress.connect(self.bruteforce_bar)
            #self.bruteforce_worker.goodcreds.connect(self.bruteforce_live_goodcreds) # FOr the live view
            
            # Good Creds
            self.bruteforce_worker.goodcreds.connect(self.live_goodcreds_box)
            self.bruteforce_goodcreds.setText("")
            
            ## Write to DB
            self.bruteforce_worker.results_list.connect(self.bruteforce_database_write)
            
            # Starting Thread
            #self.bruteforce_thread.start()
        
        except ValueError as ve:
            self.ERROR([ve, "low", "Make sure all respective fields are filled"])

        except Exception as e:
            self.ERROR([e, "??", "Unkown Error - most likely a code issue (AKA Not your fault)"])

    def bruteforce_hardstop(self):
        #pass
        print("clicked")
        try:
            pass
            #self.bruteforce_worker.thread_quit()
            #self.bruteforce_thread.exit() # exi works better than quit
            #self.bruteforce_worker.deleteLater()
        except Exception as e:
            self.ERROR([e, "Low", "Bruteforce is probably not running"])

    def bf_browser_popup(self, whichbutton):
        from PySide6.QtWidgets import QFileDialog
        print("Clicked")
        
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","All Files (*);;Python Files (*.py)", options=options)
        
        if whichbutton == "username":
            self.bruteforce_userdir.setText(fileName)
        
        elif whichbutton == "password":
            self.bruteforce_passdir.setText(fileName)

    def live_attempts_box(self, attempts):
        self.bruteforce_livetries.setText(attempts)

    def batch_total(self, total):
        self.bruteforce_panel.setTabText(1, f"Current Batch ({total[0]}/{total[1]})")
   
    def batch_update(self, batch):
        self.bruteforce_currentbatch.setText(str(batch))

    def live_goodcreds_box(self, goodcreds):
        self.bruteforce_goodcreds.setText(str(goodcreds))

    def errlog_box(self, err):
        self.bruteforce_errlog.append("[*] " + err)
        self.bruteforce_errlognum = self.bruteforce_errlognum + 1
        self.bruteforce_panel.setTabText(2, f"Log ({self.bruteforce_errlognum})")
        
    def bruteforce_bar(self, status):
        self.bruteforce_progressbar.setFormat("{:.1f}%".format(self.bruteforce_progressbar.value()))
        
        self.bruteforce_progressbar.setValue(status)
        if self.bruteforce_progressbar.value() == 99:
            self.bruteforce_progressbar.setValue(100)

    def bruteforce_download(self, wordlist):
        if wordlist == "ignis-1M":
            self.H.download([
                "https://shorturl.at/bdgY7",
                f"Modules/General/Bruteforce/Wordlists",
                "ignis-1M-passwords"
            ])
        elif wordlist == "seclist-defaults":
            self.H.download([
                "https://shorturl.at/lDKN4",
                f"{syspath.path}/Modules/General/Bruteforce/Wordlists",
                "SecList-Default-Passwords"
            ])
        elif wordlist == "seclist-top10mil":
            self.H.download([
                "https://shorturl.at/vCMPZ",
                f"{syspath.path}/Modules/General/Bruteforce/Wordlists",
                "SecList-top10mil-Passwords"
            ])
        elif wordlist == "seclist-top10mil-usernames":
            self.H.download([
                "https://shorturl.at/bmS46",
                f"{syspath.path}/Modules/General/Bruteforce/Wordlists",
                "SecList-top10mil-usernames"
            ])
        elif wordlist == "seclist-top-short":
            self.H.download([
                "https://shorturl.at/ryQV5",
                f"{syspath.path}/Modules/General/Bruteforce/Wordlists",
                "SecList-top1-short-usernames"
            ])

    def bruteforce_database_write(self, list):
        print("DB Triggered")
        try:
            cursor = self.sqliteConnection.cursor()
            
            ## Picked up this trick from chatGPT, basically each item coresponds to the number in list
            TARGET, PORT, SERVICE, CREDS, TIME, DATE = list
            
            sqlite_insert_query = f"""INSERT INTO 'BRUTEFORCE-Creds' (Target, Port, Service, Credentials, Time, Date) 
            VALUES
            ('{TARGET}', '{str(PORT).replace("{","").replace("}","")}', '{SERVICE}', '{CREDS}', '{TIME}', '{DATE}' )"""
            
            print(sqlite_insert_query)

            cursor.execute(sqlite_insert_query)
            self.sqliteConnection.commit()
            cursor.close()
            
        except Exception as e:
            self.ERROR([e, "Medium", "??"])
   
    ## ========================================
    ## BruteForce Fuzzer ======================
    ## ========================================
    
    # A fuzzer
    
    def bruteforce_fuzzer(self):
        
        try:
            #target_list = ["IP","port","wordlistdir","option1","option2"]
            
            target_list = [
                self.bruteforce_fuzz_url.toPlainText(), 
                self.bruteforce_fuzz_port.text(),
                self.bruteforce_fuzz_wordlistdir.text(),
                self.bruteforce_fuzz_delay.value(),
                self.bruteforce_fuzz_threads.value(),
                self.bruteforce_fuzz_batchsize.value(),
                self.bruteforce_fuzz_validresponsecode.toPlainText(),
                self.bruteforce_fuzz_showfullurl_option.isChecked()
                ]
            
            # Bar to 0
            self.bruteforce_fuzz_progressbar.setValue(0)
            
            self.fuzzer_worker = Fuzzer()
            self.thread_manager.start(partial(self.fuzzer_worker.fuzzer_framework, target_list))
            
            
            #Error
            self.fuzzer_worker.module_error.connect(partial(self.ERROR, target_list))
            
            #errlog
            self.fuzzer_worker.errlog.connect(self.fuzz_errlog_box)
            self.bruteforce_fuzz_errlog.setText("")
            self.bruteforce_fuzz_errlognum = 0
                    
            # Live attempts
            self.fuzzer_worker.live_attempts.connect(self.fuzz_live_attempts_box)

            # Current Batch
            self.fuzzer_worker.current_batch.connect(self.fuzz_batch_update)

            # Total batch
            self.fuzzer_worker.num_of_batches.connect(self.fuzz_batch_total)

            # Progress
            self.fuzzer_worker.progress.connect(self.fuzz_bruteforce_bar)
            #self.bruteforce_worker.goodcreds.connect(self.bruteforce_live_goodcreds) # FOr the live view
            
            # Good Creds
            self.fuzzer_worker.gooddir.connect(self.fuzz_live_gooddir_box)
            self.bruteforce_fuzz_gooddir_gui.setText("")
            
            # DB write
            self.fuzzer_worker.results_list.connect(self.bruteforce_fuzz_database_write)
        
        except ValueError as ve:
            self.ERROR([ve, "low", "Make sure all respective fields are filled"])

        except Exception as e:
            self.ERROR([e, "??", "Unkown Error - most likely a code issue (AKA Not your fault)"])
            
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)

    def bruteforce_fuzz_hardstop(self):
        #pass
        print("clicked")
        try:
            pass
            #self.fuzzer_worker.thread_quit()
            #self.fuzzer_thread.exit() # exi works better than quit
            #self.fuzzer_worker.deleteLater()
        except Exception as e:
            self.ERROR([e, "Low", "Fuzzer is probably not running"])

    def bf_fuzz_browser_popup(self, whichbutton):
        from PySide6.QtWidgets import QFileDialog
        print("Clicked")
        
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","All Files (*);;Python Files (*.py)", options=options)
        
        if whichbutton == "wordlistdir":
            self.bruteforce_fuzz_wordlistdir.setText(fileName)

    def fuzz_live_attempts_box(self, attempts):
        self.bruteforce_fuzz_livetries.setText(attempts)

    def fuzz_batch_total(self, total):
        self.bruteforce_fuzz_panel.setTabText(1, f"Current Batch ({total[0]}/{total[1]})")
   
    def fuzz_batch_update(self, batch):
        self.bruteforce_fuzz_currentbatch.setText(str(batch))

    def fuzz_live_gooddir_box(self, goodcreds):
        self.bruteforce_fuzz_gooddir_gui.setText(str(goodcreds))

    def fuzz_errlog_box(self, err):
        self.bruteforce_fuzz_errlog.append("[*] " + err)
        self.bruteforce_fuzz_errlognum = self.bruteforce_fuzz_errlognum + 1
        self.bruteforce_fuzz_panel.setTabText(2, f"Log ({self.bruteforce_fuzz_errlognum})")
        
    def fuzz_bruteforce_bar(self, status):
        self.bruteforce_fuzz_progressbar.setFormat("{:.1f}%".format(self.bruteforce_fuzz_progressbar.value()))
        
        self.bruteforce_fuzz_progressbar.setValue(status)
        if self.bruteforce_fuzz_progressbar.value() == 99:
            self.bruteforce_fuzz_progressbar.setValue(100)

    def bruteforce_fuzz_download(self, wordlist):
        if wordlist == "ignis-1M":
            self.H.download([
                "https://shorturl.at/bdgY7",
                f"{syspath.path}/Modules/General/Bruteforce/Wordlists",
                "ignis-1M-passwords"
            ])
        elif wordlist == "seclist-defaults":
            self.H.download([
                "https://shorturl.at/lDKN4",
                f"{syspath.path}/Modules/General/Bruteforce/Wordlists",
                "SecList-Default-Passwords"
            ])
        elif wordlist == "seclist-top10mil":
            self.H.download([
                "https://shorturl.at/vCMPZ",
                f"{syspath.path}/Modules/General/Bruteforce/Wordlists",
                "SecList-top10mil-Passwords"
            ])
        elif wordlist == "seclist-top10mil-usernames":
            self.H.download([
                "https://shorturl.at/bmS46",
                f"{syspath.path}/Modules/General/Bruteforce/Wordlists",
                "SecList-top10mil-usernames"
            ])
        elif wordlist == "seclist-top-short":
            self.H.download([
                "https://shorturl.at/ryQV5",
                f"{syspath.path}/Modules/General/Bruteforce/Wordlists",
                "SecList-top1-short-usernames"
            ])

    def bruteforce_fuzz_database_write(self, list):
        print("BF Fuzzer DB Triggered")
        try:
            cursor = self.sqliteConnection.cursor()
            
            ## Picked up this trick from chatGPT, basically each item coresponds to the number in list
            TARGET, PORT, CODE,SHORT_URL, LONG_URL, TIME, DATE = list
            
            sqlite_insert_query = f"""INSERT INTO 'BRUTEFORCE-Fuzzer' (Target, Port, Code, Short_Url, Long_Url, Time, Date) 
            VALUES
            ('{TARGET}', '{str(PORT).replace("{","").replace("}","")}', '{CODE}', '{SHORT_URL}', '{LONG_URL}', '{TIME}', '{DATE}' )"""
            
            print(sqlite_insert_query)

            cursor.execute(sqlite_insert_query)
            self.sqliteConnection.commit()
            cursor.close()
            
        except Exception as e:
            self.ERROR([e, "Medium", "??"])
            
## ========================================
## OSINT Tab ==============================
## ========================================

    ## ========================================
    ## Reddit Scraper =========================
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
            self.ERROR([
                "'Keyword' Field Empty",
                'low',
                "Enter a value in the 'Keyword' field, or * for all results",
            ])
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
    ## Google Dork Builder=====================
    ## ========================================

    ## A google dork builder

    def dork(self):
        try:

            dork_list = [
                self.osint_dork_searchterm.text(),
                self.osint_dork_keyword.text(), 
                self.osint_dork_intitle.text(),
                self.osint_dork_filetype.text(),

                ]

            self.dork_thread = QThread()
            self.dork_worker = Dork()
            self.dork_worker.moveToThread(self.dork_thread)
            
            ## Queing up the function to run (Slots n signals too)
            self.dork_thread.started.connect(partial(self.dork_worker.dork_framework, dork_list))
            self.dork_worker.finished.connect(self.dork_thread.exit)
            self.dork_worker.finished.connect(self.dork_worker.deleteLater)
            self.dork_worker.finished.connect(self.dork_thread.deleteLater)
            
            self.dork_worker.dork_query.connect(self.dork_query_display)
                            
            # Starting Thread
            self.dork_thread.start()

        except Exception as e:
            self.ERROR([e, "??", "Unkown Error - most likely a code issue (AKA Not your fault)"])
        
    def dork_query_display(self, dork_query):
        self.osint_dork_output.setText(dork_query)

## ========================================
## Other Tab ==============================
## ========================================

    ## ========================================
    ## Performance(2) n stuff =================
    ## ========================================
    def draw_graph_refresh(self):
        self.timer = QTimer()
        self.timer.timeout.connect(self.draw_graph)
        self.timer.start(1000)
    
        #self.prev_x, self.prev_y = 0, 0
        
    def draw_graph(self):        
        ## Disabling scroll bar CPU
        self.other_cpu_performance.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.other_cpu_performance.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        ## ram
        self.other_ram_performance.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.other_ram_performance.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        
        self.other_network_performance.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.other_network_performance.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
 
        ## Defining Pen        
        pen = QPen()
        pen.setWidth(1)
        pen.setColor(Qt.blue)

        ## Gather data from system
       
        ## plus 10 for each update for all
        self.x = self.x + 10
        
         ## CPU
        cpu_y = self.Perf.CPU_all()
        
        cpu_temp = self.Perf.CPU_temp()

        ## RAM
        ram_y = self.Perf.RAM_all()
        ram_usage = self.Perf.RAM_HumanReadable()
        
        ##Netwokr 
        network_in_y = self.Perf.Network_in()
        network_out_y = self.Perf.Network_out()

        # Append Data to list (Note, should probably clear after so long for memory reasons)
        self.cpu_data.append((self.x, (cpu_y*-1))) ## negative for properly facing graph (was inverted)
        self.ram_data.append((self.x, (ram_y*-1)))
        self.network_out_data.append((self.x, (ram_y*-1)))
        
        
        ## CPU graph
        # Clear the scene and add all the lines
        self.other_cpu_scene.clear()
        self.cpu_items = []
        
        for i in range(1, len(self.cpu_data)):
            x1, y1 = self.cpu_data[i-1]
            x2, y2 = self.cpu_data[i]
            self.other_cpu_scene.addLine(x1, y1, x2, y2, pen)
            ## Adding %
            cpu_percent = QGraphicsTextItem(f"{cpu_y}%, {cpu_temp} °C")
            cpu_percent.setPos(x2, y2)
            self.other_cpu_scene.addItem(cpu_percent)
            
            self.cpu_items.append(cpu_percent)

            if i > 1:
                self.other_cpu_scene.removeItem(self.cpu_items[i-2])
            
        ## Autoscroll
        if self.other_cpu_performance.sceneRect().width() > 0:
            self.other_cpu_performance.ensureVisible(
                self.other_cpu_performance.sceneRect().width(), 
                0,
                0, 
                self.other_cpu_performance.height()
            )

        ## RAM Graph
        self.other_ram_scene.clear()
        self.ram_items = []
        
        for i in range(1, len(self.ram_data)):
            x1, y1 = self.ram_data[i-1]
            x2, y2 = self.ram_data[i]
            self.other_ram_scene.addLine(x1, y1, x2, y2, pen)
            
            ram_percent = QGraphicsTextItem(f"{ram_y}%, {ram_usage}")
            ram_percent.setPos(x2, y2)
            self.other_ram_scene.addItem(ram_percent)
        
            self.ram_items.append(ram_percent)

            if i > 1:
                self.other_ram_scene.removeItem(self.ram_items[i-2])
        
        ## Autoscroll
        if self.other_ram_performance.sceneRect().width() > 0:
            self.other_ram_performance.ensureVisible(
                self.other_ram_performance.sceneRect().width(), 
                0,
                0, 
                self.other_ram_performance.height()
            )

        ## Network IN/Out
        self.other_network_scene.clear()
        self.network_out_items = []
        
        for i in range(1, len(self.network_out_data)):
            x1, y1 = self.network_out_data[i-1]
            x2, y2 = self.network_out_data[i]
            self.other_network_scene.addLine(x1, y1, x2, y2, pen)
            
            network_out_percent = QGraphicsTextItem(f"{network_out_y} MB, OUT")
            network_out_percent.setPos(x2, y2)
            self.other_network_scene.addItem(network_out_percent)
        
            self.network_out_items.append(network_out_percent)

            if i > 1:
                self.other_network_scene.removeItem(self.network_out_items[i-2])
        
        ## Autoscroll
        if self.other_network_performance.sceneRect().width() > 0:
            self.other_network_performance.ensureVisible(
                self.other_network_performance.sceneRect().width(), 
                0,
                0, 
                self.other_network_performance.height()
            )    
        
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
    
    def performance_benchmark(self):
        self.benchmark_worker = utility.Performance()
        self.thread_manager.start(self.benchmark_worker.benchmark)
        self.benchmark_worker.return_value.connect(self.performance_benchmark_settime)
        #self.performance_seconds.setText()
    
    def performance_benchmark_settime(self, time):
        #print("PERF SET TIME")
        self.performance_seconds.setText(time)

## ========================================
## Projects, Settings, etc. System Functions
## ========================================

    ## ========================================
    ## Project Controls =======================
    ## ========================================
    def project_open(self):
        
        ## This can be shortened into a function somehwere I'm sure
        options = QFileDialog.Options()
        #options |= QFileDialog.DontUseNativeDialog ## Makes a custom popup, sticking with system popup
        #QFileDialog.setDirectory("Modules/General/SaveFiles/")
        fileName, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", f"{sys_path}/Modules/General/SaveFiles/","ProjectFiles (*.zip)", options=options)
        
        print(fileName)
        
        options_list = [
            "load",
            fileName,
        ]
        
        print(fileName)
        
        ## Setting global project path
        self.ProjectPath = fileName
        self.PF.save_framework(options_list)
        
        try:
            ## Sending to loaders, hardcoded because this is where ALL open projects go:
            self.settings_global("/Modules/General/SaveFiles/.tmp_projectfolder/")
            self.sql_global("/Modules/General/SaveFiles/.tmp_projectfolder/")
            self.success_popup([fileName,""])
        except:
            self.ERROR("something","error","Get better at coding lol")
    
    def project_save(self):
        ## if not projectpath #aka if the path for the save file dosen't exist, popopen a save browser
        if self.ProjectPath:
            options_list = [
                "save",
                self.ProjectPath.replace(".zip",""),
            ]
            
            print(self.ProjectPath)
            
            self.PF.save_framework(options_list)
        
        else:
            self.project_saveAs()

    def project_saveAs(self):
        
        dialog = QFileDialog()
        dialog.setAcceptMode(QFileDialog.AcceptSave)  # set the dialog to "save" mode
        dialog.setNameFilter("Text Files (*.zip)")  # set a filter for text files
        # show the dialog and get the selected file name
        if dialog.exec() == QFileDialog.Accepted:
            Project_SaveAs_Location = dialog.selectedFiles()[0]
            
        #print(Project_SaveAs_Location)

        options_list = [
            "save",
            Project_SaveAs_Location,
        ]
            
        self.PF.save_framework(options_list)

    ## Need to change to make more useful & allow inputs with name, (throw error for failed attempts)
    def success_popup(self, info_list):
        filename, placeholder = info_list
        
        QMessageBox.information(
            None,
            ## Title
            'Success! Project Loaded!',
            ## Actual Error
            f'Project {filename} was loaded!',
        )
        
    ## ========================================
    ## Settings ===============================
    ## ========================================
    def settings_global(self, settings_file="default"):
        # intentional lazy import
        import yaml
        try:
            if settings_file != "default":
                with open(sys_path + settings_file, 'r') as f:
                    self.settings_path = sys_path + settings_file
                    self.settings = yaml.safe_load(f)
            
            else:
                with open(sys_path + '/Modules/General/SaveFiles/init_project/settings.yaml', 'r') as f:
                    self.settings_path = sys_path + '/Modules/General/SaveFiles/init_project/settings.yaml'
                    self.settings = yaml.safe_load(f)
                    
            # Getting settings
            #print(self.settings['general']['theme'])
              
        except Exception as e:
            print(e)
        
    
    def load_settings(self):
        pass
        # Loads settings for in program user
    
    def edit_settings(self):
        try:
        # Opens settings for editing
            with open(self.settings_path,"r") as s:
                contents = s.read()
            self.settings_edit.setText(contents)
        except Exception as e:
            self.ERROR([e, 'medium', "Make sure file exists?"])
            
        #pass
    ## Loads and puts settings file on display in the gUI
    
    def write_settings(self):
        try:
            updated_settings = self.settings_edit.toPlainText()
            with open(self.settings_path, "w") as contents:
                contents.write(updated_settings)
        except Exception as e:
            self.ERROR([e, 'medium', "Check permissions? If that fails, make sure the file exists"])
    
    ## ========================================
    ## SQL Conmn ==============================
    ## ========================================
    
    ## Initial Connection =====================
    def sql_global(self, database_file="default"):
        ## The idea here is that this function (being the SQL parent function) gets passed the DB file location. 
        ## once loaded, it creates the self.databse_file, essentially opening it up/passing it along to any other
        ## functions in the program that need to access the DB. (Most notably in 'custom_query', and q_sql)
        
        ## The if else is a guarantee that a project gets loaded, as an extracted project exists in 
        ## the path below. Loading projects uses .tmp_projectfolder which is empty by default
        
        if database_file != "default":
            print("ELSE")
            print(database_file)
            self.sqliteConnection = sqlite3.connect(sys_path + f'/{database_file}/logec_db')
            self.database_file = sys_path + f'/{database_file}/logec_db'
            print(self.database_file)
            #pass
            
        else:
            print("DEFAULT")
            self.sqliteConnection = sqlite3.connect(sys_path + '/Modules/General/SaveFiles/init_project/logec_db')
            print(sys_path + '/Modules/General/SaveFiles/init_project/logec_db')
            self.database_file = sys_path + '/Modules/General/SaveFiles/init_project/logec_db'
            print(self.database_file)
        
        
        ## Getting Q_sql set
        self.q_sql()

    def q_sql(self):
        ## I'm using a mix of Qsql & Sqlite 3 cause I din't think it through before coding this. 
        ## SO, until I fix it, this is gonna have to do.
        ## This affects the query.next() in 'custom_query'
        
        con = QSqlDatabase.addDatabase('QSQLITE')

        con.setDatabaseName(self.database_file)
        print(self.database_file)
        
        print("Database location:", con.databaseName())

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
        #return True
        

    ## Using sqlite3 instead of QSqlite for some reason - I forgot why
    def db_error_write(self, error_list):
        try:
            cursor = self.sqliteConnection.cursor()

            ## if append is not true:
            # [severity, error, fix, "time", "date"]

            sqlite_insert_query = f"""INSERT INTO Error (Severity, ErrorMessage, Fix, Time, Date) 
            VALUES
            ("{error_list[0]}", "{error_list[1]}", "{error_list[2]}", '{error_list[3]}', '{error_list[4]}')"""

            count = cursor.execute(sqlite_insert_query)
            self.sqliteConnection.commit()
            cursor.close()

        except sqlite3.Error as error:
            print('Error:', error)

        #finally:
            #if self.sqliteConnection:
                #self.sqliteConnection.close()

        self.custom_query('performance_error_db')

        ## Giving the DB a refresh

    ## ========================================
    ## Themes =================================
    ## ========================================
    def set_theme(self, theme_name):
        if theme_name != "Default":
            with open(f"{sys_path}/Gui/themes/{theme_name}","r") as f:
                stylesheet = f.read()
                
            self.setStyleSheet(stylesheet)
        else:
            pass


## ========================================
## Startup/Init Code=======================
## ========================================

if __name__ == '__main__':
    try:
        ## Creating App ==================
        app = QtWidgets.QApplication(sys.argv)
        
        ## Library Paths ==================
        library_paths = QCoreApplication.libraryPaths()
        # Print the path where QSqlDatabase is looking for drivers
        print(library_paths)
            
        ## QT stuff ==================
        window = MyApp()
        window.show()
        app.exec()

        ## Kill when exec is closed ==============
        pid = os.getpid()
        os.kill(pid, 15)   ## SIGTERM

    except Exception as e:
        import traceback
        #print(e)
        
        traceback.print_exc()
        
        '''from plyer import notification

        notification.notify(
            title = 'Logec Crash!',
            message = f'SEV: High \nERRMSG: {e} ',
            app_icon = None,
            timeout = 10,
        )
        print(f'ERROR OCCURED: \n{e}')'''
