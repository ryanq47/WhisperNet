
In .Dev, there is a 'codetest.py' file. This is used to test the server in an efficient manner. Just run it, and it should figure out where everything is, and run the test.

Note, I recommend you do it on Linux/unix, as the color codes don't work for windows. 

#### Tests:
Currentlt, a few items are tested:

1) Server spawning/startup
	2) Checks file loading
2) Logging in as admin user
	1) Checks Users DB function
3) User Management actions
	1) Creates a user (testuser)
	2) Promptly deletes that user (testuser)
4) Creating 3 listeners
	1) Checks listener & process spawn functionality
	2) Ports 8080, 9090, and 7070


All of these should have a green output. If not, something is broken server side