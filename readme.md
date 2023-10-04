# WhisperNet

  

  

\<Very  much  so  still  in  Development,  this  will  update  as  things  are  completed.>

  

  

(Yet another) Command and Control (C2)/ Offensive Infrastructure Tool. Where I aim to be different (or at least keep this project somewhat relevant) is in its flexibility.

  

What does that mean? I don't fully know yet, but I have some ideas.

  

First off, I need to define a few items:

- Clients: The control software, used to interact with the server, and Agents.

- Agents: AKA RAT's. It's my own "malware" that contacts the C2 Server.

  

Back to flexibility...

- Plugins

- Plugins are simple "tools" that do things. I'll get a better explanation later

- Profiles:

- Similar to, and inspired by Cobalt Strike's Malleable profiles.

- "Evasion" Profiles:

- Affect how the server behaves, adds some special sauce to the conversations you don't want to get caught

- "Client" Profiles:

- Essentially settings for all clients.

  
## The vision:
Here's what I'm shooting for: (I realize this is a bit small... click on it and you can zoom in)

![vision drawio](https://github.com/ryanq47/WhisperNet/assets/91687869/6f7c4188-eb8e-416b-92d1-12d9d5530842)

  
I'll put this all into words later, but a quick TLDR: A full blown C2 enviornment, with features such as remote listeners, and (easily implemented) custom plugins to suite your needs. 

  

  

----------

  

  

# QuickStart Guide

  

  

This QuickStart guide will walk you through the initial steps of setting up WhisperNet and connecting your server and client.

  

  

1.  **Starting the Server:**  <Startup  directions  &  screenshots>

  

2.  **Starting the Client:**  <Client  startup  &  screenshots>

  

3.  **Connecting to the Server:** \<Connecting  to  server  and  screenshots>

  

  

----------

  

  

# Client Guide/OverviewA

  

  

The Client Guide provides essential information on using the WhisperNet client, including:

  

  

-  **Help Menu:** Access the built-in help menu to discover available commands and their functionalities.

  

-  **Basic Shell Overview:** Familiarize yourself with the core functionalities of the WhisperNet shell, enabling you to interact with the server efficiently.

  

-  **Plugins:** Explore the extensible nature of WhisperNet through its plugin architecture, which allows you to add custom functionalities tailored to your needs.

  

  

| Plugin | Description | Path |Origin (Native/3rd party) |

  

| ----------- | ----------- | ----------- | ----------- |

  

| SystemShell | A basic, semi-interactive 'passthrough' shell for system (bash, ps, etc) commands, via the subprocess module | /home/systemshell |Native |

  

| Plugin | DESC | PATH | Native |

  

  

# Server Guide

  
The server is powered by flask and built as an API. However, it kind of acts like a normal webserver as well. What I mean by that, is that the paths '/' and '/home' both display a "normal" static webpage from an HTML file when navigated to via a web browser. Any other path results in a '200' response code with a message of 'oops not found'. Why? Simply, to make any directory brute forcing a lot harder. Seriously, spin this up, and throw Dirbuster at it. It gets mad because every URL it tries returns a 200 response code. 

If you're thinking, "wait, I don't need to bruteforce, all the endpoints are listed here" then think again. There is a config file for setting said endpoints to whatever you want them to be (see: 'Addtl Details & short guides'). Take that blue team. 

Anyways, getting back on track, the real magic happens when you interact with it like a normal API. Once authenticated, you can do a whole host of things on the server, from hosting files, to chatting with others who are connected (not quite implemented yet... it's getting there). 


 
  #### Starting the server:
  This is how you can start the server, along with a few additional common options 
	  
	  python3 server.py --ip 0.0.0.0 --port 8080 
		  (opt) --evasionprofile <path_to_profile>
		  (opt) --clientprofile <path_to_profile>
		  (opt) --apischema <path_to_profile>
  
  #### Endpoints: 
  - There are a collection of default endpoints used to interact with the server. Note, these can be changed via a yaml config file in 'Config\ApiSchemas\default.yaml'
  
  - **/server**: Anything server related
	  - /server/spawntcplistener [post]: Spawns a TCP listener.
  - **/mgmt**: The management endpoint
	  - /mgmt/login:  Log into the server
	  - /mgmt/createuser: create a user
	  - /mgmt/deleteuser: delete a user
- **/files**: For file related operations (used by droppers, etc)
	- /files/uploads: A mini file repo
  
 #### Addlt Details & short guides:
 - Evasion Profiles
 - Client Profiles
 - ApiSchema
  

-  **Setting Up a Listener:** (move this to client)

  

  

# Agent Guide

  

  

The Agent Guide covers essential topics related to WhisperNet agents:

  

  

-  **Compilation:** \<Compile  instructions>

  

-  **Limitations:** \<Limitations  here>

  

-  **Current Agent Languages:**

  

- C# - .NET version \<Version  here>

  

  

----------

  

  

# Advanced/Dev Docs

  

  

In the Advanced/Dev Docs section, you'll find comprehensive information on topics that delve deeper into WhisperNet's capabilities:

  

  

-  **Obsidian Usage:** \<Notes  about  how  to  open  the  obisidan  docs>

  

  

Feel free to contribute, provide feedback, and join the WhisperNet community as we continually enhance and evolve this tool.
