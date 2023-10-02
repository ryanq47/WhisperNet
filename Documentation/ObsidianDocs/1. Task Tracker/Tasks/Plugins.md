---
SCOPE: Whole Project - left off
TASKTYPE: Refactor/Reimplement
MODULE: All
ESTTIMETOIMPLEMENT: 3 Hours
STATUS: In Progress - nearly completed
PRIORITY: High
DUE: DATE
---


## Quick Description
Re-implementing plugins. Use logic form original server. need to think out about how to implement this.

## Possible Solutions/Plan
Key goals:


- Each plugin will have a dedicated URL. This will be it's "root" URL. Communication will be done from this endpoint (SubEndpoints sich as /plugin/subendpoint may be viable in the future. would require much more work)
	- Ex, FlaskAPI listener plugin is at /list

- Each plugin will be dynamically loaded. This logic already exists in the client code, just needs to be ported

- Each plugin will have a "template" as stated below. This allows the server to grab the correct info when loading said plugin

```
## Maybe DICTify this?
# hardcoded values
class Info:
    name    = "FlaskAPI-Listener"
    author  = "ryanq.47"
    endpoint= "/listener01"


class PLUGIN:

	def func1():


```


Current thought: For the listeners, there are a couple parts. The "plugin" that lives on the server, and the part that actually deployed (aka the listener in this case). The plugin on the server is the part that comms with the one in the wild. 

At the moment, it's easiest/the most universal to spin the plugins up as docker containers, and make them use HTTP comms, even if "local"

Another idea, come up with a "base" template for the hosted/external plugins. See attached img

For example:

```
Listener01 is at 199.0.0.50 on Azure

Server01 is at 177.0.0.50 and is the control server

Listener01 talks to the server at 177.0.0.50/listeners/listener01

Listener01 is the listener itself, and it talks to the server on its custom endpoint.

Ideally, it would be awesome if there could be more sub url's:

177.0.0.50/listeners/listener01/data 
177.0.0.50/listeners/listener01/instruction
177.0.0.50/listeners/listener01/DBsync
177.0.0.50/listeners/listener01/<TARGETHOST>/command


etc, for different actions/functions


```


![[Pasted image 20230929010420.png]]


#### Shit to figure out:

- [x] Where will plugin logic live
- [x] How will the server interact/control plugins
	- Gonna need a standard setup
- [x] How to dynamically load/setup URL's
	- Doable, ask chat GPT for this one
- [ ] How to autheticate these external plugins are legit
	- Maybe server initiates first comm? sends message to listener @ ip address, and if it responds, it's trusted?
		- Issues here, PWNED plugin for ex.
	- Server initiates first contact, gets HASH of external plugin code. if matches what is local, good to go?
		- Start simple here to get it implemented
- [ ] Dynamic URL's from a file need a rethought
- [ ] Data seperation. Need to keep that in mind, as if a plugin gets owned it would be bad if it could access other data.
- [ ] For external... SSL (eventually... start without it.)

#### Solutions:

Where will plugin logic + actual plugins live. All plugins will live in here. I originally had them broken up into subfolders, but that added complexity to the loader

The loader itself is located in server.py

```

├── PluginEngine
│   ├── PluginHandler.py
│   └── Plugins
│       ├── BasePlugin.py
│       ├── PluginTemplate.py
│       ├── FlaskAPIListenerPlugin.py



```


How will the server interact/control plugins:
```
The server will dynamically load each plugin. Each plugin has a "base class" that it inherets, which opens the possibility for some functions to be used by all plugins. On plugin load, a method called "register_routes" is called. This "registers" the routes/endpoitns for the respective URL's of the plugin. Each route is mapped to a function within the plugin. 



ex:

http://server.com/plugin01/

--> plugin01_function():
		return "plugin loaded"

See "PluginTemplate" for a more complete example/the template I use for each plugin

```
Technical connections between plugins
![[Pasted image 20231001140536.png]]