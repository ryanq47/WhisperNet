#!/bin/python3
##== Global Debug:
GLOBAL_DEBUG = True
# if GLOBAL_DEBUG else None

##== Main Imports
import json
import os
import subprocess
import sys
import random
import sqlite3
import threading
#import time
#import webbrowser
from functools import partial
import traceback

##== GUI Imports
from PySide6 import QtWidgets
from PySide6.QtCore import Qt, QThread, QThreadPool, QCoreApplication, QTimer, QPoint
from PySide6.QtGui import QAction, QPen, QFont
from PySide6.QtSql import QSqlDatabase, QSqlQuery
#from PySide6.QtUiTools import loadUiType, QUiLoader
from PySide6.QtWidgets import (
    QApplication,
    QFileDialog,
    QHeaderView,
    QLineEdit,
    QMainWindow,
    QMenuBar,
    QMessageBox,
    QPushButton,
    QTableWidgetItem,
    QAbstractItemView,
    QMenu,
    QGraphicsScene, QGraphicsTextItem
)

##== Syspath, first so things can refrence it:
sys_path = os.path.dirname(os.path.abspath(sys.argv[0]))
#print("Syspath:" + sys_path) if GLOBAL_DEBUG else None


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
from Modules.ExploitNVulns.exploitdb import LogecExploitdb

from agent.friendly_client import FClient

from gui import Ui_LogecC3

## logging
import logging
#logging.basicConfig(level=logging.DEBUG)
logging.basicConfig(filename='logs/logec-main.log', filemode='a', format='%(asctime)s - %(levelname)s - %(message)s', force=True)

#if global_debug:
#logging.getLogger().addHandler(logging.StreamHandler())


####################
## Logec Suite Class
####################

