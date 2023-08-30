---
SCOPE: Server
TASKTYPE: Implementation
MODULE: ClientHandler
ESTTIMETOIMPLEMENT: 2 hours
STATUS: In Progress
PRIORITY: High
DUE: 09-04-2023
---


## Quick Description
Goal; Have clients be able to queue a command for an agent on the server. 


## Possible Solutions/Plan


## Resources

## MindMap

## Progress Notes
- Left off working on the server side of the agent commands (clienthandler.py)
	- [ ] Fix Queue Bug (String something must be indices)
	- Theoretically, once that is fixed, clients should be able to queue commands for the agents. 
- [ ] Build out a system to get the correct client the correct message
	- SubDir? Such as home/server/agent_id_12345: 
		- Each message would have the 'msg_to' as the agent_id. Would make it a lot simpler to do multiple commands, however this may take a bit logner to implement