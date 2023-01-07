from datetime import datetime, timezone, time
import time
import psutil
import os

import speedtest  


class Timestamp:
    
    def UTC_Time():
        current_date_time = datetime.now(timezone.utc)
        
        current_time = current_date_time.strftime("%H:%M:%S")
        print(current_time)
        return current_time
    
    def UTC_Date():
        current_date_time = datetime.now(timezone.utc)
        
        current_date = current_date_time.date()
        print(current_date)
        return current_date
    
class Performance:
    
    def __init__(self):
        self.PID = os.getpid()
        
    def CPU_all(self):
        return psutil.cpu_percent()
    
    def CPU_program(self):
        p = psutil.Process(self.PID)
        print(self.PID)
        print("Program CPU USAGE")
        return p.cpu_percent()
        
    def RAM_all(self):
        self.p = int((psutil.virtual_memory()[2]))
        #print(self.p)
        return self.p
        
    def RAM_program(self):
        p = psutil.Process(self.PID)
        mem_per = p.memory_percent()
        
        mem = mem_per * .01
        print(mem)
        
        print(self.PID)
        
        mem_2 = (self.p[1] * mem)/100000
        
        return mem_2

class Network:

  
    def __init__(self):
        self.st = speedtest.Speedtest()

  
    def download(self):
        return ((self.st.download())/1000000)  
    
    def upload(self):
        return (self.st.upload()/1000000)
    
    def ping(self):
    
        servernames =[]  
    
        self.st.get_servers(servernames)  

        #print(self.st.results.ping)
    
        return self.st.results.ping

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