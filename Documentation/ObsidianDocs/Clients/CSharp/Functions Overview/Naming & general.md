## Handlers:
- A set of dedicated functions to do & process data.
	- they RETURN all the data, and do not store it
- Ex: 
	- PropertyHandler.cs
	- MessageHandler.cs
- #### Sub Classes:
	- **XxxxxExec**:
		- A handler that executes something on the host, such as PsExec.CS, It spawns PowerShell (through various methods) & runs it.
		- (TESTING/BETA) Each (method/class - haven't decided which yet) have an attribute called 'help', which will detail what it does
			- (rationale) Allows for clients to have their own specific help menus, takes it off the load of the server. makes life easier

## Data:
- A set of classes that HOLD data. 
	- Do not calcualte data
- Ex. ConfigData.cs
	- Client.ConfigData.Timeout = 5


