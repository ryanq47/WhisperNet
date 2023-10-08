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
    Stores data for access by non static classes. Kind of a weird implementation
    
    '''
    ## I hate that this exists. It's kind of dumb and hacky, but I don't have a better way to store data for static classes.
    ## In a nutshell, Tree is not static, but Actions and Handler are. With the way dispatch is set up, and there being mulieple server commands, it makes it tough to 
    ## pass the cookie via argument, so this is the best thing I can think of without re-doing it.

    # on the plus side it mgiht elimanate the need for normal classes
    cookie = None
    socket = None

class Tree:
    '''
    The 'Tree' class. It's job is to control the input that the user gives, call the respective methods, and return the results back to the dynamic_user_loop, which prints it onscreen
    
    Returns(dict[output_from_action, dir, dbg_code_source]): This is essentially passing on the 'return' from the Actions class
    '''


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

        }

        action = dispatch.get(user_input)

        if action:
            return action()
        else:
            return{"output_from_action":"Invalid command, please type 'help' for help", "dir":None, "dbg_code_source":inspect.currentframe().f_back}



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