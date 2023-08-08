try:
    import argparse
    import logging

    import Logic.DecisionTree
    import Utils.AuthenticationHandler
    import Comms.CommsHandler

except Exception as e:
    logging.debug(f"[client.py] Import Error: {e}")
    exit()

parser = argparse.ArgumentParser()
parser.add_argument('--ip', help="The IP to connect to", required=True)
parser.add_argument('--port', help="The port to connect to", required=True)
parser.add_argument('--debug','-d', help="The port to connect to", action="store_false")

args = parser.parse_args()
ip = args.ip
port = int(args.port)
debug = args.debug


"""
Here's the global Debug + Logging settings. 
Global Debug logging.debug to screen will be a setting in the future
"""
if not debug:
    print("Debugging enabled")
    global_debug = True
else:
    global_debug = False
    
##Reference: https://realpython.com/python-logging/
logging.basicConfig(level=logging.DEBUG)
## Change the path to the system path + a log folder/file somewhere
logging.basicConfig(filename='client.log', filemode='a', format='%(asctime)s - %(levelname)s - %(message)s', force=True, datefmt='%Y-%m-%d %H:%M:%S')
if global_debug:
    logging.getLogger().addHandler(logging.StreamHandler())

class Client:
    def __init__(self):
        self.cookie = None
        ## the server to conenct to
        self.server = None #[str, ip]

    def user_loop(self):
        while True:
            ## this can be argparse as well, maybe move to a util
            if self.server == None: ## conencting to server
                server_conn_tuple = (ip, port) #Utils.AuthenticationHandler.Server.get_server_to_connect_to()
                ## not the best way to show what server we're connected to, but it works
                self.server = server_conn_tuple
                server_socket = Comms.CommsHandler.connect_to_server(server_conn_tuple)

            ## !! Issue exist above. Client SHUOLD disconnect each command from server, like an API. one request = one answer.
            ## howver it's not cuase self.server != None


            if self.cookie == None: ## checking if cookie
                print(f"Enter credentials for {self.server}:")
                self.cookie = Utils.AuthenticationHandler.Credentials.authenticate_to_server(server_socket)

            user_input = input(f"{self.server[0]}:{self.server[1]}>> ")    
            logging.debug(user_input)       
            Logic.DecisionTree.Trees.user_input_tree(user_input = user_input, cookie = self.cookie, conn = server_socket)

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
    logging.debug("\nExiting...")
except Exception as e:
    logging.debug(f"Unkown error: {e}")