## Active Bugs
```dataview
table SCOPE, MODULE, SEVERITY, ESTTIMETOFIX, STATUS
from "2. Bug Tracker/Bugs"
sort SEVERITY desc where STATUS != "Done"

```


## Fixed bugs
```dataview
table SCOPE, MODULE, SEVERITY, ESTTIMETOFIX, STATUS
from "2. Bug Tracker/Bugs"
sort ESTTIMETOFIX where STATUS = "Done"

```