class LogecSuite(QMainWindow, Ui_LogecC3):
    def __init__(self):
        super(LogecSuite, self).__init__()
        self.setupUi(self)
        ##!! Dev Note, can possible wrap these in a try/except, would help with error handling/developing

        ##== Setup
        self.init_project_settings()
        self.init_thread_manager()
        ##== Getting logging going ASAP
        self.log_level_handler()

        
        ##== instances
        self.init_instances()

        ##== SQL Buttons
        self.init_sql_loading()

        ##== Other Buttons
        self.init_buttons_file_menu()
        self.init_buttons_c2_shells()
        self.init_buttons_exploitandvuln()
        self.init_buttons_osint_reddit()
        self.init_buttons_scanning()
        self.init_buttons_bruteforce_credentials()
        self.init_buttons_bruteforce_fuzzer()
        self.init_buttons_bashbuilder()
        self.init_buttons_performance_benchmarks()
        self.init_buttons_settings_settings()

        ##== Data / Tab Inits 
        ## Graphs are using lots of CPU, disabled for now.
        #self.init_data_performance_graphs()
        self.init_data_scanning_portscan()
        self.init_data_sql_tables()
        self.init_data_settings_edit()

        ## Font has to be set here for some reason
        font = QFont(self.settings['System']['Themes']['Font'], self.settings['System']['Themes']['FontSize'])
        QApplication.setFont(font)

        ##== Last but not least, opening project picker
        self.startup_project_open()
        self.content_setup()
        


    ##== Calling init's for project settings
    def init_project_settings(self) -> None:
        self.sql_global()
        self.settings_global()
        self.PF = fileops.SaveFiles()
        self.ProjectPath = None
        self.c2_layout()

        ##== Setting theme
        self.set_theme(self.settings['System']['Themes']['Theme'])

    ##== Thread Manager
    def init_thread_manager(self) -> None:
        self.thread_manager = QThreadPool()

    ##!! Tempted to move these to their respective function groups, then just call in one init function

    def log_level_handler(self):
        ## these are class vars and not local so I can change them if needed anywhere in the program
        self.log_level = self.settings['System']['Logging']['LogLevel']
        self.print_logs_to_console = self.settings['System']['Logging']['PrintToConsole']

        if self.log_level.lower() == "debug":
            logging.basicConfig(level=logging.DEBUG)
        elif self.log_level.lower() == "info":
            logging.basicConfig(level=logging.INFO)
        elif self.log_level.lower() == "warning":
            logging.basicConfig(level=logging.WARNING)
        elif self.log_level.lower() == "critical":
            logging.basicConfig(level=logging.CRITICAL)
        ## backup to insure logging incase these break for some reason
        else:
            logging.basicConfig(level=logging.DEBUG)
        # print to console or not
        if self.print_logs_to_console:
            logging.getLogger().addHandler(logging.StreamHandler())

        logging.info(f"[Logec (log_level_handler)]: Log settings: LogLevel: {self.log_level} PrintToConsole: {self.print_logs_to_console}")

    ##== Initial instances for other objects
    def init_instances(self) -> None:
        #self.N_worker = utility.Network()
        #self.thread_manager.start(
        
        self.H = utility.Host()

    ##== SQL Table loading
    def init_sql_loading(self) -> None:
        """This maps all the SQL buttons for all the tables/viewers across the program
        """
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
        self.scanning_bruteforce_refresh.clicked.connect(lambda: self.refresh_db('bruteforce_db'))
        self.scanning_bruteforce_refresh.setShortcut('r')

        ##Bruteforce Fuzzer
        self.scanning_bruteforce_fuzzer_query.clicked.connect(lambda: self.custom_query('bruteforce_fuzzer_db'))
        self.scanning_bruteforce_fuzzer_query.setShortcut('Return')
        self.scanning_bruteforce_fuzzer_refresh.clicked.connect(lambda: self.refresh_db('bruteforce_fuzzer_db'))
        self.scanning_bruteforce_fuzzer_refresh.setShortcut('r')
        
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
        # Main account that the user interacts with
        self.friendly_client = FClient()
        # Account used for background work
        self.friendly_client_background_worker = FClient()

        # conn to server
        self.c2_connect_button.clicked.connect(self.c2_server_connect)
        self.c2_disconnect_button.clicked.connect(self.c2_server_disconnect)
        self.c2_server_password.setEchoMode(QLineEdit.PasswordEchoOnEdit)
        self.c2_shell_startup()

        #local server spin up
        self.c2_server_password_local.setEchoMode(QLineEdit.PasswordEchoOnEdit)
        self.c2_start_server_local.clicked.connect(self.c2_localserver_start)
        self.c2_stop_server_local.clicked.connect(self.c2_localserver_start)
        

        ## GUI buttons/toggles
        self.c2_gui_hide_clients.toggled.connect(lambda x: self.c2_gui_groupbox_clients.setVisible(not x))
        self.c2_gui_hide_shells.toggled.connect(lambda x: self.c2_gui_groupbox_shells.setVisible(not x))
        self.c2_gui_hide_options.toggled.connect(lambda x: self.c2_gui_groupbox_options.setVisible(not x))
    
        ## client gui
        self.c2_client_table_setup()

    def init_buttons_exploitandvuln(self):
        self.exploitandvuln_search_button.clicked.connect(self.exploit_and_vuln_search)

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

    def init_buttons_scanning(self) -> None:
        self.scanning_dns_lookup.clicked.connect(self.dns_lookup)
        self.portscan_start.clicked.connect(self.portscan)

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
        """this function LOADS the data into each table on starutp
        """
        #self.view = self.table_SQLDB
        ## Showing help table on startup
        self.DB_Query_main.setText('select * from Help')
        self.custom_query('main_db')

        self.DB_Query_osint_reddit.setText('SELECT * FROM RedditResults')
        self.custom_query('reddit_osint_db')

        self.DB_Query_scanning_portscan.setText('select * from PortScan')
        self.custom_query('scanning_portscan_db')

        self.DB_Query_scanning_bruteforce.setText('select * from "BRUTEFORCE-creds"')
        self.custom_query('bruteforce_db')
        
        self.DB_Query_scanning_bruteforce_fuzzer.setText('select * from "BRUTEFORCE-Fuzzer"')
        self.custom_query('bruteforce_fuzzer_db')

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
            This handles all the SQL Queries in the program for the TABLE VIEWS. basically it grabs the data
            and formats the tables as needed. Does not use sql_db_read as I have not moved it over to that yet

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
        elif _from == 'bruteforce_fuzzer_db':
            self.view = self.scanning_bruteforce_fuzzer_db
            query_input_raw = f'{self.DB_Query_scanning_bruteforce_fuzzer.text()} ORDER BY DATE DESC, TIME DESC'    
        
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

            ## Get current value of selected item, pass to right click menu
            
            self.sql_right_click_menu(self.view, "http://google.com")

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
            max_width = int(self.settings['Sql']['SqlTableView']['MaxColumnWidth'])
            for i in range(self.view.columnCount()):
                width = min(self.view.columnWidth(i), max_width)
                self.view.setColumnWidth(i, width)
            
            ##height 
            max_height = int(self.settings['Sql']['SqlTableView']['MaxRowHeight'])
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
            
    ## right click stuff
    def sql_right_click_menu(self, tablename, cellvalue):
        self.view.setContextMenuPolicy(Qt.CustomContextMenu)
        self.view.customContextMenuRequested.connect(partial(self.show_cell_menu, cellvalue))

    def show_cell_menu(self, cellvalue, pos: QPoint):
        global_pos = self.view.mapToGlobal(pos)
        menu = QMenu()
        web_search = menu.addAction("Web Search")
        menu.addAction("Action 2")
        
        web_search.triggered.connect(partial(self.global_browser, cellvalue))
        
        #print(menu_height)
        
        ## Long story short, this gets the menu to appear right next to the cursor
        ## no it's not the right way to do it, and it doesn't scale well but idc 
        menu_height = window.height()
        global_pos.setY(global_pos.y() - (menu_height/3))
        global_pos.setX(global_pos.x() + 50)
        
        ## this is a blocking call, waits for an action to happen or it to be dismissed
        menu.exec(global_pos)

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
    
    ## the client table part of the c2 stuff
    def c2_client_table_setup(self):
        self.c2_gui_groupbox_client_table.setColumnCount(5)
        
        ##naming
        self.c2_gui_groupbox_client_table.setHorizontalHeaderLabels(['Client', 'IP/Port', 'Current Job','SleepTime', 'Last Checkin'])
        
        ##autostretch
        header = self.c2_gui_groupbox_client_table.horizontalHeader()
        # set resize mode for each section to Stretch
        for i in range(header.count()):
            header.setSectionResizeMode(i, QHeaderView.Stretch)


        ## temp test rows
        rowPosition = self.c2_gui_groupbox_client_table.rowCount()
        self.c2_gui_groupbox_client_table.insertRow(rowPosition)


        ## when adding rows, loop this & iterate the position to make it simpler
        self.c2_gui_groupbox_client_table.setItem(rowPosition, 0, QTableWidgetItem("client_127.0.0.1_XCCDE"))
        self.c2_gui_groupbox_client_table.setItem(rowPosition, 1, QTableWidgetItem("123.456.77.44"))
        self.c2_gui_groupbox_client_table.setItem(rowPosition, 2, QTableWidgetItem("Wait"))
        self.c2_gui_groupbox_client_table.setItem(rowPosition, 3, QTableWidgetItem("60s"))
        self.c2_gui_groupbox_client_table.setItem(rowPosition, 4, QTableWidgetItem("06:34:51 UTC 02/02"))
                
        ##row height:
        for i in range(self.c2_gui_groupbox_client_table.rowCount()):
            self.c2_gui_groupbox_client_table.setRowHeight(i, 10)
            
        ## no more border or grid
        self.c2_gui_groupbox_client_table.setStyleSheet("QTableView { border: none; } QTableView::item { border: none; }")
        self.c2_gui_groupbox_client_table.setShowGrid(False)
        self.c2_gui_groupbox_client_table.setGridStyle(Qt.NoPen)
        ## selects whole row
        self.c2_gui_groupbox_client_table.setSelectionBehavior(QAbstractItemView.SelectRows)
        ## hiding row numbers
        self.c2_gui_groupbox_client_table.verticalHeader().setVisible(False)



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
            logging.debug(f"[Logec (System Shell)]: {e}")
            #print(e) if GLOBAL_DEBUG else None

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
##== C2 Local Server
    def c2_localserver_start(self):
        port = self.c2_server_port_local.text()
        ip =  self.c2_server_ip_local.text()

        ##shell true is a vuln, allows command injection (;command). Only a concern IF this is compiled
        ## have to do shell=true to pass args
        #self.proc = subprocess.Popen([f"python3 {sys_path}/agent/server.py --ip {ip} --port {port}"], shell=True)
        
        ## fixed version
        self.proc = subprocess.Popen(["python3", f"{sys_path}/agent/server.py", "--ip", ip, "--port", port, "--quiet"])
        self.localserver_running = True
        self.localserver_pid = self.proc.pid
        self.c2_start_server_local.setDisabled(True)
        self.c2_start_server_local.setText("Running")
        
        self.c2_localserver_logupdate_timer()
        #pass

    def c2_localserver_stop(self):
        self.proc.terminate()
        self.c2_start_server_local.setDisabled(False)
        self.c2_start_server_local.setText("Start")

    def c2_localserver_logupdate_timer(self):
        self.localserver_timer = QTimer()
        self.localserver_timer.timeout.connect(self.c2_localserver_logupdate)
        self.localserver_timer.start(self.settings['C2']['Local']['server_log_refresh'])
    
    def c2_localserver_logupdate(self):
        ##read log file, update textedit to have new log
        with open("server.log","r") as sl:
            self.c2_server_log_local.setText(sl.read())

        # this way too long doo dad just sets the scroll bar to all the way down
        self.c2_server_log_local.verticalScrollBar().setValue(self.c2_server_log_local.verticalScrollBar().maximum())

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

            # Authenticating to server with the background account
            self.friendly_client_background_worker.connect_to_server([
                connlist[0],
                connlist[1],
                f"background_worker_{connlist[2]}",
                connlist[3]
            ])

            ## return not working, so getting validated authentication via the class itself
            if self.friendly_client.authenticated:
                self.c2_status_label.setText(f"Status: Connected to {connlist[0]}:{connlist[1]}")

            if self.friendly_client_background_worker.authenticated:
                # calling subtasks to be run
                self.c2_client_update_timer()
            
           # if self.friendly_client.err_ConnRefused_0x01:
                #self.handle_error(["ConnRefused_0x01","Low","Make sure the server is alive"])
                #self.friendly_client.err_ConnRefused_0x01 = False
    
    def c2_server_disconnect(self):
        self.friendly_client.client_disconnect()
        self.c2_status_label.setText(f"Status: Disconnected")
        
    def c2_server_interact(self, command):
        input = self.c2_servershell_input.text()

        # still the same class instance, however starting a new thread for this method
        self.thread_manager.start(partial(self.friendly_client.gui_to_server, input))
        self.friendly_client.shell_output.connect(self.shell_text_update)
    
        ## clearing text
        self.c2_servershell_input.setText("")
    
    def shell_text_update(self, input):
        #print("shell_text_update" + input) if GLOBAL_DEBUG else None
        self.c2_servershell.setText(input)

    # The subsection that updates the client GUI in the background
    def c2_client_update_timer(self):
        logging.debug("[Logec (C2 client_update_timer)]")
        ## A timer for updating the client view on the GUI. Goes every second
        # call me when succesffully authenticated to the server
        self.client_timer = QTimer()
        self.client_timer.setInterval(3000)  ## in MS
        self.client_timer.timeout.connect(self.c2_client_update)
        self.client_timer.start(self.settings['C2']['Local']['ClientRefresh'])

    def c2_client_update(self):
        """ subtask, Talks to the server, gets client info"""
        # Requesting clients (in JSON form), and sending to client_list_update
        logging.debug("[Logec (Friendly Client] Starting Subtask: Updating malicious clients for GUI")


        ## doesn't freeze the whole thread at the moment...
        # thread manager code is here just incase It's needed
        # self.thread_manager.start(partial(self.friendly_client.gui_to_server, "export-clients"))
        self.friendly_client_background_worker.gui_to_server("export-clients")
        self.friendly_client_background_worker.json_data.connect(self.client_list_update)

        # Other subtasks go here

    def client_list_update(self, client_data_from_server):
        """ takes data of current clients, parses, and updates on the GUI

             json to json obj, json obj to string for sending -> string to dict via json loads

        """
        # turn into a GUI category for these types of logs
        logging.debug(f"[Logec (client_list_update)] Updating client table")

        # clear table on calling to get new data - may change this later, could be a PITA for users
        self.c2_gui_groupbox_client_table.clear()
        self.c2_gui_groupbox_client_table.setRowCount(0)
        ##parse json
        data = json.loads(client_data_from_server)
        self.c2_gui_groupbox_client_table.setHorizontalHeaderLabels(
            ['Client', 'IP/Port', 'Current Job', 'SleepTime', 'Last Checkin'])

        for client in data['MaliciousClients']:
            try:
                # I believe this adds a row? there are prolly better ways to do this
                rowPosition = self.c2_gui_groupbox_client_table.rowCount()
                self.c2_gui_groupbox_client_table.insertRow(rowPosition)

                self.c2_gui_groupbox_client_table.setItem(rowPosition, 0, QTableWidgetItem(client['ClientFullName']))
                self.c2_gui_groupbox_client_table.setItem(rowPosition, 1, QTableWidgetItem(client['ClientIP']))
                self.c2_gui_groupbox_client_table.setItem(rowPosition, 2, QTableWidgetItem(client['CurrentJob']))
                self.c2_gui_groupbox_client_table.setItem(rowPosition, 3, QTableWidgetItem(client['SleepTime']))
                self.c2_gui_groupbox_client_table.setItem(rowPosition, 4, QTableWidgetItem(client['LatestCheckin']))
            except Exception as e:
                logging.debug(f"[Server (client_list_update)] Error with a row of json, skipping: {e}")

        # Need to disconnect at the end for some reason, otherwise exponential repeat calls to
        # this function happen
        self.friendly_client_background_worker.json_data.disconnect(self.client_list_update)

    ## exploit n vuln

    def exploit_and_vuln_search(self):
        ## load DB file path eventually, hardcoded for now
        filepath = f"{sys_path}/Content/ExploitsNstuff/ExploitDB/exploitdb-2022-10-18/files_exploits.csv"
        self.exploitdb_worker = LogecExploitdb(csv_filepath=filepath)

        self.thread_manager.start(partial(self.exploitdb_worker.search, self.exploitandvuln_search.text()))
        self.exploitdb_worker.results.connect(self.vuln_display_update)

    def vuln_display_update(self, data):
        ## turn into a table later

        self.exploitandvuln_tableview.clear()
        self.exploitandvuln_tableview.setRowCount(0)

        self.exploitandvuln_tableview.setColumnCount(7)
        self.exploitandvuln_tableview.setHorizontalHeaderLabels(
            ['Column 1', 'Column 2', 'Column 3', 'Column 4', 'Column 5', 'Column 6', 'Column 7'])

        ## NOT DISPLAYING FOR SOME REASON
        for i in data:
            try:
                #print("NEWROTW")
                #print(i)
                rowPosition = self.exploitandvuln_tableview.rowCount()
                self.exploitandvuln_tableview.insertRow(rowPosition)

                self.exploitandvuln_tableview.setItem(rowPosition, 0, QTableWidgetItem(str(i[0])))
                self.exploitandvuln_tableview.setItem(rowPosition, 1, QTableWidgetItem(str(i[1])))
                self.exploitandvuln_tableview.setItem(rowPosition, 2, QTableWidgetItem(str(i[2])))
                self.exploitandvuln_tableview.setItem(rowPosition, 3, QTableWidgetItem(str(i[3])))
                self.exploitandvuln_tableview.setItem(rowPosition, 4, QTableWidgetItem(str(i[4])))
                self.exploitandvuln_tableview.setItem(rowPosition, 5, QTableWidgetItem(str(i[5])))
                self.exploitandvuln_tableview.setItem(rowPosition, 6, QTableWidgetItem(str(i[6])))
                self.exploitandvuln_tableview.setItem(rowPosition, 7, QTableWidgetItem(str(i[7])))

            except Exception as e:
                print(e)


        #self.exploitandvuln_textedit.tableview(str(data))

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
        #print(input_ip) if GLOBAL_DEBUG else None

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

            #print(f'TIMOUT: {timeout}') if GLOBAL_DEBUG else None
            
            #print(f'DELAY: {delay}') if GLOBAL_DEBUG else None
            
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
        #print("DB Triggered") if GLOBAL_DEBUG else None
        try:
            cursor = self.sqliteConnection.cursor()
            
            ## Picked up this trick from chatGPT, basically each item coresponds to the number in list
            IP, PORT, SCANTYPE, SCANDATE, SCANTIME, RUNTIME, SCANNEDPORTS, DELAY = list
            
            sqlite_insert_query = f"""INSERT INTO PortScan (IP, PORT, ScanType, ScanDate, ScanTime, RunTime, ScannedPorts, Delay) 
            VALUES
            ({IP}, {str(PORT).replace("{","").replace("}","")}, '{SCANTYPE}', '{SCANDATE}', '{SCANTIME}', '{RUNTIME}', "{SCANNEDPORTS}", '{DELAY}')"""
            
            #print(sqlite_insert_query) if GLOBAL_DEBUG else None

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
        #print(self.bashbuild_diagnostic.isChecked())  if GLOBAL_DEBUG else None
        
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
        
        #print(packed_json) if GLOBAL_DEBUG else None
        
        self.Script.script_results.connect(self.bash_builder_display)
        
        ## Has to go last to grab signals n stiff
        self.Script.script_framework(packed_json)        
