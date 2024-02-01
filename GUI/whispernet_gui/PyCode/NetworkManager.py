
## Expirement with netmanager & stuff

from PySide6.QtCore import QObject, Signal, Slot

class NetworkManager(QObject):
    # Signal to emit when data is received
    dataReceived = Signal(str)

    def __init__(self, parent=None):
        super().__init__(parent)
        # Initialize your network access manager and other related stuff here
        self.jwt = None ## JWT

    @Slot(str)
    def getData(self, url):
        # Implement the logic to fetch data from the given URL
        # Once data is fetched, emit the dataReceived signal

        '''
        Ex Code

        ##get request or something
        ## some other stuff

        '''

        self.dataReceived.emit("Fetched data")

    @Slot(str)
    def postData(self, url):
        # Implement the logic to fetch data from the given URL
        # Once data is fetched, emit the dataReceived signal

        '''
        Ex Code

        ##get request or something
        ## some other stuff

        '''

        self.dataReceived.emit("Fetched data")
