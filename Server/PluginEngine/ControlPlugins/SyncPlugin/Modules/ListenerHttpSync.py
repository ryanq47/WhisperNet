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
        for json_entry in response:
            self.data.Listeners.HTTP.add_synced_data(data=json_entry)

        self.logger.debug(f"Data from the response has been stored successfully.")

       # print("Data in list")
        #print(self.data.Listeners.HTTP.synced_data_store)

        # access singleton
        # appendd data to it

