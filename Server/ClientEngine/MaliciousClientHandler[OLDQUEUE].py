################
## Malicious Client Handler
################ 
"""
    
    Desc: This class doesn't do much actively, and only gets called on when its created, and when a message needs to be sent to a client via the send_msg. 
    Basically, it's a glorified object for each client that holds the connection info, the connection, and can send/receieve messages with that client.
    It's a work in progress. 
    
    Additionally, and this is newer, it updates JSON keys for the malicious client, with info on said malicious client for GUI stuff (i.e. client viewer)
"""
try:
    import math
    import logging
    import traceback
    import json
    import time
    from datetime import datetime, timezone

    from Utils.UtilsHandler import str_encode, bytes_decode

    import Comms.CommsHandler
    import Utils.QueueHandler
    import DataEngine.JsonHandler

except Exception as e:
    print(f"[ServerMaliciousClientHandler.py] Import Error: {e}")
    exit()

class ServerMaliciousClientHandler:
    """
    This is the class that handles all the malicious clients, a new instance is spawned for 
    each client that checks in.
    """
    def __init__(self):
        logging.debug("[MaliciousClientHandler.__init__()] This is a new class object.")
        self.clientsocket   = None
        self.ip             = None
        self.port           = None
        self.id             = None
        self.fullname       = None
        self.command_queue  = Utils.QueueHandler.QueueHandler()

        ## temp queue add ons
       # self.command_queue.enqueue("Test")
        #self.command_queue.enqueue("123")
        self.command_queue.enqueue("help")

    def handle_client(self, response_from_client, clientsocket, clientid):
        """This method gets called to handle the client as it connects. It uses the existing class variables, and the new ones passed to it 
        to do various operations with the client

        Args:
            response_from_client (_type_): the JSON response sent to the server, from the client
            clientsocket (_type_): the socket that the client/server is currently communicating on
            clientid (_type_): the client's id
        """
        self.clientsocket   = clientsocket
        self.ip             = clientsocket.getpeername()[0]
        self.port           = clientsocket.getpeername()[1]
        self.id             = clientid
        self.fullname       = "client_" + self.ip.replace(".","_") + f"_{self.id}"

        #print(f"MaliciousClientHandler(handle_client) DEBUG: Message From {self.id} is: {len(response_from_client)} bytes")
        #print(f"Client {self.id} will now wait...")


        ## need to determine what comes here. The way the server is set up, every new message comes through there, is filtered, then is passed here (or wherever it shoudl go).
        ## That may skew the queue plan. 

        ## parse json results. Add to "results queue"?
        logging.debug("[MaliciousClientHandler.handle_client(): {} ] msg.msg_value: {}".format(self.id, response_from_client["msg"]["msg_value"]))
        
        ## Debug queue statement, delete when ready
        logging.debug(f"[MaliciousClientHandler.handle_client(): {self.id} ] Command Queue: {self.command_queue.queue}")

        ##Final steps would be to send msg back to client
        self.send_command()

    def send_command(self):
        """Sends a message on to the client. Uses the next item up in the queue. If no item is int he queue (or it errors out) The client is send a sleep command

            Only triggered when a client sends a message first. 

        """
        # get latest item in queue
        command = self.command_queue.dequeue()

        if command:
            logging.debug(f"[MaliciousClientHandler.handle_client(): {self.id} ] Sending: {command}")
            msg_to_send = DataEngine.JsonHandler.json_ops.to_json(msg_command=command)
            Comms.CommsHandler.send_msg(msg=msg_to_send, conn=self.clientsocket)
        
        else:
            logging.debug(f"[MaliciousClientHandler.handle_client(): {self.id} ] Queue empty. Sending sleep")
            msg_to_send = DataEngine.JsonHandler.json_ops.to_json(msg_command="sleep")
            Comms.CommsHandler.send_msg(msg=msg_to_send, conn=self.clientsocket)

            ## send a sleep object
        


    
