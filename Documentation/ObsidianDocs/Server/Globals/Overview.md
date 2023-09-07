There are a few global class objects used. Once initialized, they are put into a dict. 

- PathStruct:
	- Attributes:
		- sys_path
			- Used to hold the absolute path to 'server.py'. Really handy for accessing files with a relative path. Why not use os.path? I'm 99% sure that trying to run the program outside of it's dir breaks path things, so this is a safeguard
	
```
Access via:
	global_objects['PathStruct'].sys_path
```
