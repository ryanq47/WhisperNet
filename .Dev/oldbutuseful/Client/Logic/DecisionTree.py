try:
    import logging
    import Data.JsonHandler
    import Comms.CommsHandler    
    import os
    import inspect
    #import Plugins.native_SystemShell.SystemShellActions
    import Utils.PlatformData
    import Utils.AuthenticationHandler
    import Display.DisplayHandler
except Exception as e:
    print(f"[<Logic.DecisionTree.py>] Import Error: {e}")

## STATIC
class Trees:

    @staticmethod
    def home_tree(user_input=None, data_manager=None):
        '''
        Decision tree for processing user inputs. If a command is meant for the server,
        it gets passed to the server from here.
        '''

        # Initialize the class to provide easier data access
        sda_class = SystemDefaultActions(
            command=user_input,
            data_manager=data_manager
        )

        # Mapping of user commands to corresponding methods
        dispatch = {
            "help": sda_class._display_help,
            "exit": sda_class._exit,
            "clear": sda_class._display_clear,
            "reload": sda_class._hot_reload,
            "home": sda_class._set_dir_home_shell,
            "plugins": sda_class._show_plugins,
            "show platform data": sda_class._show_platform_data,
            "connect to server": Utils.AuthenticationHandler.Server.get_server_to_connect_to,
            "cd <DIR>": sda_class._cd_to_dir
        }

        # Handle different actions based on user input
        action = dispatch.get((user_input.lower().split())[0])
        if user_input.startswith("cd"):
            return sda_class._cd_to_dir(user_input=user_input)
        elif action:
            return action()
        else:
            return {"output_from_action": "Invalid command. Type 'help' for available commands.", "dir": None}

class SystemDefaultActions:
    """
    Actions to take based on the decision trees above. These methods are meant to be a set of wrappers for
    different items throughout the program.

    For example, in your plugin, you can call 'Logic.DecisionTree.SystemDefaultActions._display_clear()' to clear the display

    Static methods:
        Some methods do not need class data, so they are marked with @staticmethod.
        These can be called from sub classes in plugins.

    Naming convention:
        _prefix_what_it_does/command
    """
    def __init__(self, data_manager=None, command=None):
        self.data_manager = data_manager
        self.command = command

    @staticmethod
    def _display_help():
        result = """Help Menu:
        'help'        : Display this menu
        'exit'        : Exit the program
        'clear'       : Clear the screen
        'cd <TOOL DIR>': Change directory to specified tool directory
        'plugins'     : Show loaded plugins
              """
        return {"output_from_action": result, "dir": None, "dbg_code_source": inspect.currentframe().f_back}

    ## == Static methods == #
    @staticmethod
    def _exit():
        exit("Exiting...")

    @staticmethod
    def _display_clear():
        os.system("cls") if Utils.PlatformData.Platform.os == "nt" else os.system("clear")
        return {"output_from_action": None, "dir": None, "dbg_code_source": inspect.currentframe().f_back}

    @staticmethod
    def _cd_to_dir(user_input = None):
        '''
            user_input: The raw user input, which is parsed for the correct directory:
                dir = (user_input.split()[1]).strip()
        '''
        try:
            # Get the second part of the command (directory), stripping whitespace
            dir = (user_input.split()[1]).strip()
            return {"output_from_action": None, "dir": dir}
        except Exception as e:
            return {"output_from_action": f"Could not change directory. Error: {e}", "dir": None}

    # this only exists so it's easier to get to the home directory. every other directory has to use CD. 
    @staticmethod
    def _set_dir_home_shell():
        return {"output_from_action": None, "dir": "home"}

    ## == The rest of the methods are not static, and they require class data to operate == ##
    def _hot_reload(self):
        return {"output_from_action": "[*] Hot reload Not Implemented", "dir": None, "dbg_code_source": inspect.currentframe().f_back}

    def _show_platform_data(self):
        Display.DisplayHandler.Display.print_platform_data()

    def _show_plugins(self):
        formatted_plugin_dirs = ""
        for plugin_dir in self.data_manager.loaded_plugins_directory:
            formatted_plugin_dirs += f"[*] <name> {plugin_dir} \t\t - <short desc> \n"
            #"[*] <name> " + plugin_dir + "\n"
        return {"output_from_action": f"{formatted_plugin_dirs}", "dir": None, "dbg_code_source": inspect.currentframe().f_back}



# Parser notes...
