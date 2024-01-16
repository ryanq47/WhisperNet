# WhisperNet

  

  

\<Very  much  so  still  in  Development,  this  will  update  as  things  are  completed. \<Not Implemented> means the feature is being worked on, but not yet ready>

  

  

(Yet another) Command and Control (C2)/ Offensive Infrastructure Tool. Where I aim to be different (or at least keep this project somewhat relevant) is in its flexibility, via the Node system. 

  

What does that mean? I don't fully know yet, but I have ideas hashed out below:

  

First off, lets define a few items:

- ?? : The control software, used to interact with the server, and Clients.

- Clients: AKA RAT's. It's my own "malware" that contacts the C2 Server.

  



  
## The vision:
Here's what I'm shooting for: (I realize this is a bit small... click on it and you can zoom in)

![vision drawio](https://github.com/ryanq47/WhisperNet/assets/91687869/6f7c4188-eb8e-416b-92d1-12d9d5530842)


Key Features:

 - Plugins:
     Plugins are tools you can implement serverside, if you wish. Plugins can either be standalone, or communicate with nodes. A plugin template is provided in <path>. See <anchor to plugin guide> for more info


 - Nodes:
     The younger sibling of the Server. Nodes add a layer between your server (aka crown jewels) and the targets. Yes, this can be achieved with typical C2 best practices (redirectors, multiple domains, etc), but I thought a new setup may be a fun idea to try & build. 

	 Pros:
	   - Flexibility
	   - Abstraction: If a node gets owned, taken down, blocked, etc, you can just spin up a new one. Having nodes infront of the server keeps it nested a layer deep, and (in my unproven opinion) safer. 
	   - Simplicity: From a code & functionality perspective, nodes are simple. Do their subroutines/jobs, and send relevant info to the server. 

	 Cons:
	   - Complexity, both from a communication, and deployment point of view. There's a fair bit of compensation that happens to make sure the Nodes & server talk properly, and securely


 - Logging:
	I've learned the hard way that *every* action on a pentest needs to be logged, for a variety of reasons (CYA, Reporting, etc). Due to this, every action run through WhisperNet is logged in a dedicated log file. <Not Implemented>

  

  

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

  
The server is powered by flask and built as an API. 


 
  #### Starting the server:
  This is how you can start the server, along with a few additional common options 
	  
	  python3 server.py --ip 0.0.0.0 --port 8080 


  #### Endpoints: 
  - There are a collection of default endpoints used to interact with the server.

  - **/api**: API calls. Most items are nested here for Nodes & ?? to interact with


  

-  **Setting Up a Listener:** 

  

  

# Client Guide

  

  

The Client Guide covers essential topics related to WhisperNet agents:

  

  

-  **Compilation:** \<Compile  instructions>

  

-  **Limitations:** \<Limitations  here>

  

-  **Current Agent Languages:**:
	- C++ <In Progress>

  

  

  

----------

  

  

# Advanced/Dev Docs

  

  

In the Advanced/Dev Docs section, you'll find comprehensive information on topics that delve deeper into WhisperNet's capabilities:

  

  

-  **Obsidian Usage:** \<Notes  about  how  to  open  the  obisidan  docs>
-  ** Postman Docs ** \<PDF docs for postman, throw in docs section or folder>

  

  

Feel free to contribute, provide feedback, and join the WhisperNet community as we continually enhance and evolve this tool.
