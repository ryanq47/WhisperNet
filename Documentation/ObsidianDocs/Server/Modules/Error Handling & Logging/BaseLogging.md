
A parent class for logging operations. Keeps the logging consistent across the project. Just inheret the class into your class, and you'll have access to a few items:


```



self.logger: The logger. Call with 'self.logger.debug', or any other logging function (warning, info, etc)


```

## Notes

In this image, BaseLogger is only inhereted by BasePlugin, but it can be inherited by any class instance

![[Pasted image 20231003212206.png]]