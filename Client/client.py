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

    def user_loop(self):
        '''
        The main loop. This takes the user input, and throws it at the correct decision tree
        based on the 'current directory'
        '''
        while True:

            user_input = input(f"\n{self.current_dir} >> ")

            if self.current_dir == "home":
                results = Logic.DecisionTree.Trees.home_tree(user_input = user_input)

                if results != None:
                    self.current_dir = results
                '''
                if results of command == dir
                
                or a dir update somehow
                '''
                ## decision tree local
                ...

            ## Ideally I'd like the server name to be there, not sure how to pull that off yet
            elif self.current_dir == "home/server":
                print("server_decision_tree")
                ...

            elif self.current_dir == "home/systemshell":
                results = Logic.DecisionTree.Trees.system_shell_tree(cmd = user_input)
                
                output  = results["output_from_action"]
                dir     = results["dir"]

                print(output)
                #logging.debug(f"results of command: {output}, Results of Dir: {dir}")

                if dir != None:
                    self.current_dir = dir

    def startup_tasks(self):
        #Plugins.PluginHandler.PluginHandler._display_loaded()
        Utils.PlatformData.Platform.gather_data()

    def dynamic_user_loop(self):
        '''
        Dynamically handles the plugins, the mapping to their trees,  etc.no if else trees anymore :)
        
        '''

        ## hardcoded paths. The goal is to have these, then some dynamically pulled in as well
        plugin_tree_dict = {
            "home": Logic.DecisionTree.Trees.home_tree
        }

        '''
        ## adding plugins from file to plugin_tree_dict
        for i in list_of_plugins:
            import i #<< this one will be tough
            plugin_tree_dict["plugin.path"]
        
        '''

        with open('plugin_list.txt', 'r') as file:
            plugin_names = file.read().splitlines()

        # Dynamically import the modules, needed to grab the corrent data from each one
        for plugin_name in plugin_names:
            try:
                plugin = importlib.import_module(plugin_name)
                #print(plugin.Info.name)

                ## In english: Take the plugin "fake" in tool directory, use that as the key. The value is then the plugin.Tree.tree_input method
                ## Note, the command must still be in home tree for now, working on a fix to have the commands added dynamically
                plugin_tree_dict[plugin.Info.dir] = plugin.Tree.tree_input

                logging.debug(f"Plugin {plugin_name} imported successfully.")
            except ImportError:
                print(f"Failed to import module {plugin_name}.")


        while True:

            user_input = input(f"\n{self.current_dir} >> ")

            ## Actually execute said plugintree based off of self.current_dir
            action = plugin_tree_dict.get(self.current_dir)
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





try:
    Display.DisplayHandler.Display.print_startup()
    c = Client()
    c.startup_tasks()
    c.dynamic_user_loop()
except KeyboardInterrupt:
    logging.debug("\nExiting...")
except Exception as e:
    logging.debug(f"Unkown error: {e}")