from datetime import datetime, timezone, time
import time
import psutil
import os

import speedtest 
#import dns
import dns.resolver
import dns.query
import requests
import logging

import zipfile
import tarfile

from plyer import notification
from PySide6.QtCore import Signal, QObject

logging.basicConfig(level=logging.DEBUG)
logging.basicConfig(filename='logs/utility.log', filemode='a', format='%(name)s - %(levelname)s - %(message)s', force=True)
class Timestamp:
    ## using static here cause ther is no need to initialize this class all over. 
    @staticmethod
    def UTC_Time():
        current_date_time = datetime.now(timezone.utc)
        
        current_time = current_date_time.strftime("%H:%M:%S")
        #print(current_time)
        return current_time
    @staticmethod
    def UTC_Date():
        current_date_time = datetime.now(timezone.utc)
        
        current_date = current_date_time.date()
        #print(current_date)
        return current_date
    
class Performance(QObject):
    return_value = Signal(str)
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.PID = os.getpid()
        self.net_io_counters = psutil.net_io_counters()
        
    def CPU_all(self):
        return psutil.cpu_percent()
    
    def CPU_program(self):
        p = psutil.Process(self.PID)
        print(self.PID)
        print("Program CPU USAGE")
        return p.cpu_percent()
    
    def CPU_temp(self):
        ## Doesn't work in most VM's need to do a try/except for this
        try:
            temp = psutil.sensors_temperatures()['coretemp'][0].current
        except:
            temp = "N/A"
        return temp
        
    def RAM_all(self):
        self.p = int((psutil.virtual_memory()[2]))
        #print(self.p)
        return self.p
    
    def RAM_HumanReadable(self):
        mem = psutil.virtual_memory().used
        mem_str = psutil._common.bytes2human(mem)
        
        return mem_str
        
    def RAM_program(self):
        p = psutil.Process(self.PID)
        mem_per = p.memory_percent()
        
        mem = mem_per * .01
        print(mem)
        
        print(self.PID)
        
        mem_2 = (self.p[1] * mem)/100000
        
    def Network_out(self):
        bytes_sent = self.net_io_counters.bytes_sent
        return round((bytes_sent / 1048576), 2)
    
    def Network_in(self):
        bytes_recv = self.net_io_counters.bytes_recv
        return bytes_recv

    def start_time(self):
        self._start_time = time.time()
        
    def end_time(self):
        self._end_time = time.time()
        
        time_to_run = self._end_time - self._start_time
        self._start_time = 0
        self._end_time = 0
        
        return str(round(time_to_run,2))

    def benchmark(self):
        self.start_time()
        init_number = 0
        
        #100mil
        while init_number <= 1000000000:
            init_number = init_number + 1
                
            #init_number * (init_number/5)
        self.return_value.emit(str(self.end_time()))


class Host(QObject):
    def __init__(self):
        super().__init__()
    
    def sys_notification(self, notif_list):
        notification.notify(
            title = f"{notif_list[0]}",
            message = f"{notif_list[1]}",
            app_icon = "IMAGE",
            timeout = 10
            )
        
    def download(self, download_dict):
        #url = download_list[0]
        #save_location = download_list[1]
        #name = download_list[2]
    
        dir = download_dict['SavePath'] + "/" + download_dict['SaveName']

        logging.info(f"[Utility (download)] Making request for: {download_dict['URL']}")
        #print("Making Request")
        r = requests.get(download_dict['URL'], allow_redirects=True)
        #print("writing")
        #print(r.content)
        try:
            with open(dir,'wb+') as filewrite:
                filewrite.write(r.content)
        except Exception as e:
            print(e)
        logging.info(f"[Utility (download)] Download Complete: {download_dict['URL']}")

        if download_dict['IsZipArchive']:
            logging.info(f"[Utility (download)] Extracting {download_dict['SavePathAndName']} to {download_dict['SavePath']}")
            FileOps.unzip(filepath=download_dict['SavePathAndName'], extract_path=download_dict['SavePath'])


