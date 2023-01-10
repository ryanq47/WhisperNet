#! /usr/bin/python3
##portscanner.py
## TCP flags: https://www.firewall.cx/networking-topics/protocols/tcp/136-tcp-flag-options.html

## really cool scapy connection stuff:
#https://0xbharath.github.io/art-of-packet-crafting-with-scapy/network_recon/host_discovery/index.html

from logging import getLogger, ERROR
getLogger("scapy.runtime").setLevel(ERROR)

from scapy.all import *
import sys
from datetime import datetime
from time import strftime
import sqlite3
import os.path


import Modules.General.utility as utility
print("IMPORTED")
print(utility)

#ports = range(int(min_port), int(max_port)+1)
start_clock = datetime.now()
SYNACK = 0x12
RSTACK = 0x14
    
def checkhost(ip):
    #conf.verb = 0
    try:
        ping = sr1(IP(dst = ip)/ICMP(), timeout = 3)
        if ping == None:
            return False
        else:
            return True
    
    except Exception as e:
        print(e)
        #print("Could not resolve target")
        sys.exit(1)
    
## =====
## Standard Scan
## =====

def standard_scan(target_list):
    print("Started Standard Scan")

    #print(port_range)
    #        target_list = [ip, min_port, max_port, extra_port]
    Date = utility.Timestamp.UTC_Date()
    Time = utility.Timestamp.UTC_Time()
    ScanType = "Standard"
    
                    ## Min Port         Max Port            Extra Ports
    ScannedPorts = f"{target_list[1]}-{target_list[2]},{str(target_list[3]).replace(']','').replace('[','')}" 
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
    
    #print(f"DEBUG: PORTS TO SCAN {ports_to_scan}")
    
    ## == Main loop to scan ports
    for i in ports_to_scan: ## +1 due to range function
        srcport = RandShort()
        conf.verb = 0
        
        ## sending packet and getting flags back
        try:
            SYNACKpkt = sr1(IP(dst = target_list[0])/TCP(sport = srcport, dport = i, flags = "S"), timeout = 2)
            ## Handling weird stoppage problem
            if SYNACKpkt == None:
                pktflags = None
                continue
            else:
                pktflags = SYNACKpkt.getlayer(TCP).flags
            
        except Exception as e:
            pktflags = None
            print(e)
        
        ## RST packet
        FINpkt = IP(dst = target_list[0])/TCP(sport = srcport, dport = i, flags = "F")
        
        ## return logic
        if pktflags == SYNACK:
            send(FINpkt)
            print(f"{i}/tcp is open")
            open_list.append(i)
        
        elif pktflags == None:
            continue
        else:
            pass

        if i == target_list[2]:
            print("COMPLETE!")
            
    ## Writing DB
    database_write(f"'{open_list[0]}'", ScanType, Date, Time, "01:00", ScannedPorts, {str(set(open_list[1:]))}) #[1:] means to end of list

## =====
## Stealth (RST) Scan
## =====

#def stealth_scan(target_ip, port_range):
def stealth_scan(target_list):
    print("Started Stealth Scan")
    #print(port_range)
    #        target_list = [ip, min_port, max_port, extra_port]
    Date = utility.Timestamp.UTC_Date()
    Time = utility.Timestamp.UTC_Time()
    ScanType = "Stealth"
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
    
    #print(f"DEBUG: PORTS TO SCAN {ports_to_scan}")
    
    ## == Main loop to scan ports
    for i in ports_to_scan: ## +1 due to range function
        #print(f"DEBUG: {target_ip}, {port}")
        
        srcport = RandShort()
        conf.verb = 0
        
        ## sending packet and getting flags back
        try:
            SYNACKpkt = sr1(IP(dst = target_list[0])/TCP(sport = srcport, dport = i, flags = "S"), timeout = .01)
            ## Handling weird stoppage problem
            if SYNACKpkt == None:
                pktflags = None
                continue
            
            else:
                pktflags = SYNACKpkt.getlayer(TCP).flags
            
        except Exception as e:
            pktflags = None
            print(e)
        
        ## RST packet
        RSTpkt = IP(dst = target_list[0])/TCP(sport = srcport, dport = i, flags = "R")
        
        ## return logic
        if pktflags == SYNACK:
            send(RSTpkt)
            print(f"{i}/tcp is open")
            
            open_list.append(i)
        
        elif pktflags == None:
            continue
        else:
            pass

        if i == target_list[2]:
            print("COMPLETE!")
    
    ## Writing DB
    database_write(f"'{open_list[0]}'", ScanType, Date, Time, "01:00", ScannedPorts, {str(set(open_list[1:]))}) #[1:] means to end of list

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
    
    

def event_loop(target_list, scantype_list):
    
    '''
    cheatsheet for lists
    target_list = [ip, min_port, max_port, extra_port]
    scantype_list = [standard, stealth]
    '''
    
    ## info if needed for data manip
    ip = target_list[0]
    min_port = target_list[1]
    max_port = target_list[2]
    extra_port = target_list[3]
    

    ## scantype logic
    if scantype_list[0]: ## standard scan
        #pass
        standard_thread = threading.Thread(target=standard_scan, args=([target_list]))
        #standard_scan(target_list)
        standard_thread.start()
        
    if scantype_list[1]: ## standard scan
        stealth_thread = threading.Thread(target=stealth_scan, args=([target_list]))
        #standard_scan(target_list)
        stealth_thread.start()
    
    
    '''
    user_input_list = user_input()
    
    ## passing min, and max port into the port calc. Portcalc is its own function for future scalability reasons
    port_calc_list = port_calc(user_input_list[1],user_input_list[2])
    
    #print(f"[DEBUG]: {port_calc_list}")
    print("Starting scan... please be patient")
    
    #       Start POrt              End port                 Additional ports
    port = [int(user_input_list[1]), int(user_input_list[2]), user_input_list[3]]
    status = stealth_scan(user_input_list[0], port) '''

## For standalone... not being used rn, will be used later
def user_input():
    conf.verb = 0
    
    input_values = []
    
    input_values.append(input("Enter IP Address: "))
    
    ## Host check
    print("Checking if host is online to save some typing...")
    if checkhost(input_values[0]) == True:
        print("Host is online!")
    else:
        print("Host is seemingly OFFLINE! - it may just not be responding to pings. Hit Enter to continue anyways:")
        input()
    
    input_values.append(input("Enter Min Port: "))
    input_values.append(input("Enter max port: "))
    
    ## logic for addon ports
    ports_addon_list = []
    ports_addon = input("Enter AddOn ports (seperate by a comma): ")
    for i in ports_addon:
        ports_addon_list.append(i)
    
    ## splitting the user input in the list
    input_values.append(ports_addon.split(','))
    
    ## return list 
    return input_values
    
    

def port_calc(min_port, max_port):
    ports = range(int(min_port), int(max_port)+1)
    return ports


#checkhost("127.0.0.1")
#event_loop()