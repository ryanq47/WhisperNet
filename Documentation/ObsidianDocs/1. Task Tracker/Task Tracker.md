
Notes:


Currently just established a few new items:
- ServerData.DB for holding general server items
- ServerDataDbHandler for interacting with it

Up next: 
- BaseErrorClass


```dataview
table TASKTYPE, SCOPE, MODULE, ESTTIMETOIMPLEMENT as TTI, STATUS, PRIORITY, DUE
from "1. Task Tracker/Tasks"
sort PRIORITY descending where STATUS != "Done"

```

#### Completed Tasks

```dataview
table TASKTYPE, SCOPE, MODULE, ESTTIMETOIMPLEMENT, STATUS
from "1. Task Tracker/Tasks"
sort ESTTIMETOIMPLEMENT where STATUS = "Done"

```








