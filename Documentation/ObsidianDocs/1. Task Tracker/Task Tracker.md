
Notes:


Currently just established a few new items:
- ServerData.DB for holding general server items
- ServerDataDbHandler for interacting with it


okay -- Everything *should* be in place now (save for a template for external plugings). So, full steam ahead with developing/focusing on plugins!!! 



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








