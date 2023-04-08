#!/bin/python3
##== Global Debug:
GLOBAL_DEBUG = True
# if GLOBAL_DEBUG else None

##== Main Imports
import json
import os
import sys
import random
import sqlite3
import threading
import time
import webbrowser
from functools import partial
import traceback

##== GUI Imports
from PySide6 import QtWidgets
from PySide6.QtCore import Qt, QObject, QThread, QFile, Signal, Slot, QThreadPool, QCoreApplication, QTimer
from PySide6.QtGui import QIcon, QAction, QPen
from PySide6.QtSql import QSqlDatabase, QSqlTableModel, QSqlQuery
from PySide6.QtUiTools import loadUiType, QUiLoader
from PySide6.QtWidgets import (
    QApplication,
    QFileDialog,
    QHeaderView,
    QInputDialog,
    QLabel,
    QLineEdit,
    QMainWindow,
    QMenuBar,
    QMessageBox,
    QPushButton,
    QTableWidget,
    QTableWidgetItem,
    QTableView, QSizePolicy, QAbstractItemView,
    QTabBar,
    QTabWidget,
    QMenu,
    QGraphicsScene, QGraphicsTextItem
)

##== Syspath, first so things can refrence it:
sys_path = os.path.dirname(os.path.abspath(sys.argv[0]))
print("Syspath:" + sys_path) if GLOBAL_DEBUG else None



##== Plugin Path, for SQL driver 
plugin_path = 'plugins'
os.environ['QT_PLUGIN_PATH'] = plugin_path
# Add the path to the plugin directory
QCoreApplication.addLibraryPath(plugin_path)

##== Internal Imports (later so they can refrence using sys path if needed)
from Gui.Encryptor import Ui_Form as Encryptor_Popup
from Gui.listen_popup import Ui_listener_popup
from Gui.portscan_popup import Ui_PortScan_Popup
from Gui.shell_popup import Ui_shell_SEND
from Gui.startup_projectbox import Ui_startup_projectbox
#from Gui.agent_compile import Ui_AgentEditor

from Modules.General.Bruteforce.bruteforce import Bruteforce, Fuzzer
from Modules.General.OSINT.dork import Dork
#from Modules.General.SaveFiles.fileops import *
import Modules.General.SaveFiles.fileops as fileops
from Modules.General.ScriptGen import ScriptGen
from Modules.General.SysShell.shell import Shell
from Modules.General.portscanner import Portscan
import Modules.General.utility as utility
from Modules.Linux.Reverse_Shells.reverse_shells import target as rev_shell_target
from Modules.Windows.Reverse_Shells.win_reverse_shells import target as rev_shell_target_win

from agent.friendly_client import FClient

from gui import Ui_LogecC3

## logging
import logging
logging.basicConfig(level=logging.DEBUG)
logging.basicConfig(filename='osint_reddit.log', filemode='a', format='%(name)s - %(levelname)s - %(message)s', force=True)
#if global_debug:
logging.getLogger().addHandler(logging.StreamHandler())

####################
## Logec Suite Class
####################

