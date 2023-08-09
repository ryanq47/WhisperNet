'''
Runs specific commands for the os. It is a handler, so it returns all data


'''
try:
    import subprocess
    import logging
except Exception as e:
    print(f"[Plugins.native_SystemShell.SystemShellHandler.py] Import Error: {e}")


class SystemShell:
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





