################
## Friendly client
################ 

try:            

    import DataEngine.DBHandler
    import DataEngine.JsonHandler
    import SecurityEngine.AuthenticationHandler

except Exception as e:
    print(f"[ClientEngine.ClientHandler.py] Import Error: {e}")
    exit()

class ClientHandler:
    def __init__(self):
        pass

    def handle_client(self, request_from_client):
        pass
        '''
        client_json_dict = JsonHandler.from_json(json_data)
        

        Find out if client is using password or cookie (json key)

        
        if client_json_dict["general"]["auth_type"] == "password":
            validate_password():
            generate_random_cookie()
        
        elif client_json_dict["general"]["auth_type"] == "cookie":
            validate_cookie()

        else:
            logging.warning("[ERROR STUFF HERE ] Bad Auth Method attemtped")
        

        
        '''
        client_json_dict = DataEngine.JsonHandler.json_ops.from_json(request_from_client)

        auth_type   = client_json_dict["general"]["auth_type"]
        password    = client_json_dict["general"]["auth_value"]

        
        if auth_type == "password":
            ClientEngine.AuthenticationHandler.validate_password(password)
            ClientEngine.AuthenticationHandler.generate_random_cookie()
            #send cookie back
        
        elif auth_type == "cookie":
            if ClientEngine.AuthenticationHandler.validate_cookie(): ## maybe use DB to store cookies?
                decision_tree()

        else:
            print(f"[ERROR STUFF HERE ] Bad Auth Method attemtped {auth_type}")
            #logging.warning("[ERROR STUFF HERE ] Bad Auth Method attemtped")


