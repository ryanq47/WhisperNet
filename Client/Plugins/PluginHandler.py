'''
Handles plugin related things

'''

## will come back to this



import Plugins.native_SystemShell

class PluginHandler:
    ## Don't know how to autodetect these yet, so hardcoding in the meantime
    plugins = {
        "native_SystemShell": Plugins.native_SystemShell.SystemShellActions.SystemShellActions,
    }


    @staticmethod
    def _display_loaded():
        '''
        Prints out loaded modules
        '''

        '''
        create plugin dict

        for I in dict,
            if I._test_plugin() == True
                print("succes")
            else:
                print("warning, failure to load {errmsg}")
        
        '''

        for plugin_key, plugin_object in PluginHandler.plugins.items():
            if plugin_object._test_plugin():
                print(f"[*] {plugin_object.name} ({plugin_object.author}) Loaded Successfully")
            else:
                print(f"[!] Failed to load: '{plugin_object.name}'")

