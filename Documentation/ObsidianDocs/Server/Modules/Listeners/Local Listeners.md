
Local listeners are spawned via python's subprocess module, in a new thread. This is so I don't have to deal with import errors & can keep consistency between the 'remote' and 'local' listener code. They are essentially standalone units that do their communicating via http. 


By default, the listeners are spawned with `threaded_process_spawner` from the Utils.UtilsHandler handler. This spawns them in a new thread, with daemon mode on. When the control server shuts down, so do the listeners. This may change in the future, but for now is the easiest way to manage these processes.