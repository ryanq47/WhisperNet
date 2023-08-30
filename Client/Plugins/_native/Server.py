'''
Actions. This calls the respective handler, which returns data.


'''

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
    import Logic.DecisionTree

except Exception as e:
    ##print this error, as there's a chance logging is the one that failed, or that it doesnt get loaded.
    print(f"[<PluginPath>] Import Error: {e}")

function_debug_symbol = "[^]"

## == Data == ##
## used for imports
class Info:
    name    = "Server"
    author  = "ryanq.47"
    dir     = "home/server"

class ClassData:
    '''
    Stores data for access by non static classes. Kind of a weird implementation. Think of this as a (jank) struct
    
    '''
    ## I hate that this exists. It's kind of dumb and hacky, but I don't have a better way to store data for static classes.
    ## In a nutshell, Tree is not static, but Actions and Handler are. With the way dispatch is set up, and there being mulieple server commands, it makes it tough to 
    ## pass the cookie via argument, so this is the best thing I can think of without re-doing it.

    # on the plus side it mgiht elimanate the need for normal classes
    cookie = None
    socket = None
    server_details = None
    client_id = None

class Tree:
    '''
    The 'Tree' class. It's job is to control the input that the user gives, call the respective methods, and return the results back to the dynamic_user_loop, which prints it onscreen
    
    Returns(dict[output_from_action, dir, dbg_code_source]): This is essentially passing on the 'return' from the Actions class
    '''
    def __init__(self):
        pass
        #self.cookie = None

    ## Do not change the name of 'tree_input', it's used while  importing this Plugin
    def tree_input(self, user_input = None, data_manager = None):
        dispatch = {
            ## Default commands...
            "help": Actions._display_help,
            "home": Logic.DecisionTree.SystemDefaultActions._set_dir_home_shell,
            "clear": Logic.DecisionTree.SystemDefaultActions._display_clear,

            ## add yours here... no (), as we are just passing the object, not running it 
            #"mycommand":Actions._test_action
            "connect to server": Actions._connect_to_server,
            "show connection details": Actions._show_connection_details,

            "_debug_run_server_command":Actions._debug_run_server_command

        }

        action = dispatch.get(user_input)
        #print(f"action: {action}")

        ## special handling of this inpupt
        if user_input == "connect to server":
            try:
                Actions._connect_to_server()["output_from_action"]
                return{"output_from_action":f"Cookie successfully obtained: {ClassData.cookie}", "dir":None, "dbg_code_source":inspect.currentframe().f_back}
            
            except Exception as e:
                logging.debug(f"{function_debug_symbol} {inspect.stack()[0][3]}: {e}")
                return{"output_from_action":f"Error retrieveing cookie: {e}", "dir":None, "dbg_code_source":inspect.currentframe().f_back}

        elif user_input[:2] == "cd":
            return Logic.DecisionTree.SystemDefaultActions._cd_to_dir(user_input = user_input)

        elif action:
            return action()
        else:
            ## Else, run command on server.
            response = Actions._run_server_command(
                command = user_input
            )

            ##Note, this returns out the full json return dict.
            return{"output_from_action":response, "dir":None, "dbg_code_source":inspect.currentframe().f_back}


