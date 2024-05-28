## Listener Class, one for each listener that exists. 


import time
from Utils.Logger import LoggingSingleton
import requests

class Listener:
    # init with needed items
    def __init__(self, lid, address, sync_endpoint):
        self.logger = LoggingSingleton.get_logger()
        self.lid = lid
        self.address = address
        self.sync_endpoint = sync_endpoint
        self.current_clients = []
        

    
    def forward_request(self, request):
        """
            Forwards request to listener        

        Args:
            request (_type_): _description_


            Tofigure out: New request ID or No? I'm thinking no as it's being FORWARDED to the listener. 
        """

        self.logger.debug(f"forwarding request to listener {self.lid} at {self.address}/{self.sync_endpoint}")
        r = requests.post(
            url=f"{self.address}/{self.sync_endpoint}",
            data=request,
        )

        if r.status_code != 200:
            self.logger.warning(f"Forward to {self.lid} at {self.address}/{self.sync_endpoint} was unsuccessful!")
            self.logger.debug(r.text)
    
    # going to need a sync key that contains clients
    # ListenerHttpClientSync?
    def add_client(self, cid, **kwargs):
        """
        Adds a client dict to the current_clients list.

        Args:
            cid (str): Client ID
            **kwargs: Additional client-specific information

        Client Dict:

        {
            "cid":"1234-1234-1234-1234"
        }
        
        """
        client_data = {"cid": cid}
        client_data.update(kwargs)
        
        self.current_clients.append(client_data)
        self.logger.debug(f"Added client {cid} with data {client_data} to listener {self.lid}")

    def check_if_client_is_apart_of_listener(self, cid):
        """
            Checks if client is apart of listener. 

            Currently uses only data it has access to locally, does *not* reach out to listener.         

        Args:
            cid (_type_): _description_
        """
        for client in self.current_clients:
            iter_cid = client.get("cid")
            if iter_cid == cid:
                self.logger.debug(f"Client {cid} exists in listener {self.lid}")
                return True
        
        
        self.logger.debug(f"Client {cid} does not exist in listener {self.lid}")
        return False
