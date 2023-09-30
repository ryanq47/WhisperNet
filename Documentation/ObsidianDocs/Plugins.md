---
SCOPE: Whole Project
TASKTYPE: Refactor/Reimplement
MODULE: All
ESTTIMETOIMPLEMENT: 3 Hours
STATUS: In Progress
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

- [ ] Where will plugin logic live
- [ ] How will the server interact/control plugins
	- Gonna need a standard setup
- [ ] How to dynamically load/setup URL's
	- Doable, ask chat GPT for this one
- [ ] How to autheticate these external plugins are l;egit
	- Maybe server initiates first comm? sends message to listener @ ip address, and if it responds, it's trusted?
		- Issues here, PWNED plugin for ex.
	- Server initiates first contact, gets HASH of external plugin code. if matches what is local, good to go?
		- Start simple here to get it implemented
- [ ] Data seperation. Need to keep that in mind, as if a plugin gets owned it would be bad if it could access other data.
- [ ] SSL (eventually... start without it.)

## MindMap