

The FlaskAPI listener is very similar to the 'server.py' file, it's basically a copy with a few items adjusted. Think of it as a self contained mini server focused on serving Agents instead of clients. A lot of modules are copied in here, as the (eventual) goal is to have these listeners be deployed anywhere, and communicate over the internet vs locally

Update:
Easier to just jump to network comms now. Listeners will be spawned via an OS.ssytem or similar command, and the PID's will be tracked. All comms will be done via network operations to the flask servers on each listener


What is handled by what?

#### Server:
- User (client) Logins
- Control of listeners

#### Listener:
- Where Agents check in
	- Agent commands
	- Agent Responses
- File Hosting


Folder Namign:
- Everything is named the same, with the addition of 'listener' appended to the front. This is due to namespace reasons when importing modules

This does present some challenges... For example config files are not an easy copy paste anymore. Will need to think through

```
Utils -> ListenerUtils

```


## Endpoints:

```
## Default Agent URL
/agent
	## RandomGen URL for specific agents
	/agent/ABCDEFG/

/file
	#uploaded files - need to figure how this will be done.
	/file/upload
	#Files to download
	/file/download


## Not used yet. will be used for netcomms between server & listeners. Will require auth - most likely JWT
/data


```
