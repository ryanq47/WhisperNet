class BasePlugin:
    def __init__(self, app):
        self.app = app
        print("BaseClass init")


    def register_routes(self):
        # Define common route registration logic here.
        pass