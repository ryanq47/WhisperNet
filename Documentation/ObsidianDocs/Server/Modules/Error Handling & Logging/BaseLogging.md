
A parent class for logging operations. Keeps the logging consistent across the project. Just inheret the class into your class, and you'll have access to a few items:


```



self.logger: The logger. Call with 'self.logger.debug', or any other logging function (warning, info, etc)


```

## Notes

You'll have to define `self.logger` with `self.logger = super().logger` if you use an `__init__()` statement in your plugin's class. This reaches into the parent class to grab the logging instance. 

Otherwise, Python will try to grab 'self.logger' from the current class instance, and won't be able to find it

Ex:
```
class ServerDataDbHandler(Utils.LoggingBaseClass.BaseLogging):
   
	def __init__(self):
		self.data01 = "somedata"
		self.logger = super().logger
```


In this image, BaseLogger is only inhereted by BasePlugin, but it can be inherited by any class instance

![[Pasted image 20231003212206.png]]