
This data base holds general server information, and stats.


## Tables:
"Plugins" - Holds the actively discovered plugins. 
- Name: Name of plugin
- Author: Author of plugin
- Endpoint: The endpoint the plugin maps to
- Loaded: Bool, if plugin successfully loaded (0), or if there was an error (1)
	- Might be handy to add an error message field?
- Type: Type of plugin. Ex "Builtin" or "Custom"

Create with:
```
CREATE TABLE "Plugins" (
	"Name"	TEXT,
	"Author"	TEXT,
	"Endpoint"	TEXT,
	"Loaded"	INTEGER,
	"Type"	TEXT
);
```