## A set of classes that handles the logic of listener management. Detached from the plugin so the plugin can focus *just* on the flask requets, etc. 
# These should probably have a fair amount of static methods.
from PluginEngine.PublicPlugins.ListenerHTTP.ListenerHTTP import ListenerHTTP
from Utils.DataSingleton import Data
from Utils.Logger import LoggingSingleton
from multiprocessing import Process

logger = LoggingSingleton.get_logger()

class HttpListenerHandler:
    #def __init__(self):
    #    pass

    @staticmethod
    def start(bind_address = None, bind_port = None, nickname = None):
        '''
        bind_address: What address to bind/listen on
        bind_port: what port to bind/listen on

        nickname: Name of the listener. 

        Starts the listener & adds it to the datasingleton for management. Calls the same methods as if called standalone, this is just a wrapper.
        
        '''
        try:
            ## check if exist in data singleton

            ## Init Instance
            listener_instance = ListenerHTTP(
                bind_port = bind_port,
                bind_address = bind_address,
                nickname = nickname
            )
            # with this call, the listener has been started.

            # Miiiight need to new thread this? It hangs and doesnt return a response to the HTTP call. Othewise seems to work fine.
            #listener_instance.main()

            ## Need to figure out the Join stuff as well? - DO NOT JOIN. joins to main thread and causes probelsm
            p = Process(target=listener_instance.main)
            p.start()

            data_singleton = Data()

            # add to data singleton for management. 
            #data_singleton.Listeners.Http.add_listener(class_object = listener_instance, nickname = nickname)
        
            # info class for holding infoation. Doing this instead of individual func args for expandadibility
            info = {
                "bind_port":bind_port,
                "bind_address":bind_address,
                "nickname": nickname
            }

            data_singleton.Listeners.Http.add_listener(process = p, info = info)
            #p.join()

            # add a check to make sure listener is actually up?
            logger.info(f"Started HTTP listener on {bind_address}:{bind_port}!")

            ## return true or something
        
        except Exception as e:
            logger.warning(e)
    
    @staticmethod
    def stop(bind_address = None, bind_port = None):
        pass

        ## check if exist in data singleton

        ## Init Instance


        ## Add to data singleton. 
    
        ## return true or something
    

        """
        p = Process(target=run_app, args=(port,))
        p.start()
        processes.append(p)

    # Join processes to the main process to wait for them to end
    for process in processes:
        process.join()
        """


    