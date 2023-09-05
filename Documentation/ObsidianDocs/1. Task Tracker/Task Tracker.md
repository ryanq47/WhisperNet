
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








