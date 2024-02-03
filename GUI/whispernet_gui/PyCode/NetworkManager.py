
## Expirement with netmanager & stuff

## weird issue, data not being reutred to NetManagerExample, it comes in as a QQucikItem object?

from PySide6.QtCore import QObject, Signal, Slot, QByteArray
from PySide6.QtNetwork import QNetworkAccessManager, QNetworkRequest
from PySide6.QtCore import QUrl

'''
    Fuuuuck didn't think about this, not sure if this will work when not directly called from QML.
'''

class NetworkManager(QObject):
    # Signal to emit when data is received
    dataReceived = Signal(str)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.networkAccessManager = QNetworkAccessManager(self)
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

    @Slot(str, str)
    def postData(self, url, data):
        #self.dataReceived.emit("Your string here")
        #print(self.dataReceived)

        request = QNetworkRequest(QUrl(url))
        request.setHeader(QNetworkRequest.ContentTypeHeader, "application/json")
        #self.networkAccessManager.post(request, QByteArray(data.encode("utf-8")))
        # Send N Get reply
        reply = self.networkAccessManager.post(request, QByteArray(data.encode("utf-8")))
        # connect to handle reply
        reply.finished.connect(lambda: self.handleReply(reply))



    def handleReply(self, reply):
        print("hi")
        if reply.error():
            print("Error:", reply.errorString())
            self.dataReceived.emit("Error: " + reply.errorString())
            #self.dataReceived.emit("if error")

        else:
            response = reply.readAll().data().decode("utf-8")
            self.dataReceived.emit(response)

        reply.deleteLater()

