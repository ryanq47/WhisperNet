'''


'''
## Don't remove me. This is the base plugin class, parent to all classes for plugins.
from PluginEngine.Plugins.baseplugin import BasePlugin


'''
## If you want JWT tokens on your endpoint, uncomment the lines below

Then, add '@jwt_required' decorator to your function. Boom, you now need an account/authorization to access
this endpoint.

'''
#from flask_jwt_extended import jwt_required



class Info:
    name    = "PluginTemplate"
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
        self.app.route(f'/{Info.name}')(self.plugin_function)
    
    def plugin_function(self):
        startup_message = (f"Plugin Name: {Info.name}\n \
        Plugin Author: {Info.author}\n \
        Plugin Endpoint: {Info.endpoint}\n")

        return startup_message