class LogecSuite(QMainWindow, Ui_LogecC3):
    def __init__(self, parent=None):
        super(LogecSuite, self).__init__(parent)
        self.setupUi(self)
        ##!! Dev Note, can possible wrap these in a try/except, would help with error handling/developing

        ##== Setup
        self.init_project_settings()
        self.init_thread_manager()

        ##== SQL
        self.init_sql_loading()

        ##== Buttons
        self.init_buttons_file_menu()
        self.init_buttons_c2_shells()
        self.init_buttons_osint_reddit()
        self.init_buttons_bruteforce_credentials()
        self.init_buttons_bruteforce_fuzzer()
        self.init_buttons_bashbuilder()
        self.init_buttons_performance_benchmarks()
        self.init_buttons_settings_settings()

        ##== Data / Tab Inits 
        self.init_data_performance_graphs()
        self.init_data_scanning_portscan()
        self.init_data_sql_tables()
        self.init_data_settings_edit()

        ##== Last but not least, opening project picker
        self.startup_project_open()

    ##== Calling init's for project settings
    def init_project_settings(self) -> None:
        self.sql_global()
        self.settings_global()
        self.PF = fileops.SaveFiles()
        self.ProjectPath = None
        self.c2_layout()

        ##== Setting theme
        self.set_theme(self.settings['general']['theme'])

    ##== Thread Manager
    def init_thread_manager(self) -> None:
        self.thread_manager = QThreadPool()

    ##!! Tempted to move these to their respective function groups, then just call in one init function

    ##== Initial instances for other objects
    def init_instances(self) -> None:
        self.N = utility.Network()
        self.H = utility.Host()

    ##== SQL Table loading
    def init_sql_loading(self) -> None:
        #self.table_RefreshDB_Button.clicked.connect(lambda: self.refresh_db('c2_db'))
        #self.table_RefreshDB_Button.setShortcut('r')

        #self.table_QueryDB_Button.clicked.connect(lambda: self.custom_query('c2_db'))
        #self.table_QueryDB_Button.setShortcut('Return')

        self.table_RefreshDB_Button_main.clicked.connect(lambda: self.refresh_db('main_db'))
        self.table_RefreshDB_Button_main.setShortcut('r')

        self.table_QueryDB_Button_main.clicked.connect(lambda: self.custom_query('main_db'))
        self.table_QueryDB_Button_main.setShortcut('Return')
        ##== Reddit DB
        self.table_RefreshDB_Button_osint_reddit.clicked.connect(lambda: self.refresh_db('reddit_osint_db'))
        self.table_RefreshDB_Button_osint_reddit.setShortcut('r')

        self.table_QueryDB_Button_osint_reddit.clicked.connect(lambda: self.custom_query('reddit_osint_db'))
        self.table_QueryDB_Button_osint_reddit.setShortcut('Return')
        ##== portscan DB
        self.table_RefreshDB_Button_scanning_portscan.clicked.connect(lambda: self.refresh_db('scanning_portscan_db'))
        self.table_RefreshDB_Button_scanning_portscan.setShortcut('r')

        self.table_QueryDB_Button_scanning_portscan.clicked.connect(lambda: self.custom_query('scanning_portscan_db'))
        self.table_QueryDB_Button_scanning_portscan.setShortcut('Return')
        ##==Bruteforce DB
        self.scanning_bruteforce_query.clicked.connect(lambda: self.custom_query('bruteforce_db'))
        self.scanning_bruteforce_query.setShortcut('Return')
        ##==Perfrormance
        self.table_RefreshDB_Button_performance.clicked.connect(lambda: self.custom_query('performance_error_db'))
        
    ####################
    ## Buttons
    ####################
    ##== Button Connectors for the file menu
    def init_buttons_file_menu(self) -> None:
        self.actionOpen_Project.triggered.connect(self.project_open)
        self.actionSave_Project.triggered.connect(self.project_save)
        self.actionSaveAs_Project.triggered.connect(self.project_saveAs)

        self.actionRELOAD.triggered.connect(self.restart)


    ##== Button Connectors for the c2 shell 
    def init_buttons_c2_shells(self) -> None:
        self.c2_systemshell_send.clicked.connect(self.sys_shell)
        self.c2_systemshell_input.setFocus()

        self.c2_servershell_send.clicked.connect(self.c2_server_interact)
        self.friendly_client = FClient()

        self.c2_connect_button.clicked.connect(self.c2_server_connect)
        self.c2_disconnect_button.clicked.connect(self.c2_server_disconnect)
        self.c2_server_password.setEchoMode(QLineEdit.Password)
        self.c2_shell_startup()
    
    ##== Buttons for OSINT reddit
    def init_buttons_osint_reddit(self) -> None:
        self.osint_reddit_search.clicked.connect(self.osint_reddit)
        ## DB table buttons
        self.table_RefreshDB_Button_osint_reddit.clicked.connect(lambda: self.refresh_db('reddit_osint_db'))
        self.table_RefreshDB_Button_osint_reddit.setShortcut('r')
        self.table_QueryDB_Button_osint_reddit.clicked.connect(lambda: self.custom_query('reddit_osint_db'))
        self.table_QueryDB_Button_osint_reddit.setShortcut('Return')
        ## GUI buttons
        ## lamdba for reverse toggle
        self.osint_reddit_gui_hide_search.toggled.connect(lambda x: self.osint_reddit_searchbox.setVisible(not x))

    ##== buttons for Bruteforce Credentials
    def init_buttons_bruteforce_credentials(self) -> None:
        self.bruteforce_start.clicked.connect(self.bruteforce)
        self.bruteforce_stop.clicked.connect(self.bruteforce_hardstop)
        self.bruteforce_user_browse.clicked.connect(partial(self.bf_browser_popup, "username"))
        self.bruteforce_pass_browse.clicked.connect(partial(self.bf_browser_popup, "password"))
        ##== List Downloads
        self.bruteforce_download_ignis_1M.clicked.connect(partial(self.bruteforce_download, "ignis-1M"))
        self.bruteforce_download_seclist_defaults.clicked.connect(partial(self.bruteforce_download, "seclist-defaults"))
        self.bruteforce_download_seclist_top10mil.clicked.connect(partial(self.bruteforce_download, "seclist-top10mil"))
        self.bruteforce_download_seclist_top10mil_usernames.clicked.connect(partial(self.bruteforce_download, "seclist-top10mil-usernames"))
        self.bruteforce_download_seclist_topshort.clicked.connect(partial(self.bruteforce_download, "seclist-top-short"))
    
    ##== buttons for Bruteforce Fuzzer
    def init_buttons_bruteforce_fuzzer(self) -> None:
        self.bruteforce_fuzz_start.clicked.connect(self.bruteforce_fuzzer)
        self.bruteforce_stop.clicked.connect(self.bruteforce_fuzz_hardstop)
        self.bruteforce_fuzz_wordlist_browse.clicked.connect(partial(self.bf_fuzz_browser_popup, "wordlistdir"))
    
    ##== Buttons for bash builder
    def init_buttons_bashbuilder(self) -> None:
        self.bashbuilder_generate.clicked.connect(self.bash_builder)

    ##== buttons for the benchmarks
    def init_buttons_performance_benchmarks(self) -> None:
        self.performance_speedtest.clicked.connect(self.performance_networkspeed)
        self.performance_benchmark_button.clicked.connect(self.performance_benchmark)

    ##== Buttons for settings 
    def init_buttons_settings_settings(self) -> None:
        self.settings_reload.clicked.connect(self.edit_settings)
        self.settings_write.clicked.connect(self.write_settings)
        self.program_reload.clicked.connect(self.restart)

    ####################
    ## Data / Tab Inits
    ####################
    ##== Data for the graphs
    def init_data_performance_graphs(self) -> None:
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
    
    ##== Live updates to port range
    def init_data_scanning_portscan(self) -> None:
        self.portscan_1_1024.toggled.connect(lambda: self.portscan_minport.setText('1'))
        self.portscan_1_1024.toggled.connect(lambda: self.portscan_maxport.setText('1024'))

        self.portscan_1_10000.toggled.connect(lambda: self.portscan_minport.setText('1'))
        self.portscan_1_10000.toggled.connect(lambda: self.portscan_maxport.setText('10000'))

        self.portscan_1_65535.toggled.connect(lambda: self.portscan_minport.setText('1'))
        self.portscan_1_65535.toggled.connect(lambda: self.portscan_maxport.setText('65535'))

    ##== Loading all the data into the respective tables
    def init_data_sql_tables(self) -> None:
        #self.view = self.table_SQLDB
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

    def init_data_settings_edit(self) -> None:
        self.edit_settings()

