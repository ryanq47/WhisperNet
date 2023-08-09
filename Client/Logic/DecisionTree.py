import logging
import Data.JsonHandler
import Comms.CommsHandler
import Utils.PlatformData
import Utils.AuthenticationHandler
import Display.DisplayHandler
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
            "show platform data": Actions._show_platform_data,
            "connect to server": Utils.AuthenticationHandler.Server.get_server_to_connect_to,
            "show": Trees.prefix_show_tree
        }

        ## this can fail easily if input == ""
        action = dispatch.get((user_input.lower().split())[0])
        if action == Trees.prefix_show_tree:
            action(cmd = user_input)

        elif action:
            action()
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

## move these to their own file

class Actions:
    """
    Actions to take based on the decision trees above

    naming:
        _prefix_whatitdoes/command
    """
    def _display_help():
        print("Help Menu:\n\t'help'\t: Spawns this menu\n\t'exit'\t: Exits the program")
    
    def _exit():
        exit("Exiting...")

    def _display_clear():
        os.system("cls") if Utils.PlatformData.Platform.os == "nt" else os.system("clear")

    def _show_platform_data():
        Display.DisplayHandler.Display.print_platform_data()







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