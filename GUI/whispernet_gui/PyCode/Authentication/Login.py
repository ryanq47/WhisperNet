from PySide6.QtCore import QObject, Property, Slot
import inspect
import json

from PyCode.Network.NetworkManager import NetworkManager
from PyCode.Utils.BaseLogging import BaseLogging
from PyCode.Data.Data import Data
class Login(QObject, BaseLogging):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.logger.debug(f"Initialized Backend Component: {self.__class__.__name__}")

    @Slot(str, str, str)
    def to_server(self, username=None, password=None, server=None):
        '''
        Stuff, creates login json & then makes the request, returns jwt. Need to figure out where to set JWT so it can be accesed by everything needed
                                                                        maybe create a data something class, init at start, expose to qml.
        '''
        print(username)

        try:
            login_dict = {
                "username":username,
                "password":password,
            }

            login_json = json.dumps(login_dict)

            net_manager = NetworkManager()
            
            net_manager.postData(
                url = "http://127.0.0.1:5000/api/login",
                data = login_json
            )

            # for debugging
            #net_manager.dataReceived.connect(lambda data: print("Data received:", data))

            net_manager.dataReceived.connect(self.parse_data)

        except Exception as e:
            self.logger.error(f"{self.__class__.__name__}.{inspect.currentframe().f_code.co_name}: {e}")


    def parse_data(self, json_data):
        '''
            Parses & Sets data
        '''
        login_response_dict = json.loads(json_data)
        access_token = login_response_dict["access_token"]

        global_data = Data()
        #set data to singleton
        global_data.auth.set_jwt(access_token)

        #this works, so not getting JWT is a qml problem
        #print(global_data.auth.get_jwt())
