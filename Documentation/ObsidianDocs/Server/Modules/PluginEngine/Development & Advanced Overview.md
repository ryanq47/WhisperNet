
I've tried my best to make plugins as easy to develop as possible. in `PluginEngine/Plugins` there is a file named `PluginTemplate.py`. This is the base plugin, and contains everything you need to create a plugin.






#### Maps & Addtl Docs
Here is a quick glance at how plugins are integrated into the project.

#### Base plugin
Each plugin inherits the "BasePlugin". 

The base plugin contains:
- the "Data" class instance
	- This holds relevant data that may be needed throughout the project. (Link To Docs)
- The "Flask" instance
	- Allows the plugins to add their own routes, and perform other flask operations

#### Error Handling
 See PluginTemplate.py


#### PluginLoader
The plugin loader loads plugins. It's located in server.py. 

For each plugin:
- An instance is created
- The "main" method is called for that instance
	- This method calls "register_routes()", which registers the plugin's respective routes in the flask app. 



![[Pasted image 20231001140536.png]]