class Actions:
    '''
        Action methods, called directly from the 'Tree' class. These are the methods for the actual commands listed from the help menu

        Returns(dict[output_from_action, dir, dbg_code_source]): All methods return this dict to the Tree class
    
    '''

    def _display_help():
        help_menu = ("""Help Menu:\n
        ## Built In ##
        'help'\t: Spawns this menu
        'home'\t: Exits the program
        'clear'\t: Clears the screen
        'cd <TOOL DIR>'\t: "cd" to the directory of the tool. Ex: 'cd home/systemshell'. 
                     
        ## Plugin Specific ##
        'connect to server'       : Connect to a server instance.
        'show connection details' : Shows connection details

        ## Debug ##
        _debug_run_server_command: Lets you fill in whatever you want in the JSON feilds for testing/debugging
                     
        ## Once connected: ## (work in progress)
        '<server help menu here>'

              """)
        return{"output_from_action":help_menu, "dir":None, "dbg_code_source":inspect.currentframe().f_back}
    
    def _start_server():
        pass
        ## do actions here,

        ## Handler.my_method()

        return{"output_from_action":"Start Server", "dir":None, "dbg_code_source":inspect.currentframe().f_back}
    
    def _connect_to_server():
        '''
        Connects to server

        Sets:
            ClassData.cookie
            ClassData.username

        '''
        ## do actions here,

        try:
            server_details = Utils.AuthenticationHandler.Server.get_server_to_connect_to()
            ClassData.server_details = server_details
            socket = Handler._create_socket_connection(server_details_tuple=server_details) ## Need to figure out socket

            ## Get creds from user
            client_id = Utils.AuthenticationHandler.Credentials.get_username()
            password = Utils.AuthenticationHandler.Credentials.get_password()
            ## get cookie
            cookie = Handler._get_cookie(
                socket      = socket,
                client_id   = client_id,
                password    = password
            )

            ## setting class data items
            ClassData.cookie    = cookie
            ClassData.client_id = client_id

            return{"output_from_action":cookie, "dir":None, "dbg_code_source":inspect.currentframe().f_back}
        
        except Exception as e:
            logging.debug(f"{function_debug_symbol} {inspect.stack()[0][3]}: {e}")

            return{"output_from_action":e, "dir":None, "dbg_code_source":inspect.currentframe().f_back}


    def _show_connection_details():
        conn_details_formatted = f"Server: {ClassData.server_details} \n" \
        f"Cookie: {ClassData.cookie} \n" \
        f"Username/Client_ID: {ClassData.cookie.client_id}\n"

        return{"output_from_action":conn_details_formatted, "dir":None, "dbg_code_source":inspect.currentframe().f_back}

    def _run_server_command(command = None):
        '''
        Pass a command along to the server. This does not work for client commands, as the msg_to is hardcoded

        
        ## steps
        ## check if server is conencted or not

        Send json to server asking for agents

        get that data

        return parsed response
        
        '''
        #print(Info.cookie)

        try:
            ## Create socket
            socket = Handler._create_socket_connection(server_details_tuple=ClassData.server_details) ## Need to figure out socket

            json_str_results = Handler._send_recv_command_to_server(
                cookie      = ClassData.cookie,
                msg_command = command,
                msg_to      = "server",
                socket      = socket,
                client_id   = ClassData.client_id
            )

            parsed_results = Data.JsonHandler.json_ops.from_json(
                json_string=json_str_results
            )

            cmd_results = f'{ClassData.server_details}: {parsed_results["msg"]["msg_value"]}'

            return{"output_from_action":cmd_results, "dir":None, "dbg_code_source":inspect.currentframe().f_back}
        except Exception as e:
            logging.debug(f"{function_debug_symbol} {inspect.stack()[0][3]}: {e}")
            return{"output_from_action":e, "dir":None, "dbg_code_source":inspect.currentframe().f_back}
        
    def _run_agent_command(command = None, agent_id = None):
        '''
        Pass a command to the server, for an agent. That command will get queued for running the next time the agent connects.

        command (str): A string with the command to be queued for the client
            Currently, only JSON communication is supported, so this should be a json string constructed with the 
            Data.JsonHandler.json_ops.to_json() function
        
            
            Ideas for actually reaching this code... CD into an "agent directory" (home/server/agent_1234) then just call this function
        '''
        #print(Info.cookie)

        try:
            ## Create socket
            socket = Handler._create_socket_connection(server_details_tuple=ClassData.server_details)

            json_str_results = Handler._send_recv_command_to_server(
                cookie      = ClassData.cookie,
                msg_command = command,
                msg_to      = agent_id,
                socket      = socket,
                client_id   = ClassData.client_id
            )

            parsed_results = Data.JsonHandler.json_ops.from_json(
                json_string=json_str_results
            )

            cmd_results = f'{ClassData.server_details}: {parsed_results["msg"]["msg_value"]}'

            return{"output_from_action":cmd_results, "dir":None, "dbg_code_source":inspect.currentframe().f_back}
        except Exception as e:
            logging.debug(f"{function_debug_symbol} {inspect.stack()[0][3]}: {e}")
            return{"output_from_action":e, "dir":None, "dbg_code_source":inspect.currentframe().f_back}




    def _debug_run_server_command():
        '''
        Does the same thing as run_server_command, but allows you to input custom data into the feilds.

        I think I need one for the clients as well.. shoot. Figure out later
        
        '''
        #print(Info.cookie)

        sleep_string = '''{"general": {"action": "sleep", "client_id": "", "client_type": "", "password": ""}, "conn": {"client_ip": "", "client_port": ""}, "msg": {"msg_to": "", "msg_content": "", "msg_command": "sleep", "msg_value": "", "msg_length": "", "msg_hash": ""}, "stats": {"latest_checkin": "", "device_hostname": "", "device_username": ""}, "security": {"client_hash": "", "server_hash": ""}}'''

        print("Command for server, 'server help' is a good one")
        s_msg_command = input("[FOR-SERVER] msg_command:")
        ## Hack to send sleep string as if it were a client recieving it. 
        if s_msg_command == "sleep":
            s_msg_command = sleep_string
        print("This is either 'server' or an agent name")
        s_msg_to = input("[FOR-SERVER]msg_to: ")
        print("Must be same username/id for cookie reasons.")
        s_client_id = input("[FOR-SERVER] your client_id/username: ")

        ## NOT HERE< do this in a _debug_run_client_commadn 
        #debug_msg = Data.JsonHandler.json_ops.to_json(
        #    msg_command = ("[FOR-CLIENT] msg_command:")
        #)

        try:
            ## Create socket
            socket = Handler._create_socket_connection(server_details_tuple=ClassData.server_details) ## Need to figure out socket

            json_str_results = Handler._send_recv_command_to_server(
                cookie      = ClassData.cookie,
                msg_command = s_msg_command,
                msg_to      = s_msg_to,
                socket      = socket,
                client_id   = s_client_id,
            )

            parsed_results = Data.JsonHandler.json_ops.from_json(
                json_string=json_str_results
            )

            cmd_results = f'{ClassData.server_details}: {parsed_results["msg"]["msg_value"]}'

            return{"output_from_action":cmd_results, "dir":None, "dbg_code_source":inspect.currentframe().f_back}
        except Exception as e:
            logging.debug(f"{function_debug_symbol} {inspect.stack()[0][3]}: {e}")
            return{"output_from_action":e, "dir":None, "dbg_code_source":inspect.currentframe().f_back}