class FileOps:
    @staticmethod
    def unzip(filepath="", extract_path=""):
        """Extract files from archive, handles tar.gz and .zip"""
        if filepath.endswith('.zip'):
            with zipfile.ZipFile(filepath, 'r') as archive:
                archive.extractall(extract_path)

        elif filepath.endswith('.tar.gz') or filepath.endswith('.tgz'):
            with tarfile.open(filepath, 'r:gz') as archive:
                archive.extractall(extract_path)
        else:
            logging.debug(f"[Utility (FileOps.unzip)] Unknown filetype: {filepath}")


## this guy could use a rewrite/optimization wiht some error handling too
class Network(QObject):
    lookupall = Signal(dict)
  
    def __init__(self):
        super().__init__()
        try:
            self.st = speedtest.Speedtest()
        except:
            print("ERROR: SpeedTest Down")

  
    def download(self):
        return ((self.st.download())/1000000)  
    
    def upload(self):
        return (self.st.upload()/1000000)
    
    def ping(self):
    
        servernames =[]  
    
        self.st.get_servers(servernames)  

        #print(self.st.results.ping)
        return self.st.results.ping
    
    def lookup_A(self, cname):
        try:
            ## Returns a list of items
            name = dns.resolver.resolve(cname, 'A')
            print(f"NAME: {name}")
            
            namelist = []

            for i in name:
                namelist.append(i.to_text())
            
            return namelist
        except Exception as e:
            print(e)
            return "NONE"
    
    def lookup_CNAME(self, name):
        try:
            ## Returns a list of items
            name = dns.resolver.resolve(name, 'CNAME')
            
            namelist = []

            for i in name:
                namelist.append(i.to_text())
            
            return namelist
        
        except:
            return "NONE"    
    def lookup_MX(self, name):
        try:
            ## Returns a list of items
            name = dns.resolver.resolve(name, 'MX')
            
            namelist = []

            for i in name:
                namelist.append(i.to_text())

            return namelist
        
        except:
            return "NONE"
        
    def lookup_TXT(self, name):
        try:
            ## Returns a list of items
            name = dns.resolver.resolve(name, 'TXT')
            
            namelist = []

            for i in name:
                namelist.append(i.to_text())

            return namelist
        except:
            return "NONE"
    
    def lookup_NS(self, name):
        try:
            ## Returns a list of items
            name = dns.resolver.resolve(name, 'NS')
            
            namelist = []

            for i in name:
                namelist.append(i.to_text())

            return namelist
        except:
            return "NONE"
    
    def lookup_REVERSE(self, IP):
        try:
            ## Returns a list of items
            name = dns.reversename.from_address(IP)
            
            ## No iteration due to python seperating the string at each . :(
            
            namelist = (str(dns.resolver.resolve(name,"PTR")[0]))
            return namelist  
        
        except:
            return "NONE"
    
    def lookup_RAW(self, IP):
        """Being a pain, will figure out later"""
        try:
            raw_record = dns.response.to_wire(IP)
        
        except:
            raw_record = "NONE"
            
        return raw_record
    
    def lookup_All(self, IP):        
        record_list = {
            'A' : self.lookup_A(IP),
            'CNAME' : self.lookup_CNAME(IP),
            'MX' : self.lookup_MX(IP),
            'Reverse': self.lookup_REVERSE(IP),
            'TXT' : self.lookup_TXT(IP),
            'NS' : self.lookup_NS(IP),
            'RAW' : self.lookup_RAW(IP)
            }
        #print(record_list)
        self.lookupall.emit(record_list)
        #return record_list
        
            
    
    
#N = Network()
#print(N.lookup_NS("courts.state.mn.us"))
#N.lookup_Reverse("8.8.8.8")

'''
N = Network()


print(N.download())
print(N.upload())
print(N.ping())'''
'''

ml = 1

while True:
    ml = ml *2 **20 **2
    os.system('clear')
    P = Performance()
    print(P.CPU_all())
    print(P.CPU_program())

    #print(P.RAM_all())
    #print(P.RAM_program())
    time.sleep(.0001)'''
