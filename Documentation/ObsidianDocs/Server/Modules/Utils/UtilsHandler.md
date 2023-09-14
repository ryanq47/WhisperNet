**Location**: Server/Utils/UtilsHandler.py


This module holds a ton of frequently used utility functions. 


#### process_spawner():

Process Spawner spawns processes via python's subprocess module

#### threaded_process_spawner():

Does the same as Process Spawner, but wraps it in a thread to prevent blocking. Additionally, the thread is set to "daemon mode", which means that on close, these threads will be closed as well.

