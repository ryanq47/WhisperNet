try:
    import Logic.DecisionTree
    import Utils.AuthenticationHandler

except Exception as e:
    print(f"[client.py] Import Error: {e}")
    exit()

class Client:
    def __init__(self):
        pass
        self.cookie = None
        ## the server to conenct to
        self.server = None #[str, ip]

    def user_loop(self):
        while True:
            ## this can be argparse as well, maybe move to a util
            if self.server == None:
                Utils.AuthenticationHandler.Server.get_server_to_connect_to()


            if self.cookie == None:
                print(f"Enter credentials for {self.server}:")
                Utils.AuthenticationHandler.Credentials.authenticate_to_server()

            user_input = (f">{self.server[0]:self.server[1]}> ")     
            print(user_input)       

        '''
        ## not doing a persistent cnonection to server, just one off's
        While True:
            if self.cookie == None:
                ask_for_creds()
                Auth_to_server()

            get_user_input()
            decision_tree(user_input, cookie)

        
        
        '''


c = Client()
c.user_loop()