##GUI Updater
    def bash_builder_display(self, final_script):
        #print("triggered") if GLOBAL_DEBUG else None
        self.bashbuild_textoutput.setText(final_script)

##== dns_lookup
    """

    Description: The DNS handler code
    """
    def dns_lookup(self):

        ## All handler
        ## Setting object instance
        #self.tablewidget = self.test_table

        #self.tablewidget.setRowCount(4)
        #self.tablewidget.setColumnCount(1)
        ##self.tablewidget.setItem(0, 0, QTableWidgetItem('ns2.google.com.'))
        #self.tablewidget.setItem(1, 0, QTableWidgetItem('ns3.google.com.'))

        #self.tablewidget.horizontalHeader().setStretchLastSection(True)
        #self.tablewidget.horizontalHeader().setSectionResizeMode(
        #    QHeaderView.Stretch
        #)

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
            #pass
            self.N_worker = utility.Network()
            self.thread_manager.start(partial(self.N_worker.lookup_All, self.scanning_dns_query.text()))
            
            self.N_worker.lookupall.connect(self.dns_lookup_table)

    def dns_lookup_table(self, lookup_dict):
        #print(lookup_dict)
        self.dns_table_formatting(self.dns_a_table, 'Not Found', 'A') if lookup_dict['A'] == 'NONE' else self.dns_table_formatting(self.dns_a_table, lookup_dict['A'], 'A')
        self.dns_table_formatting(self.dns_CNAME_table, 'Not Found', 'CNAME') if lookup_dict['CNAME'] == 'NONE' else self.dns_table_formatting(self.dns_CNAME_table, lookup_dict['CNAME'], 'CNAME')
        self.dns_table_formatting(self.dns_MX_table, 'Not Found', 'MX') if lookup_dict['MX'] == 'NONE' else self.dns_table_formatting(self.dns_MX_table, lookup_dict['MX'], 'MX')
        self.dns_table_formatting(self.dns_Reverse_table, 'Not Found', 'Reverse') if lookup_dict['Reverse'] == 'NONE' else self.dns_table_formatting(self.dns_Reverse_table, lookup_dict['Reverse'], 'Reverse')
        self.dns_table_formatting(self.dns_TXT_table, 'Not Found', 'TXT') if lookup_dict['TXT'] == 'NONE' else self.dns_table_formatting(self.dns_TXT_table, lookup_dict['TXT'], 'TXT')
        self.dns_table_formatting(self.dns_NS_table, 'Not Found', 'NS') if lookup_dict['NS'] == 'NONE' else self.dns_table_formatting(self.dns_NS_table, lookup_dict['NS'], 'NS')

        #pass
        
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
        #print("clicked") if GLOBAL_DEBUG else None
        try:
            pass
            #self.bruteforce_worker.thread_quit()
            #self.bruteforce_thread.exit() # exi works better than quit
            #self.bruteforce_worker.deleteLater()
        except Exception as e:
            self.handle_error([e, "Low", "Bruteforce is probably not running"])

    def bf_browser_popup(self, whichbutton):
        from PySide6.QtWidgets import QFileDialog
        #print("Clicked") if GLOBAL_DEBUG else None
        
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
        ## Just in case a value doesn't make it back
        try:
            TARGET, PORT, SERVICE, CREDS, TIME, DATE = list
        except Exception as e:
            logging.debug(f"[Logec (Bruteforce Credentials)] Error with list values. {e}")
            TARGET, PORT, SERVICE, CREDS, TIME, DATE = None, None, None, None, None, None

        query = f"""INSERT INTO 'BRUTEFORCE-Creds' (Target, Port, Service, Credentials, Time, Date) 
            VALUES
            ('{TARGET}', '{str(PORT).replace("{","").replace("}","")}', '{SERVICE}', '{CREDS}', '{TIME}', '{DATE}' )"""
        
        self.sql_db_write(query)
        
   
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
            #print(exc_type, fname, exc_tb.tb_lineno) if GLOBAL_DEBUG else None

    def bruteforce_fuzz_hardstop(self):
        #pass
        #print("clicked") if GLOBAL_DEBUG else None
        try:
            pass
            #self.fuzzer_worker.thread_quit()
            #self.fuzzer_thread.exit() # exi works better than quit
            #self.fuzzer_worker.deleteLater()
        except Exception as e:
            self.handle_error([e, "Low", "Fuzzer is probably not running"])

    def bf_fuzz_browser_popup(self, whichbutton):
        from PySide6.QtWidgets import QFileDialog
        #print("Clicked") if GLOBAL_DEBUG else None
        
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
        ## Just in case a value doesn't make it back
        try:
            TARGET, PORT, CODE,SHORT_URL, LONG_URL, TIME, DATE = list

        except Exception as e:
            logging.debug(f"[Logec (Bruteforce Fuzzer)] Error with list values. {e}")
            TARGET, PORT, CODE,SHORT_URL, LONG_URL, TIME, DATE = None, None, None, None, None, None, None

        query = f"""INSERT INTO 'BRUTEFORCE-Fuzzer' (Target, Port, Code, Short_Url, Long_Url, Time, Date) 
            VALUES
            ('{TARGET}', '{str(PORT).replace("{","").replace("}","")}', '{CODE}', '{SHORT_URL}', '{LONG_URL}', '{TIME}', '{DATE}' )"""
        
        self.sql_db_write(query)

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
            "username" : self.settings['Osint']['Reddit']['Username'],
            "password" : self.settings['Osint']['Reddit']['Password'],
            "secret_token" : self.settings['Osint']['Reddit']['SecretToken'],
            "client_id" : self.settings['Osint']['Reddit']['ClientId']
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
                logging.debug("[Logec (OSINT Reddit)] Error with search type. Most likely due to a bug")
                #print("STYPE ERROR")
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
        #print("URL SET TRIGGERED")
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
## Other functions, webbrowser etc
####################
    def global_browser(self, site: str):
        """Used for popping a websearch/direct url. 

        Args:
            site (str): the site/URL/URI that the user wants to go to
        """
        ## Lazy Import
        try:
            import webbrowser
        except ImportError as IE:
            logging.warning(f"[Logec (Webbrowser)]: 'webbrowser' import error: {IE}")
        
        ## maybe use a regex to validate the url
        if "http://" or "https://" not in site:
            site = f"https://{self.settings['Sql']['SqlTableView']['SqlRightclickMenu']['DefaultBrowserUrl']}{site}"
            
        try:
            webbrowser.open(site)
        except Exception as e:
            logging.warning(f"[Logec (Webbrowser)] Error: {e}")

