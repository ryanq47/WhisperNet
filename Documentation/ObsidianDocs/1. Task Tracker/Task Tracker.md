
Notes:


Currently just established a few new items:
- ServerData.DB for holding general server items
- ServerDataDbHandler for interacting with it


okay -- Everything *should* be in place now (save for a template for external plugings). So, full steam ahead with developing/focusing on plugins!!! 
- The last thing to maybe figure out is the path struct stuff - or I can just say fuck it and make the user work from the server.py directory. might be easier  to add a check & say just work in said dir.



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








