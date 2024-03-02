# Plugins

Plugins are pieces of code that `plugin` to the CRS (or any flask app really, please steal this design if you want for your own projects). In the case of the CRS, the plugins are primarily model based, meaning they exist to interact with specific models. 

Plugins are great for modularity, as you can work exclusively on your "plugin", and as long as a few items are met, have it literally "plug in" to the project. Additionally, if one breaks, no biggie as it just gets skipped while the rest load. 

Ex:

 - C Plugin: 

    - interacts with a model tied to C

    - May have the following endpoints:

        - /api/model/c/detect-vulnerabilites

        - /api/model/c/fix-vulnerabilites

## Plugin Loader

Loads plugins from the `Model` folder. Each Subfolder contains a plugin, which is a template/framework class that gets loaded on the API startup. 

This function is currenly in the Api.py file, named `load_plugins`. It's a tad bit messy, with about 3 nested loops, and could use a rework, but functions as expected, so it's fine for now.

In a nutshell, the loader does the following:

 1. Finds the plugin (or in this case, `model`) directory
 2. Iterates over the folders in the directory
 3. in each folder, searches for a py file.
 4. Imports that Py file
 5. Pulls needed items from Py file & Info class (Class name, Plugin Name, Plugin Path, etc)
 6. Takes the Class of the plugin, initializes it, passes in the `app` (the flask app instance), and runs the `main` method.
 7. If the `main` method is setup correctly (see example below), it should register all of its routes with the flask app, and start.

## Plugin Code Template

The following is a bare minumum of what a plugin should contain, and what it needs to successfully work: 

```
from Utils.Logger import LoggingSingleton

################################################
# Info class
################################################
'''Info class
Fill in your info for the plugin here. This is defined near the top, so it's accessible
by anything that may need it.
'''
class Info:
    name    = "ExamplePlugin"
    author  = "author_name"
    endpoint = "/api/model/endpoint"
    classname = "ClassName"

class ClassName():
    def __init__(self, app):
        self.logger = LoggingSingleton.get_logger()
        self.app = app

################################################
# Main Stuff
################################################

    # main function for the plugin, gets called by the plugin loader
    def main(self):
        '''
        Main function/entry point for the plugin. Called when plugin is loaded
        '''
        self.logger.debug(f"Loading {Info.name}")
        self._register_routes()

    ## Put all the routes here.
    def _register_routes(self):
        self.app.route(f'{Info.endpoint}', methods = ["GET"])(self.model_endpoint)
        self.app.route(f'{Info.endpoint}/predict', methods = ["POST"])(self.model_predict)

    # note, change/delete this method. Multiple methods accross the project with the same name & registered routes will cause issues
    def example_endpoint(self):
        '''
        example endpoint
        
        '''
        # do whatever you want here, call other funcs/classes, etc. Just make sure 
        # it returns a value if it's mapped to an endpoint
        
        # Calculate last digit of pi
        # Find the meaning of life
        
        return jsonify({"status":f"Plugin {Info.name} successfully started"})

```