####################
## Errors, Checks and Debugs
####################
    def handle_error(self, error_list: list) -> None:
        """
        ##== handle_error

        Description:
            Displays a critical error message box with the specified error message, severity, and fix.
            It also writes the error to a database and emits an error signal.

        Args:
            error_list (list): A list containing the error, severity, and fix.

        Returns:
            None
        """
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

        error_list = [severity, error, fix, Time, Date]        
        self.db_error_write(error_list)

    def root_check(self, name:str) -> None:
        """
        ##== Description:
        Check if the program is running as root user

        :param name: name of the program
        """
        if os.geteuid() != 0:
            self.handle_error([f"You are not running as root, note that {name} may not work as expected", "Medium", "Restart program as root"])

####################
## Main SQL Handling
####################

    def clear_db_table(self) -> None:
        self.view.clear()
        self.view.setRowCount(0)

    def refresh_db(self, _from) -> None:
        # removing old rows:
        self.clear_db_table()
        self.custom_query(_from)

    def custom_query(self, _from) -> None:
        """
        ##== custom Query

        Description:
            This handles all the SQL Queries in the program

        Args:
            _from: Where the query is coming from, so the function knows where to display
            The data

        Returns:
            None
        """

        # Setting which QTable Object to output on
        if _from == 'c2_db':
            self.view = self.table_SQLDB
            query_input_raw = self.DB_Query.text()
        elif _from == 'main_db':
            self.view = self.table_SQLDB_main
            query_input_raw = self.DB_Query_main.text()
        elif _from == 'reddit_osint_db':
            self.view = self.table_SQLDB_osint_reddit
            query_input_raw = self.DB_Query_osint_reddit.text()
        elif _from == 'scanning_portscan_db':
            self.view = self.scanning_portscan_db
            query_input_raw = f'{self.DB_Query_scanning_portscan.text()} ORDER BY ScanDate DESC, ScanTime DESC'
        elif _from == 'performance_error_db':
            self.view = self.table_SQLDB_performance_error
            query_input_raw = 'SELECT * FROM Error ORDER BY Date DESC, Time DESC'
        elif _from == 'bruteforce_db':
            self.view = self.scanning_bruteforce_db
            query_input_raw = f'{self.DB_Query_scanning_bruteforce.text()} ORDER BY DATE DESC, TIME DESC'
        else:
            query_input_raw = ""
            self.view = ""
            self.handle_error(['No Query Input Provided', 'Low', 'Enter an input to fix'])
            return

        # Temp workaround for shortcuts not working"
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

        print(query_input)
        '''

        # Clearing DB and resetting _from
        self.clear_db_table()
        # _from = None

        # Getting query data
        query = QSqlQuery(query_input)
        # Connecting to DB for more data
        connection = sqlite3.connect(self.database_file)
        try:
            cursor = connection.execute(query_input)
            names = [x[0] for x in cursor.description]
            connection.close()
            ## variabels for the column/row names
            names_num = 0
            names_list = []
            query_num = 0
            

            # Loop for column names
            for i in names:
                names_list.append(i)
                names_num += 1

            ## Column formattiing
            self.view.setColumnCount(len(names_list))
            self.view.setHorizontalHeaderLabels(names_list)


            # Loop for data in each column
            while query.next():
                rows = self.view.rowCount()
                self.view.setRowCount(rows + 1)

                for i in range(0, len(names_list)):
                    self.view.setItem(rows, i, QTableWidgetItem(str(query.value(i))))

                query_num += 1

            ## auto resizes
            self.view.resizeColumnsToContents()
            
            ## Scroll Mode:
            self.view.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
            self.view.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)
            
            ## width
            max_width = int(self.settings['sql_table_view']['max_column_width'])
            for i in range(self.view.columnCount()):
                width = min(self.view.columnWidth(i), max_width)
                self.view.setColumnWidth(i, width)
            
            ##height 
            max_height = int(self.settings['sql_table_view']['max_row_height'])
            for i in range(self.view.rowCount()):
                height = min(self.view.rowHeight(i), max_height)
                self.view.setRowHeight(i, height)

                
        except sqlite3.OperationalError as operror:
            logging.warn(f"[SQL] Operational error: {operror}")
            self.handle_error([operror, "warn", "Enter a valid SQL query"])
        except sqlite3.Error as error:
            #print('Error:', error) if GLOBAL_DEBUG else None
            logging.warn(f"[SQL]Error writing to SQL DB: {error}")
        except Exception as e:
            logging.warn(f"[SQL] Unkown error: {e}")


####################
## C2
####################

##== C2 Local 

    def c2_layout(self) -> None:
        """
        ##== c2_layout

        Description:
            This handles the layout of the C2 tab, as you can't add a nested bar with QT Designer

        """
        # create menu bar
        self.c2_menuBar = QMenuBar()

        # create options tab
        self.menuOptions = QMenu("Options", self.c2_menuBar)
        self.actionQuit = QAction('Quit', self)
        self.actionQuit.triggered.connect(self.close)
        self.menuOptions.addAction(self.actionQuit)
        self.c2_menuBar.addAction(self.menuOptions.menuAction())

        # create client tab
        self.menuClient = QMenu("Client", self.c2_menuBar)
        self.actionStart_Listener = QAction('Start Listener', self)
        self.actionClient_Editor = QAction('Client Editor', self)

        # add actions to the menu bar
        self.menuClient.addAction(self.actionStart_Listener)
        self.menuClient.addAction(self.actionClient_Editor)
        self.c2_menuBar.addAction(self.menuClient.menuAction())
        # set menu bar
        self.tabWidget.widget(0).layout().setMenuBar(self.c2_menuBar)

        ##
        self.actionClient_Editor.triggered.connect(self.c2_editor)

    ## Gonna need some work, this currently creates one thread for each command
    def sys_shell(self):
        """
        Description:
            The handler for the local system (partially interactive) shell

        """
        
        # get input list from GUI
        input_list = [self.c2_systemshell_input.text()]

        # create worker
        self.sysshell_worker = Shell()

        # start thread
        self.thread_manager.start(partial(self.sysshell_worker.shell_framework, input_list))

        # connect output to function
        self.sysshell_worker.sys_out.connect(self.sys_shell_results)

    def sys_shell_results(self, results):
        """
        Description:
            Displays results onto the GUI

        """
        try:
            # set results
            self.c2_systemshell.setText(results)
            self.c2_systemshell_input.setText("")
        except Exception as e:
            print(e) if GLOBAL_DEBUG else None

    def c2_editor(self):
        ## Lazy imports
        #from Gui.startup_projectbox import Ui_startup_projectbox
        
        self.c2_window = QtWidgets.QMainWindow()
        self.c2_editor_popup = Ui_AgentEditor()#Ui_startup_projectbox()
        self.c2_editor_popup.setupUi(self.window)
        self.window.show()
        
        ## ========================================
        ## Startup Buttons ========================
        ## ========================================
        ## down here due to the import, and it technically being in a different class
        #self.project_popup.startup_project_openproject.clicked.connect(self.project_open)
        #self.project_popup.startup_project_exit.clicked.connect(self.program_exit)

##== C2 Server Interaction
        """
        ##== c2 Server

        Description:
            These functions handle the server connetion to the C2 server

        """

    def c2_shell_startup(self):
        dir_path = sys_path + "/agent/ascii-art/"
        files = os.listdir(dir_path)
        with open(dir_path + random.choice(files), "r") as graphic:
            self.shell_text_update(graphic.read())
        
    def c2_server_connect(self):
        ## if connected this stops you from connecting with an already active session
        if not self.friendly_client.authenticated:
            connlist = [
                self.c2_server_ip.text(),
                self.c2_server_port.text(),
                self.c2_server_username.text(),
                self.c2_server_password.text(),
            ]

            self.friendly_client.connect_to_server(connlist)

            ## return not working, so getting validated authentication via the class itself
            if self.friendly_client.authenticated:
                self.c2_status_label.setText(f"Status: Connected to {connlist[0]}:{connlist[1]}")
            
           # if self.friendly_client.err_ConnRefused_0x01:
                #self.handle_error(["ConnRefused_0x01","Low","Make sure the server is alive"])
                #self.friendly_client.err_ConnRefused_0x01 = False
    
    def c2_server_disconnect(self):
        self.friendly_client.client_disconnect()
        self.c2_status_label.setText(f"Status: Disconnected")
        
    def c2_server_interact(self, command):
        input = self.c2_servershell_input.text()

        
        self.thread_manager.start(partial(self.friendly_client.gui_to_server, input))
        self.friendly_client.shell_output.connect(self.shell_text_update)
    
        ## clearing text
        self.c2_servershell_input.setText("")
    
    def shell_text_update(self, input):
        print("shell_text_update" + input) if GLOBAL_DEBUG else None
        self.c2_servershell.setText(input)


####################
## Scanning Enumeration
####################
        """
        ##== Scanning & Enum

        Description:
            These functions handle the server connetion to the C2 server

        """
##== Portscan Handler
    """
    ##== Portscan Handler

    Description: The handler for the portscan module. 
    """
    def portscan(self, QObject):
        input_ip = self.portscan_IP.text()
        print(input_ip) if GLOBAL_DEBUG else None

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

            print(f'TIMOUT: {timeout}') if GLOBAL_DEBUG else None
            
            print(f'DELAY: {delay}') if GLOBAL_DEBUG else None
            
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
            self.handle_error([ve, "low", "Make sure all respective fields are filled"])

        except Exception as e:
            self.handle_error([e, "??", "Unkown Error - most likely a code issue (AKA Not your fault)"])

##== GUI bar  
    def portscan_bar(self, status): ## I wonder if this dosen't work due to all the threads waiting to join back up? maybe portscanner writing the value to a tmp file would have to do it, or to the DB in a .hiddentable
        self.stealth_bar.setValue(status)
        if self.stealth_bar.value() == 99:
            self.stealth_bar.setValue(100)
##GUI Liveports
    def portscan_liveports(self, ports):
        self.portscan_liveports_browser.setText("")
        #self.portscan_liveports_browser.setText(str(ports))
        for i in ports:
            self.portscan_liveports_browser.append(f"[+] {i}/tcp")
## Database
        """
        Description:
            Writing to the DB, will probably need a re-work, or at least point to a standard
            DB write function

        """
    def portscan_database_write(self, list):
        print("DB Triggered") if GLOBAL_DEBUG else None
        try:
            cursor = self.sqliteConnection.cursor()
            
            ## Picked up this trick from chatGPT, basically each item coresponds to the number in list
            IP, PORT, SCANTYPE, SCANDATE, SCANTIME, RUNTIME, SCANNEDPORTS, DELAY = list
            
            sqlite_insert_query = f"""INSERT INTO PortScan (IP, PORT, ScanType, ScanDate, ScanTime, RunTime, ScannedPorts, Delay) 
            VALUES
            ({IP}, {str(PORT).replace("{","").replace("}","")}, '{SCANTYPE}', '{SCANDATE}', '{SCANTIME}', '{RUNTIME}', "{SCANNEDPORTS}", '{DELAY}')"""
            
            print(sqlite_insert_query) if GLOBAL_DEBUG else None

            cursor.execute(sqlite_insert_query)
            self.sqliteConnection.commit()
            cursor.close()
            
        except Exception as e:
            self.handle_error([e, "Medium", "??"])

##== BashBuilder
    """

    Description: The Bash Builder function 
    """
    def bash_builder(self):
        self.Script = ScriptGen.Script()
        
        ## Doing json here for expandability, rather than a list
        ## If the checks are checked, they return true. The scriptgen.py uses true & false
        ## for which blocks to build with
        print(self.bashbuild_diagnostic.isChecked())  if GLOBAL_DEBUG else None
        
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
        
        print(packed_json) if GLOBAL_DEBUG else None
        
        self.Script.script_results.connect(self.bash_builder_display)
        
        ## Has to go last to grab signals n stiff
        self.Script.script_framework(packed_json)        
##GUI Updater
    def bash_builder_display(self, final_script):
        print("triggered") if GLOBAL_DEBUG else None
        self.bashbuild_textoutput.setText(final_script)

##== dns_lookup
    """

    Description: The DNS handler code
    """
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
            self.handle_error([
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
## GUI Formatter
    """
    Desc: Formats the results into tables

    Inputs:
        table_object:
        list: 
        name:

    """
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

####################
## Bruteforce
####################
## == Bruteforce (credentials)
    """
    Desc: Bruteforces credentials

    inputs:
        See target_list, all that is gathered from the GUI


    """
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
            self.bruteforce_worker.module_error.connect(partial(self.handle_error, target_list))
            
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
            self.handle_error([ve, "low", "Make sure all respective fields are filled"])

        except Exception as e:
            self.handle_error([e, "??", "Unkown Error - most likely a code issue (AKA Not your fault)"])

    def bruteforce_hardstop(self):
        #pass
        print("clicked") if GLOBAL_DEBUG else None
        try:
            pass
            #self.bruteforce_worker.thread_quit()
            #self.bruteforce_thread.exit() # exi works better than quit
            #self.bruteforce_worker.deleteLater()
        except Exception as e:
            self.handle_error([e, "Low", "Bruteforce is probably not running"])

    def bf_browser_popup(self, whichbutton):
        from PySide6.QtWidgets import QFileDialog
        print("Clicked") if GLOBAL_DEBUG else None
        
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","All Files (*);;Python Files (*.py)", options=options)
        
        if whichbutton == "username":
            self.bruteforce_userdir.setText(fileName)
        
        elif whichbutton == "password":
            self.bruteforce_passdir.setText(fileName)

## Bruteforce GUI Stuff

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
## Bruteforce Downlaod Stuff
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
## Bruteforce DB Stuff
    def bruteforce_database_write(self, list):
        print("DB Triggered")  if GLOBAL_DEBUG else None
        try:
            cursor = self.sqliteConnection.cursor()
            
            ## Picked up this trick from chatGPT, basically each item coresponds to the number in list
            TARGET, PORT, SERVICE, CREDS, TIME, DATE = list
            
            sqlite_insert_query = f"""INSERT INTO 'BRUTEFORCE-Creds' (Target, Port, Service, Credentials, Time, Date) 
            VALUES
            ('{TARGET}', '{str(PORT).replace("{","").replace("}","")}', '{SERVICE}', '{CREDS}', '{TIME}', '{DATE}' )"""
            
            print(sqlite_insert_query) if GLOBAL_DEBUG else None

            cursor.execute(sqlite_insert_query)
            self.sqliteConnection.commit()
            cursor.close()
            
        except Exception as e:
            self.handle_error([e, "Medium", "??"])
   
##== Fuzzer    
    """
    Desc: Bruteforces websites/fuzzes things

    inputs:
        See target_list, all that is gathered from the GUI


    """
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
            self.fuzzer_worker.module_error.connect(partial(self.handle_error, target_list))
            
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
            self.handle_error([ve, "low", "Make sure all respective fields are filled"])

        except Exception as e:
            self.handle_error([e, "??", "Unkown Error - most likely a code issue (AKA Not your fault)"])
            
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno) if GLOBAL_DEBUG else None

    def bruteforce_fuzz_hardstop(self):
        #pass
        print("clicked") if GLOBAL_DEBUG else None
        try:
            pass
            #self.fuzzer_worker.thread_quit()
            #self.fuzzer_thread.exit() # exi works better than quit
            #self.fuzzer_worker.deleteLater()
        except Exception as e:
            self.handle_error([e, "Low", "Fuzzer is probably not running"])

    def bf_fuzz_browser_popup(self, whichbutton):
        from PySide6.QtWidgets import QFileDialog
        print("Clicked") if GLOBAL_DEBUG else None
        
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","All Files (*);;Python Files (*.py)", options=options)
        
        if whichbutton == "wordlistdir":
            self.bruteforce_fuzz_wordlistdir.setText(fileName)
##== Fuzzer GUI stuff
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
##== Fuzzer DB Stuff
    def bruteforce_fuzz_database_write(self, list):
        print("BF Fuzzer DB Triggered") if GLOBAL_DEBUG else None
        try:
            cursor = self.sqliteConnection.cursor()
            
            ## Picked up this trick from chatGPT, basically each item coresponds to the number in list
            TARGET, PORT, CODE,SHORT_URL, LONG_URL, TIME, DATE = list
            
            sqlite_insert_query = f"""INSERT INTO 'BRUTEFORCE-Fuzzer' (Target, Port, Code, Short_Url, Long_Url, Time, Date) 
            VALUES
            ('{TARGET}', '{str(PORT).replace("{","").replace("}","")}', '{CODE}', '{SHORT_URL}', '{LONG_URL}', '{TIME}', '{DATE}' )"""
            
            print(sqlite_insert_query)  if GLOBAL_DEBUG else None

            cursor.execute(sqlite_insert_query)
            self.sqliteConnection.commit()
            cursor.close()
            
        except Exception as e:
            self.handle_error([e, "Medium", "??"])

####################
## OSINT
####################       

##== Reddit OSINT
    """
    Needs to move to Qthread
    """

    def osint_reddit(self):
        ## lazy import for performance/easy err handling
        try:
            from Modules.General.OSINT.reddit_osint import OsintReddit
        except Exception as e:
            self.handle_error(e, "Medium", "error")

        ## need to load credentials
        ## using a dict so I don't have to worry about the order. Just makes this side cleaner
        credentials = {
            "username" : self.settings['osint']['reddit']['username'],
            "password" : self.settings['osint']['reddit']['password'],
            "secret_token" : self.settings['osint']['reddit']['secret_token'],
            "client_id" : self.settings['osint']['reddit']['client_id']
            }
    
        keyword = self.osint_reddit_keyword.text()

        ## == Error handling

        if keyword == '':
            self.handle_error([
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
            
            ## Type Filter
            if self.osint_reddit_onlycomments.isChecked():
                stype = "comments"
            elif self.osint_reddit_onlyprofile.isChecked():
                stype = "profile"
            elif self.osint_reddit_onlysubreddit.isChecked():
                stype = "subreddit"
            elif self.osint_reddit_onlypost.isChecked():
                stype = "post"   
            else:
                print("STYPE ERROR")
                #stype = "post"       
                
            '''only_comments = self.osint_reddit_onlycomments.isChecked()
            only_profile = self.osint_reddit_onlyprofile.isChecked()'''

            # if subreddit empty, don't search by sub
            '''if subreddit != '':
                search_subbreddit = False
            else:
                search_subbreddit = True'''

            ## Convert to DICT eventuallly, keeping as list for now
            search_list = [keyword, "subreddit", time, sort, limit, stype]
            
            options_list = [
                download_media,
                "search_subbreddit",
            ]

            ## creating class instance
            #r = OsintReddit(credentials)
            self.osint_reddit_worker = OsintReddit(credentials)
            self.thread_manager.start(partial(self.osint_reddit_worker.osint_reddit_framework, search_list, options_list))
            #r.osint_reddit_framework(search_list, options_list)

            ## Clearing RedditResults table
            self.sql_db_write("DELETE FROM RedditResults")

            self.osint_reddit_worker.result_list.connect(self.osint_reddit_db_write)
            self.osint_reddit_worker.search_url.connect(self.osint_reddit_search_url_display)
        
            #self.osint_reddit_search.setText('-->> Search <<--')
            
        
            ## bar
            ## its putting the bar at 100% right away due to it being after the r.main... hmmm need a way to fix that
            
            ##== progress bar stuff
            #maxval = r.total_posts
            #currentval = r.current_post

            #self.reddit_progressbar.setMaximum(maxval)
            #self.reddit_progressbar.setValue(currentval)
    def osint_reddit_search_url_display(self, url):
        print("URL SET TRIGGERED")
        self.osint_reddit_searchurl.setText(url.replace("oauth.",""))
            
    def osint_reddit_db_write(self, list_to_write):
        """Generates a string for sql_db_write to write to DB

        Args:
            list_to_write (list): a list with the info needed.
        """ 
        try:
            subreddit, title, comment, upvote, downvote, post_url, media_url, date, time, user = list_to_write
            
            #print(list_to_write)
            
            query = f"""INSERT INTO RedditResults  (
                "Subreddit",
                "Title",
                "Comment",
                "User",
                "Upvotes",
                "Downvotes",
                "PostURL",
                "MediaURL",
                "CreationDate",
                "CreationTime"
            )
            VALUES
            ("{subreddit}", "{title}", "{comment}", '{user}', '{upvote}', "{downvote}", "{post_url}", "{media_url}", '{time}', '{date}')"""
            self.sql_db_write(query)

        except Exception as e:
            logging.warning("[Logec (RedditOsint)]Error with formatting SQL Query")
        

##== Google Dork

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
            self.handle_error([e, "??", "Unkown Error - most likely a code issue (AKA Not your fault)"])
## Google Dork GUI     
    def dork_query_display(self, dork_query):
        self.osint_dork_output.setText(dork_query)


###################
## Other Tab
###################
    """
    the other tab is for everything Ihave no idea where to put
    """
##== Graph Draw    

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
        
##== Graph Data    

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
##== Netowrk Bench       
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
##== CPU Bench
    def performance_benchmark(self):
        self.benchmark_worker = utility.Performance()
        self.thread_manager.start(self.benchmark_worker.benchmark)
        self.benchmark_worker.return_value.connect(self.performance_benchmark_settime)
        #self.performance_seconds.setText()
    
    def performance_benchmark_settime(self, time):
        #print("PERF SET TIME")
        self.performance_seconds.setText(time)

####################
## Settings & Controls
####################

##== Project Startup
        """

        Description:
            Handles the startup popup box

        """
    def startup_project_open(self):
        ## Lazy imports
        #from Gui.startup_projectbox import Ui_startup_projectbox
        
        self.window = QtWidgets.QMainWindow()
        self.project_popup = Ui_startup_projectbox()
        self.project_popup.setupUi(self.window)
        self.window.show()
        
        ## ========================================
        ## Startup Buttons ========================
        ## ========================================
        ## down here due to the import, and it technically being in a different class
        self.project_popup.startup_project_openproject.clicked.connect(self.project_open)
        self.project_popup.startup_project_exit.clicked.connect(self.program_exit)
    
##== Project Controls
        """
        Description:
            Handles the saving/opening of project files

        """
    def project_open(self):
        
        ## This can be shortened into a function somehwere I'm sure
        options = QFileDialog.Options()
        #options |= QFileDialog.DontUseNativeDialog ## Makes a custom popup, sticking with system popup
        #QFileDialog.setDirectory("Modules/General/SaveFiles/")
        fileName, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", f"{sys_path}/Modules/General/SaveFiles/","ProjectFiles (*.zip)", options=options)
        
        print(fileName) if GLOBAL_DEBUG else None
        
        options_list = [
            "load",
            fileName,
        ]
        
        print(fileName) if GLOBAL_DEBUG else None
        
        ## Setting global project path
        self.ProjectPath = fileName
        self.PF.save_framework(options_list)
        
        try:
            ## Sending to loaders, hardcoded because this is where ALL open projects go:
            self.settings_global("/Modules/General/SaveFiles/.tmp_projectfolder/")
            self.sql_global("/Modules/General/SaveFiles/.tmp_projectfolder/")
            self.success_popup([fileName,""])
        except:
            self.handle_error("something","error","Get better at coding lol")
    
    def project_save(self):
        ## if not projectpath #aka if the path for the save file dosen't exist, popopen a save browser
        if self.ProjectPath:
            options_list = [
                "save",
                self.ProjectPath.replace(".zip",""),
            ]
            
            print(self.ProjectPath) if GLOBAL_DEBUG else None
            
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
        
##== Settings
        """
        Description:
            Handles the settings file
            
        accesing settings:
        self.settings[setting][setting]

        """
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
                    print("Succesfully opened default project")
                    
            # Getting settings
            print(self.settings['general']['theme'])
              
        except Exception as e:
            logging.warning(f"[LogecSuite (Settings)] Error loading Settings: {e}")
            print(e) if GLOBAL_DEBUG else None
        
    
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
            self.handle_error([e, 'medium', "Make sure file exists?"])
            
        #pass
    ## Loads and puts settings file on display in the gUI
    
    def write_settings(self):
        try:
            updated_settings = self.settings_edit.toPlainText()
            with open(self.settings_path, "w") as contents:
                contents.write(updated_settings)
        except Exception as e:
            self.handle_error([e, 'medium', "Check permissions? If that fails, make sure the file exists"])
    
##== SQL Communication
        """
        Description:
            Handles the SQL communication

        """
    
    ## Initial Connection =====================
    def sql_global(self, database_file="default"):
        ## The idea here is that this function (being the SQL parent function) gets passed the DB file location. 
        ## once loaded, it creates the self.databse_file, essentially opening it up/passing it along to any other
        ## functions in the program that need to access the DB. (Most notably in 'custom_query', and q_sql)
        
        ## The if else is a guarantee that a project gets loaded, as an extracted project exists in 
        ## the path below. Loading projects uses .tmp_projectfolder which is empty by default
        
        if database_file != "default":
            print("ELSE") if GLOBAL_DEBUG else None
            print(database_file) if GLOBAL_DEBUG else None
            self.sqliteConnection = sqlite3.connect(sys_path + f'/{database_file}/logec_db')
            self.database_file = sys_path + f'/{database_file}/logec_db'
            print(self.database_file) if GLOBAL_DEBUG else None
            #pass 
            
        else:
            print("DEFAULT") if GLOBAL_DEBUG else None
            self.sqliteConnection = sqlite3.connect(sys_path + '/Modules/General/SaveFiles/init_project/logec_db')
            print(sys_path + '/Modules/General/SaveFiles/init_project/logec_db') if GLOBAL_DEBUG else None
            self.database_file = sys_path + '/Modules/General/SaveFiles/init_project/logec_db'
            print(self.database_file) if GLOBAL_DEBUG else None
        
        
        ## Getting Q_sql set
        self.q_sql()

    def q_sql(self):
        ## I'm using a mix of Qsql & Sqlite 3 cause I din't think it through before coding this. 
        ## SO, until I fix it, this is gonna have to do.
        ## This affects the query.next() in 'custom_query'
        
        con = QSqlDatabase.addDatabase('QSQLITE')

        con.setDatabaseName(self.database_file)
        print(self.database_file) if GLOBAL_DEBUG else None
        
        print("Database location:", con.databaseName()) if GLOBAL_DEBUG else None

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
                print('Error connecting to DB & QApp not constructed.') if GLOBAL_DEBUG else None
        #return True
    
    ## SQL global writer
    def sql_db_write(self, query):
        """
        The global write function. Not fully utilized, some modules still need to be moved here. 
        Handy as it's a one stop shop into the DB and prevents lockups
        
        Each module that needs to write here needs a db_write method that provides the query string

        Args:
            query (str): The query for SQL
            Looks like: INSER INTO tablename (column, column2)
        """
        try:
            cursor = self.sqliteConnection.cursor()
            
            cursor.execute(query)
            self.sqliteConnection.commit()
            cursor.close()

        ## this first as sqlite3.error is a catchall
        except sqlite3.OperationalError as operror:
            logging.warn(f"[SQL] Operational error: {operror}")
            self.handle_error([operror, "warn", "Enter a valid SQL query"])

        except sqlite3.Error as error:
            #print('Error:', error) if GLOBAL_DEBUG else None
            logging.warn(f"[SQL]Error writing to SQL DB: {error}")

        except Exception as e:
            logging.warn(f"[SQL] Unkown error: {e}")

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
            print('Error:', error) if GLOBAL_DEBUG else None

        #finally:
            #if self.sqliteConnection:
                #self.sqliteConnection.close()

        self.custom_query('performance_error_db')

        ## Giving the DB a refresh

##== Themes
        """
        Description:
            Handles the theme settings

        """
    def set_theme(self, theme_name):
        if theme_name != "Default":
            with open(f"{sys_path}/Gui/themes/{theme_name}","r") as f:
                stylesheet = f.read()
                
            self.setStyleSheet(stylesheet)
        else:
            pass

##== Sys Functions
        """
        Description:
            Handles the system functions like restarting the program
        """
        
    def restart(self): ## MEMORY LEAK !!
        # Restart the Python interpreter
        args = sys.argv[:]
        args.insert(0, sys.executable)
        self.close()
        sys.exit(os.spawnvp(os.P_WAIT, sys.executable, args))
        
    def program_exit(self):
        sys.exit()



if __name__ == '__main__':
    try:
        # Creating App
        app = QtWidgets.QApplication(sys.argv)

        # Library Paths
        library_paths = QCoreApplication.libraryPaths()
        # Print the path where QSqlDatabase is looking for drivers
        print(library_paths) if GLOBAL_DEBUG else None

        # QT stuff
        window = LogecSuite()
        window.show()
        app.exec()

        # Kill when exec is closed
        pid = os.getpid()
        os.kill(pid, 15)   # SIGTERM

    except Exception as e:
        traceback.print_exc()
