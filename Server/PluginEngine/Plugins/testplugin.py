'''


'''
#from server import ControlServer
from PluginEngine.Plugins.baseplugin import BasePlugin


'''
## If you want JWT tokens on your endpoint, uncomment the lines below


'''
#from flask_jwt_extended import jwt_required



class Info:
    name    = "Plugin Template"
    author  = "Plugin Author"
    endpoint = "Plugin Endpoint"


## Inherets BasePlugin
class PluginClass(BasePlugin):
    def main(self):
        '''
        Main function/entry point for the plugin.
        
        '''

        ## does stuff

    ## Put all the routes here.
    def register_routes(self):
        self.app.route('/plugin')(self.plugin_function)
    
    def plugin_function(self):
        return Info.name
