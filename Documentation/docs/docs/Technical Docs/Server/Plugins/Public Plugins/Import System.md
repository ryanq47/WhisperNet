### Import System Methodology

All of the plugins that have a standalone mode use a dynamic import methodology to adjust module import paths based on the execution context — standalone or integrated within a larger framework.

At the moment, just the Public Plugins have standalone modes.

#### Standalone Mode:
- When the script runs as the main program (`__name__ == "__main__"`), it operates in standalone mode. In this mode, it uses the default `sys.path` which already includes the directory of the script.

#### Integrated Mode:
- If the script is not the main program, it assumes it's part of an integrated system.
- It dynamically adds its current directory to the start of `sys.path`. This ensures that imports search this directory first before any other system paths. This is particularly useful for maintaining separate environments within a larger application architecture.
  
#### Common Imports:
- After setting the import path, the script imports necessary modules like `ActionLogger`, `Logger`, `Client`, `HTTPJsonRequest`, and utilities. These imports use the adjusted `sys.path` to locate modules whether in standalone or integrated mode.

This approach minimizes import errors and ensures modularity, allowing the same codebase to function differently depending on its operational context.


Example:

```
## Standalone
if __name__ == "__main__":
    print("Standalone Mode")

## Integrated
else:
    ## Hacky little method to keep one import section, but just tell the 
    ## interpreter where to look for these plugins
    current_directory = os.path.dirname(os.path.abspath(__file__))
    print("Integrated mode")
    #("Current directory:", current_directory)

    # Insert this path at the start of the sys.path
    # This ensures that it is the first location Python looks for modules to import
    sys.path.insert(0, current_directory)

## Now, based on the sys.path, the interpreter will know where to look for the correct module.
from Utils.ActionLogger import ActionLogger
from Utils.Logger import LoggingSingleton
from Modules.Client import Client
from Modules.HTTPJsonRequest import HTTPJsonRequest
from Utils.Utils import Standalone
from Utils.DataSingleton import Data

```