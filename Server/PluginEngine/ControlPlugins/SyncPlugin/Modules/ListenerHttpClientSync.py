# handles ListenerHttpClientSync Sync Keys

from Utils.DataSingleton import Data
from Utils.Logger import LoggingSingleton

class ListenerHttpClientSync:
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
                {"lid":"1234-1234-1234-1234", "cid": "0234-1234-1234-1235"},
            ]

        """
        for dict_entry in response:
            # Assuming `add_synced_data` is commented out for now
            # self.data.Listeners.HTTP.add_synced_data(data=dict_entry)

            # Extract the listener ID (lid) from the dictionary entry
            lid = dict_entry.get("lid")
            if lid is None:
                self.logger.warning("Listener ID (lid) is missing in the response entry.")
                continue

            # Extract the client ID (cid) from the dictionary entry
            cid = dict_entry.get("cid")
            if cid is None:
                self.logger.warning("Client ID (cid) is missing in the response entry.")
                continue

            # Retrieve the listener object using the listener ID
            listener_object = self.data.Listeners.HTTP.get_listener_class_object_by_lid(lid)
            if listener_object is None:
                self.logger.warning(f"Listener object for LID {lid} not found.")
                continue

            # Add client to the listener object
            try:
                listener_object.add_client(cid=cid)
                self.logger.debug(f"Client {cid} added to listener {lid}.")
            except Exception as e:
                self.logger.error(f"Failed to add client {cid} to listener {lid}: {e}")





