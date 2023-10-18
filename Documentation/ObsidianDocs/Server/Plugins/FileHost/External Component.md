
The External FileHost component serves as a remote file host instance. 

High level overview of what's going on:
![[Pasted image 20231013100938.png]]


## Major Components 
There are 2 major compontents to the FileHost Plugin, the 'Control Daemon', and the Flask Instance. Each has a crucial role to play in order to keep this plugin functional.

#### Flask Instance
The flask instance is what serves the files. You WILL need to port forward whatever port you choose to spin the flask server up on. (* Note, if running the entire WhisperNet server on one machine, you can use the local FileHost plugin to serve files -- not quite implemented yet, will link docs later).

~~Then, your target/victim just has to be coerced into navigating to the Flask server to get ahold of a payload:~~

Sorry, I mean to say that anyone can now download files from said flask server, "legally" obtaining whatever "safe" files you feel like sharing

```
http://notsafedomain01.com/malicious.exe (FileHost instance)

http://notsafedomain02.com/malicious.exe (Another FileHost instance)
```


Additionally, these will download "as attachments" meaning that they will "auto download" once the correct URL is reached:
![[Pasted image 20231013103045.png]]


#### Daemon

The daemon is used to communicate *with* the Control Server, along with managing some other tasks. The Daemon initiates the conversation to the Control Server, so no special setup is needed on the networking side, just make sure the Control Server is reachable. 

At the moment, here are the key functions of the Daemon:


- Sync files from Control server. (Note, each action is logged, to keep an eye on what's going on)
	- Every heartbeat, the Daemon will compare files from the Control Server, to it's own file "cache/store". 
		- If a file is on the CS, but not on the FileHost Plugin:
			- it will request to download it from the CS. 
		
		- If a file does exist already:
			-  MD5 hashes of the files will be compared. If the hashes do not match, the FileHost Plugin will pull the files from the CS, overwriting its local copy. 
				- This is a design choice. Honestly, it was the most simple way of doing basic file tracking. Maybe I'll step it up in the future, but for now this works fine.
			- If hashes DO match, no action is taken. This saves on bandwidth/redownloading files the plugin already has. 






## IDea Section

Checkin messages to CS. Post to /api/filehost/checkin? then the CS could take said data, organize as needed, and display on webserver. Might be a good idea to dump these messages in a DB as well.

```

{
	plugin_name: {
		"name":"",
		"ip":"",
		"message":"syncing | sync successful | sync failed | error"
		"timestamp":""
	
	
	}
	
}

```



- [ ] create an endpoint for taking in file access logs, similar to the checkin. Same setup as checkin but with this

```

{

	"filename":"",
	"hostip":"",
	"hostingserver":"syncing | sync successful | sync failed | error"
	"timestamp":""

}

```