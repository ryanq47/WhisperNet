# This Python file uses the following encoding: utf-8

class Login():
    def __init__(self):
        pass


    def to_server(self, username=None, password=None, server=None):
        '''
        Stuff, creates login json & then makes the request, returns jwt. Need to figure out where to set JWT so it can be accesed by everything needed
                                                                        maybe create a data something class, init at start, expose to qml.
        '''
        print(username)
        pass
