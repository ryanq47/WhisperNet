---
SCOPE: Server/Client
MODULE: ClientHandler.py
SEVERITY: medium
ESTTIMETOFIX: 30 Min
STATUS: Done
---
## Fix:
Not applicable due to move to Rest
## Quick Description
When a command is sent to the server, it sometimes causes a halt/waiting issue.

Client: 
```
home/server >> bob
Tree being accessed: <bound method Tree.tree_input of <Plugins._native.Server.Tree object at 0x000001677D888AF0>>
[CommsHandler.receive_msg()] Sent message of length: 441

(just ends here)
```

Not sure if server is not listening, or there's something else going on

Follow up - the second I try this again of course it doesn't do this lol. 
## Code In Question


## Possible Solutions


## Resources
