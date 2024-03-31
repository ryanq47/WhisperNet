'''
TLDR: an "event loop" that does actions needed for the GUI to update.

Logs in here are primarily warning & critical, as this is a critical component of the gui... or will be. 

'''

from Utils.Logger import LoggingSingleton
import inspect
from PySide6.QtCore import QTimer, QObject

class Event(QObject):
    _instance = None  # Class-level attribute to store the singleton instance
    _is_initialized = False  # Flag to check if the instance has been initialized

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Event, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        #if not hasattr(self, 'initialized'): ## prevents reinit
        if not self._is_initialized:
            super().__init__()
            self.logger = LoggingSingleton.get_logger()
            self.event_loop_list = []
            self._setup_timer()
            
            self._is_initialized = True  # Set the flag to True after initialization


    def _setup_timer(self):
        '''
        Sets up timer for event loop
        '''
        try:
            self.logger.debug(f"{self.__class__.__name__}.{inspect.currentframe().f_code.co_name}: Setting up event loop timer")
            self.timer = QTimer()
            self.timer.timeout.connect(self.process_events)
            self.timer_interval = 1000  # milliseconds

        except Exception as e:
                self.logger.critical(f"{self.__class__.__name__}.{inspect.currentframe().f_code.co_name}: Could not setup event loop timer: {e}")

    def add_to_event_loop(self, event, *args, **kwargs):
        '''
        :param event: The event function to add.
        :param args: Positional arguments for the event function.
        :param kwargs: Keyword arguments for the event function.

        Adds an event to the event loop
        
        '''
        try:
            self.logger.info(f"{self.__class__.__name__}.{inspect.currentframe().f_code.co_name}: Added event: {event} to the event loop")
            self.event_loop_list.append((event, args, kwargs))
        except Exception as e:
                self.logger.warning(f"{self.__class__.__name__}.{inspect.currentframe().f_code.co_name}: Could not add event to the event loop: {e}")

    def start_event_loop(self):
        '''
        Starts the event loop
        '''
        try:
            self.logger.info(f"{self.__class__.__name__}.{inspect.currentframe().f_code.co_name}: Starting event loop...")
            self.timer.start(self.timer_interval)
        except Exception as e:
                self.logger.critical(f"{self.__class__.__name__}.{inspect.currentframe().f_code.co_name}: Could not start event loop: {e}")

    def process_events(self):
        for event, args, kwargs in self.event_loop_list.copy():  
            # Process a copy of the list, tldr this prevents and weird actions from happening with the iterations, especially if somethign gets added/removed from the event list
            # Creates a shallow copy of the event, which is just a ref to the original func instead of fully copying it. saves on resources
            try:
                self.logger.debug(f"{self.__class__.__name__}.{inspect.currentframe().f_code.co_name}: proccessing event: {event}")
                event(*args, **kwargs)
            except Exception as e:
                self.logger.warning(f"{self.__class__.__name__}.{inspect.currentframe().f_code.co_name}: Error with proccessing events: {e}")


''' Example useage
if __name__ == "__main__":
    event_loop = Event()

    # Define a test event with arguments
    def test_event(arg1, arg2, kwarg1=None):
        print(f"Event triggered with arg1: {arg1}, arg2: {arg2}, kwarg1: {kwarg1}")

    # Add the test event with arguments to the event loop
    event_loop.add_to_event_loop(test_event, "Hello", "World", kwarg1="Python")

    event_loop.start_event_loop()

    # This would print: "Event triggered with arg1: Hello, arg2: World, kwarg1: Python" periodically
'''