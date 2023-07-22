
## Server

- [ ] Make sure the server is receiving everything correctly 
	- Note, I created some debug statements that print directly from json data on line 209 of server.py
	- [ ] Server needs some work & Documentation before continuing on the C# comms side
		- [x] Renaming Files
		- [ ] Fixing now broken items due to rename
		- [ ] Clean up, better var/function naming, and notes


## CSharp

Left off getting the client to send data over to the server. It works! I still need to:
- [ ] Validate everything is working correctly & is clean/**documented** with sending to the server.
	- [x] Document revised JSON structure as well.
	- [ ] C# client can talk TO the server. 

- [ ] Re-organize the Program.cs file & clean it up
	- [x] IN PROG
	- [x] Properties moved to PropertyHandler.cs
	- [ ] Removeal of old message class
		- [ ] NOTE! decision tree is partially broken due to this, with Message.Parse. Relevant/error lines are commented out for now
	- [ ] Remove other old classes/methods & move to respective folders
	