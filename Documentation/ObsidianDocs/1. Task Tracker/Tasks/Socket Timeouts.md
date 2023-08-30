---
SCOPE: All
TASKTYPE: Implementation/Fix/Bulletproofing
MODULE: ClientHandler
ESTTIMETOIMPLEMENT: 30 min
STATUS: In Progress
PRIORITY: High
---


## Quick Description

The sockets need a timeout. Otherwise, they have the possibility of hanging forever, which is not good for server uptime


Things to think about:
- Socket Timeout Time (Maybe make a setting?)


## Possible Solutions/Plan


## Resources
[Python socket connection timeout - Stack Overflow](https://stackoverflow.com/questions/3432102/python-socket-connection-timeout)

## MindMap

## Progress Notes
- Before each handler (client, and agent), the socket is set to have a timeout of 5 seconds. This is done here because otherwise the main socket gets the timeout (pre-connection) and times out lol. Look if this timeout can be set any earlier in order to catch any odd scenarios where the code may not be reached