################
## Friendly client
################ 

try:            

    import DataEngine.DBHandler
    import DataEngine.JsonHandler
    import SecurityEngine.AuthenticationHandler
    import logging
    import inspect

except Exception as e:
    print(f"[ClientEngine.ClientHandler.py] Import Error: {e}")
    exit()

function_debug_symbol = "[^]"

class ClientHandler:
    def __init__(self):
        pass

    def handle_client(self, request_from_client):
        logging.debug(f"{function_debug_symbol} {inspect.stack()[0][3]}")

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
        print("Handle Client called successfully")

