import socket
import os
from typing import Tuple
import logging
from PySide6.QtCore import QThread, Signal, QObject, Slot


global_debug = True

logging.basicConfig(level=logging.DEBUG)
logging.basicConfig(filename='../friendly_client.log', filemode='a', format='%(name)s - %(levelname)s - %(message)s', force=True)

if global_debug:
    logging.getLogger().addHandler(logging.StreamHandler())

class FClient(QObject):
    shell_output = Signal(str)
    authenticated = Signal(bool)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.encoding = 'utf-8'
        self.buffer = 1024
        self.authenticated = False
        self.shellbanner = "NotConnected"
        self.current_client_list = []

    def connect_to_server(self, connlist: Tuple[str, str, str, str]) -> None:
        self.ip, self.port, self.username, password = connlist

        logging.debug(f"Connection List: {connlist}")

        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_addr = (self.ip, int(self.port))

        try:
            self.server.connect(self.server_addr)
        except ConnectionRefusedError:
            self.authenticated = False
            logging.debug("Connection Refused")
        except Exception as e:
            logging.debug(f"Unkown Error: {e}")
    ##== Login String
        self.server.send(self.str_encode(f"!_userlogin_!\\|/{self.username}\\|/{password}"))
        auth_attempt_response = int(self.server.recv(1024).decode())

        logging.debug(f"Server Authentication Respones: {auth_attempt_response}]")

        if auth_attempt_response == 0:
            logging.debug("Authentication Succeeded")
            ## will be used for GUI purposes
            self.shellbanner = f"{self.ip}:{self.port}"
            self.authenticated = True
            self.shellformat()

        else:
            logging.debug("Authentication Failed")
            self.authenticated = False

    ##== Done

    ##== Server Commands & Interaction
    def gui_to_server(self, command):
        self.shellbanner = f"{self.ip}:{self.port}"
        if command.lower() == "clients":
            self.shellformat(self.server_request("clients"))

        elif command.lower() == "clear":
            self.shellformat()
        
        elif command.lower() == "get-jobs":
            server_supported_jobs = (
                "Possible Jobs (Some may not be available on older clients):\n"
                "set-heartbeat\n"
                "wait\n"
                "run-command\n"
            )
            self.shellformat(server_supported_jobs)

        elif command.lower() == "help" or command.lower() == "":
            print("HELPMENU TRIGGERED")
            helpmenu = (
                "Home: \n"
                "refresh - refreshes the current connected clients \n"
                "stats - ' [BETA] Prints all clients stats'\n"
            )
            self.shellformat(helpmenu)

        elif command in self.current_client_list:
            self.shellformat("Client Exists")
            logging.debug("Client Exists, and is present")  
            self.gui_to_client("client_interact",command)

        else:
            self.shellformat(f"command not found")
            logging.debug(f"Command {command} not found.") 

    ##== Client Commands & Interaction

    def gui_to_client(self, command, client_name):
        """
            A subshell of the gui_to_server shell, meant to handle
            an individual client. 

            Works in a loop, and when a user types home, it *should*
            put itself back into the gui_to_server function
        """
        self.shellformat = f"{client_name}"
        while True:
            if command == "" or command == "help":
                self.shellformat("Standin for help menu from server")
            
            elif command == "client_interact":
                self.shellformat()
            elif command == "home":
                self.gui_to_server("clear")
                break

        

  


    ##== Additional GUI
    def shellformat(self, results="") -> None:
        """Format the shell output and emit the formatted results."""
        print("Debug: " + results)

        formatted_results = (
            f"{self.shellbanner}>\n{results}"
        )

        self.shell_output.emit(formatted_results)

    ##== QOL
    def str_decode(self, input) -> str:
        decoded_result = input.decode()
        return decoded_result

    ## str -> bytes
    def str_encode(self, input) -> bytes:
        encoded_result = input.encode()
        return encoded_result

"""
Basically:

connect to client

take  command, if  for client, send for client (!_clientcommand_!)

if for server, send to server (!_servercommand_!)

receive response, and display respose
"""

