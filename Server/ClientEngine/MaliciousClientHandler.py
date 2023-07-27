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

except Exception as e:
    print(f"[ServerMaliciousClientHandler.py] Import Error: {e}")
    exit()

class ServerMaliciousClientHandler:
    """
    This is the class that handles all the malicious clients, a new instance is spawned for 
    each client that checks in.
    """
    def __init__(self, clientsocket, clientid):
        self.clientsocket = clientsocket
        self.ip = clientsocket.getpeername()[0]
        self.port = clientsocket.getpeername()[1]
        self.id = clientid
        self.fullname = "client_" + self.ip.replace(".","_") + f"_{self.id}"

    def handle_client(self, response_from_client):
        print(f"MaliciousClientHandler(handle_client) DEBUG: Message From {self.id} is: {len(response_from_client)} bytes")
        print(f"Client {self.id} will now wait...")

        ## need to determine what comes here. The way the server is set up, every new message comes through there, is filtered, then is passed here (or wherever it shoudl go).
        ## That may skew the queue plan. 

        ##Final steps would be to send msg back to client





    
