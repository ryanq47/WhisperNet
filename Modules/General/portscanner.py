from logging import getLogger, ERROR
getLogger("scapy.runtime").setLevel(ERROR)

from PyQt5.QtCore import QRunnable, Qt, QThreadPool, QObject, QThread, pyqtSignal
from scapy.all import *
import sys
from datetime import datetime
from time import strftime
import sqlite3
import os.path
from telnetlib import Telnet

from concurrent.futures import ThreadPoolExecutor
import Modules.General.utility as utility


#ports = range(int(min_port), int(max_port)+1)
start_clock = datetime.now()
SYNACK = 0x12
RSTACK = 0x14


class Portscan(QObject):
    finished = pyqtSignal()
    progress = pyqtSignal(int)
    liveports = pyqtSignal(list)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.open_port_list = []
        self.scantype = ""
        self.stealth_scan_status = 0
        self.standard_scan_status = 0
        self.N = utility.Network()
        self.scan_progress = 0
        
        
    def clean(self):
        self.open_port_list = []
    
    def scan_framework(self, target_list, scantype):
        # target_list = [ip, min_port, max_port, timeout, delay, extra_port]
        # scantype list = [standard, stealth, ??] A list of scan booleans, true means do it, false means dont
                        ## Min Port         Max Port            Extra Ports
        ScannedPorts = f"{target_list[1]}-{target_list[2]},{str(target_list[3]).replace(']','').replace('[','')}" ## jank but it works
        open_list = [target_list[0]]
        
        self.host = target_list[0]
        self.minport = target_list[1]
        self.maxport = target_list[2]
        self.timeout = target_list[3]
        self.delay = target_list[4]

        ## == Creating components of port list
        ## Init ports to be scanned list
        ports_to_scan = []
        
        ## port range
        port_range_list = range(target_list[1],target_list[2])
        for i in port_range_list:
            ports_to_scan.append(i)
        
        ## == extra addon ports
        for i in target_list[5]:
            ports_to_scan.append(int(i))
            
        ## == Date n time
        Date = utility.Timestamp.UTC_Date()
        Time = utility.Timestamp.UTC_Time()
        
        '''
        ## Host lookup (easier on error handling to have the utility file do it instead of scapy with executor)
        ## For multiple input IP's create a for loop to each do them
        self.host = self.N.lookup_A(target_list[0])[0]
        #print(self.host)
        if self.host == "N": ## workaround to keep multiple ip functionality intact (list[0] returns N)
            print("HOST NOT FOUND")
            #self.GUI.ERROR("Host Not Found","Low","The host could not be located, double check hostnames/IP addresses") << causes segfailt, would need to use connectors
            #self.GUI.root_check("portscan")
            exit()'''
            
        with ThreadPoolExecutor() as executor:
            # submit the scan_port function for each port in the ports_to_scan list
            if scantype[0]: #Telnet Standard
                standard_futures = [executor.submit(self.telnet_standard_scan, self.host, port, scantype[-1], self.delay) for port in ports_to_scan]
                standard_P = utility.Performance()
                standard_P.start_time()

                for future in standard_futures:
                    future.result()

                self.final_time = standard_P.end_time()

                
            if scantype[1]: #Scapy stealth
                #self.stealth_scan(self.host, ports_to_scan)
                
                stealth_futures = [executor.submit(self.stealth_scan, self.host, port, scantype[-1], self.delay) for port in ports_to_scan]
                stealth_P = utility.Performance()
                stealth_P.start_time()
                
                for future in stealth_futures:
                    future.result()  
                    #print("1")     
                self.final_time = stealth_P.end_time()
                
            # wait for all the futures to complete
            '''
            if scantype[2]: #Scapy fast
                fast_futures = [executor.submit(self.fast_scan, self.host, port, scantype[-1]) for port in ports_to_scan]
                fast_P = utility.Performance()
                fast_P.start_time()
                
                
                for future in fast_futures:
                    future.result() 
                    #print("2")    
                self.final_time = fast_P.end_time()'''
        print(self.open_port_list)
        
        #print(self.stealth_scan_status)
        ## Need to return/emit this as a list back to the main program
        database_write(f"'{open_list[0]}'", self.scantype, Date, Time,  self.final_time, ScannedPorts, {str(set(self.open_port_list))}, str(self.delay).replace("[","").replace("]","").replace(",","-")) #[1:] means to end of list
        self.clean()
        ## Emiting that program is done
        #self.progress.emit(100)
        self.finished.emit()    

    ##########
    # Telnet Scans
    ##########

    def telnet_standard_scan(self, ip, port, timeout_time, delay):
        #print(f"TIMEOUT TIME IN MODULE: {timeout_time}")
        #srcport = RandShort()
        conf.verb = 0
        self.scantype = "Standard"

        
        #print(ip, port)
        try:
            #with Telnet(ip, port, timeout_time) as tn:
            tn = Telnet(ip, port)
            self.open_port_list.append(port)
            self.liveports.emit(self.open_port_list)
            tn.close()
        except Exception as e:
            try:
                tn.close()
            except:
                pass
            #print("closed")

        self.scan_progress = self.scan_progress + 1
        self.progress.emit(int(self.scan_progress / self.maxport * 100))  
        
        time.sleep(random.uniform(delay[0], delay[1]))


    ##########
    # Scapy Scans
    ##########
    def stealth_scan(self, ip, port, timeout_time, delay):
        srcport = RandShort()
        conf.verb = 0
        self.scantype = "Stealth"

        SYNACKpkt = sr1(IP(dst=ip)/TCP(sport=srcport, dport=port, flags="S"), timeout=timeout_time, verbose=0)
        
        if SYNACKpkt and SYNACKpkt.getlayer(TCP).flags == SYNACK:
            send(IP(dst=ip)/TCP(sport=srcport, dport=port, flags="R"), verbose=0)
            
            print(f"{port}/tcp is open")
            self.open_port_list.append(port)

        self.scan_progress = self.scan_progress + 1
        self.progress.emit(int(self.scan_progress / self.maxport * 100))
        
        time.sleep(random.uniform(delay[0], delay[1]))

    '''
    def fast_scan(self, ip, port, timeout_time):
        srcport = RandShort()
        conf.verb = 0
        self.scantype = f"Fast ({float(timeout_time)} S)"
        
        try:
            SYNACKpkt = sr1(IP(dst = ip)/TCP(sport = srcport, dport = port, flags = "S"), timeout = float(timeout_time)) ##<< This is what makes this the fast scan
            if SYNACKpkt == None:
                pktflags = None
            else:
                pktflags = SYNACKpkt.getlayer(TCP).flags
                
        except Exception as e:
            pktflags = None
            print(e)
            
        if pktflags == SYNACK:
            print(f"{port}/tcp is open")
            self.open_port_list.append(port)

        self.scan_progress = self.scan_progress + 1
        self.progress.emit(int(self.scan_progress / self.maxport * 100))  '''
            
            
