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
            logging.debug("[Logec (friendly_client: Authentication)] Authentication Succeeded")
            ## will be used for GUI purposes
            self.shellbanner = f"{self.ip}:{self.port}"
            self.authenticated = True
            self.shellformat()

        else:
            logging.debug("[Logec (friendly_client: Authentication)] Authentication Failed")
            self.authenticated = False

##########
##== Server Commands & Interaction
##########

    ##== GUI to Server
    """     
        =======================================
        gui_to_server:
        
        This function talks directly to the server. 
                                    If valid client name-> gui_to_client -> server
        Flow: GUI -> gui_to_server ^-> send function -> Server
        
        TLDR: Sends command to server. If command is not for server (determined by a valid client name in the command), 
        server passes it onto the client. 
        
        if/else actions & Explanation:
        
            "self.shellformat(self.send_msg(formatted_request))"
                self.shellformat: The function that displays text in the GUI on the 'remote shell'
                self.send_msg: The universal message sending function. Has proper error handling & segmented sends (i.e over 1024 bytes)
                formatted_request: Just the request to be sent to the server, formatted so it can read it
        
            "try (command.split())[2]":
                This function decides if the command is meant for the server or the client. If a 3rd item in the list 
                exists, that means the client name has been included in the command and it is meant for a client. 
                It's right away to be more efficient/not cause any errors later
        
    """
    def gui_to_server(self, command):
        #print("gui to server triggered")
        self.shellbanner = f"{self.ip}:{self.port}"
        
        formatted_request = f"!_servercommand_!\\|/{self.username}\\|/{command}"
        
        try:
            command.split()[2] in self.current_client_list
            self.gui_to_client(command)
        
        except:
            if command.lower() == "clients":
                self.shellformat(self.send_msg(formatted_request))

            elif command.lower() == "clear":
                self.shellformat()
            
            elif command.lower() == "export-clients":
                self.shellformat(self.send_msg("export-clients"))
                
            else:
                #self.gui_to_client(command)
                self.shellformat(f"command {command} not found")
                logging.debug(f"Command {command} not found.") 

    ##== GUI to client 
        """     
        =======================================
        gui_to_client:
        
        If A command is not meant for the server, it comes here. See the diagram
        
                                 !!>>   If valid client name-> gui_to_client -> server <<!!
        Flow: GUI -> gui_to_server ^-> send function -> Server
        
        TLDR: Sends command to server that are meant for clients. 
        
        if/else actions & Explanation:
        
        """
        
    def gui_to_client(self, raw_command):

        #self.shellbanner = f"{client_name}"
        command = raw_command.split()

        try:
            client_command = command[0]
            client_command_value = command[1]
            client_name = command[2]
        except:
            self.shellformat("Please enter a valid command")
            
        formatted_request = f"!_clientcommand_!\\|/{self.username}\\|/{client_command} {client_command_value} {client_name}"
        
        if client_command == "" or client_command == "help":
            self.shellformat("Standin for help menu from server")

        else:
            #print("ELSE")
            #yes I know this is blindly sending commands to the server, but it makes it easier to manage all 3 puzzle pieces
            self.shellformat(self.send_msg(formatted_request))

    ##== Additional GUI
        """     
        =======================================
        shellformat:
        
        The backbone of this module, this emit's (via a Signal) the results of a command to the 'Remote Shell' in the gui.
        
                
        Flow: Response From server -> shellformat -> GUI
        
        Addtl Explanation:
            'f"{self.shellbanner}>\n{results}"':
                This line jsut adds the shellbanner to the 'Remote Shell', which is 'ip:port>'
                It makes it look cool/like a real shell
                "Am I a real shell?" [https://www.youtube.com/watch?v=_jkg6xcetV0]
        
        """
    def shellformat(self, results="Empty Result Set") -> None:
        #print("Debug: " + results)
        #print("shellformat triggered")
        formatted_results = (
            f"{self.shellbanner}>\n{results}"
        )

        self.shell_output.emit(formatted_results)
    ##== Send n Receive
        """     
        =======================================
        send_msg:
        
        Sends the message to the server, and receives it. Returns the message to whatever called it (then piped into self.shellformat)
        
                
                              If valid client name-> gui_to_client -> send function \
        Flow: GUI -> gui_to_server ^-> send function -----------------------------> / -> Server Response From server -> shellformat -> GUI

        
        """
    def send_msg(self, message=""):
        ## Add error handling later
        logging.debug(f"[Logec (friendly_client: send_msg)] sending: {message}")
        try:
            self.server.send(self.str_encode(message))
        except Exception as e:
            logging.debug(f"[Logec (friendly_client: send_msg)] Error Sending '{message}': {e}")


        full_msg = ""
        new_msg = True
        HEADERSIZE = 10

        logging.debug(f"[Logec (friendly_client: send_msg)] Waiting on response...")
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
        """     
        =======================================
        decode & encode funcitons:
        
        A set of universal functions for encoding and decoding text. handy for error handling & unique character sets,
        however that is not implemented yet.
        
        Input: The input to be decoded/encoded
        
        Output/Return: Returns a string or bytes, depending on the respective function
        
        """
    def str_decode(self, input) -> str:
        decoded_result = input.decode()
        return decoded_result

    ## str -> bytes
    def str_encode(self, input) -> bytes:
        encoded_result = input.encode()
        return encoded_result
    