Todo:

- [x] Find a way to store/hold onto the data posted by clients, and get itback to the server. Maybe a dedicated endpoint under clientname/results/data or soemthign taht holds the JSON? need to think about it.
	- Solved: Post to /clientdata, that endpoint takes the json provided, and pops it into a db. Each unqiue ID gets a table in the SimpleC2Data.db


- [ ] Setup external listener to be able to post successfully to this endpoint. 
	- [x] Data posted from client comes in successfully 
		- /clentdata --
	- [x] Data is cached in a subroutine (think batches) -- in progress, testing & solidyfying jank ass logic
	- [ ] Data is then forwarded to server

- [ ] Fixing jank logoc:
```
Moved away form inheretence
Detailed thread drawing in SimpleC2 Drawing. keep it like this, I find this layout best
Keep fixing jank logic. Specifically left off on getting the serverconnector working as intneded/wokring with the main flow, and documenting it. 

```



Simple desc


```
Client Checkin Chain:

POST /checkin
GET /command
<actions>
POST /clientdata
<sleep>


```

## Per Endpoint Details

#### /synccommand

Endpoint for server to POST new commands to the nodes to queue for the client.

so: Hacker/user (posts command) -> server (posts command) -> Node -> (appends) ClientIdCommandQueue <- (client checks in)

```
{
'command':['powershell', 'whoami /all'] #to get added to queue
'client': "clientid" # which client to add this command to

}
```

#### /command

Node for C2 clients getting commands from server


```
{
		//    suffix         option
	command: ["powershell", "whoami /all"]
	

}


```

- Starter command suffixes:

```

powershell: Run powershell command
 - ["powershell", "<command>"]
ExecuteBinary: Run a binary
 - ["executebinary", "<binary + args>"]

upload: upload to a server (post)
 - ["upload", "<server url>", "<File to upload>"]
download: download from a server
 - ["download", "<server url>", "<savepath>"]


```


etc etc fill me in 

#### /checkin
A checkin for the clients to check in at. 
```
{
	id: 
	timestamp:
	message: (if applicable)

}


```

#### /clientdata

A post endpoint to post results of commands. A little different than the usual post results on a heartbeat, this would instantly post to the respective listener upon command completion, instead of waiting


```
{
	id: 
	txid: transaction id, to track transaction?
	timestamp:
	data: "domain/username"

}


```