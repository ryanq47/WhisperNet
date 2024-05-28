"""
"ListenerInfo": {
    "uuid":"1234-1234-1234-1234"
},

"""

from Utils.DataSingleton import Data
from Utils.Logger import LoggingSingleton
from PluginEngine.ControlPlugins.SimpleC2Plugin.Utils.Listener import Listener

class ListenerInfo:
    def __init__(self):
        self.data = Data()
        self.logger = LoggingSingleton.get_logger()

    def store_response(self, response):
        """
        Stores each key-value pair from the response dictionary in the data singleton.

        Args:
            response (dict): The dictionary containing the data to be stored. Each key-value pair in this dictionary will be added to the synced data store.
        """
        # get data from listenerInfo vessel
        lid = response.get('lid')
        address = response.get('address')
        sync_endpoint = response.get('sync_endpoint')

        # verify listener is legit (pub key maybe? - not sure how to handle this)
            # see obsidian
            #if not good, return fasle
        self.logger.warning("Eventual Listener Authentication - Any listener is valid currently. ")

        # Check if listener object exists, if not, create it and retrieve it
        listener_object = self.data.Listeners.HTTP.get_listener_by_lid(lid)

        if not listener_object:
            self.logger.info(f"New Listener communicating with server, LID: {lid}, Address: {address}")
            self.logger.debug("Listener object not found, creating")
            
            #Create object
            class_object = Listener(
                lid=lid,
                address=address,
                sync_endpoint=sync_endpoint
            )

            # add object
            self.data.Listeners.HTTP.add_listener(
                lid=lid, class_object=class_object
            )

        # aka listener is good to go
        return True

            #listener_object = self.data.Listeners.HTTP.get_listener_by_lid(lid)

        #self.data.Listeners.HTTP.get_listener_by_lid(lid)
        
        # done! Listener can now be queried/used for gettig/pushing data. 
