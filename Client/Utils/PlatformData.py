'''
Holds relevant platform data for the client to use.
'''
import os

class Platform:
    os = None

    def gather_data():
        '''
        Runs methods to gather required data for platform. Called with startup

        Currently gathers:
            OS Type (NT or Linux)
            
        Don't worry. This data is not saved, or sent anywhere. It's only used internally
        '''
        Platform.os = Platform.get_os()

    def get_os():
        return os.name
    


