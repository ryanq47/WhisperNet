## Listener Class, one for each listener that exists. 


import time
from Utils.Logger import LoggingSingleton


class Listener:
    # init with needed items
    def __init__(self, lid, address, sync_endpoint):
        self.logger = LoggingSingleton.get_logger()
        self.lid = lid
        self.address = address
        self.sync_endpoint = sync_endpoint
        

    
    def forward_request(self, request):
        """
            Forwards request to listener        

        Args:
            request (_type_): _description_
        """
        ...

