---
SCOPE: Server/Client/Agent/Whole Project
TASKTYPE: Implementation/Docmentation/Review/Refactor
MODULE: If appliacble... the moduel
ESTTIMETOIMPLEMENT: Whatever you think it is, double it
STATUS: In Progress
PRIORITY: Low/med/High
DUE: DATE
---


## Quick Description
Adjusting listeners to work from the main server.

Some goals

- [ ] Listener Management
	- [ ] Spawn listener
	- [ ] Kill Listener
- [ ] Listener setup
	- [ ] Flask Frontend
	- [ ] 


Notes, I'm jumping directly to network comms (via flask)

Current isues;

line 242 of server.py, getting a winsock error when spawning listener. The idea here is to spawn a listener via os/subprocess, and then collect it's PID. All comms will be done over http/flask. It works fine alone.
- Fix: Turn off debug mode on windows. That was stupid lol


Okay subprocess thread thing works, needs some review & cleanup:
- [ ] Errors switched to 'raise'
- [ ] Return PID's and other info if needed.
- [ ] Some way to track each listener (listener dict?, DB might be great, but is a lot more work)



Once completed, next steps are to:
- Map out endpoints for communication between server & listener
- move Listener name prefix off stuff.
## Possible Solutions/Plan


## Resources

## MindMap