'''
The base plugin. Required at the moment, and adds extra methods to sub classes that
could be useful.


'''


class BasePlugin:
    def __init__(self, app):
        self.app = app
        self.print_symbol = "[*]"
        print("BaseClass init")


    def register_routes(self):
        # Define common route registration logic here.
        pass

