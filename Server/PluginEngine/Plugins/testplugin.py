'''


'''
#from server import ControlServer
from PluginEngine.Plugins.baseplugin import BasePlugin

class Info:
    name    = "plugin_name"
    author  = "plugin_author"
    endpoint = "plugin_endpoint"


## Static or not?
class PluginClass(BasePlugin):

    def main():
        '''
        Main function/entry point for the plugin.
        
        '''

        ## does stuff

    def register_routes(self):
        self.app.route('/plugin2')(self.plugin2_function)
    

    def plugin2_function(self):
        return "plugin online"
