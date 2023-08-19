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
parser.add_argument('--debug','-d', help="The port to connect to", action="store_false")

args = parser.parse_args()
#ip = args.ip
#port = int(args.port)
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
        self.plugin_dir_list = []

    '''
    INitial prompt input

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

    def dynamic_user_loop(self):
        '''
        Dynamically handles the plugins, the mapping to their trees,  etc.no if else trees anymore :)
        
        '''

        ## this could go in the startup area at the bottom as well
        self.dynamic_plugin_load()
        ## Need to append this in here for some reason, it's getting overwritten if dclared  in __init__ for some reason
        self.plugin_dir_list.append("home")

        while True:

            user_input = input(f"\n{self.current_dir} >> ")

            ## Valid current Dir check
            #print(self.current_dir)
            #print(self.plugin_dir_list)
            if self.current_dir not in self.plugin_dir_list:
                logging.warning(f"Directory '{self.current_dir}' does not exist! Perhaps a typo, or a failed plugin? run with -d for the plugin loading sequence")
                self.current_dir = "home"
                continue

            ## Actually execute said plugintree based off of self.current_dir
            action = self.plugin_tree_dict.get(self.current_dir)
            logging.debug(f"Tree being accessed: {action}")
            # this runs the tree (as specified in pligin_tree_dict) and passes it the command arg
            results = action(user_input = user_input)

            try:
                output  = results["output_from_action"]
                dir     = results["dir"]

                logging.debug(f"results: {results}")

                if output != None:
                    print(output)

                if dir != None:
                    self.current_dir = dir
            
            ##incase I forget to put a  return, or a plugin is  misbehaving
            except Exception as e:
                logging.warning(f"Error with results of command: {e}")

    def dynamic_plugin_load(self):
        '''
        Dynamically loads plugins,and adds to the current plugin dict
        
        '''

        print("[*] Loading plugins...")
        ## hardcoded paths. Only the home_tree is hardcoded (for now), the rest are dynamically loaded
        self.plugin_tree_dict = {
            "home": Logic.DecisionTree.Trees.home_tree
        }
        self.plugin_dir_list = []

        ## Need to add sys_path before this
        with open('Plugins/plugin_list.txt', 'r') as file:
            plugin_names = file.read().splitlines()

        # Dynamically import the modules, needed to grab the corrent data from each one
        for plugin_name in plugin_names:
            try:                
                ## If a static class...
                if plugin_name[:8] == "[static]":
                    plugin = importlib.import_module(plugin_name[8:])

                    ## pull any needed data
                    self.plugin_dir_list.append(plugin.Info.dir)

                    ## In english: Take the plugin "fake" in tool directory, use that as the key. The value is then the plugin.Tree.tree_input method
                    ## Note, the command must still be added in home tree description for now, working on a fix to have the commands added dynamically
                    self.plugin_tree_dict[plugin.Info.dir] = plugin.Tree.tree_input

                ## if not a static class...
                else:
                    ## Import plugin
                    plugin = importlib.import_module(plugin_name)
                    
                    ## pull any needed data
                    self.plugin_dir_list.append(plugin.Info.dir)

                    ## create class instance
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

        #print(self.plugin_dir_list)
        Plugins.PluginHandler.PluginHandler._print_loaded_dirs(self.plugin_dir_list)


def load_program():
    try:
        Display.DisplayHandler.Display.print_startup()
        c = Client()
        c.startup_tasks()
        c.dynamic_user_loop()
    except KeyboardInterrupt:
        logging.debug("\nExiting...")
    except Exception as e:
        logging.debug(f"Unkown error: {e}")

if __name__ == "__main__":
    load_program()