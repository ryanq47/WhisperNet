from PluginEngine.PublicPlugins.ListenerHTTP.ListenerHTTP import ListenerHTTP
from Utils.DataSingleton import Data
from Utils.Logger import LoggingSingleton
from multiprocessing import Process
import time
import uuid

logger = LoggingSingleton.get_logger()

class HttpListenerHandler:
    @staticmethod
    def spawn(bind_address=None, bind_port=None, nickname=None):
        '''
        Spawn (Create a new)  listener & adds it to the DataSingleton for management.
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
                "lpid": uuid.uuid4(), # generate process id
                "type":"HTTP"
            }
            data_singleton.Listeners.HTTPProcess.add_listener_process(process=p, info=info)

            logger.info(f"Spawned HTTP listener {nickname} on {bind_address}:{bind_port}!")
        except Exception as e:
            logger.warning(e)

    @staticmethod
    def kill(nickname=None):
        '''
        Kill a listener based on its nickname.
        '''
        try:
            data_singleton = Data()
            # change this to a getter method eventually
            listener_info = data_singleton.Listeners.HTTPProcess.get_listener_process_by_nickname(nickname=nickname)

            if listener_info:
                logger.debug("Warning, still using .terminate() to shut down listeners. May cause problems")
                # Directly terminate the process - Not a problem at the moment, but could be more graceful if needed in the future
                listener_info['process'].terminate()
                listener_info['process'].join()  # Wait for the process to be terminated
                logger.info(f"Killed HTTP listener {nickname} successfully.")
            else:
                logger.info(f"Listener {nickname} does not exist, cannot kill it.")
        except Exception as e:
            logger.error(e)


