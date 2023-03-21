#!/bin/python3
##== Global Debug:
GLOBAL_DEBUG = True

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
    QTableView,
    QTabBar,
    QTabWidget,
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

from Modules.General.Bruteforce.bruteforce import Bruteforce, Fuzzer
from Modules.General.OSINT.dork import Dork
from Modules.General.SaveFiles.fileops import *
from Modules.General.ScriptGen import ScriptGen
from Modules.General.SysShell.shell import Shell
from Modules.General.portscanner import Portscan
import Modules.General.utility as utility
from Modules.Linux.Reverse_Shells.reverse_shells import target as rev_shell_target
from Modules.Windows.Reverse_Shells.win_reverse_shells import target as rev_shell_target_win

from agent.friendly_client import FClient

from gui import Ui_LogecC3

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
        self.table_RefreshDB_Button.clicked.connect(lambda: self.refresh_db('c2_db'))
        self.table_RefreshDB_Button.setShortcut('r')

        self.table_QueryDB_Button.clicked.connect(lambda: self.custom_query('c2_db'))
        self.table_QueryDB_Button.setShortcut('Return')

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

        self.actionDEBUG.triggered.connect(self.DEBUG)
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
            print("BF DB")
            self.view = self.scanning_bruteforce_db
            query_input_raw = f'{self.DB_Query_scanning_bruteforce.text()} ORDER BY DATE DESC, TIME DESC'
        else:
            query_input_raw = ""
            self.view = ""
            self.handle_error(['No Query Input Provided', 'Low', 'Enter an input to fix'])
            return

        # Temp workaround for shortcuts not working
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
        cursor = connection.execute(query_input)
        names = [x[0] for x in cursor.description]
        connection.close()

        names_num = 0
        names_list = []
        query_num = 0

        # Loop for column names
        for i in names:
            names_list.append(i)
            names_num += 1

        self.view.setColumnCount(len(names_list))
        self.view.setHorizontalHeaderLabels(names_list)

        # Loop for data in each column
        while query.next():
            rows = self.view.rowCount()
            self.view.setRowCount(rows + 1)

            for i in range(0, len(names_list)):
                self.view.setItem(rows, i, QTableWidgetItem(str(query.value(i))))

            query_num += 1

        self.view.resizeColumnsToContents()

if __name__ == '__main__':
    try:
        # Creating App
        app = QtWidgets.QApplication(sys.argv)

        # Library Paths
        library_paths = QCoreApplication.libraryPaths()
        # Print the path where QSqlDatabase is looking for drivers
        print(library_paths)

        # QT stuff
        window = LogecSuite()
        window.show()
        app.exec_()

        # Kill when exec is closed
        pid = os.getpid()
        os.kill(pid, 15)   # SIGTERM

    except Exception as e:
        traceback.print_exc()
