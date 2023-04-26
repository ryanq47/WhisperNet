import socket
import os
from typing import Tuple
import logging
from PySide6.QtCore import QThread, Signal, QObject, Slot
import math
import time


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

    ## Connection to server
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
                
        Final notes, gui_to_client tries to split it's command into 3 parts, as it's meant for client commands, so if you only need a one 
        liner command (i.e: sanity-check) put it here, otherwise it'll error out down there on the split
        
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
                self.shellformat(self.send_msg(msg=formatted_request, conn=self.server))
            
            elif command.lower() == "sanity-check":
                self.shellformat(self.send_msg(msg=formatted_request, conn=self.server))

            elif command.lower() == "clear":
                self.shellformat()
            
            elif command.lower() == "export-clients":
                self.shellformat(self.send_msg(msg="export-clients", conn=self.server))
                
            else:
                self.shellformat(self.send_msg(msg=command, conn=self.server))
                
                #self.shellformat(f"command '{command}' not found")
                #logging.debug(f"Command {command} not found.") 

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
            self.shellformat(self.send_msg(msg=formatted_request, conn=self.server))

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
    
    ### If you saw the note in the server code about these being indepent, ignore that for this instnace. They are chained together 
    ### becuase it's easiest to send, recieve and return a message all in one go rather than have independent calls
    
    def send_msg(self, msg, conn):
        #msg = str_encode(_msg)
        
        #conn = server
        ## clients need to have a shared known header beforehand. Default is 10
        HEADER_BYTES = 10
        BUFFER = 1024
        
        ## get the length of the message in bytes
        msg_length = len(msg)
        
        ## create a header for the message that includes the length of the message
        header = self.str_encode(str(msg_length).zfill(HEADER_BYTES))#.encode()
        
        ## send the header followed by the message in chunks
        print(f"SENDING HEADER: {header}")
        conn.send(header)
        
        for i in range(0, math.ceil(msg_length/BUFFER)):
            
            ## gets the right spot in the message in a loop
            chunk = msg[i*BUFFER:(i+1)*BUFFER]
            print(f"SENDING CHUNK: {chunk}")
            conn.send(self.str_encode(chunk))
            print("CHUNK SENT ^^^^^^")
            
            ## test delay
            time.sleep(0.01)
        
        
        ## calling receive msg
        recv_msg = self.recieve_msg(self.server)
        return recv_msg
    
    
    def recieve_msg(self, conn):
        complete_msg = ""
        ## clients need to have a shared known header beforehand. Default is 10
        HEADER_BYTES = 10
        BUFFER = 1024
        header_value = 0
        header_contents = ""
        
        msg_bytes_recieved_so_far = 0
        
        print(f"WAITING ON HEADER TO BE SENT:")
        header_msg_length = conn.recv(HEADER_BYTES).decode() #int(bytes_decode(msg)
        print("HEADER:" + header_msg_length)
        
        ## getting the amount of chunks/iterations eneded at 1024 bytes a message
        chunks = math.ceil(int(header_msg_length)/BUFFER)
        #print(chunks)
        
        #print(bytes_decode(msg))
        
        complete_msg = "" #bytes_decode(msg)[10:]
        
        #while True:
        for i in range(0, chunks):
            print(f"RECEVING CHUNK:")
            msg = conn.recv(BUFFER)  # << adjustble, how many bytes you want to get per iteration
            
            ## getting the amount of bytes sent so far
            msg_bytes_recieved_so_far = msg_bytes_recieved_so_far + len(self.bytes_decode(msg))

            complete_msg += self.bytes_decode(msg)
            
            print(self.bytes_decode(msg))
            
            print(f"""DEBUG:
                Full Message Length (based on header value) {header_msg_length}
                Header size: {HEADER_BYTES}

                Size of message recieved so far: {msg_bytes_recieved_so_far}  
                
                Chunks: {chunks}          
                
                """)
            
            ## if complete_msg is the same length as what the headers says, consider it complete. 
            if len(complete_msg) == header_msg_length:
                print("MSG TRANSFER COMPLETE")
        
        print("VALUE OF MSG: \n" + complete_msg)
        return complete_msg
        
        
        ##==========================================================================================


    ##== QOL
        """     
        =======================================
        decode & encode funcitons:
        
        A set of universal functions for encoding and decoding text. handy for error handling & unique character sets,
        however that is not implemented yet.
        
        Input: The input to be decoded/encoded
        
        Output/Return: Returns a string or bytes, depending on the respective function
        
        """
    def bytes_decode(self, input) -> str:
        decoded_result = input.decode()
        return decoded_result

    ## str -> bytes
    def str_encode(self, input) -> bytes:
        encoded_result = input.encode()
        return encoded_result
    