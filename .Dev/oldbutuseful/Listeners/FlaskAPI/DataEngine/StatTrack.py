from datetime import datetime
from requests import get

class StatTrack:
    '''
    Used for stat tracking

    '''

    def __init__(self):
        self.start_time = None
        self.ext_ip     = None
        self.listener_name = None

    def set_time(self):
        self.start_time = datetime.utcnow()

    def set_ext_ip(self):
        self.ext_ip = get('https://api.ipify.org').content.decode('utf8')

    def set_listener_name(self, name="Listener"):
        self.listener_name = name