class Handler:
    '''
    Handles Actions related to shell operations. Seperate from  'Actions', for flexibility & function re-use. Directly returns to the 'Action' class

    Returns (str): All methods return the results of the action the method performs
    
    '''

    @staticmethod
    def _get_cookie(socket = None, client_id = None, password = None):
        '''
        Gets the cookie from the server.

        Args:
            socket: The socket connection to the server
            user: The username
            password: The password for the server

        Populates these keys in the JSON that gets sent to the server:
            action
            client_id
            auth_type
            auth_value
        
        '''
        try:

            json = Data.JsonHandler.json_ops.to_json_for_server(
                action      = "!_userlogin_!", 
                client_id   = client_id,
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
    
        except Exception as e:
            logging.debug(f"{function_debug_symbol} {inspect.stack()[0][3]}: {e}")
            return e

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
    
    def _send_recv_command_to_server(cookie = None, client_id = None, msg_to = None, msg_command = None, socket = None) -> str:
        '''
        Sends & receives msg from server. Requires a cookie.
        '''
        ## Precheck stuff - get chatgpt to make more efficient
        if cookie == None:
            return("cookie is empty!")
        if cookie == socket:
            return("Socket is empty!")

        try:
            ## Create json
            
            json = Data.JsonHandler.json_ops.to_json_for_server(
                action      = "!_userlogin_!", 
                client_id   = client_id,
                auth_type   = "cookie",
                auth_value  = cookie,

                ## gonna need these 2 as args
                msg_to      = msg_to,
                msg_command = msg_command
            )

            Comms.CommsHandler.send_msg(
                msg     = json,
                conn    = socket
            )

            msg_from_server = Comms.CommsHandler.receive_msg(
                conn = socket
            )

            return msg_from_server
            #return json
        except Exception as e:
            logging.debug(f"{function_debug_symbol} {inspect.stack()[0][3]}: {e}")
            return e
