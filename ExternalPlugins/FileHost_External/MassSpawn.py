endrange = 100
import os
import time
import threading

def zefunc():
    os.system(f"python3 FileHost_External.py --ip 127.0.0.1 --port 500{i} --name filehost0{i} --quiet")

for i in range(1,endrange):
    z = threading.Thread(target=zefunc)
    z.setDaemon = True
    z.start()