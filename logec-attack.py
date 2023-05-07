#!/bin/python3
##== Global Debug:
GLOBAL_DEBUG = True
# if GLOBAL_DEBUG else None

#
##== Main Imports
import json
import os
import subprocess
import sys
import random
import sqlite3
import threading
import csv
#import time
#import webbrowser
from functools import partial
import traceback

##== GUI Imports
from PySide6 import QtWidgets
from PySide6.QtCore import Qt, QThreadPool, QCoreApplication, QTimer, QPoint
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
from Gui.startup_projectbox import Ui_startup_projectbox
#from Gui.agent_compile import Ui_AgentEditor

import Modules.General.SaveFiles.fileops as fileops
from Modules.General.ScriptGen import ScriptGen
from Modules.General.SysShell.shell import Shell
import Modules.General.utility as utility
from Modules.ExploitNVulns.exploitdb import LogecExploitdb
from Modules.Wrappers.CompilationWrapper import (
    GccWrapper,
    NuitkaWrapper
)

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
        self.init_buttons_performance_benchmarks()
        self.init_buttons_settings_settings()
        self.init_buttons_compile_toolbox()

        ##== Data / Tab Inits 
        ## Graphs are using lots of CPU, disabled for now.
        #self.init_data_performance_graphs()
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

    def init_buttons_scanning(self) -> None:
        self.scanning_dns_lookup.clicked.connect(self.dns_lookup)
        self.portscan_start.clicked.connect(self.portscan)


    ##== buttons for the benchmarks
    def init_buttons_performance_benchmarks(self) -> None:
        self.performance_speedtest.clicked.connect(self.performance_networkspeed)
        self.performance_benchmark_button.clicked.connect(self.performance_benchmark)

    ##== Buttons for settings 
    def init_buttons_settings_settings(self) -> None:
        self.settings_reload.clicked.connect(self.edit_settings)
        self.settings_write.clicked.connect(self.write_settings)
        self.program_reload.clicked.connect(self.restart)

    def init_buttons_compile_toolbox(self):
        self.agentbuilder_toolbox_python_compile_button.clicked.connect(self.python_compile)

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


    ##== Loading all the data into the respective tables
    def init_data_sql_tables(self) -> None:
        """this function LOADS the data into each table on starutp
        """
        #self.view = self.table_SQLDB
        ## Showing help table on startup
        self.DB_Query_main.setText('select * from Help')
        self.custom_query('main_db')

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

        else:
            query_input_raw = "SELECT name FROM sqlite_schema WHERE type='table' ORDER BY name"
            self.view = ""
            #self.handle_error(['No Query Input Provided', 'Low', 'Enter an input to fix'])
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
        self.main_tab_widget.widget(0).layout().setMenuBar(self.c2_menuBar)

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

    """
    These functions are what drive the current vuln & exploit seacher.
    
    The seraching is pretty basic, but eventually I'd like it to be similar to this:
    name=OpenSSH platform=windows 
    
    with each feild being searched and if it exists, get added. yes it won't be the fastest, but it'll work
    
    """
    def exploit_and_vuln_search(self):
        ## load DB file path eventually, hardcoded for now
        filepath = f"{sys_path}/Content/ExploitsNstuff/ExploitDB/exploitdb-main/files_exploits.csv"
        self.exploitdb_worker = LogecExploitdb(csv_filepath=filepath)

        with open(filepath) as csvFile:
            reader = csv.reader(csvFile)
            self.header_list = next(reader)

        self.thread_manager.start(partial(self.exploitdb_worker.search, self.exploitandvuln_search.text()))
        self.exploitdb_worker.results.connect(self.vuln_display_update)

    def vuln_display_update(self, data):
        self.exploitandvuln_tableview.clear()
        self.exploitandvuln_tableview.setRowCount(0)

        try:
            self.exploitandvuln_tableview.setColumnCount(len(data[0]))
            ## set AFTER column count
            self.exploitandvuln_tableview.setHorizontalHeaderLabels(self.header_list)

            #self.exploitandvuln_tableview.setColumnCount(2)
            for i in data:
                rowPosition = self.exploitandvuln_tableview.rowCount()
                self.exploitandvuln_tableview.insertRow(rowPosition)
                for z in range(0, len(data[0])):
                    try:
                        self.exploitandvuln_tableview.setItem(rowPosition, z, QTableWidgetItem(str(i[z])))
                    except Exception as e:
                        #print(e)
                        logging.debug(f"[Logec (exploit_and_vuln_search)] Error: {e}")
        except Exception as e:
            print(e)
            logging.debug(f"[Logec (exploit_and_vuln_search)]: Search yielded no results")
            self.exploitandvuln_tableview.setColumnCount(1)
            self.exploitandvuln_tableview.insertRow(0)
            self.exploitandvuln_tableview.setItem(0, 0, QTableWidgetItem("search yeilded no results"))

