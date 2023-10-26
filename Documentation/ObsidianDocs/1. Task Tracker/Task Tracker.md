
Notes:

Immediate to do:
	- Server could use some optimization in time (ongoing)
		[here](obsidian://open?vault=ObsidianDocs&file=1.%20Task%20Tracker%2FTasks%2FServer%20Optimizations)
- [x] Fix webserver variable issue (should be quick)
- [ ] Upload button in GUI
	- [ ] "working" on the gui side, Still protoyping/testing
- [ ] CLI args for logging levels for server, (and ext plugins)
- [ ] Docs all of this
- [ ] General bug test/cleanup.
	- [ ] Perf Testing, 20-100 node load test :)
- [ ] 

Post that, c2 design time. 

```dataview
table TASKTYPE, SCOPE, ESTTIMETOIMPLEMENT as TTI, STATUS, PRIORITY, DUE
from "1. Task Tracker/Tasks"
sort PRIORITY ascending where STATUS != "Done"

```

#### Completed Tasks

```dataview
table TASKTYPE, SCOPE, MODULE, ESTTIMETOIMPLEMENT, STATUS
from "1. Task Tracker/Tasks"
sort ESTTIMETOIMPLEMENT where STATUS = "Done"

```








