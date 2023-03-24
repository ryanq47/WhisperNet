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

    ##== Initial Connection
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
                self.id = response_list[0]
                self.message = response_list[1]
                logging.debug(f"Client Established: {self.client_remote_ip_port} id={self.id}")

            except:
                ## Not setting self.id as it's first in the list, and SHOULD alwys have a value
                ## however an empty request may fool it
                self.message = "None"
                logging.debug(f"No message value was recieved. id={self.id} message={self.message}")

            ## == Decisions based on parsed messages
            if self.id == "!_userlogin_!":
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
                    logging.critical(f"Failed logon  from {username}, {self.client_remote_ip_port}")

################
## Client Fucntions
################ 

## If the job is not meant for the server, it filters down to here.
## this interacts with the self.clients interact function, which sets jobs 
## for the event loop to do on heartbeats

## TLDR: This sets jobs or gets current data from the current selected client

#                           Action      Value    Target Client 
#requests look like this: set-heartbeat 15 client_127_0_0_1_FCECW


##! Up next, per client, and then after that, friendlt client classes




################
## QOL Functions
################
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
