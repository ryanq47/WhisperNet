#!/usr/bin/python3
try:
    import argparse
    import logging
    import importlib

    import Logic.DecisionTree
    import Utils.AuthenticationHandler
    import Comms.CommsHandler
    import Display.DisplayHandler
    import Utils.PlatformData
    import Plugins.PluginHandler

except Exception as e:
    print(f"[client.py] Import Error: {e}")
    exit()

parser = argparse.ArgumentParser()
## nuke these 2
parser.add_argument('--ip', help="The IP to connect to", required=False)
parser.add_argument('--port', help="The port to connect to", required=False)
parser.add_argument('--debug','-d', help="Enable debugging output", action="store_false")

args = parser.parse_args()
debug = args.debug

"""
Here's the global Debug + Logging settings. 
Global Debug logging.debug to screen will be a setting in the future
"""
if not debug:
    print("Debugging enabled")
    global_debug = True
else:
    global_debug = False

##Reference: https://realpython.com/python-logging/
logging.basicConfig(level=logging.DEBUG)
## Change the path to the system path + a log folder/file somewhere
logging.basicConfig(filename='client.log', filemode='a', format='%(asctime)s - %(levelname)s - %(message)s', force=True, datefmt='%Y-%m-%d %H:%M:%S')
if global_debug:
    logging.getLogger().addHandler(logging.StreamHandler())

class Client:
    def __init__(self):
        self.cookie = None
        ## the server to conenct to
        self.server = None #[str, ip]
        self.current_dir = "home"
        self.plugin_tree_dict = {}
        self.plugin_handler_class = None
        self.data_manager = None

    '''
    Initial prompt input

    multiple trees:
        server_decision_tree
        client_decision_tree (for local commands)

        fake file struct?

        home> (if self.current_dir == home, use local decision tree)

        home/server> (if self.current_dir == server, use server_decision_tree)

        ## this one will take some extra work, as multiple clients, etc can be a pain
        home/server/client> (no idea for this one, maybe later, or just stick with the server being the deepest you can go for now.
                            actually, just use json, and prepack it with the client's ID for msg_to
        )

        Whisper>
        Whisper/127.0.0.1:80>client_127001_abcd>
    '''
    def startup_tasks(self):
        #Plugins.PluginHandler.PluginHandler._display_loaded()
        Utils.PlatformData.Platform.gather_data()
        ## init data manager class
        self.data_manager = DataManager()

    def dynamic_user_loop(self):
        '''
        Dynamically handles the plugins, the mapping to their trees,  etc. No if-else trees anymore :)
        '''
        ## this could go in the startup area at the bottom as well
        self.dynamic_plugin_load()
        ## appending 'home' to the list of plugins. Need to do this, otherwise, it's seen as an invalid directory
        self.data_manager.loaded_plugins_directory.append("home")

        while True:
            user_input = input(f"\n{self.current_dir} >> ")

            ## Valid current Dir check
            if self.current_dir not in self.data_manager.loaded_plugins_directory:
                logging.warning(f"Directory '{self.current_dir}' does not exist! Perhaps a typo, or a failed plugin? Run with -d for the plugin loading sequence")
                self.current_dir = "home"
                continue

            ## Actually execute said plugin tree based on self.current_dir
            action = self.plugin_tree_dict.get(self.current_dir)
            logging.debug(f"Tree being accessed: {action}")
            # This runs the tree (as specified in plugin_tree_dict) and passes it the command arg
            results = action(user_input=user_input, data_manager=self.data_manager)

            ## handling results of actions
            try:
                output = results["output_from_action"]
                dir = results["dir"]

                logging.debug(f"results: {results}")

                if output != None:
                    print(output)

                if dir != None:
                    self.current_dir = dir
            
            ## In case I forget to put a  return, or a plugin is misbehaving
            except Exception as e:
                logging.warning(f"Error with results of command: {e}")

    def dynamic_plugin_load(self):
        '''
        Dynamically loads plugins and adds to the current plugin dict
        '''
        print("[*] Loading plugins...")
        ## hardcoded paths. Only the home_tree is hardcoded (for now), the rest are dynamically loaded
        self.plugin_tree_dict = {
            "home": Logic.DecisionTree.Trees.home_tree
        }

        ## Need to add sys_path before this
        with open('Plugins/plugin_list.txt', 'r') as file:
            plugin_names = file.read().splitlines()

        # Dynamically import the modules, needed to grab the correct data from each one
        for plugin_name in plugin_names:
            try:                
                ## If a static class...
                if plugin_name[:8] == "[static]":
                    plugin = importlib.import_module(plugin_name[8:])
                    ## pull any needed data
                    ## add plugin directory to the valid directory list
                    self.data_manager.loaded_plugins_directory.append(plugin.Info.dir)
                    ## In English: Take the plugin "fake" in the tool directory, use that as the key. The value is then the plugin.Tree.tree_input method
                    ## Note, the command must still be added in the home tree description for now, working on a fix to have the commands added dynamically
                    self.plugin_tree_dict[plugin.Info.dir] = plugin.Tree.tree_input
                ## if not a static class...
                else:
                    ## Import plugin
                    plugin = importlib.import_module(plugin_name)
                    ## pull any needed data
                    self.data_manager.loaded_plugins_directory.append(plugin.Info.dir)
                    ## create a class instance
                    plugin_instance = plugin.Tree()
                    self.plugin_tree_dict[plugin.Info.dir] = plugin_instance.tree_input

                logging.debug(f"Plugin {plugin_name} imported successfully.")
            except ImportError as ie:
                logging.warning(f"Failed to import module '{plugin_name}'.")
                logging.debug(f"{plugin_name} Error message: {ie}")
            except Exception as e:
                logging.warning(f"Failed to import module '{plugin_name}'.")
                logging.debug(f"{plugin_name} Error message: {e}")

        ## Need a way to get the paths of all loaded plugins, to 1) verify that the dir the user goes to is correct, and 2) be able to display loaded plugins
        ## Creating plugin_handler_class to handle the current plugin data
        #self.plugin_handler_class = Plugins.PluginHandler.PluginHandler(self.plugin_tree_dict)
        #self.plugin_handler_class._display_loaded()

        Plugins.PluginHandler.PluginHandler._print_loaded_dirs(self.data_manager.loaded_plugins_directory)

## singleton test
class DataManager:
    '''
    Singleton to hold data the progam needs. 

    current objects:
        loaded_plugins_directory = Holds all the paths/directories of the loaded plugins

    Currently using multiple attributes instead of one dict. That may come back to bite me later
    '''
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(DataManager, cls).__new__(cls)
            #cls._instance.data = {}  # Store your shared data here -- may utilize in future
            ## Holds loaded plugins
            cls._instance.loaded_plugins_directory = []
        return cls._instance
    
def load_program():
    try:
        Display.DisplayHandler.Display.print_startup()
        c = Client()
        c.startup_tasks()
        c.dynamic_user_loop()
    except KeyboardInterrupt:
        logging.debug("\nExiting...")
    except Exception as e:
        logging.debug(f"Unknown error: {e}")

if __name__ == "__main__":
    load_program()

