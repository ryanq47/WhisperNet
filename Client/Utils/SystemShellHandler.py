'''
Runs shell commans. retuns them
'''
import os


class SystemShell:
    @staticmethod
    def run_via_os(command = None):
        '''
        Runs methods to gather required data for platform. Called with startup

        Currently gathers:
            OS Type (NT or Linux)
            
        Don't worry. This data is not saved, or sent anywhere. It's only used internally
        '''
        command_results = ""

        try:
            command_results = os.system(command)
            return command_results
        except Exception as e:
            print(f"[Utils.SystemShellHandler.SystemShell.run_via_os ()] : {e}")




