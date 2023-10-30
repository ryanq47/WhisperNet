Todo:


Simple desc

## Per Endpoint Details

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
