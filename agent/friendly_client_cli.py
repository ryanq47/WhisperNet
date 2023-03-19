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
        self.client_info_fetch()
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
            self.client_info_fetch()
            
            self.shellformat("")
            
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

        elif client_name in self.clients:
            print("Valid Client. Control not implemented")
            print("DEBUG: client is in the client list!") if global_debug else None
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
        
        print("\n\n========Current Clients========")
        #self.server_request("clients")
        print(self.clients)
        
        print("===============================")
        print("!! Clients populate on heartbeat, be patient\n\n")   
        
        print(results)
        

################
## Client Interact
################  

    ## Interacting with clients via the server as a middle man
    ## Meant to be called per message
    def client_interact_through_server(self, client_command):
        if client_command == "stats":
            stats_list = []

            for client_name, client_instance in self.clients.items():
                ## Maybe turn into JSON for transport back to safe client
                stats_string = (
                    f"Client: {client_name}",
                    f"Heartbeats: {client_instance.stats_heartbeats}",
                    f"Heartbeat Interval: {client_instance.stats_heartbeats}",
                    f"Non wait Jobs run: {client_instance.stats_jobsrun}",
                    f"Last Checkin: {client_instance.stats_latestcheckin}"
                )

                #print(stats_string)
                stats_list.append(f"{stats_string}\n")
                # access the variable from the client instance
                variable_value = client_instance.stats_heartbeats
                
                # do something with the variable value, e.g. print it
                #print(f"{client_name}: {variable_value}")

            return stats_list
            #print(stats_list)
            #input("Type home for home: ")



        else:
            print("command not found")
            #print(f"{client_name} not found.")
            #os.system("clear")
            #self.client_interact_through_server()

            
################
## Server Functions
################  
    ## grabs info and foramts it
    def client_info_fetch(self):
        print("Requesting self.clients...")
        self.clients = list(self.server_request("clients").split())
        #self.client_stats = self.server_request("stats")

    ## THe main interface for gettin data from the server
    ## will handle all encoding & bs, just pass it the string
    def server_request(self, request):
        formatted_request = f"!_usercommand_!\\|/{self.username}//|\\\\{request}"

        if request == "clients":
            print(f"DEBUG: Sending {formatted_request}") if global_debug else None
            self.server.send(self.str_encode(formatted_request))

            ## return this eventually to the function that called it to print
            print("DEBUG: waiting on response...") if global_debug else None
            
            serv_response = self.str_decode(self.server.recv(1024))
            print(f"DEBUG: Serv Response: {serv_response}") if global_debug else None
            return serv_response


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