################
## Friendly client
################ 

try:            

    import DataEngine.DBHandler
    import DataEngine.JsonHandler
    import SecurityEngine.AuthenticationHandler
    import Comms.CommsHandler
    import logging
    import inspect

except Exception as e:
    print(f"[ClientEngine.ClientHandler.py] Import Error: {e}")
    exit()

function_debug_symbol = "[^]"

class ClientHandler:
    def __init__(self,request_from_client = None, client_socket = None):
        self.request_from_client = request_from_client
        self.client_socket = client_socket

    def handle_client(self):
        logging.debug(f"{function_debug_symbol} {inspect.stack()[0][3]}")

        print(len(self.request_from_client))
        
        ## Temp response to client - delete once the decisions work, etc
        cookie_json = DataEngine.JsonHandler.json_ops.to_json_for_client(msg_value="Authentication Successful")
        Comms.CommsHandler.send_msg(conn = self.client_socket, msg = cookie_json)

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

