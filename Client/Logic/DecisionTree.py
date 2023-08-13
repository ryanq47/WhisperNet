try:
    import logging
    import Data.JsonHandler
    import Comms.CommsHandler
    import Utils.PlatformData
    import Utils.AuthenticationHandler
    import Display.DisplayHandler
    #import Plugins.native_SystemShell.SystemShellActions
    import os
    import inspect
except Exception as e:
    print(f"[<Logic.DecisionTree.py>] Import Error: {e}")

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
            "reload": SystemDefaultActions._hot_reload,
            "systemshell": SystemDefaultActions._set_dir_system_shell,
            "home":SystemDefaultActions._set_dir_home_shell,
            "show platform data": SystemDefaultActions._show_platform_data,
            "connect to server": Utils.AuthenticationHandler.Server.get_server_to_connect_to,
            "show": Trees.prefix_show_tree,
            "cd <DIR>": SystemDefaultActions._cd_to_dir 
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

        ## hacky cd fix. Probably worth a look into a better solution for other commands that take arguments (if any)
        elif user_input[:2] == "cd":
            return SystemDefaultActions._cd_to_dir(cmd = user_input)

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
        'cd <TOOL DIR>': "cd" to the directory of the tool. Ex: 'cd home/systemshell'. !! Non valid paths cause errors dammit. run cd arg against current lsit of loaded plugins
        'systemshell': Spawns a propmt that passes commands to the local system
        'plugins':Shows loaded plugins [NOT IMPLEMENTED yet]. (devnote: just print the paths of all the plugins)
              """)
        
        return {"output_from_action":result, "dir":None, "dbg_code_source":inspect.currentframe().f_back}

    
    def _exit():
        exit("Exiting...")
        #no need to return here

    def _display_clear():
        os.system("cls") if Utils.PlatformData.Platform.os == "nt" else os.system("clear")
        return {"output_from_action": None, "dir":None, "dbg_code_source":inspect.currentframe().f_back}

    def _hot_reload():
        ## might be a circlular import
        '''try:
            import client
            SystemDefaultActions._display_clear()
            client.load_program()
        except Exception as e:
            logging.warning("[!] Hot-Reload failed. Please ctrl+C and re-launch")'''
        return {"output_from_action": "[*] Hot reload Not Implemented", "dir":None, "dbg_code_source":inspect.currentframe().f_back}


    def _show_platform_data():
        Display.DisplayHandler.Display.print_platform_data()

    def _set_dir_system_shell():
        '''
        A local TTY passthroguh. Not fully interactive at the moment

        at the moment this just retuns the "home/systemshell", which changes the directory to the shell dir
        '''

        return{"output_from_action": None, "dir":"home/systemshell"}

    def _set_dir_home_shell():
        '''
        A local TTY passthroguh. Not fully interactive at the moment

        at the moment this just retuns the "home/systemshell", which changes the directory to the shell dir
        '''
        return{"output_from_action": None, "dir":"home"}

    def _cd_to_dir(cmd = None):
        '''
        'CD's' you to where you want. Note, there is no checking that these are valid dir's, just a try/except
        
        '''
        try:
            ## Get second half of command, which SHOULD be the directory, and then strip any whitespace
            dir = (cmd.split()[1]).strip()
            return{"output_from_action": None, "dir":dir}
        
        except Exception as e:
            return{f"output_from_action": "Could not CD to directory. Error:{e}", "dir": None}





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