#P = Portscan()
#P.scan_framework(["192.168.0.1", 1, 65535,"0"], "Stealth")



## For later - also put the input as a list
def database_write(IP, SCANTYPE, SCANDATE, SCANTIME, RUNTIME, SCANNEDPORTS, PORT, DELAY):
    try:
        ## Accesing DB in root dir
        sqliteConnection = sqlite3.connect(os.path.dirname(__file__) + '/../../logec_db')
        cursor = sqliteConnection.cursor()
        print("Successfully Connected to SQLite")
        
        ## QUick Data Fixes:
        print(str(PORT))
        if 'set' in str(PORT):
            print("FIX")
            PORT = "'No Open Ports'"

        sqlite_insert_query = f"""INSERT INTO PortScan (IP, PORT, ScanType, ScanDate, ScanTime, RunTime, ScannedPorts, Delay) 
        VALUES
        ({IP}, {str(PORT).replace("{","").replace("}","")}, '{SCANTYPE}', '{SCANDATE}', '{SCANTIME}', '{RUNTIME}', "{SCANNEDPORTS.replace("'","")}", '{DELAY}')""" ## idfk - had to manually set the '' for some reason
        
        print(sqlite_insert_query)

        #count = cursor.execute(sqlite_insert_query)
        cursor.execute(sqlite_insert_query)
        sqliteConnection.commit()
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to insert data into sqlite table", error)
        
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            #print("The SQLite connection is closed")