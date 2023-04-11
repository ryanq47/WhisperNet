import socket
import os
from typing import Tuple
import logging
from PySide6.QtCore import QThread, Signal, QObject, Slot


global_debug = True

logging.basicConfig(level=logging.DEBUG)
logging.basicConfig(filename='friendly_client.log', filemode='a', format='%(name)s - %(levelname)s - %(message)s', force=True)

#if global_debug:
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

    ##== Server Commands & Interaction
    """
        This function is for the shell that interacts with the server, it's the first
        shell presented to the user in the gui

        Requests to the server are often one liners:
            self.shellformat(self.server_request("clients"))
        
            This asks the server for client data by sending it the 'clients' command
            and then passes the return value (which in this case is the clients)
            into the shellformat, which displays it on the GUI (via an emit)
    """
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
        
        elif command.lower() == "clients":
            self.shellformat(self.server_request("clients"))

        elif command.lower() == "help" or command.lower() == "":
            print("HELPMENU TRIGGERED")
            helpmenu = (
                "Home: \n"
                "refresh - refreshes the current connected clients \n"
                "stats - ' [BETA] Prints all clients stats'\n"
            )
            self.shellformat(helpmenu)

        elif (command.split())[0] in self.current_client_list:
            #logging.debug("Client Exists, and is present") 
            ## Getting hung here
            self.gui_to_client(command)

        else:
            self.shellformat(f"command {command} not found")
            logging.debug(f"Command {command} not found.") 

    ##== requests to server
    """
        This function actually sends the commands to the server, and returns its repsonses
        
    """
    def server_request(self, request, client_name=None):
        if request == "clients":
            formatted_request = f"!_servercommand_!\\|/{self.username}\\|/{request}"
            logging.debug(f"Sending {formatted_request}")
            self.server.send(self.str_encode(formatted_request))

            """
            THis function is slighty special as it sets the output to a self variable,
            then returns it, hency why it needs its own if
            """
            self.current_client_list = self.receive() 

            return self.current_client_list
        
        else:
            logging.debug(f"Invalid request: {request}")
            return "Invalid Server Request"

    ##== Client Commands & Interaction

    def gui_to_client(self, raw_command):
        """
            This function is for controlling clients
            syntax is
            client-name job value

            Error handling:
            The server does all the error handling on any bad commands,
            but if there is a local issue this code handles it. 

        """
        #self.shellbanner = f"{client_name}"
        command = raw_command.split()

        try:
            client_name = command[0]
            client_command = command[1]
            client_command_value = command[2]
        except:
            self.shellformat("Please enter a valid command")

        print(raw_command)
        
        if client_command == "" or client_command == "help":
            self.shellformat("Standin for help menu from server")

        else:
            #print(f"Command not recognized: {client_command}")
            com = f"{client_command} {client_command_value}"
            self.shellformat(self.client_request(com, client_name))

    ##==client requeset
    """
        This function is very simialr to the server_request,  but uses !_clientcommand_!
        as its header instead of !_servercommand_!

        All it does, is formats and sends requests to the server,
        the recieves the response, and returns it so it can get formatted &
        displayed

        A correctly formatted_request may look liek:
        !_clientcommand_!\\|/bob\\|/set-heartbeat 15 client_127_0_0_1_UDDSZ

        The server recieves the command as:
        Command      Value ClientName
        set-heartbeat 15 client_127_0_0_1_FCECW

        In a nutshell, these 2 are broken up for clarity

    """
    def client_request(self, request, client_name):
        print(request)
        formatted_request = f"!_clientcommand_!\\|/{self.username}\\|/{request} {client_name}"
        logging.debug(f"Formatted request: {formatted_request}")
        self.server.send(self.str_encode(formatted_request))
        return self.receive()


    ##== Additional GUI
    def shellformat(self, results="") -> None:
        """Format the shell output and emit the formatted results."""
        print("Debug: " + results)

        formatted_results = (
            f"{self.shellbanner}>\n{results}"
        )

        self.shell_output.emit(formatted_results)

    ##== Some Networking stuff
    def receive(self):
        """
        Receives response from the server, and breaks it down into
        1024 (or whatever you want the size to be - see self.buffer) bytes
        """
        full_msg = ""
        new_msg = True
        HEADERSIZE = 10

        while True:
            msg = self.server.recv(int(self.buffer))  # << adjustble, how many bytes you want to get per iteration
            if new_msg:
                # Carving up msg into the first X bytes (X = headersize)
                msglen = int(msg[:HEADERSIZE])
                new_msg = False

            print(f"full message length: {msglen}") if global_debug else None
            print(f"msg partial:" + msg.decode()) if global_debug else None
            full_msg += self.str_decode(msg)

            print("total bytes received: " + str(len(full_msg))) if global_debug else None

            # if the full message matches the originally sent message size (msglen) (excluding headers) message has been sent
            if len(full_msg) - HEADERSIZE == msglen:
                print("full msg recvd") if global_debug else None
                print(full_msg[HEADERSIZE:]) if global_debug else None
                new_msg = True

                # returning full message and stripping header
                return full_msg[HEADERSIZE:]

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

