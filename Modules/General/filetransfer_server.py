import socket
from pathlib import Path
import os


def s_recieve_file(LISTEN_IP, LISTEN_PORT, SAVE_FILEPATH):
    
    s = socket.socket()
    host = LISTEN_IP
    port = int(LISTEN_PORT) ## converting to integer because it is sent as a string 

    s.bind((host,port))
    s.listen() ## a block waiting for a connection
    #print("DEBUG  FT server listening")

    while True:
            
        c, addr = s.accept()
        #print("DEBUG got connection from", addr)
        #print("DEBIUG getting data")
        
        ## receiving inital bits, aka the name in this case
        path_raw = c.recv(128).decode()
        
        #print(f"NAME = {name}")
        #print(f"NAME CLEANED UP={name_raw.replace('=','')}")
        
        path_clean = path_raw.replace('=','')
        #print(path_clean)
        
        name_clean = Path(path_clean).name
        #print(f"NAME: {name_clean}")
        
        ## putting in EXFIL_DATA folder
        name = os.path.dirname(__file__) + "/../../EXFIL_DATA/" + name_clean
        #print(f"FINAL NAME:{name}")
        
        
        #print("DEBUG OPENING FILE")
        f = open(name,'wb')

        ## initializing l
        l =  c.recv(1024)
        
        while (l):
            #print(l)
            f.write(l)
            l =  c.recv(1024)
            

        
        c.close()
        f.close()
        #print("done")

#s_recieve_file("0.0.0.0", 5000, "./exfil_data_123")