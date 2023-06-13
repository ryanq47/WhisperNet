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
    from Modules.ServerUtils import str_encode, bytes_decode

except Exception as e:
    print(f"[ServerMaliciousClientHandler.py] Import Error: {e}")
    exit()

class ServerMaliciousClientHandler:
    """
    This is the class that handles all the malicious clients, a new instance is spawned for 
    each client that checks in.
    """
    def __init__(self):
        self.first_time = 0
        # setting current job to none to start


        ## stats
        self.stats_heartbeats = 0
        self.stats_heartbeat_timer = 15
        self.stats_jobsrun = 0
        self.stats_latestcheckin = 0

        ## errors
        self.Sx12 = "[Server] A malicious client tried to connect without a valid ID:"


    def handle_client(self, conn, message, id):
        self.conn = conn
        self.ip = self.conn.getpeername()[0]
        self.port = self.conn.getpeername()[1]
        self.id = id
        ## ugly yes, but it works for now. 
        self.fullname = "client_" + self.ip.replace(".","_") + f"_{self.id}"
        self.under_control = False
        self.current_job = "Wait"
        
        self.data_list = [
            self.stats_heartbeats,
            self.stats_heartbeat_timer,
            self.stats_jobsrun,
            self.stats_latestcheckin
        ]

        self.handle_stats()


    def handle_stats(self):
        new_client = {
            "ClientFullName": f"{self.fullname}",
            "ClientIP": f"{self.ip}",
            "ClientPort": f"{self.port}",
            "ClientId": f"{self.id}",
            "CurrentJob": f"{self.current_job}",
            "SleepTime": f"{self.stats_heartbeat_timer}",
            "LatestCheckin": str(datetime.now(timezone.utc)),
            "FirstCheckin": str(datetime.now(timezone.utc)),
            "Active": "yes"
        }
        ## Runs every checkin, howeer the method will not write data if a record of this client exists
        Data.json_new_client(json.dumps(new_client))

    def cleanup(self):
        self.current_job = "wait\\|/wait"
    
    def send_msg_to_maliciousclient(self, msg:str):
        ## lazy fix to map self.conn to conn
        conn = self.conn
        
        ## clients need to have a shared known header beforehand. Default is 10
        HEADER_BYTES = 10
        BUFFER = 1024
        
        ## get the length of the message in bytes
        msg_length = len(msg)
        
        ## create a header for the message that includes the length of the message
        header = str_encode(str(msg_length).zfill(HEADER_BYTES))#.encode()
        
        ## send the header followed by the message in chunks
        logging.debug(f"[Server (send_msg_to_maliciousclient: {self.id})] SENDING HEADER: {header}")
        conn.send(header)

        chunks = math.ceil(msg_length/BUFFER)
        for i in range(0, chunks):
            
            try:
                ## gets the right spot in the message in a loop
                chunk = msg[i*BUFFER:(i+1)*BUFFER]
                logging.debug(f"[Server (send_msg_to_friendlyclient: {self.id})] SENDING CHUNK {i+1}/{chunks}")
                conn.send(str_encode(chunk))
            except Exception as e:
                logging.debug(f"[Server (send_msg_to_maliciousclient: {self.id})] error sending: {e}")
        
        #recv_msg = self.recieve_msg_from_maliciousclient()
        #return recv_msg

    def recieve_msg_from_maliciousclient(self) -> str:
        conn = self.conn
        complete_msg = ""
        ## clients need to have a shared known header beforehand. Default is 10
        HEADER_BYTES = 10
        BUFFER = 1024
        header_value = 0
        header_contents = ""
        
        msg_bytes_recieved_so_far = 0
        
        logging.debug(f"[Server (recieve_msg_from_maliciousclient: {self.id})] WAITING ON HEADER TO BE SENT:")
        header_msg_length = conn.recv(HEADER_BYTES).decode() #int(bytes_decode(msg)
        logging.debug(f"[Server (recieve_msg_from_maliciousclient: {self.id})] HEADER: {header_msg_length}")
        
        ## getting the amount of chunks/iterations eneded at 1024 bytes a message
        chunks = math.ceil(int(header_msg_length)/BUFFER)
        
        complete_msg = "" #bytes_decode(msg)[10:]
        
        #while True:
        for i in range(0, chunks):
            logging.debug(f"[Server (recieve_msg_from_maliciousclient: {self.id})] WAITING TO RECEIEVE CHUNK {i + 1}/{chunks}:")
            msg = conn.recv(BUFFER)  # << adjustble, how many bytes you want to get per iteration
            
            ## getting the amount of bytes sent so far
            msg_bytes_recieved_so_far = msg_bytes_recieved_so_far + len(bytes_decode(msg))

            complete_msg += bytes_decode(msg)

            '''print(f"""DEBUG:
                Full Message Length (based on header value) {header_msg_length}
                Header size: {HEADER_BYTES}

                Size of message recieved so far: {msg_bytes_recieved_so_far}  
                
                Chunks: {chunks}          
                
                """)'''
            
            ## if complete_msg is the same length as what the headers says, consider it complete. 
            if len(complete_msg) == header_msg_length:
                logging.debug(f"[Server (recieve_msg_from_maliciousclient: {self.id})] MSG TRANSFER COMPLETE")

        return complete_msg
            