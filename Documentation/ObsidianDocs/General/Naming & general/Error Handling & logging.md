**Error Handling Documentation: Logging Format**

For consistent and standardized error handling across the project, it is recommended to follow the specified formatting for logging error messages. The prescribed format is as follows:


#### Logging.Debug():

Anything that the user can live without, but the dev wants to see. 

All logging.debug will use "inspect.currentframe().f_back" for their outputs. This is an easy way to track where things are happening.

Each function will have a   `logging.debug(f"{function_debug_symbol} {inspect.stack()[0][3]}")` right under the function call. This allows easier tracking of what is being called. This supplements the inspect tracebacks. 

#### Logging.info():
Anything the user should see, such as auth type, new connection's, etc

`logging.info("[*] Cookie Authentication")`
#### Logging.Warning():

Anything that could be a concern (such as a weird value, or connection) should be a warning. Warnings are allowed to continue operation, and shown to the user


#### Logging.Critical

Anything that is so bad, that it requires the program, or current thread to exit. Keep this at a minimal whenever possible


#### Logging philosophy.
The Server will (try to) log as much as possible, that includes client IP addresses, etc. It's up to the clients to disable sending that info on their end.