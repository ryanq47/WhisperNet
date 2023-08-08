try:
    import argparse
    import Logic.DecisionTree
    import Utils.AuthenticationHandler
    import Comms.CommsHandler

except Exception as e:
    print(f"[client.py] Import Error: {e}")
    exit()

parser = argparse.ArgumentParser()
parser.add_argument('--ip', help="The IP to connect to", required=True)
parser.add_argument('--port', help="The port to connect to", required=True)

args = parser.parse_args()
ip = args.ip
port = int(args.port)

class Client:
    def __init__(self):
        pass
        self.cookie = None
        ## the server to conenct to
        self.server = None #[str, ip]

    def user_loop(self):
        while True:
            ## this can be argparse as well, maybe move to a util
            if self.server == None: ## conencting to server
                server_conn_tuple = (ip, port) #Utils.AuthenticationHandler.Server.get_server_to_connect_to()
                server_socket = Comms.CommsHandler.connect_to_server(server_conn_tuple)

            if self.cookie == None: ## checking if cookie
                print(f"Enter credentials for {self.server}:")
                Utils.AuthenticationHandler.Credentials.authenticate_to_server(server_socket)

            user_input = (f">{self.server[0]:self.server[1]}> ")     
            print(user_input)       
            ## decision_tree(self.cookie, input)

        '''
        ## not doing a persistent cnonection to server, just one off's
        While True:
            if self.cookie == None:
                ask_for_creds()
                Auth_to_server()

            get_user_input()
            decision_tree(user_input, cookie)

        
        
        '''

try:
    c = Client()
    c.user_loop()
except KeyboardInterrupt:
    print("Exiting...")
except Exception as e:
    print(f"Unkown error: {e}")