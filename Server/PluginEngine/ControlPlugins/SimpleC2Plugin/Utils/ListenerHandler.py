from PluginEngine.PublicPlugins.ListenerHTTP.ListenerHTTP import ListenerHTTP
from Utils.DataSingleton import Data
from Utils.Logger import LoggingSingleton
from multiprocessing import Process
import time

logger = LoggingSingleton.get_logger()

class HttpListenerHandler:
    @staticmethod
    def start(bind_address=None, bind_port=None, nickname=None):
        '''
        Starts the listener & adds it to the DataSingleton for management.
        '''
        try:
            listener_instance = ListenerHTTP(
                bind_port=bind_port,
                bind_address=bind_address,
                nickname=nickname
            )
            # Prepare a stop event for this listener
            #stop_event = Event() # would be handy for graceful shutodwn N stuff, aka no .terminate()

            p = Process(target=listener_instance.main)
            p.start()

            data_singleton = Data()
            # Storing the process and its stop event for later management
            info = {
                "bind_port": bind_port,
                "bind_address": bind_address,
                "nickname": nickname,
                "type":"HTTP"
            }
            data_singleton.Listeners.HTTP.add_listener(process=p, info=info)

            logger.info(f"Started HTTP listener on {bind_address}:{bind_port}!")
        except Exception as e:
            logger.warning(e)

    @staticmethod
    def stop(nickname=None):
        '''
        Stops a listener based on its nickname.
        '''
        try:
            data_singleton = Data()
            # change this to a getter method eventually
            listener_info = data_singleton.Listeners.HTTP.get_listener_by_nickname(nickname=nickname)

            if listener_info:
                logger.debug("Warning, still using .terminate() to shut down listeners. May cause problems")
                # Directly terminate the process - Not a problem at the moment, but could be more graceful if needed in the future
                listener_info['process'].terminate()
                listener_info['process'].join()  # Wait for the process to be terminated
                logger.info(f"Stopped HTTP listener {nickname} successfully.")
            else:
                logger.info(f"Listener {nickname} does not exist, cannot stop it.")
        except Exception as e:
            logger.error(e)


