################
## Friendly client
################ 

try:            

    import DataEngine.DBHandler
except Exception as e:
    print(f"[ClientEngine.ClientHandler.py] Import Error: {e}")
    exit()

class ClientHandler:
    def __init__(self):
        pass

    def handle_client(self):
        pass
        '''
        Find out if client is using password or cookie
        
        if pass:
            validate_password():
            generate_random_cookie()

        
        '''


