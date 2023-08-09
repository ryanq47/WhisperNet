'''
Actions. This calls the respective handler, which returns data.


'''
try:
    ## just have to import it, everything else is taken care of in client.py
    import logging
    
    ## Make sure to import your Handler that actually performs the actions, and returns them
    import Plugins.native_SystemShell.SystemShellHandler

except Exception as e:
    ##print this error, as there's a chance logging is the one that failed, or that it doesnt get loaded.
    print(f"[<PluginPath>] Import Error: {e}")



class SystemShellActions:
    '''
    Everythign here takes teh command arg, but not every method does something with it. 
    Rationle: easier to do this, than build in specific logic above in the system_shell_tree action() method
    
    '''
    def _display_help():
        result = ("""Help Menu:\n
        'help'\t: Spawns this menu
        'home' or 'exit'\t: Exits the program
        'clear'\t: Clears the screen
        <Any Other command>'\t: Will get passed to whatever shell you are using (powershell, bash, etc) and return the results."
              """)
        return {"output_from_action":result, "dir":None}

    def _run_command(command = None):
        result = Plugins.native_SystemShell.SystemShellHandler.SystemShell.run_via_os(command = command)

        ## returns a dict, with the result of the commandm, and the directory to change to if applicable. This value is returned all the way back to client.py, where it is parsed/displayed
        return {"output_from_action":result, "dir":None}

