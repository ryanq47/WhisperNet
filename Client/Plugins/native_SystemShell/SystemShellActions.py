'''
System Shell Actions


'''
try:
    import Plugins.native_SystemShell.SystemShellHandler

except Exception as e:
    print(f"[<Plugins.native_SystemShell.SystemShellActions.py>] Import Error: {e}")


class SystemShellActions:
    '''
    Everythign here takes teh command arg, but not every method does something with it. 
    Rationle: easier to do this, than build in specific logic above in the system_shell_tree action() method
    
    '''
    def _display_help():
        help_menu = ("""Help Menu:\n
        'help'\t: Spawns this menu
        'home' or 'exit'\t: Exits the program
        'clear'\t: Clears the screen
        <Any Other command>'\t: Will get passed to whatever shell you are using (powershell, bash, etc) and return the results."
              """)
        return{"output_from_action":help_menu, "dir":None}

    def _run_command(command = None):
        command_results = Plugins.native_SystemShell.SystemShellHandler.SystemShell.run_via_os(command = command)
        return{"output_from_action":command_results, "dir":None}
