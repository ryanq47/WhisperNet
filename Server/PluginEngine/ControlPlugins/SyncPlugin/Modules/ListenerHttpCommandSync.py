from Utils.DataSingleton import Data
from Utils.Logger import LoggingSingleton

class ListenerHttpCommandSync:
    def __init__(self):
        self.data = Data()
        self.logger = LoggingSingleton.get_logger()

    def store_response(self, response):
        """
        Stores each key-value pair from the response dictionary in the data singleton.

        Args:
            response (dict): The dictionary containing the data to be stored. Each key-value pair in this dictionary will be added to the synced data store.
        """
        self.logger.debug(f"Storing data")
        #print(response)
        if not isinstance(response, list):
            self.logger.error("Invalid response type: Expected a list.")
            return

        # Iterate over each key-value pair in the response dictionary
        # json entry: `{"action": "powershell","executable": "ps.exe","command": "whoami", "aid":"1234"}`
        #for json_entry in response:
            #self.data.Listeners.HTTP.add_synced_data(data=json_entry)

        ## New (ineffecient) way:
        # for each entry:
            #store w/ Listeners.HTTP.add_synced_data(data=json_entry) # ideally this will record requests/do any other non networking procesing
            # Get all of that data, find listener for respective request (need a lookup), and send.
            # format into request
            # forward *to* client. 

        # problems; ineffecient. Lots of requests. No "universal" packet being sent to client. 
        # lets try it.

        """
            Response Example:
            [
                {'client_nicnkname': 'standin_nickname', 'action': 'powershell', 'executable': 'ps.exe', 'command': 'whoami', 'aid': 'standin_aid'}, 
                {'client_nicnkname': 'standin_nickname', 'action': 'powershell', 'executable': 'ps.exe', 'command': 'whoami', 'aid': 'standin_aid'}
            ]

        """

        for dict_entry in response:
            self.data.Listeners.HTTP.add_synced_data(data=dict_entry)

            #print(dict_entry)
            #print(type(dict_entry))

            # Extract the client nickname (eventually this should be changed to LID/UUID)
            client_nickname = dict_entry.get("client_nickname")
            if client_nickname is None:
                self.logger.warning("Client nickname is missing in the response entry.")
                continue

            # Extract the listener object based on the current clients from the listener
            listener_object = self.data.Listeners.HTTP.get_client_listener(cid=client_nickname)
            if listener_object is None:
                self.logger.warning(f"Listener LID for CID {client_nickname} not found.")
                continue

            # Retrieve the listener object using the listener LID
            #listener_object = self.data.Listeners.HTTP.get_listener_class_object_by_lid(listener_lid)
            #if listener_object is None:
            #    self.logger.warning(f"Listener object for LID {listener_lid} not found.")
            #    continue

            # Forward the request to the listener
            try:
                listener_object.forward_request(dict_entry)
                self.logger.debug(f"Request forwarded to listener {listener_object.lid} for client {client_nickname}.")
            except Exception as e:
                self.logger.error(f"Failed to forward request to listener {listener_object.lid} for client {client_nickname}: {e}")






        self.logger.debug(f"Data from the response has been stored successfully.")

       # print("Data in list")
        #print(self.data.Listeners.HTTP.synced_data_store)

        # access singleton
        # appendd data to it

