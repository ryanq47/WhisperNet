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
    def __init__(self, request_from_client:str = None, client_socket = None):
        '''
        self.request_from_client = JSON string from client
        self.client_socket       =  The socket that is currently in communication with the client

        self.dict_request_from_client = The dictionary version of the request_from_client
        '''
        self.request_from_client = request_from_client
        self.client_socket = client_socket

        self.dict_request_from_client = None


    def handle_client(self):
        logging.debug(f"{function_debug_symbol} {inspect.stack()[0][3]}")

        print(len(self.request_from_client))
        
        ## Temp response to client - delete once the decisions work, etc
        #cookie_json = DataEngine.JsonHandler.json_ops.to_json_for_client(msg_value="Authentication Successful")
        #Comms.CommsHandler.send_msg(conn = self.client_socket, msg = cookie_json)

        ## DO THIS PART NEXT
        self.dict_request_from_client = DataEngine.JsonHandler.json_ops.from_json(json_string=self.request_from_client)

        msg_to = self.dict_request_from_client["msg"]["msg_to"]

        print("Handle Client called successfully")

        ## Tree for which to go to:
        
        if msg_to == "server":
            print("msg_to_server")
            self.server_tree()



        ## this will need some work to get the valid agent names in
        elif msg_to == "valid_agent_name":
            print("msg_to_agent")
            self.agent_tree()

        else:
            logging.debug("TEMP - Invalid message from client")
            response_json = DataEngine.JsonHandler.json_ops.to_json_for_client(msg_value="Invalid msg_to parameter.")
            Comms.CommsHandler.send_msg(conn = self.client_socket, msg = response_json)
    

    def server_tree(self):




        '''
        May be able to do all the actions here in a similar format to how plugins work. Map the function needed, and that function does the stuff, and returns the request

        Would make dev really really fast
        
        '''

        ## placeholder ifelse b4 plugins

        msg_command = self.dict_request_from_client["msg"]["msg_command"]

        if msg_command == "test":
            response_json = DataEngine.JsonHandler.json_ops.to_json_for_client(msg_value="Server Hears you loud N Clear! Lets fuck some stuff up")
            Comms.CommsHandler.send_msg(conn = self.client_socket, msg = response_json)
        
        else:
            response_json = DataEngine.JsonHandler.json_ops.to_json_for_client(msg_value="server_tree - bad command")
            Comms.CommsHandler.send_msg(conn = self.client_socket, msg = response_json)


    def agent_tree(self):
        response_json = DataEngine.JsonHandler.json_ops.to_json_for_client(msg_value="agent_tree")
        Comms.CommsHandler.send_msg(conn = self.client_socket, msg = response_json)

'''
To implement:

    MSG parser (json)

    Queue function for agent commands ( may be able to reuse what is already there )
        - Use the 'msg_to' feild for that

    Decision tree?



    Other functinos...
        
'''