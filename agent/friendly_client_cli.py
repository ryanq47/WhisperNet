import socket
import os

global_debug = True


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
            print("Connected!")
            self.server_interact()
        else:
            print("Auth failed.")
            self.connect_to_server()


    def server_interact(self):
        if os.name == "nt":
            os.system("cls")

        else:
            os.system("clear")

        ## This will be returned to the client later
        print(" ===== Logec C2 Manual Shell +++++\n\n")
        
        print("\n\n========Current Clients========")
        #self.server_request("clients")
        '''for var_name in globals():
            if var_name.startswith("client_"):
                print(var_name)'''
        print("FAKECLIENTS")
        
        
        print("===============================")
        print("!! Clients populate on heartbeat, be patient\n\n")
        
        ## dict 
        client_name = input("Enter a client name to interact, 'help', or 'refresh': ")

        # get the corresponding instance from the clients dictionary and call its method
        
        ## Part of this needs to stay here, the other part needs to go back to the server
        '''
        if client_name in self.clients:
            client_instance = self.clients[client_name]
            
            while True:
                user_input_for_client = input(f"Client (jobs for options): [{self.ip_address}]: ")

                if user_input_for_client == "home":
                    self.server_interact()

                else:
                    client_instance.interact(user_input_for_client)'''
        
        if client_name.lower() == "refresh":
            '''if os.name == "nt":
                os.system("cls")

            else:
                os.system("clear")'''

            self.server_interact()

        elif client_name.lower() == "stats":
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

            print(stats_list)
            input("Type home for home: ")
            self.server_interact()


        elif client_name.lower() == "clients":
            self.server_request("clients")

        elif client_name.lower() == "help":
            print(
            "Home: \n" \
            "refresh - refreshes the current connected clients \n" \
            "stats - ' [BETA] Prints all clients stats'\n" \
            )
            ## change these to enter
            input("Type Home for Home: ")
            self.server_interact()

        else:
            print(f"{client_name} not found.")
            os.system("clear")
            self.server_interact()

    ## THe main interface for gettin data from the server
    def server_request(self, request):
        formatted_request = f"!_usercommand_!\\|/{self.username}//|\\\\{request}"
        print(f"DEBUG: Formatted Request: {formatted_request}")

        if request == "clients":
            self.server.send(self.str_encode(formatted_request))

            ## return this eventually to the function that called it to print
            print("waiting on response...")
            print(self.str_decode(self.server.recv(1024)))
    
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