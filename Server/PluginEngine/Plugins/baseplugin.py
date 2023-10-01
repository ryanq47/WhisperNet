'''
The base plugin. Required at the moment, and adds extra methods to sub classes that
could be useful.


'''


class BasePlugin:
    def __init__(self, app, DataStruct):
        self.app = app
        self.print_symbol = "[*]"
        ## A class with data that might be handy
        self.DataStruct = DataStruct
        print("BaseClass init")


    def register_routes(self):
        # Define common route registration logic here.
        pass

