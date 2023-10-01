'''
Hey! This is the plugin template. You can create your own plugins with this template.

The first section is plugin options, aimed at making some harder settings a bit easier to configure.

Throw a description of your plugin here as well:
################################################
<desc> Plugin makes the world go around.
################################################


Last but not least, fill in the "Info" class with the proper fields. 
'''
## Don't remove me. This is the base plugin class, parent to all classes for plugins.
from PluginEngine.Plugins.BasePlugin import BasePlugin


''' Authentication
## If you want JWT tokens on your endpoint, uncomment the lines below

Then, add '@jwt_required' decorator to your functions you want protected. 

Boom, you now need an account/authorization to access this endpoint.

'''
from flask_jwt_extended import jwt_required

from flask import Flask, jsonify, request, send_from_directory, render_template, Response
import logging
import os

class Info:
    name    = "FlaskAPIListener"
    author  = "ryanq.47"
    endpoint = "/listener"


## Inherets BasePlugin
class FlaskAPIListener(BasePlugin):
    def main(self):
        '''
        Main function/entry point for the plugin.
        
        '''
        print(f"{self.print_symbol} Loading {Info.name}")
        self.register_routes()

        ## does stuff

    ## Put all the routes here.
    def register_routes(self):
        ## Base Endpoint
        self.app.route(f"/{Info.endpoint}", methods=["POST", "GET"])(self._plugin_function)
    

    ## Define your plugin functions here.

    def _plugin_function(self):
        startup_message = (f"Plugin is up!<br>Plugin Name: {Info.name}<br> \
        Plugin Author: {Info.author}<br> \
        Plugin Endpoint: {Info.endpoint}<br>")

        return startup_message
    
