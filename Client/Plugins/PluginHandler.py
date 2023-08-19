'''
Handles plugin related things

'''

## will come back to this

#import Plugins.native_SystemShell

class PluginHandler:
    ## Don't know how to autodetect these yet, so hardcoding in the meantime

    def __init__(self):
        self.loaded_plugins = {
            #"native_SystemShell": Plugins.native_SystemShell.SystemShellActions.SystemShellActions,
        }

    @staticmethod
    def _print_loaded_dirs(list_of_loaded_dirs):
        '''
        Prints out loaded modules' directories
        '''

        for dir in list_of_loaded_dirs:
            print(f"\t{dir}")