####################
## Payload Builder & wrapper
####################
    """ The idea here is that you cn build payloads easily, wheter that be in 
python, bash, powershell, c, C# etc. Really, this benefits me just as much as anyone else, 
as I get to learn all these fun ways of doing things in different scripting languages
    """
    def python_compile(self):
        self.nuitka_worker = NuitkaWrapper(
            codefile=f"{sys_path}/agent/python/client.py",
            savefile=self.agentbuilder_toolbox_python_compile_savedir.text(),
            savefile_name=self.agentbuilder_toolbox_python_compile_savename.text(),
            flags=self.agentbuilder_toolbox_python_compile_flags.text(),
            process_timeout=self.agentbuilder_toolbox_python_compile_timeout.value(),
        )
        self.thread_manager.start(self.nuitka_worker.compile_framework())
        ##not wokring :(
        self.nuitka_worker.Update.connect(
            ## supposed to be a short update function for the GUI compilation log
            lambda x, text="text": self.agentbuilder_compilation_log.setText(text)
        )



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
        # there's prolly a more efficient way to do this.
        self.other_content_password_layout_SecList_placeholder.hide()
        self.other_content_password_layout_SecList_placeholder_button.hide()

        self.other_content_password_layout_DefaultPasswords_placeholder_button.hide()
        self.other_content_password_layout_DefaultPasswords_placeholder.hide()
    
        self.other_content_password_layout_WeakPasswords_placeholder.hide()
        self.other_content_password_layout_WeakPasswords_placeholder_button.hide()
        
        self.other_content_password_layout_LeakedPasswords_placeholder.hide()
        self.other_content_password_layout_LeakedPasswords_placeholder_button.hide()

        self.other_content_exploit_layou_exploitdb_placeholder.hide()
        self.other_content_exploit_layou_exploitdb_placeholder_button.hide()

        ## usernames
        self.other_content_usernames_layout_general_button_placeholder.hide()
        self.other_content_usernames_layout_general_placeholder.hide()

        self.other_content_usernames_layout_default_button_placeholder.hide()
        self.other_content_usernames_layout_default_placeholder.hide()

        self.other_content_usernames_layout_other_placeholder.hide()
        self.other_content_usernames_layout_other_button_placeholder.hide()

        # Directories:
        self.other_content_directory_layout_general_placeholder.hide()
        self.other_content_directory_layout_general_button_placeholder.hide()

        self.other_content_directory_layout_application_placeholder.hide()
        self.other_content_directory_layout_application_button_placeholder.hide()

        self.other_content_directory_layout_commonURL_placeholder.hide()
        self.other_content_directory_layout_commonURL_button_placeholder.hide()

        self.other_content_directory_layout_other_placeholder.hide()
        self.other_content_directory_layout_other_button_placeholder.hide()

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

            
            if Category == "Other/Fun":
                ##hover text
                push_button.setToolTip(ListUrl)
                ## This creates a button for each entry, which is tied to the data from the SQL entry
                push_button.clicked.connect(partial(self.content, url=ListUrl, savepath=f"{sys_path}/Content/Wordlists",
                                                    savename=f"{Category}-{ListName}"))

                self.other_content_password_layout_SecList.addWidget(line_edit)
                self.other_content_password_layout_SecList.addWidget(push_button)
                
                line_edit.setText(str(ListName))
                push_button.setText("Download")
                
            elif Category == "DefaultPasswords":
                push_button.setToolTip(ListUrl)
                push_button.clicked.connect(partial(self.content, url=ListUrl, savepath=f"{sys_path}/Content/Wordlists",
                                                    savename=f"{Category}-{ListName}"))

                self.other_content_password_layout_DefaultPasswords.addWidget(line_edit)
                self.other_content_password_layout_DefaultPasswords.addWidget(push_button)
                
                line_edit.setText(str(ListName))
                push_button.setText("Download")
                
            elif Category == "WeakPasswords":
                push_button.setToolTip(ListUrl)
                push_button.clicked.connect(partial(self.content, url=ListUrl, savepath=f"{sys_path}/Content/Wordlists",
                                                    savename=f"{Category}-{ListName}"))
                self.other_content_password_layout_WeakPasswords.addWidget(line_edit)
                self.other_content_password_layout_WeakPasswords.addWidget(push_button)
                
                line_edit.setText(str(ListName))
                push_button.setText("Download")

            elif Category == "LeakedPasswords":
                push_button.setToolTip(ListUrl)
                push_button.clicked.connect(partial(self.content, url=ListUrl, savepath=f"{sys_path}/Content/Wordlists",
                                                    savename=f"{Category}-{ListName}"))
                self.other_content_password_layout_LeakedPasswords.addWidget(line_edit)
                self.other_content_password_layout_LeakedPasswords.addWidget(push_button)
                
                line_edit.setText(str(ListName))
                push_button.setText("Download")

            elif Category == "GeneralUsernames":
                push_button.setToolTip(ListUrl)
                push_button.clicked.connect(partial(self.content, url=ListUrl, savepath=f"{sys_path}/Content/Wordlists",
                                                    savename=f"{Category}-{ListName}"))
                self.other_content_usernames_layout_general.addWidget(line_edit)
                self.other_content_usernames_layout_general.addWidget(push_button)

                line_edit.setText(str(ListName))
                push_button.setText("Download")

            elif Category == "DefaultUsernames":
                push_button.setToolTip(ListUrl)
                push_button.clicked.connect(partial(self.content, url=ListUrl, savepath=f"{sys_path}/Content/Wordlists",
                                                    savename=f"{Category}-{ListName}"))
                self.other_content_usernames_layout_default.addWidget(line_edit)
                self.other_content_usernames_layout_default.addWidget(push_button)

                line_edit.setText(str(ListName))
                push_button.setText("Download")

            elif Category == "OtherUsernames":
                push_button.setToolTip(ListUrl)
                push_button.clicked.connect(partial(self.content, url=ListUrl, savepath=f"{sys_path}/Content/Wordlists",
                                                    savename=f"{Category}-{ListName}"))
                self.other_content_usernames_layout_other.addWidget(line_edit)
                self.other_content_usernames_layout_other.addWidget(push_button)

                line_edit.setText(str(ListName))
                push_button.setText("Download")

            elif Category == "GeneralDirectory":
                push_button.setToolTip(ListUrl)
                push_button.clicked.connect(partial(self.content, url=ListUrl, savepath=f"{sys_path}/Content/Wordlists",
                                                    savename=f"{Category}-{ListName}"))
                self.other_content_directory_layout_general.addWidget(line_edit)
                self.other_content_directory_layout_general.addWidget(push_button)

                line_edit.setText(str(ListName))
                push_button.setText("Download")

            elif Category == "CommonDirectory":
                push_button.setToolTip(ListUrl)
                push_button.clicked.connect(partial(self.content, url=ListUrl, savepath=f"{sys_path}/Content/Wordlists",
                                                    savename=f"{Category}-{ListName}"))
                self.other_content_directory_layout_commonURL.addWidget(line_edit)
                self.other_content_directory_layout_commonURL.addWidget(push_button)

                line_edit.setText(str(ListName))
                push_button.setText("Download")

            elif Category == "ApplicationsDirectory":
                push_button.setToolTip(ListUrl)
                push_button.clicked.connect(partial(self.content, url=ListUrl, savepath=f"{sys_path}/Content/Wordlists",
                                                    savename=f"{Category}-{ListName}"))
                self.other_content_directory_layout_application.addWidget(line_edit)
                self.other_content_directory_layout_application.addWidget(push_button)

                line_edit.setText(str(ListName))
                push_button.setText("Download")

            elif Category == "OtherDirectory":
                push_button.setToolTip(ListUrl)
                push_button.clicked.connect(partial(self.content, url=ListUrl, savepath=f"{sys_path}/Content/Wordlists",
                                                    savename=f"{Category}-{ListName}"))
                self.other_content_directory_layout_other.addWidget(line_edit)
                self.other_content_directory_layout_other.addWidget(push_button)

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
        # random colors
        if accent == "random":
            color_list = ["#32b354","#347bc2","#7DF9FF","#be1cd4","#db1818","#ffff33","ff5e00"]
            accent = random.choice(color_list)

        elif accent == "professional":
            accent = "#C0C0C0"


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

        ## tab widget to center(values: center, left, right)
        self.main_tab_widget.setStyleSheet('''
        QTabWidget::tab-bar {
            alignment: left;
        }''')
            
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
