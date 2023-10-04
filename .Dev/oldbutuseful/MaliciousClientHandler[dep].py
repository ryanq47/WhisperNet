################
## Malicious Client Handler
################ 
"""
    
    Desc: This class doesn't do much actively, and only gets called on when its created, and when a message needs to be sent to a client via the send_msg. 
    Basically, it's a glorified object for each client that holds the connection info, the connection, and can send/receieve messages with that client.
    It's a work in progress. 
    
    Additionally, and this is newer, it updates JSON keys for the malicious client, with info on said malicious client for GUI stuff (i.e. client viewer)
"""
## TEMP
sleep_string = '''{"general": {"action": "sleep", "client_id": "", "client_type": "", "password": ""}, "conn": {"client_ip": "", "client_port": ""}, "msg": {"msg_to": "", "msg_content": "", "msg_command": "sleep", "msg_value": "", "msg_length": "", "msg_hash": ""}, "stats": {"latest_checkin": "", "device_hostname": "", "device_username": ""}, "security": {"client_hash": "", "server_hash": ""}}'''

try:
    import inspect
    import math
    import logging
    import traceback
    import json
    import time
    from datetime import datetime, timezone

    from Utils.UtilsHandler import str_encode, bytes_decode

    import Comms.CommsHandler
    import Utils.QueueHandler
    import Utils.UtilsHandler
    import DataEngine.JsonHandler
    import DataEngine.DBHandler
    import DataEngine.EvasionHandler

    from pprint import pprint

except Exception as e:
    print(f"[ServerMaliciousClientHandler.py] Import Error: {e}")
    exit()

function_debug_symbol = "[^]"

class ServerMaliciousClientHandler:
    """
    This is the class that handles all the malicious clients, a new instance is spawned for 
    each client that checks in.

    sys_path: The system path as referenced FROM the server.py folder. (ex: 'C:\Logec\Server\' is the path.)
    """
    ## Technically gets called in prior thread. Can get funky with DB
    def __init__(self, sys_path=None, evasion_profile_path = None):
        logging.debug(f"{function_debug_symbol} {inspect.stack()[0][3]}")
        #logging.debug("[MaliciousClientHandler.__init__()] This is a new class object.")
        self.clientsocket   = None
        self.ip             = None
        self.port           = None
        self.id             = None
        self.fullname       = None
        self.command_queue  = None  #Utils.QueueHandler.QueueHandler()
        self.sys_path       = sys_path
        self.evasion_profile_path = evasion_profile_path
        #print(f"MCLIENT {self.sys_path} + {self.evasion_profile_path}")


        ## temp queue add ons
       # self.command_queue.enqueue("Test")
        #self.command_queue.enqueue("123")
        #self.command_queue.enqueue("help")

    def handle_client(self, raw_response_from_client, clientsocket, clientid):
        logging.debug(f"{function_debug_symbol} {inspect.stack()[0][3]}")

        """This method gets called to handle the client as it connects. It uses the existing class variables, and the new ones passed to it 
        to do various operations with the client

        Args:
            dict_response_from_client (DICT): the JSON response sent to the server, from the client. Needs to be passed in as a DICT
            raw_response_from_client (JSON): the JSON response sent to the server, from the client. Needs to be passed in as the raw JSON string

            clientsocket (SOCKET): the socket that the client/server is currently communicating on
            clientid (str): the client's id
        """
        try:
            ## self.command_queue has to be down to be apart of this thread, and as such, interact with the DB.
            self.command_queue  = DataEngine.DBHandler.SQLDBHandler(db_name="DevDB.db")
            self.clientsocket   = clientsocket
            self.ip             = clientsocket.getpeername()[0]
            self.port           = clientsocket.getpeername()[1]
            self.id             = clientid
            self.fullname       = "client_" + self.ip.replace(".","_") + f"_{self.id}"

            ## Some setup... ## lots of moving peieces here, a try/except would probably be a good idea

            ## == SQL table stuff == ##
            ## create client table if not exist...
            self.command_queue.create_client_table(client_name=self.fullname)
            ## create queue track table if not exist...
            self.command_queue.create_client_queuetrack_table()
            ## create a row for the client in teh queue track table
            self.command_queue.create_client_queuetrack_row(client_name=self.fullname)

            ## Turn raw string into Dict object
            dict_response_from_client = DataEngine.JsonHandler.json_ops.from_json(raw_response_from_client)

            ## parse json results. Add to "results queue"?
            logging.debug("[MaliciousClientHandler.handle_client(): {} ] msg.msg_value: {}".format(self.id, dict_response_from_client["msg"]["msg_value"]))
            
            ## DEBUG - temprarily here to create fake jobs
            self.command_queue.enqueue_client_row(client_name=self.fullname)


            ## write to DB response
            self.command_queue.add_response_from_client(response = raw_response_from_client, client_name=self.fullname)

            ## Debug queue statement, delete when ready
            #logging.debug(f"[MaliciousClientHandler.handle_client(): {self.id} ] Command Queue: {self.command_queue.queue}")

            ## == Evasion Profile Setup == ##
            self.evasion_profile = DataEngine.EvasionHandler.EvasionProfile(sys_path = self.sys_path, evasionprofile_file_path = self.evasion_profile_path)


            ##Final steps would be to send msg back to client
        except Exception as ge:
            logging.debug(f"[MaliciouClientHandler (handle_client)] General error: {ge}")

        finally:
            self.send_command()

    def send_command(self):
        logging.debug(f"{function_debug_symbol} {inspect.stack()[0][3]}")

        """Sends a message on to the client. Uses the next item up in the queue. If no item is int he queue (or it errors out) The client is send a sleep command

            Only triggered when a client sends a message first. 

        """
        # get latest item in queue
        #command = self.command_queue.dequeue()

        '''
        Explanation here:
            the command in queue comes in as a JSON string. I was mistakelny passing said string to teh msg_command, thinking it was just the command to run
            That led to a weird delimited string that was fucked up. It now gets converted to a dict (see below) then the correct dict item ["msg"]["msg_command"] is passed
        '''

        json_string_command    = self.command_queue.dequeue_next_cmd(client_name=self.fullname)

        ## janky python stuff here. If the json is legit, it returns the dict (which is true). If not, it returns False, and will failover to the sleep command
        #command         = DataEngine.JsonHandler.json_ops.from_json(json_string_command)

        if json_string_command:
            ## run by evasionhandler.mystify()
            try:
                mystified_command = self.evasion_profile.mystify(json_string=json_string_command)

            except Exception as e:
                mystified_command = sleep_string
                print(f"[ADD LATER] Errro with obsfuctaiong json command. Sending sleep. {e}")
            
            ## send to client
            Comms.CommsHandler.send_msg(msg=mystified_command, conn=self.clientsocket)

        
        else:
            logging.debug(f"[MaliciousClientHandler.handle_client(): {self.id} ] Queue empty. Sending sleep")
            ## Creating the sleep json command, instead of using the input from the DB
            msg_to_send = DataEngine.JsonHandler.json_ops.to_json(msg_command="sleep", timestamp=Utils.UtilsHandler.timestamp())
            mystified_command = self.evasion_profile.mystify(json_string=json_string_command)
            Comms.CommsHandler.send_msg(msg=msg_to_send, conn=self.clientsocket)

            ## send a sleep object
        


'''
steps


Dequeue command (json string)

passes to mall_prof()
    - Modifies json string as neccesary
        - unpacks & adds values, etc
        - Repacks once done
    - returns json string.

modified json string is written to DB (modified_command).
    - The modified_command feild is just a record of what is being sent, it does not actually have any data pulled from it

Modified json is sent to client. 






'''    
