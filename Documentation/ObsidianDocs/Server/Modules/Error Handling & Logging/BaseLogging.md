
A parent class for logging operations. Keeps the logging consistent across the project. Just inheret the class into your class, and you'll have access to a few items:


```



self.logger: The logger. Call with 'self.logger.debug', or any other logging function (warning, info, etc)


```

## Notes

In this image, BaseLogger is only inhereted by BasePlugin, but it can be inherited by any class instance

![[Pasted image 20231003212206.png]]



## Hacky Fixes

so... I made some classes static which makes it tough to use inheritance. As such, each static class uses this fix:

```
## This is super hacky. My Dumbass made this a static method, so to properly use the BaseLogging class, I need to to
## init the instance, and then call the logging function

base_logging = BaseLogging()
function_debug_symbol = base_logging.function_debug_symbol
```

Just replace `logging` with `base_logging.logger`