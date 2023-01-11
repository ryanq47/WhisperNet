from logging import getLogger, ERROR
getLogger("scapy.runtime").setLevel(ERROR)

from scapy.all import *
import sys
from datetime import datetime
from time import strftime
import sqlite3
import os.path

from concurrent.futures import ThreadPoolExecutor
#import Modules.General.utility as utility

#ports = range(int(min_port), int(max_port)+1)
start_clock = datetime.now()
SYNACK = 0x12
RSTACK = 0x14

class Portscan:
    def __init__(self):
        self.open_port_list = []
        self.stealth_scan_status = 0
        
    def clean(self):
        self.open_port_list = []
    
    def scan_framework(self, target_list, scantype):
        #print(port_range)
        #        target_list = [ip, min_port, max_port, extra_port]
        #Date = utility.Timestamp.UTC_Date()
        #Time = utility.Timestamp.UTC_Time()
        
                        ## Min Port         Max Port            Extra Ports
        ScannedPorts = f"{target_list[1]}-{target_list[2]},{str(target_list[3]).replace(']','').replace('[','')}" ## jank but it works
        open_list = [target_list[0]]
        
        ## Init ports to be scanned list
        ports_to_scan = []
        
        ## == Creating components of port list
        ## port range
        port_range_list = range(target_list[1],target_list[2])
        for i in port_range_list:
            ports_to_scan.append(i)
        
        # extra addon ports
        for i in target_list[3]:
            #print(i)
            ports_to_scan.append(int(i))

        
        with ThreadPoolExecutor() as executor:
            # submit the scan_port function for each port in the ports_to_scan list
            if scantype[0]: #Stealth
                stealth_futures = [executor.submit(self.stealth_scan, target_list[0], port) for port in ports_to_scan]
                
                for future in stealth_futures:
                    future.result()
                
            if scantype[1]: #standard
                standard_futures = [executor.submit(self.stealth_scan, target_list[0], port) for port in ports_to_scan]
                
                for future in standard_futures:
                    future.result()            
            # wait for all the futures to complete

        print(self.open_port_list)
        print(self.stealth_scan_status)
        #database_write()
        self.clean()        

    def stealth_scan(self, ip, port):
        srcport = RandShort()
        conf.verb = 0
        
        self.standard_scan_status = self.standard_scan_status + 1
        
        try:
            SYNACKpkt = sr1(IP(dst = ip)/TCP(sport = srcport, dport = port, flags = "S"), timeout = 1)
            if SYNACKpkt == None:
                pktflags = None
            else:
                pktflags = SYNACKpkt.getlayer(TCP).flags
                
        except Exception as e:
            pktflags = None
            print(e)
            
        if pktflags == SYNACK:
            send(IP(dst = ip)/TCP(sport = srcport, dport = port, flags = "R"))
            print(f"{port}/tcp is open")
            self.open_port_list.append(port)
            
    def standard_scan(self, ip, port):
        srcport = RandShort()
        conf.verb = 0
        
        self.stealth_scan_status = self.stealth_scan_status + 1
        
        try:
            SYNACKpkt = sr1(IP(dst = ip)/TCP(sport = srcport, dport = port, flags = "S"), timeout = 1)
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

    def fast_scan(self, ip, port):
        srcport = RandShort()
        conf.verb = 0
        
        self.stealth_scan_status = self.stealth_scan_status + 1
        
        try:
            SYNACKpkt = sr1(IP(dst = ip)/TCP(sport = srcport, dport = port, flags = "S"), timeout = .1) ##<< This is what makes this the fast scan
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
            
            
#P = Portscan()
#P.scan_framework(["192.168.0.1", 1, 65535,"0"], "Stealth")



## For later - also put the input as a list
def database_write(IP, SCANTYPE, SCANDATE, SCANTIME, RUNTIME, SCANNEDPORTS, PORT):
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

        sqlite_insert_query = f"""INSERT INTO PortScan (IP, PORT, ScanType, ScanDate, ScanTime, RunTime, ScannedPorts) 
        VALUES
        ({IP}, {str(PORT).replace("{","").replace("}","")}, '{SCANTYPE}', '{SCANDATE}', '{SCANTIME}', '{RUNTIME}', "{SCANNEDPORTS.replace("'","")}")""" ## idfk - had to manually set the '' for some reason
        
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