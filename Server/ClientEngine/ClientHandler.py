################
## Friendly client
################ 

try:            

    import DataEngine.DBHandler
    import DataEngine.JsonHandler
    import SecurityEngine.AuthenticationHandler
    import Comms.CommsHandler
    import Utils.UtilsHandler

    import ClientEngine.ClientPlugins._Native.Default
    import ClientEngine.ClientPlugins._Native.Stats

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
        Utils.UtilsHandler.interaction_logger(json_string = self.request_from_client)

        msg_to = self.dict_request_from_client["msg"]["msg_to"]
        print("Handle Client called successfully")

        ## Placeholder
        valid_agent_names = ["agent_1", "agent_2"]

        ## Tree for which to go to:
        
        if msg_to == "server":
            print("msg_to_server")
            self.server_tree()

        ## this will need some work to get the valid agent names in. Might be best to put in the singleton
        elif msg_to in valid_agent_names:
        #elif msg_to == "valid_agent_name":
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


        Some notes,

        - Solidify logging correctly
        - Try/Except.
        - Review & refactor, This is a rough draft for the code
        - Document
        Everything here works as intended at the moment, which is good.
        
        '''
        logging.debug(f"{function_debug_symbol} {inspect.stack()[0][3]}")

        try:
            dispatch = {
                ## Default commands...
                #"test": Actions._display_help,
                "server help": ClientEngine.ClientPlugins._Native.Default.Actions._return_help,
                #"exit": Logic.DecisionTree.SystemDefaultActions._set_dir_home_shell,
                #"clear": Logic.DecisionTree.SystemDefaultActions._display_clear,
                "server stats": ClientEngine.ClientPlugins._Native.Stats.Actions._return_stats

                ## add yours here... no (), as we are just passing the object, not running it 
                #"mycommand":Actions._test_action

            }
            msg_command = self.dict_request_from_client["msg"]["msg_command"]


            action = dispatch.get(msg_command)

            if action:
                result = action()["output_from_action"]

                response_json = DataEngine.JsonHandler.json_ops.to_json_for_client(msg_value=result)
                Comms.CommsHandler.send_msg(conn = self.client_socket, msg = response_json)

            else:
                response_json = DataEngine.JsonHandler.json_ops.to_json_for_client(msg_value="server_tree - bad command")
                Comms.CommsHandler.send_msg(conn = self.client_socket, msg = response_json)

        except Exception as e:
            logging.warning(e)
            response_json = DataEngine.JsonHandler.json_ops.to_json_for_client(msg_value="Error. See server logs")
            Comms.CommsHandler.send_msg(conn = self.client_socket, msg = response_json)       



    def agent_tree(self):
        '''
        The decision tree for all agent related items.


        Takes the request from the client, parses it. 
        Then, it Enqueues the command to the respective client. 

        Dev...
            From here, this can go 2 ways:
            1) Wait on new value in response table from client, and send that back. (good for low sleep times)
            2) aknowledge a successful command has been queued, and send taht back. (good for long sleep times.)
        '''
        logging.debug(f"{function_debug_symbol} {inspect.stack()[0][3]}")

        #response_json = DataEngine.JsonHandler.json_ops.to_json_for_client(msg_value="agent_tree has been reached!")
        #Comms.CommsHandler.send_msg(conn = self.client_socket, msg = response_json)

        try:
            ## Right now, super simple. Just queue the command for the client.
            ## Later, will need to figure out how to view things from the client.

            msg_command = self.dict_request_from_client

            ## Get command from json
            agent_id        = msg_command["msg"]["msg_to"]
            agent_command   = msg_command["msg"]["msg_command"] # Should be json.

            #print(f"Debug agent_id: {agent_id}")
            #print(f"Debug agent_id: {agent_command}")
            #logging.debug("Contents of ")

            ## Add to DB queue
            #plugin.enque(agent=agent_id, command=agent_command)
            command_db = DataEngine.DBHandler.SQLDBHandler(db_name="DevDB.db")
            command_db.enqueue_client_row(
                client_name = agent_id,
                msg         = agent_command
            )
            response_json = DataEngine.JsonHandler.json_ops.to_json_for_client(msg_value="Command Queued successfully")
            Comms.CommsHandler.send_msg(conn = self.client_socket, msg = response_json)
        
        except Exception as e:
            logging.warning(f"{function_debug_symbol} {inspect.stack()[0][3]} Failure to queue command: {e}")
            response_json = DataEngine.JsonHandler.json_ops.to_json_for_client(msg_value="failure to queue command")
            Comms.CommsHandler.send_msg(conn = self.client_socket, msg = response_json)
'''
To implement:

    MSG parser (json)

    Queue function for agent commands ( may be able to reuse what is already there )
        - Use the 'msg_to' feild for that

    Decision tree?



    Other functinos...
        
'''

'''
OI read me

Todo:
    Database with stats/general use. Seperate from the command DB.
        Handler/plugin for that DB.

    More commands in the tree. 


    once that is all implemented,
    focus on the agent tree, with control of agents, etc


'''