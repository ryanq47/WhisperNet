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


##Reference: https://realpython.com/python-logging/
logging.basicConfig(level=logging.DEBUG)
logging.basicConfig(filename='server.log', filemode='a', format='%(name)s - %(levelname)s - %(message)s', force=True)
#logging.debug('This will get logged')

global_debug = True

class ServerSockHandler:
    """
    Description: A class that handles the inital connections, and sends them
    to the other respective classes as needed

    
    """

    def __init__(self):
        self.server_password = "1234"

        ##Errors relevant to this funtion
        self.Sx01 = "conn_broken_pipe: A pipe was broken"
        self.Sx02 = "Socket Close: The socket was successfully closed"
        self.Sx10 = "client_unkown_input: An unkown input was receieved from the client"

        self.SxXX = "Unkown error: "
    def socket_cleanup(self):
        #pass
        try:
            self.server.close()
            logging.debug(self.Sx02)

        except Exception as e:
            logging.warning(f"{self.SxXX}:{e}")
    

            
            #if value:
                #err_string += f"Err: {i[1]}"
                
        #print(err_string)


s = ServerSockHandler()
s.socket_cleanup()
logging.debug("ServerSockHandler Called")
