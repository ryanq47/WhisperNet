# HTTP listener. Meant to be standalone, most things must be done throgh API calls to it. (ex: no direct neo4j interaction, call the main server api for that.)

# for standalone running
if __name__ == "__main__":
    #print("Plugin running in standalone mode!")
    import logging
    from Modules.Logger import LoggingSingleton # hmm gonna need to inlcude a logger in utils?
    from Modules.Client import Client
    from Modules.HTTPJsonRequest import HTTPJsonRequest

# for NODE/Server running
else:
    from Utils.Logger import LoggingSingleton
    from PluginEngine.PublicPlugins.ListenerHTTP.Modules.Client import Client
    from PluginEngine.PublicPlugins.ListenerHTTP.Modules.HTTPJsonRequest import HTTPJsonRequest

from flask import jsonify, make_response, Flask
import inspect

class Info:
    name    = "ListenerHTTP"
    author  = "ryanq47"
    endpoint = "/http"
    classname = "ListenerHTTP"
    plugin_type = "Portable"


class ListenerHTTP:
    def __init__(self, app = None, bind_address = None, bind_port = None, nickname = None):
        if __name__ == "__main__":
            self.logger = LoggingSingleton.get_logger(log_level=logging.DEBUG)

        else:
            # needed as the singleton is initialized on the standalone, but is not when run as a plugin. Init takes an extra arg, 
                #as seen above.
            self.logger = LoggingSingleton.get_logger()

        self.app = app

        self.bind_address = bind_address
        self.bind_port = bind_port
        self.nickname = nickname

        self.client_class_dict = {}

    def main(self):
        '''
        Main function/entry point for the plugin.
        '''
        try:

            ## OKAY rework this chain/put in functions?

            self.logger.debug(f"{inspect.stack()[0][3]}")
            self.logger.debug(f"Loading & starting {Info.name}")


            # if no flask instance, create one - prolly don't need a sep func for this.
            if self.app == None:
                self.logger.debug(f"App is none, initializing")
                self.app = create_flask_instance()

            # register routes
            self.register_routes()

            # actually start the app
            self.app.run(
                host = self.bind_address,
                port=self.bind_port,
                debug=False
            )

        except Exception as e:
            self.logger.warning(e)

    def register_routes(self):
        self.app.route(f'/', methods = ["GET"])(self.listener_http_base_endpoint)
        self.app.route(f'{Info.endpoint}/get', methods = ["GET"])(self.listener_http_get_endpoint)
        self.app.route(f'{Info.endpoint}/post', methods = ["POST"])(self.listener_http_post_endpoint)


    def listener_http_base_endpoint(self):
        return "base_endpoint"

    def listener_http_get_endpoint(self):
        '''
            Init post endpoint. will be used for something
        '''

        # for now, just returning the mock JSON format
        dummy_request = HTTPJsonRequest()

        dummy_request.callback.server.hostname = "callbackserver" # pull this from the singleton somehwere

        dummy_request_json = dummy_request.generate_json()

        return make_response(dummy_request_json, 200)


    def listener_http_post_endpoint(self):
        '''
            Initial checkin endpoint. Registers client if new, and gives URL for client to use going forward
        
        '''

        # for now, just returning the mock JSON format
        dummy_request = HTTPJsonRequest()

        dummy_request.callback.server.hostname = "callbackserver" # pull this from the singleton somehwere

        dummy_request_json = dummy_request.generate_json()

        return make_response(dummy_request_json, 200)


        #self.client_checkin_validation("data")

        #return make_response("POST ENDPOINT - JSON HERE", 200)


    def client_checkin_validation(self):
        pass
        # check if client exists, via query to main server DB

        # if not exists, create in main Server db

        # create class instance
        #new_client = Client(data)

        # add to dict of current clients. key is name
    
def create_flask_instance():
    '''
    Creates a flask instance. Used when the plugin is NOT in standalone mode
    
    '''
    app = Flask("http_listener")
    return app


## Standalone mode options
if __name__ == "__main__":
    print(f"Starting {Info.name} in standalone mode.")

    # Do with args later
    app = Flask("http_listener")

    print(f"Hosting on: http://0.0.0.0:1000, ControlServer: 127.0.0.1")
    ## Create flask info

    plugin_instance = ListenerHTTP(
        app = app,
        bind_port=1000,
        bind_address="0.0.0.0"
    )
    plugin_instance.main()
    #plugin_instance.main()
    #app.run(host="0.0.0.0", port="1000", debug=False)
