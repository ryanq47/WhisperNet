
I've tried my best to make plugins as easy to develop as possible. in `PluginEngine/Plugins/PluginTemplate` there is a file named `PluginTemplate.py`. This is the base plugin, and contains everything you need to create a plugin.

Each plugin has it's own directory that must be named the same as the plugin name. This is so plugins can be in their own folder, and was the simplest way to implement in the loader

Ex:
```
Server/PluginEngine/Plugins/PluginTemplate/PluginTemplate.py


├── BasePlugin.py
├── FlaskAPIListenerPlugin
│   ├── FlaskAPIListenerPlugin.py

├── PluginTemplate
│   ├── PluginTemplate.py

├── UserPlugin
│   ├── UserPlugin.py


```




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


Plugin setup alone:
![[Pasted image 20231001140536.png]]

Plugin setup + Extended tie in to project
![[Pasted image 20231001150030.png]]




#### Plugins using Jinja/dynamic loading:
There is a small catch when creating these plugins. You'll have to store your assets (css, HTML, and images) at Server/templates and Server/static respectively. I can't find a way to make flask load templates from different paths, so this is the next best solution. Note, you will have to name your assets something related to your plugin, such as "myplugin-index.html"

Additionally, this makes these plugins not as easy to drag & drop into your server instance... which kinda sucks.

here's the file structure:
```
ryan@DESKTOP-FDIVIMF:/mnt/c/Users/Ryan/Documents/GitHub/logec-suite/Server/templates$ tree
.
├── webserverfrontendplugin-dashboard.html
└── webserverfrontendplugin-index.html

0 directories, 2 files
ryan@DESKTOP-FDIVIMF:/mnt/c/Users/Ryan/Documents/GitHub/logec-suite/Server/templates$ cd ../static/; tree
.
├── css
│   └── webserverfrontend-styles.css
└── images
    ├── fp-dots.png
    ├── fp-dots2.png
    ├── login.gif
    └── login2.gif

```