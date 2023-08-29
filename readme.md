# WhisperNet

  
  

\<Very  much  so  still  in  Development,  this  will  update  as  things  are  completed.>

  

(Yet another) Command and Control (C2) Infrastructure Setup Tool. Where I aim to be different (or at least keep this project somewhat relevant) is in its flexibility. 

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

  

<ChatGPT Generated CorpoGarbo: WhisperNet  is  a  versatile  and  powerful  Command  and  Control  (C2)  infrastructure  setup  tool  designed  to  streamline  the  process  of  establishing  secure  communication  channels  between  servers  and  clients.  With  a  focus  on  ease  of  use  and  flexibility,  WhisperNet  simplifies  the  setup  of  your  C2  infrastructure,  allowing  you  to  focus  on  your  objectives.>

  

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

  

The Server Guide offers insights into managing your WhisperNet server:

  

-  **Evasion Profiles:** Learn how to configure evasion profiles, enhancing the stealth and resilience of your server's communication.

-  **Other Profiles:** \<Figure  out  later>

-  **Setting Up a Listener:** \<how  to  set  up  a  listener,  requires  some  server  dev  first>

  

----------

  

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