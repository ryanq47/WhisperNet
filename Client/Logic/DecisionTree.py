import logging
import Data.JsonHandler
import Comms.CommsHandler
import Utils.PlatformData
import Utils.AuthenticationHandler
import Display.DisplayHandler
import Utils.SystemShellHandler
import os
from collections.abc import Mapping


class Trees:

    def home_tree(user_input = None):
        '''
        The decision tree for the user_inputs. if a command is meant for the server, it gets passed to the server from here
        '''

        ## no () here, it's looking for the class/object name itself, not to execute it
        dispatch = {
            "help": Actions._display_help,
            "exit": Actions._exit,
            "clear": Actions._display_clear,
            "systemshell": Actions._set_dir_system_shell,
            "home":Actions._set_dir_home_shell,
            "show platform data": Actions._show_platform_data,
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
            print("Invalid command. Type 'help' for available commands.")

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
            "help": Actions._display_help,
            "platform data": Actions._display_help,
        }


        action = dispatch.get(cmd)

        if action:
            action()
        else:
            print("Invalid 'show' command. Type 'show help' for available commands.")


        print(f"prefix, whole cmd: {cmd}")
    
    def system_shell_tree(cmd = None):
        dispatch = {
            "help": SystemShellActions._display_help,
            "home": Actions._set_dir_home_shell,
            "exit": Actions._set_dir_home_shell
        }


        action = dispatch.get(cmd)

        '''
        Due to the natuer of everything getting passed into the system shell, 
        only certain commands (i.e. help) are called via action(). eveerything else is passed
        directly to _run_command
        
        '''
        if action:
            return action()
        else:
            SystemShellActions._run_command(command = cmd)
            #print("Invalid 'show' command. Type 'show help' for available commands.")

## move these to their own file

class Actions:
    """
    Actions to take based on the decision trees above

    naming:
        _prefix_whatitdoes/command
    """
    def _display_help():
        print("""Help Menu:\n
        'help'\t: Spawns this menu
        'exit'\t: Exits the program
        'systemshell': Spawns a propmt that passes commands to the local system
              """)
    
    def _exit():
        exit("Exiting...")

    def _display_clear():
        os.system("cls") if Utils.PlatformData.Platform.os == "nt" else os.system("clear")

    def _show_platform_data():
        Display.DisplayHandler.Display.print_platform_data()

    def _set_dir_system_shell():
        '''
        A local TTY passthroguh. Not fully interactive at the moment

        at the moment this just retuns the "home/systemshell", which changes the directory to the shell dir
        '''
        return "home/systemshell"
        print('shell')
        pass
    def _set_dir_home_shell():
        '''
        A local TTY passthroguh. Not fully interactive at the moment

        at the moment this just retuns the "home/systemshell", which changes the directory to the shell dir
        '''
        return "home"

class SystemShellActions:
    '''
    Everythign here takes teh command arg, but not every method does something with it. 
    Rationle: easier to do this, than build in specific logic above in the system_shell_tree action() method
    
    '''
    def _display_help():
        print("Help Menu:\n\t'help'\t: Spawns this menu\n\t\'home' or 'exit': will take you to the home shell\n\t'<Any Other command>'\t: Will get passed to whatever shell you are using (powershell, bash, etc) and return the results.")


    def _run_command(command = None):
        Utils.SystemShellHandler.SystemShell.run_via_os(command = command)




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