
## Server 

- [ ] Make sure the server is receiving everything correctly 
	- Note, I created some debug statements that print directly from json data on line 209 of server.py
	- [ ] Server needs some work & Documentation before continuing on the C# comms side
		- [x] Renaming Files
		- [x] Fixing now broken items due to rename
		- [x] Clean up, better var/function naming, and notes
		- [x] Find what you can remove from the main server.py & put in it's own file
		- [ ] Test functionality between server & client, to make sure the variable naming & new structure does not error out anywhere. 
			-  There are a couple so far
			- [ ] Document new server.py function structure
		- [x] SSL Key generate argument
			- [ ] Add in file placement/location i argument
			- [ ] FileCheck in Utils came from this, create a dedicated function/list of critical files.
		- [ ] SSL
			- [ ] Re-Learn SSL & watch some vids on it. 
			- [ ] Error handle respective SSL errors correctly. 
				- [ ] Fix 'no attribute' errors resulting from variables being init'd wrong, or not at all. AKA bulletproof it

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
- [ ] SSL 