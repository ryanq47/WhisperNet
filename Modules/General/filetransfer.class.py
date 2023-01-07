import socket
import time

class s_recieve():
    def __init__(self):
        self.c = False
    
    def connect(self):
        self.s_ = socket.socket()
        host = "0.0.0.0"
        port = 5000

        self.s_.bind((host,port))
        
    def transfer(self):
        with open('data_exfil.txt','wb') as f:
            self.s_.listen()
            print("listening")

            while True:
                
                self.c, addr = self.s_.accept()
                print("got connection from", addr)
                print("getting data")

                ## receiving inital bit
                l = self.c.recv(1024)
                #print(f"{l} << should be data here")

                ## while there is data being transfered, write to  file
                while (l):
                    print(l)
                    f.write(l)
                    l =  self.c.recv(1024)

                print("done")
                self.c.close()
    def main(self):
        self.c = False
    
        while True:
            
            if self.c:
                print("connected")
                #pass
            else:
                print("Listening for connection")
                s_recieve.connect(s_recieve)
                self.transfer(s_recieve)
                
                
            time.sleep(.001)

s_recieve.main(s_recieve)