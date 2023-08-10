import logging
import Data.JsonHandler
import Comms.CommsHandler
import Utils.PlatformData
import Utils.AuthenticationHandler
import Display.DisplayHandler
import Plugins.native_SystemShell.SystemShellActions
import os
import inspect


class Trees:

    def home_tree(user_input = None):
        '''
        The decision tree for the user_inputs. if a command is meant for the server, it gets passed to the server from here
        '''

        ## no () here, it's looking for the class/object name itself, not to execute it
        dispatch = {
            "help": SystemDefaultActions._display_help,
            "exit": SystemDefaultActions._exit,
            "clear": SystemDefaultActions._display_clear,
            "systemshell": SystemDefaultActions._set_dir_system_shell,
            "home":SystemDefaultActions._set_dir_home_shell,
            "show platform data": SystemDefaultActions._show_platform_data,
            "connect to server": Utils.AuthenticationHandler.Server.get_server_to_connect_to,
            "show": Trees.prefix_show_tree
        }

        ## this can fail easily if input == ""
        '''
        Idea for returns:
            the current dir is returned from these, if not None << sticking with this for now. easy enoguht to switch to the other option

            or return a dict of current data? i.e. current dir, command results, etc
        
        '''
        action = dispatch.get((user_input.lower().split())[0])
        if action == Trees.prefix_show_tree:
            action(cmd = user_input)

        elif action:
            return action()
        else:
            return {"output_from_action":"Invalid command. Type 'help' for available commands.", "dir":None}

        '''
        #idea, just have 'show', and have it go into it's own tree for 'show' commands.
        Do this for all prefix commands (show, connect, etc)

        _platform_data()

        _servers()

        etc
        '''
    def server_tree():
        '''
        Sends commands to server, or packs other items
        
        '''
        pass

    
    def prefix_show_tree(cmd = None):
        '''
        Prefix tree. 
        
        '''

        dispatch = {
            "help": SystemDefaultActions._display_help,
            "platform data": SystemDefaultActions._display_help,
        }


        action = dispatch.get(cmd)

        if action:
            action()
        else:
            return {"output_from_action":"Invalid show command. Type 'help' for available commands.", "dir":None}

    
    def system_shell_tree(user_input = None):
        dispatch = {
            "help": Plugins.native_SystemShell.SystemShellActions.SystemShellActions._display_help,
            "home": SystemDefaultActions._set_dir_home_shell,
            "exit": SystemDefaultActions._set_dir_home_shell,
            "clear": SystemDefaultActions._display_clear
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
            ##returning the dict that's being passed back already
            return Plugins.native_SystemShell.SystemShellActions.SystemShellActions._run_command(command = user_input)

            #print("Invalid 'show' command. Type 'show help' for available commands.")

## move these to their own file

class SystemDefaultActions:
    """
    Actions to take based on the decision trees above

    naming:
        _prefix_whatitdoes/command
    """
    def _display_help():
        result = ("""Help Menu:\n
        'help'\t: Spawns this menu
        'exit'\t: Exits the program
        'clear' : Clears the screen
        'systemshell': Spawns a propmt that passes commands to the local system
        'plugins':Shows loaded plugins [NOT IMPLEMENTED yet]
              """)
        
        return {"output_from_action":result, "dir":None, "dbg_code_source":inspect.currentframe().f_back}

    
    def _exit():
        exit("Exiting...")
        #no need to return here

    def _display_clear():
        os.system("cls") if Utils.PlatformData.Platform.os == "nt" else os.system("clear")
        return {"output_from_action": None, "dir":None, "dbg_code_source":inspect.currentframe().f_back}


    def _show_platform_data():
        Display.DisplayHandler.Display.print_platform_data()

    def _set_dir_system_shell():
        '''
        A local TTY passthroguh. Not fully interactive at the moment

        at the moment this just retuns the "home/systemshell", which changes the directory to the shell dir
        '''

        return {"output_from_action": None, "dir":"home/systemshell"}

    def _set_dir_home_shell():
        '''
        A local TTY passthroguh. Not fully interactive at the moment

        at the moment this just retuns the "home/systemshell", which changes the directory to the shell dir
        '''
        return {"output_from_action": None, "dir":"home"}





'''
Parser notes

    input   :  'bob one two'
    list    :  ['bob', 'one', 'two']
    ID      :  AABBC12
    command :  reload file.exe


    ## breaking the parser:

    ## multiple spaces on input will (may...) break the command section. be careful with spaces lol

        input   :  '     bob one two'
        list    :  ['bob', 'one', 'two']
        ID      :  AABBC12
        command :  '     reload file.exe'


'''