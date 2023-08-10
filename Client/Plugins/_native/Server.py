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

    ## Do not change the name of 'tree_input', it's used while  importing this Plugin
    def tree_input(user_input = None):
        dispatch = {
            ## Default commands...
            "help": Actions._display_help,
            "home": Logic.DecisionTree.SystemDefaultActions._set_dir_home_shell,
            "exit": Logic.DecisionTree.SystemDefaultActions._set_dir_home_shell,
            "clear": Logic.DecisionTree.SystemDefaultActions._display_clear

            ## add yours here... no (), as we are just passing the object, not running it 
            #"mycommand":Actions._test_action
        }


        action = dispatch.get(user_input)

        '''
        Due to the natuer of everything getting passed into the system shell, 
        only certain commands (i.e. help) are called via action(). eveerything else is passed
        directly to _run_command
        
        '''
        if action:
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
        ## do actions here,

        ## Handler.my_method()

        return{"output_from_action":"Start Server", "dir":None, "dbg_code_source":inspect.currentframe().f_back}
    
    def _connect_to_server():
        ## do actions here,

        ## Authentication stuff (cookies, etc)
        ## Need to find a way to store the cookie

        ## Handler.my_method()

        return{"output_from_action":"Connect To Server", "dir":None, "dbg_code_source":inspect.currentframe().f_back}


class Handler:
    '''
    Handles Actions related to shell operations. Seperate from  'Actions', for flexibility & function re-use. Directly returns to the 'Action' class

    Returns (str): All methods return the results of the action the method performs
    
    '''

    @staticmethod
    def my_method(command = None):
        ## Do actions here...

        ## return results of action
        return "command_results"