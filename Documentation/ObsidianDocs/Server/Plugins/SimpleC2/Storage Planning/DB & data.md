
#### Node -> Server

POST to /simplec2/X

X: Datapost?
X: clientdata

each post will:
1) get JSON data (as raw str, not per key)
2) Call sqlite library to write TO db, in the respective table of the client
	1) Handles the if table exists, etc
3) 



#### Server -> Perst. Data (db)


Store in sqlite DB, DB lives in DB folder. 

JSON: [json](obsidian://open?vault=ObsidianDocs&file=Server%2FPlugins%2FSimpleC2%2FNodes%2FHTTP%20Node)
#### DB formats

Storing as raw JSON string, instead of parsing. 

Idea: 
One table for each client that checks in

## DB Fields:
Data: Holds raw json string of data
Timestamp: Hodls unix timestamp at time of db insertion.