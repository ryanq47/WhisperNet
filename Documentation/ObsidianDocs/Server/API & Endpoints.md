
## All ideas for now

These can be "changed to whatevrr" endpoints you want via a settings file

/server
- All server related things
	- Spawn listeners
	- etc

/agent:
- Where the agents check in. 



Security:
- Authentication of some sort eventually

- EVERYTHING returns 200. Even a true 400/404 should return the error page of 404err.txt, which is a 200. this helps prevent stuff from being enum'd from the server

#### General Layout & design




#### Default Endpoints

/server
- All server related things, 
	- Spawn listeners
	- etc
- /schema: 
	- Holds a schema of all the modified endpoint names. Import into client to hit the right endpoints
	- Should be behind authentication
- /login
	- The one endpoint that should stay consistent. The client needs to log into this to get the schema, to know which endpoints map to which functions

/agent:
- Agent checkpoint where the agents check in. 

/uploads
- File Endpoint for hosting files.


/ & /home:
- A "fake" homepage for the site. Pulled from an HTML/CSS comboed file in assets/HTML

/AnyOtherEndpoint:
- returns a "Not Found" page (200 response code) from /assets/HTML/errorcodes

#### Security:
- Some form of OAuth
- HTTPS
- Most responses should be 200 codes. This prevents/makes things harder:
	- Enumeration vs directory bruteforcing (or at least makes it slighty more complicated, have to measure by site size)
		- Maybe a few different error pages, that are different sizes, randomized to throw off that detection even more