##== Content
    def content_setup(self):
        """This is the logic behind the content tab. This coudl have been much simpler, but the expanding 
        list design sounded cool, and was flexible as f*ck. Basically, this reads the CONTENT-Wordlists table,
        and creates TextEdit (for showing the name) and a download button for each list in the db. it also formats where
        those items go based on the Category key
        
        to add an entry, pop open the DB, and create a new row with the data needed. order does not matter as long as 
        you set the Category
        
        Because these are in the DB, they are persistent in your project file.

        Some insight on the for loop, each iteration creates a new button, & line edit that are
        tied to data from each iteration
        """
        ## Hiding placeholder buttons, needed to keep layout in line
        self.other_content_directory_layout_SecList_placeholder.hide()
        self.other_content_directory_layout_SecList_placeholder_button.hide()

        self.other_content_directory_layout_DefaultPasswords_placeholder_button.hide()
        self.other_content_directory_layout_DefaultPasswords_placeholder.hide()
    
        self.other_content_directory_layout_WeakPasswords_placeholder.hide()
        self.other_content_directory_layout_WeakPasswords_placeholder_button.hide()
        
        self.other_content_directory_layout_LeakedPasswords_placeholder.hide()
        self.other_content_directory_layout_LeakedPasswords_placeholder_button.hide()

        self.other_content_exploit_layou_exploitdb_placeholder.hide()
        self.other_content_exploit_layou_exploitdb_placeholder_button.hide()

        ## read DB, 
        ## DB here
        sql_data = self.sql_db_read("select * from 'CONTENT-Wordlists'")
        #print(sql_data)
        
        ## for each in db, create qtextedit with name, and a button for downloading, button
            ## is named whatever the name is, so when download is clicked, it gets the row, and url to download
        
        for i in sql_data:
            ## this is inherently a limitation on categories, need to include an "other" tab
            ## for others
            
            ## Names line up with names in DB, that's why they are capatalized
            try:
                Category = i[0].strip() ## removes accidental \n's if they occur
                ListName = i[1]
                ListUrl = i[2]
            except:
                logging.debug(f"[Logec (Content)] Error with reading SQL row: {i}")
            
            line_edit = QLineEdit()
            push_button = QPushButton()
            
            ## stylesheet stuff
            '''push_button.setStyleSheet(
            "QPushButton:hover { background-color: grey }"
            )'''

            
            if Category == "SecList":
                ##hover text
                push_button.setToolTip(ListUrl)
                ## This creates a button for each entry, which is tied to the data from the SQL entry
                push_button.clicked.connect(partial(self.content, url=ListUrl, savepath=f"{sys_path}/Content/Wordlists",
                                                    savename=f"{Category}-{ListName}"))

                self.other_content_directory_layout_SecList.addWidget(line_edit)
                self.other_content_directory_layout_SecList.addWidget(push_button)
                
                line_edit.setText(str(ListName))
                push_button.setText("Download")
                
            elif Category == "DefaultPasswords":
                push_button.setToolTip(ListUrl)
                push_button.clicked.connect(partial(self.content, url=ListUrl, savepath=f"{sys_path}/Content/Wordlists",
                                                    savename=f"{Category}-{ListName}"))

                #pass # other_content_directory_layout_DefaultPasswords
                self.other_content_directory_layout_DefaultPasswords.addWidget(line_edit)
                self.other_content_directory_layout_DefaultPasswords.addWidget(push_button)
                
                line_edit.setText(str(ListName))
                push_button.setText("Download")
                
            elif Category == "WeakPasswords":
                push_button.setToolTip(ListUrl)
                push_button.clicked.connect(partial(self.content, url=ListUrl, savepath=f"{sys_path}/Content/Wordlists",
                                                    savename=f"{Category}-{ListName}"))
                #pass # other_content_directory_layout_WeakPasswords
                self.other_content_directory_layout_WeakPasswords.addWidget(line_edit)
                self.other_content_directory_layout_WeakPasswords.addWidget(push_button)
                
                line_edit.setText(str(ListName))
                push_button.setText("Download")
                
                
            elif Category == "LeakedPasswords":
                push_button.setToolTip(ListUrl)
                push_button.clicked.connect(partial(self.content, url=ListUrl, savepath=f"{sys_path}/Content/Wordlists",
                                                    savename=f"{Category}-{ListName}"))
                #pass # other_content_directory_layout_LeakedPasswords
                self.other_content_directory_layout_LeakedPasswords.addWidget(line_edit)
                self.other_content_directory_layout_LeakedPasswords.addWidget(push_button)
                
                line_edit.setText(str(ListName))
                push_button.setText("Download")

            elif Category == "ExploitDB":
                push_button.setToolTip(ListUrl)
                push_button.clicked.connect(partial(self.content,
                                                    url=ListUrl,
                                                    savepath=f"{sys_path}/Content/ExploitsNstuff/ExploitDB/",
                                                    savename=f"{Category}-{ListName}",
                                                    isziparchive=True))

                self.other_content_exploit_layou_exploitdb.addWidget(line_edit)
                self.other_content_exploit_layou_exploitdb.addWidget(push_button)

                line_edit.setText(str(ListName))
                push_button.setText("Download and Extract")


            
            else:
                logging.debug(f"[Logec (Content)] Row has invalid 'Content' key set: {i}")

    def content(self, url=None, savepath=None, savename=None, isziparchive=False, istargzarchive=False):

        if isziparchive:
            savename = f"{savename}.zip"
        elif istargzarchive:
            savename = f"{savename}.tar.gz"

        download_dict = {
            "URL" : str(url),
            ## Hardcoded for now
            "SavePath" : savepath, #sys_path + "/Content/Wordlists",
            "SaveName" : str(savename),
            "SavePathAndName": f"{savepath}/{savename}",
            "IsZipArchive": isziparchive,
            "IsTarGzArchive" : istargzarchive
        }
        logging.debug(f"[Logec (content)] Starting download for {url}, saving to {savepath}")
        ## Download in new thread
        self.thread_manager.start(partial(self.H.download, download_dict))




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
        if self.settings['System']['Startup']['ShowProjectPicker']:
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
        
        #print(fileName) if GLOBAL_DEBUG else None
        logging.debug(f"[Logec (ProjectFile)] ProjectName: {fileName}")
        
        options_list = [
            "load",
            fileName,
        ]
        
        #print(fileName) if GLOBAL_DEBUG else None
        
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
            
            #print(self.ProjectPath) if GLOBAL_DEBUG else None
            logging.debug(f"[Logec (ProjectFile)] Project Path: {self.ProjectPath}")
            
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
                    logging.debug("[Logec (Project Files)] Default project loaded")
                    #print("Succesfully opened default project")
                    
            # Getting settings
            #print(self.settings['general']['Theme'])
              
        except Exception as e:
            logging.warning(f"[LogecSuite (Settings)] Error loading Settings: {e}")
            #print(e) if GLOBAL_DEBUG else None
        
    
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
            #print(database_file) if GLOBAL_DEBUG else None
            self.sqliteConnection = sqlite3.connect(sys_path + f'/{database_file}/logec_db')
            self.database_file = sys_path + f'/{database_file}/logec_db'
            #print(self.database_file) if GLOBAL_DEBUG else None
            #pass 
            logging.debug(f"[Logec (Project Files)] Project NAME SQL loaded")
            
        else:
            #print("DEFAULT") if GLOBAL_DEBUG else None
            self.sqliteConnection = sqlite3.connect(sys_path + '/Modules/General/SaveFiles/init_project/logec_db')
            #print(sys_path + '/Modules/General/SaveFiles/init_project/logec_db') if GLOBAL_DEBUG else None
            self.database_file = sys_path + '/Modules/General/SaveFiles/init_project/logec_db'
            #print(self.database_file) if GLOBAL_DEBUG else None
            logging.debug(f"[Logec (Project Files)] Default Project SQL loaded")
        
        ## Getting Q_sql set
        self.q_sql()

    def q_sql(self):
        ## I'm using a mix of Qsql & Sqlite 3 cause I din't think it through before coding this. 
        ## SO, until I fix it, this is gonna have to do.
        ## This affects the query.next() in 'custom_query'
        
        con = QSqlDatabase.addDatabase('QSQLITE')

        con.setDatabaseName(self.database_file)
        #print(self.database_file) if GLOBAL_DEBUG else None
        
        #print("Database location:", con.databaseName()) if GLOBAL_DEBUG else None

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
            except Exception as e:
                logging.warning(f"[Logec (Project File)] Error connecting to DB: {e}")
                #print('Error connecting to DB & QApp not constructed.') if GLOBAL_DEBUG else None
        #return True
    
    ## SQL global writer
    def sql_db_write(self, query):
        """
        The global write function. Not fully utilized, some modules still need to be moved here. 
        Handy as it's a one stop shop into the DB and prevents lockups
        
        Each module that needs to write here needs a db_write method that provides the query string. Those methods
        need to supply some data, even if it's "None"
        
        All the error handling is done here as well

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
    
    ## SQL global reader - similar to sql_db_write, but returns a value
    def sql_db_read(self, query):
        """
        The global read function. Not fully utilized, some modules still need to be moved here. 
        Handy as it's a one stop shop into the DB to read and prevents lockups
        
        All the error handling is done here as well

        Args:
            query (str): The query for SQL
            Looks like: SELECT * FROM tablename (column, column2)
        """
        try:
            cursor = self.sqliteConnection.cursor()
            
            results_raw = cursor.execute(query)
            self.sqliteConnection.commit()
            results = results_raw.fetchall()

            cursor.close()
            
            return results

        ## this first as sqlite3.error is a catchall
        except sqlite3.OperationalError as operror:
            logging.warn(f"[SQL] Operational error: {operror}")
            self.handle_error([operror, "warn", "Enter a valid SQL query"])

        except sqlite3.Error as error:
            #print('Error:', error) if GLOBAL_DEBUG else None
            logging.warn(f"[SQL]Error reading SQL DB: {error}")

        except Exception as e:
            logging.warn(f"[SQL] Unkown error: {e}")


    ## THis is depracated, and will be removed once all modules are moved off of it
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
            logging.warning(f"[Logec (SQL)] Error: {error}")
            #print('Error:', error) if GLOBAL_DEBUG else None

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
    def system_theme_chooser(self):
        accent = self.settings['System']['Themes']['Accent']

        if self.settings['System']['Themes']['Theme'] == "dark":
            import qdarktheme
            qdarktheme.setup_theme("dark", custom_colors={"primary": accent})
        elif self.settings['System']['Themes']['Theme'] == "light":
            import qdarktheme
            qdarktheme.setup_theme("light", custom_colors={"primary": accent})
        elif self.settings['System']['Themes']['Theme'] == "system":
            import qdarktheme
            qdarktheme.setup_theme("auto", custom_colors={"primary": accent})
        elif self.settings['System']['Themes']['Theme'] == "default":
            pass
        else:
            logging.debug(f"[Logec (Theme)] Unkown theme: {self.settings['System']['Themes']['Theme']}")
            
    def set_theme(self, theme_name):
        """ Old/not used function for css themes
        """
        pass
        '''
        if theme_name != "Default":
            with open(f"{sys_path}/Gui/themes/{theme_name}","r") as f:
                stylesheet = f.read()
                
            self.setStyleSheet(stylesheet)
        else:
            pass'''

##== Sys Functions
        """
        Description:
            Handles the system functions like restarting the program
        """
        
    def restart(self): ## MEMORY LEAK !!
        logging.debug("[Logec] Restarting program & interpreter")
        # Restart the Python interpreter
        args = sys.argv[:]
        args.insert(0, sys.executable)
        self.close()
        sys.exit(os.spawnvp(os.P_WAIT, sys.executable, args))
        
    def program_exit(self):
        logging.debug("[Logec (shutdown)] Exiting program")
        self.exit_functions()
        sys.exit()
    
    def exit_functions(self):
        ## kills local server if still running
        try:
            if self.localserver_running and self.settings['C2']['Local']['KillServerOnExit']:
                logging.debug(f"[Logec (local server)] Server running, killing. setting: kill_server_on_gui_exit")
                os.kill(self.proc.pid, 15)
        except:
            logging.debug("[Logec (shutdown)] localserver not running, ignore")


if __name__ == '__main__':
    try:
        # Creating App
        app = QtWidgets.QApplication(sys.argv)

        # Library Paths
        library_paths = QCoreApplication.libraryPaths()
        # Print the path where QSqlDatabase is looking for drivers
        # not a logging.debug YEt as it's only useful for dev
        #print(library_paths) if GLOBAL_DEBUG else None



        # QT stuff
        window = LogecSuite()
        window.show()
        window.system_theme_chooser()
        
        import cProfile
        cProfile.run('app.exec()', filename=f'{sys_path}/logs/logec-perf.prof')

        # Kill when exec is closed
        #pid = os.getpid()
        #os.kill(pid, 15)   # SIGTERM
        
        window.program_exit()

    except Exception as e:
        print("===== Traceback =====")
        traceback.print_exc()
