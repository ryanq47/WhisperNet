## Handlers:

- A set of dedicated functions to do and process data.
    - They **return** all the data and do not store it.
- Examples:
    - PropertyHandler.cs
    - MessageHandler.cs

### Exceptions to the 'return' rule:

- Server->ClientEngine -> FriendlyClientHandler
- Server->ClientEngine -> MaliciousClientHandler
    - Both are handlers for clients that hold class instances instead of returning data to the calling function.

#### Sub Classes:

- Everything in this section is a 'Handler'.
- **XxxxxExec**:
    - A handler that executes something on the host, such as PsExec.CS. It spawns PowerShell (through various methods) & runs it.
    - _(TESTING/BETA)_ Each (method/class - haven't decided which yet) has an attribute called 'help,' which will detail what it does.
        - _(Rationale)_ Allows clients to have their specific help menus, reducing the server's load and making life easier.
- XXXXXX Engine:
    - Backbone components used primarily on the server side. The term 'engine' was chosen because it sounds badass.

## Data:

- A set of classes that **hold data**.
    - They do not calculate data.
- Example:
    - ConfigData.cs
        - `Client.ConfigData.Timeout = 5`


## Clients:
- Malicious Clients (AKA RATS:)
	- Name: ??? HiveClient? FloodSpore? Something professionalish
- Friendly Client (aka users)
	- Name: ??




