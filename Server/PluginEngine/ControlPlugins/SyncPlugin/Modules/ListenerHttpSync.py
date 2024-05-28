from Utils.DataSingleton import Data
from Utils.Logger import LoggingSingleton

class ListenerHttpSync:
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

        # rename json_entry to something better
        for json_entry in response:
            self.data.Listeners.HTTP.add_synced_data(data=json_entry)
            
            # maybe just have listener objects tbh?
            
            # extract which listener based on current clietns from listener
            #self.data.Listeners.HTTP.get_listener_from_client_uuid(client_uuid)    # returns listener UUID

            #self.data.Listeners.HTTP.get_listener_by_nickname(listener_uuid)       # change to UUID

            # send request to said listener. 
            #listener_object.forward_request(json_entry)





        self.logger.debug(f"Data from the response has been stored successfully.")

       # print("Data in list")
        #print(self.data.Listeners.HTTP.synced_data_store)

        # access singleton
        # appendd data to it

