'''
Actions. This calls the respective handler, which returns data.


'''


from tkinter import E


try:
    ## just have to import it, everything else is taken care of in client.py
    import logging
    ##used for tracking errors, super useful. a traceback is included in all  the return  functions in the "dbg_code_source" key
    import inspect
    
    ## this is where the SystemDefaultActions live.
    import Logic.DecisionTree
    
    import Utils.AuthenticationHandler
    import Data.JsonHandler
    import Comms.CommsHandler

except Exception as e:
    ##print this error, as there's a chance logging is the one that failed, or that it doesnt get loaded.
    print(f"[<PluginPath>] Import Error: {e}")

## == Data == ##
## used for imports
class Info:
    name    = "Server"
    author  = "ryanq.47"
    dir     = "home/server"


class Tree:
    '''
    The 'Tree' class. It's job is to control the input that the user gives, call the respective methods, and return the results back to the dynamic_user_loop, which prints it onscreen
    
    Returns(dict[output_from_action, dir, dbg_code_source]): This is essentially passing on the 'return' from the Actions class
    '''
    def __init__(self):
        self.cookie = None

    ## Do not change the name of 'tree_input', it's used while  importing this Plugin
    def tree_input(self, user_input = None):
        dispatch = {
            ## Default commands...
            "help": Actions._display_help,
            "home": Logic.DecisionTree.SystemDefaultActions._set_dir_home_shell,
            "exit": Logic.DecisionTree.SystemDefaultActions._set_dir_home_shell,
            "clear": Logic.DecisionTree.SystemDefaultActions._display_clear,

            ## add yours here... no (), as we are just passing the object, not running it 
            #"mycommand":Actions._test_action
            "connect to server": Actions._connect_to_server,
            "show connection details": Actions._show_connection_details


        }

        action = dispatch.get(user_input)

        ## special handling of this inpupt
        if user_input == "connect to server":
            try:
                cookie = Actions._connect_to_server()["output_from_action"]
                print(cookie)
                self.cookie = cookie
                return{"output_from_action":f"Cookie successfully obtained: {self.cookie}", "dir":None, "dbg_code_source":inspect.currentframe().f_back}
            except Exception as e:
                return{"output_from_action":f"Error retrieveing cookie: {e}", "dir":None, "dbg_code_source":inspect.currentframe().f_back}



        elif action:
            return action()
        else:
            ## If the command doesn't exist, return this
            return{"output_from_action":"Invalid command. Type 'show help' for available commands.", "dir":None, "dbg_code_source":inspect.currentframe().f_back}



class Actions:
    '''
        Action methods, called directly from the 'Tree' class. These are the methods for the actual commands listed from the help menu

        Returns(dict[output_from_action, dir, dbg_code_source]): All methods return this dict to the Tree class
    
    '''

    def _display_help():
        help_menu = ("""Help Menu:\n
        'help'\t: Spawns this menu
        'home' or 'exit'\t: Exits the program
        'clear'\t: Clears the screen
        'connect to server'\t: Connect to a server instance.
        'start server'\t: start a local server instance

        ## Once connected: ## (work in progress)
        'show agents'

              """)
        return{"output_from_action":help_menu, "dir":None, "dbg_code_source":inspect.currentframe().f_back}
    
    def _start_server():
        pass
        ## do actions here,

        ## Handler.my_method()

        return{"output_from_action":"Start Server", "dir":None, "dbg_code_source":inspect.currentframe().f_back}
    
    def _connect_to_server():
        ## do actions here,

        server_details = Utils.AuthenticationHandler.Server.get_server_to_connect_to()

        socket = Handler._create_socket_connection(server_details_tuple=server_details) ## Need to figure out socket

        ## Get creds from user
        ## get cookie
        cookie = Handler._get_cookie(
            socket      = socket
        )


        return{"output_from_action":cookie, "dir":None, "dbg_code_source":inspect.currentframe().f_back}

    def _show_connection_details():
        conn_details_formatted = f"Server: IP:PORT \n"
        f"Cookie: cookie \n"\
        f"Other?\n"

        return{"output_from_action":conn_details_formatted, "dir":None, "dbg_code_source":inspect.currentframe().f_back}


class Handler:
    '''
    Handles Actions related to shell operations. Seperate from  'Actions', for flexibility & function re-use. Directly returns to the 'Action' class

    Returns (str): All methods return the results of the action the method performs
    
    '''

    @staticmethod
    def _get_cookie(socket = None):
        ##  Constuct json

        user = Utils.AuthenticationHandler.Credentials.get_username()
        password = Utils.AuthenticationHandler.Credentials.get_password()

        json = Data.JsonHandler.json_ops.to_json_for_server(
            action      = "!_userlogin_!", 
            client_id   = user,
            auth_type   = "password",
            auth_value  = password
        )

        
        Comms.CommsHandler.send_msg(
            msg     = json,
            conn    = socket
        )

        msg_from_server = Comms.CommsHandler.receive_msg(
            conn = socket
        )

        ## convert from JSON to python dict

        json_dict = Data.JsonHandler.json_ops.from_json(
            json_string=msg_from_server
        )

        cookie = json_dict["msg"]["msg_value"]

        ## return results of action
        return cookie
    
    def _create_socket_connection(server_details_tuple = ("127.0.0.1", 80)):
        '''
        Calls Comms.CommsHandler.connect_to_server to create a socket, either SSL or plaintext.

        I could just call Comms.CommsHandler.connect_to_server directly in the actions class, but doing it here allows for readability.

        If you are creating a plugin, please use the Comms.CommsHandler.connect_to_server, not this one
        
        returns a socket
        '''

        try:
            server_sock = Comms.CommsHandler.connect_to_server(
                server_conn_tuple=server_details_tuple
            )

        except ConnectionError as ce:
            logging.warning(f"Connection error to: {server_details_tuple}. {ce}")

        return server_sock
