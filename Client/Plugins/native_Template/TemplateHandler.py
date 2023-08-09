'''
Template for custom plugin handlers
'''

try:
    ## just have to import it, everything else is taken care of in client.py
    import logging

except Exception as e:
    ##print this error, as there's a chance logging is the one that failed, or that it doesnt get loaded.
    print(f"[<PluginPath>] Import Error: {e}")


'''
Class info:

you *can* do a standard class if you want, but I stick to static classes for these to knock down the complexity

'''
class CLASSNAME:
    @staticmethod
    def method(command = None):
        '''
        A method to call

        '''
        command_results = ""

        try:
            command_results = "Do Action Here"
            
        except Exception as e:
            logging.debug(f"[Utils.SystemShellHandler.SystemShell.run_via_os ()] : {e}")

        ## returning the output of the command
        return command_results





