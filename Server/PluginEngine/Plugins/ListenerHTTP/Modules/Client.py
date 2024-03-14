## Client class, one per client joined. Takes app as a ref to the flask app to add url's N stuff


class Client():
    def __init__(self, app):
        self.app = None

