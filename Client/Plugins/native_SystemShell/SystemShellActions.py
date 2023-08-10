'''
System Shell Actions


'''
try:
    import subprocess
    import logging
    import inspect


except Exception as e:
    print(f"[<Plugins.native_SystemShell.SystemShellActions.py>] Import Error: {e}")


class SystemShellActions:
    path    = "Plugins.native_SystemShell.SystemShellActions.py"
    name    = "SystemShell"
    author  = "ryanq.47"
    '''
        some methods for doing certain actions within a tree. 
    
    '''
    def _display_help():
        help_menu = ("""Help Menu:\n
        'help'\t: Spawns this menu
        'home' or 'exit'\t: Exits the program
        'clear'\t: Clears the screen
        <Any Other command>'\t: Will get passed to whatever shell you are using (powershell, bash, etc) and return the results."
              """)
        return{"output_from_action":help_menu, "dir":None, "dbg_code_source":inspect.currentframe().f_back}

    def _run_command(command = None):
        command_results = SystemShellHandler.run_via_subprocess(command = command)
        return{"output_from_action":command_results, "dir":None, "dbg_code_source":inspect.currentframe().f_back}
    
    def _test_plugin():
        ## Teesting plugin
        pass
        '''try:
            import subprocess
            import logging
            return True
        except Exception as e:
            print(f"[<Plugins.native_SystemShell.SystemShellActions.py>] Import Error: {e}")
            return False'''



class SystemShellHandler:
    '''
    Performs Actions related to shell operations. Stored in this file, as it's directly realted to the SystemShellActions class
    
    '''

    @staticmethod
    def run_via_subprocess(command = None):
        '''
        Runs methods to gather required data for platform. Called with startup

        Currently gathers:
            OS Type (NT or Linux)
            
        Don't worry. This data is not saved, or sent anywhere. It's only used internally
        '''
        command_results = ""

        try:
            command_results = subprocess.getoutput(command)
        except Exception as e:
            logging.debug(f"[Utils.SystemShellHandler.SystemShell.run_via_subprocess ()] : {e}")
        
        return command_results
