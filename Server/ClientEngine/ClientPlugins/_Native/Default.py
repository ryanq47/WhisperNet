import inspect
class Actions:
    '''
        Action methods, called directly from the 'Tree' class. These are the methods for the actual commands listed from the help menu

        Returns(dict[output_from_action, dir, dbg_code_source]): All methods return this dict to the Tree class
    
    '''

    def _return_help():
        help_menu = ("""Server Help Menu:\n
        'help'\t: Spawns this menu
        'home' or 'exit'\t: Exits the program
        'clear'\t: Clears the screen
              """)
        return{"output_from_action":help_menu, "dir":None, "dbg_code_source":inspect.currentframe().f_back}
    
    def _my_method():

        ## do actions here,

        ## output = Handler.my_method()

        return{"output_from_action":"output", "dir":None, "dbg_code_source":inspect.currentframe().f_back}


class Handler:
    '''
    Handles Actions related to shell operations. Seperate from  'Actions', for flexibility & function re-use. Directly returns to the 'Action' class

    Returns (str): All methods return the results of the action the method performs
    
    '''

    @staticmethod
    def _my_method():
        ## Do stuff

        ## return results of action
        return "results"



'''
Try Excepts & logging:
use this:
    logging.debug(f"{function_debug_symbol} {inspect.stack()[0][3]}: {e}")




doc notes:

Tree:
    The main interaction class, aka the entry point

Actions:
    The methods that the Tree class maps to.

Handler:
    An interface for interacting with the WhisperNet 'libraries', or any custom ones you want to do.

    These are more meant for one off/specific calls, i.e. connect to a server, and return a socket. 

    Actions is meant for multiple Handler calls, such as: 
        Handler.conn_to_server()
        handler.create_msg_for_server()
        handler.send_msg_to_server()
        handler.recv_msg_to_server()

        return results of all of this





'''