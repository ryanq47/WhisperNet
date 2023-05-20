import socket
import os
from typing import Tuple
import logging
from PySide6.QtCore import Signal, QObject
import math
import time
import sys
import json

sys_path = os.path.dirname(os.path.abspath(sys.argv[0]))

logging.basicConfig(level=logging.DEBUG)
logging.basicConfig(filename='logs/friendly_client.log', filemode='a', format='%(name)s - %(levelname)s - %(message)s', force=True)

class FClient(QObject):
    shell_output = Signal(str)
    authenticated = Signal(bool)
    json_data = Signal(str)

    def __init__(self, parent=None, log_level="debug", print_logs_to_console=True):
        super().__init__(parent)
        self.encoding = 'utf-8'
        self.buffer = 1024
        self.authenticated = False
        self.shellbanner = "NotConnected"
        self.current_client_list = []
        ## log level, defaults to debug if not supplied
        self.log_level = log_level
        self.print_logs_to_console = print_logs_to_console

        # calling the log level handler


    ## Connection to server
    def connect_to_server(self, connlist) -> None:
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
        #old
        #self.server.send(self.str_encode(f"!_userlogin_!\\|/{self.username}\\|/{password}"))

        #new
        ## In english, formats & returns JSON, and sends it to server (self.send_msg handles conversion to bytes)
        ## Also, the send & recv are tied togehter in this instance, hence why the recv is commented out
        auth_attempt_response = self.send_msg(msg = self.json_format(action="!_userlogin_!"), conn= self.server)

        #auth_attempt_response = int(self.recieve_msg(conn=self.server))

        logging.debug(f"Server Authentication Respones: {auth_attempt_response}]")

        if auth_attempt_response == "0":
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
        self.shellbanner = f"{self.ip}:{self.port}"
        
        #formatted_request = f"!_servercommand_!\\|/{self.username}\\|/{command}"
        formatted_request = self.json_format(action="!_servercommand_!",
                                             msg_content=command)

        if command.lower() == "clients":
            self.send_msg(msg=formatted_request, conn=self.server)
            self.shellformat(self.recieve_msg(self.server))

        #self.recieve_msg(self.server)
            
        elif command.lower() == "sanity-check":
            self.send_msg(msg=formatted_request, conn=self.server)
            self.shellformat(self.recieve_msg(self.server))

        elif command.lower() == "clear":
            self.shellformat()

        ## this just listens forever causeeeee i set it up that way. fuuuuuck need to change a few things
        elif command.lower() == "disconnect":
            self.send_msg(msg=formatted_request, conn=self.server)
            self.shellformat(self.recieve_msg(self.server), is_json=True)
            exit()
            
        elif command.lower() == "export-clients":
            pass
            logging.debug("[Friendly Client (gui_to_server)] requesting client JSON data from server")
            #self.shellformat(self.send_msg(msg="export-clients", conn=self.server))
            json_data_from_server = self.send_msg(msg=f"!_servercommand_!\\|/{self.username}\\|/export-clients", conn=self.server)
            self.json_data.emit(json_data_from_server)

            ## upload/download from the server
        elif command.lower() == "server-upload-file":
            pass
            try:
                filepath = command.split()[1]
            except Exception as e:
                logging.debug(f"[Friendly Client (gui_to_server)] Please enter a filepath: {e}")
                
            filedata = self.fileread(filepath)

            ## Need to tell server that data is inbound
            self.send_msg(f"!_servercommand_!\\|/{self.username}\\|/server-upload-file {filepath}")
                
            self.send_msg(filedata)
            
            ## file handler, returns file data
                
            #self.send_msg("filedata")
                
            self.shellformat("uploaded {name} to server")
            
            
        elif "server-download-file" in command.lower():
            pass
            try:
                filepath = command.split()[1]
            
            except Exception as e:
                self.shellformat(f"[Friendlyclient (server-download-file)] Error: {e}")
            
            self.send_msg(f"!_servercommand_!\\|/{self.username}\\|/server-download-file {filepath}")
            data_to_write = self.recieve_msg(self.server)
                
            self.filewrite(filepath = f"{sys_path}/Content/DataExfil/FromServer/TEMPNAME", data=data_to_write)
                
        else:
            ## filter down to gui_to_client if not a server command
            self.gui_to_client(command)

    ##== GUI to client 
        """     
        =======================================
        gui_to_client:
        
        If A command is not meant for the server, it comes here. See the diagram
        
                                 !!>>   If valid client name-> gui_to_client -> server <<!!
        Flow: GUI -> gui_to_server ^-> send function -> Server
        
        TLDR: Sends command to server that are meant for clients. In its own method
        just incase I need to hardcode any special commands in
                
        """
        
    def gui_to_client(self, raw_command):
        logging.debug(f"[FriendlyClient (gui-to-client)] command: {raw_command} ")

        '''
        # Client name is always last for these commands, hence we take the last value from the list, and
        # toss it as the client. Compatability issues may arise with spaces in names (which shouldn't happen anyways)
        # or multi word commands, which also shoudln't happen
        
        msg_to is needed for the server to use the ID as the global object name for the right client. The client
        name technically is the "value" key when run through the json parser, but it's easier/cleaner to do this hack
        on this side and keep the server as clean as possible
        '''
        try:
            client = (raw_command.split())[-1]
            #print(f"RAW COMMAND: {client}")
        except IndexError as e:
            logging.warning(f"[FriendlyClient (gui_to_client] A client name is required to run any commands meant for"
                            "the client. Error msg: {e}")
        except Exception as e:
            logging.warning(f"[FriendlyClient (gui_to_client] Unknown error occured: {e}")

        #formatted_request = f"!_clientcommand_!\\|/{self.username}\\|/{raw_command}"
        formatted_request = self.json_format(action="!_clientcommand_!", msg_content=raw_command, msg_to=client)

        print(formatted_request)

        #yes I know this is blindly sending commands to the server, but it makes it easier to manage all 3 puzzle pieces
        try:
            self.send_msg(msg=formatted_request, conn=self.server)
            self.shellformat(results=self.recieve_msg(self.server), is_json=True)
        except Exception as e:
            logging.debug(f"[Friendly Client (gui_to_client)] {e}")

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
    def shellformat(self, results="Empty Result Set", is_json=False) -> None:
        """

        results: The results of a command being run, to be displayed on the gui
        is_json: Determening if the data is in json, and only showing the value of that key

        Note, eventually I need to figure out how to allow custom keys as an argument, but I haven't done that yet

        """

        if is_json:
            try:
                json_msg_results = json.loads(results)

                formatted_results = (
                    f'{self.shellbanner}>\n{json_msg_results["Main"]["msg"]["msg_content"]["value"]}'
                )
            except KeyError as ke:
                logging.warning(f"[Friendly Client (shellformat)] Error with JSON key to display: {ke}")
            except Exception as e:
                logging.warning(f"[Friendly Client (shellformat)] Unknown Error: {e}")

        else:
            formatted_results = (
                f"{self.shellbanner}>\n{results}"
            )

        self.shell_output.emit(formatted_results)

    ## == JSON formatter n stuff

    def json_format(self, action="", msg_content="", msg_to=""):

        '''
        JSON formatter for sending messages to the server

        Returns a json object

        '''

        ## Quick parse on the command - grabs the command via strip, then replaces it with "" for the value
        ## bandaid solution, but it works for now
        try:
            cmd = msg_content.split()[0]
            cmd_value = msg_content.replace(cmd, "")
        except Exception as e:
            logging.debug(f"[Server (JSON format)] error with parsing command {msg_content}: {e}")
            cmd = msg_content
            cmd_value = "empty"

        ## Expanded our here for readability
        user_msg_to_be_sent = {
            "Main": {
                "general": {
                    "action": action,
                    "client_id": str(self.username),
                    "client_type": "friendly",
                    "password": "1234"
                },
                "conn": {
                    "client_ip": "127.0.0.1",
                    "client_port": 6969
                },
                "msg": {
                    "msg_to": msg_to,
                    "msg_content": {
                        "command": cmd,
                        "value": cmd_value
                    },
                    "msg_length": 1234,
                    "msg_hash": "hash of message (later)"
                },
                "stats": {
                    "latest_checkin": "time.now",
                    "device_hostname": "hostname",
                    "device_username": "username"
                },
                "security": {
                    "client_hash": "hash of client (later)",
                    "server_hash": "hash of server (later)"
                }
            }
        }

        return json.dumps(user_msg_to_be_sent)


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
        logging.debug(f"[FriendlyClient (send_msg)] SENDING HEADER: {header}")
        conn.send(header)
        
        ## Visual Stuff
        #visual_bar = "Sending ["
        
        for i in range(0, math.ceil(msg_length/BUFFER)):
            ## gets the right spot in the message in a loop
            chunk = msg[i*BUFFER:(i+1)*BUFFER]
            logging.debug(f"[FriendlyClient (send_msg)] SENDING CHUNK: {chunk}")
            conn.send(self.str_encode(chunk))
            #visual_bar += "="
            #self.shellformat(visual_bar)
            ## test delay
            time.sleep(0.01)
        
        #visual_bar += "] Done!"
        
        
        ## calling receive msg
        #recv_msg = self.recieve_msg(self.server)
        #return recv_msg
    
    
    def recieve_msg(self, conn):
        complete_msg = ""
        ## clients need to have a shared known header beforehand. Default is 10
        HEADER_BYTES = 10
        BUFFER = 1024
        header_value = 0
        header_contents = ""
        
        msg_bytes_recieved_so_far = 0

        logging.debug(f"[FriendlyClient (recieve_msg)] waiting on header...")
        header_msg_length = conn.recv(HEADER_BYTES).decode() #int(bytes_decode(msg)
        #print("HEADER:" + header_msg_length)
        logging.debug(f"[FriendlyClient (recieve_msg)] HEADER: {header_msg_length}")

        ## getting the amount of chunks/iterations eneded at 1024 bytes a message
        chunks = math.ceil(int(header_msg_length)/BUFFER)

        complete_msg = ""
        
        ## Visual Stuff
        #visual_bar = "Receiving ["
        
        #while True:
        for i in range(0, chunks):
            # i + 1 as i starts at 0
            logging.debug(f"[FriendlyClient (recieve_msg)] RECEVING CHUNK {i + 1}/{chunks}")
            msg = conn.recv(BUFFER)  # << adjustble, how many bytes you want to get per iteration
            ## add a = to the bar & update
            #visual_bar += "="
            #self.shellformat(visual_bar)
            
            ## getting the amount of bytes sent so far
            msg_bytes_recieved_so_far = msg_bytes_recieved_so_far + len(self.bytes_decode(msg))

            complete_msg += self.bytes_decode(msg)
            
        #visual_bar += "] Done!"
        logging.debug(f"[FriendlyClient (recieve_msg)] FUll MSG recieved")
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
    
        """
        =======================================
        file read & write
        
        
        A set of file handlers that have some error handling and other make-life-easy features built in. 
        
        """
    
    def fileread(self, filepath=""):        
        if os.path.isfile(filepath):
            with open(filepath, "r") as file_to_read:
                file_data = file_to_read.read()  
                return file_data
        else:
            logging.debug(f"[Friendly Client (fileread)] File does not exist at: {filepath}")
            self.shellformat(f"[Friendly Client (fileread)] File does not exist at: {filepath}")
        
    def filewrite(self, filepath="", data=""):
        if os.path.exists(filepath):
            with open(filepath, "w") as file_to_write:
                file_to_write.write(data)  
            
        else:
            logging.debug(f"[Friendly Client (filewrite)] Directory does not exist at: {filepath}")
            self.shellformat(logging.debug(f"[Friendly Client (filewrite)] Directory does not exist at: {filepath}"))