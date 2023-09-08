---
SCOPE: Server
TASKTYPE: Implementation
MODULE: If appliacble... the moduel
ESTTIMETOIMPLEMENT: Whatever you think it is, double it
STATUS: In Progress - left off
PRIORITY: High
DUE: DATE
---


## Quick Description
authentication to the Rest & Other endpoints.

Database based

passwords should be hashed, not plaintext
- Need to find best hashng

## Possible Solutions/Plan

DB home: DataBases/users.db


## Left off notes

Left off working on getting the DB connection coded. AuthenticationHandler will talk to the DB classes once that is complete, and then I can hook the APIup to it.
- [ ] DB connector is coded, needs testing & error handling

The methods are there for those 2, just fill them in

globas is broke. find a way to fix
- Moved to a struct/class obj that I can pass around

FIXED: password is not being retrieved frmo the DB : ( 

Latest issue:
- checkpw function being weird, the real one works, butthe one in encryption is beingfunjky
- also, document the guard clauses, and implement where possbile.

!! Documentation for JWT process. Very important to understand the risks & potential pitfalls of using

ToDO:
- [ ] Implement user management functions
	- [x] create
		- [ ] Needs a healthy error review
		- [ ] Need to add JWT requiremnet decorator
		- [ ] Needs a custom path in the yaml file
	- [ ] delete
		- [ ] simlar as create but just change to delete
	- [ ] modify
- [ ] Get data from POST request (probably just json)
	- [ ] Figure out how a success/fail response will be handled (hide it in cookies? or just straight up say fail)
- [ ] Document process/modules

## Resources

## MindMap