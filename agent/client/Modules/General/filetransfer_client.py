import socket               # Import socket module
import os
import math
import time


def c_connect(IP, PORT):
    c_connect.s = socket.socket() 
    host = IP 
    port = PORT

    try:
        c_connect.s.connect((host, port))
        return True
    except ConnectionRefusedError:
        print("DEBUG cannot find server")
        time.sleep(30)


def c_transfer(FILEPATH):
    try:
        f = open(FILEPATH,'rb')
        size = os.path.getsize(FILEPATH)

        number_of_it =  math.ceil(size / 1024)

        print(size)
        print(number_of_it)
        
        ## == Calculcating buffer n stuff
        
        ## length of name
        name_len = len(FILEPATH)
        print(f"{name_len} <<LENGTH OF NAME")
        
        ## calculating buffer size
        buffer = 128 - name_len
        
        ## buffer block equal to 128 bits - yes I know this excedes the PEP max amount of characters per line
        buffer_block = "================================================================================================================================"
        
        ## Getting filepath, aka name
        name = FILEPATH
        
        ## putting name, + buffer together for the name "frame"
        name_frame = name + (buffer_block[:buffer])
        
        print(name_frame)
        
        print("DEBUG: Sending NAMe")
        
        ## sending name frame
        c_connect.s.send(name_frame.encode())
        
        
        print('DEBUG Sending...')
        
        # sending rest of data
        for i in range(1, number_of_it + 1): # sending interations + 1 to get all data

            #while (l):
            print('DEBUG Sending...')
            data = f.read(1024)
            l = data
            c_connect.s.send(l)
            

        f.close()
        print("DEBUG Done Sending")

        c_connect.s.shutdown(socket.SHUT_WR)
        print("DEBUG End of script")
        c_connect.s.close 
    
    ## catching errors so this dosen't crash
    except Exception as e:
        ## trying to send error message back, not working
        c_connect.s.send(str(e).encode())
        print(f"DEBUG: {e}")

def main(IP, PORT, FILEPATH):

    if c_connect(IP, PORT):
        c_transfer(FILEPATH)

    else:
        print("DEBUG Not Connected")

    
    
    
## each click will do one transfer, while the server will always be listening
#main("127.0.0.1", 5000, "./data.txt")