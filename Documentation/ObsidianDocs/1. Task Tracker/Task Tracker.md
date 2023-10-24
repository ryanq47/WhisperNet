
Notes:

Left off:
- Implemetnign GUI node logs.
	- Notes, Everythign works well. JSON is spit out properly by server, and GUI reflects that. Good job.
	- Server could use some optimization in time
		[here](obsidian://open?vault=ObsidianDocs&file=1.%20Task%20Tracker%2FTasks%2FServer%20Optimizations)
	- Need to get File Logs working, and then rethink/double check the GUI code for better ways/layouts before continuing with it.
	- Additionally, upload button woutl be nice to have as well

- [ ] CLI args for logging levels for server, and ext plugins
- [ ] Docs all of this

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








