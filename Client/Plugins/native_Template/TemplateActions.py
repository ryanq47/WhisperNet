'''
Actions. This calls the respective handler, which returns data.


'''
try:
    ## just have to import it, everything else is taken care of in client.py
    import logging
    

except Exception as e:
    ##print this error, as there's a chance logging is the one that failed, or that it doesnt get loaded.
    print(f"[<PluginPath>] Import Error: {e}")



class SystemShellActions:
    ## used for loading info
    name = "NameHere"
    author = "Author Here"
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


'''
Any functional actions you may want to do. These are handler classes, so they RETURN data. They can be called/used from anywhere if imported, and that flexibility is 
why they are a seperate class from the above class (the XXActions class). 

For example, lets this class contains a method that retrieves the hostanme of the device, called _get_hostname.
you would do: 
    import Plugins.native_Template.CLASSNAME

    ## remember, this returns a value
    print(Plugins.native_Template.CLASSNAMEHANDLER._get_hostname())
    


Class info:

you *can* do a standard class if you want, but I stick to static classes for these to knock down the complexity

'''
class CLASSNAMEHANDLER:
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
