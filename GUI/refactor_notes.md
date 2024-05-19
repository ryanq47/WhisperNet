Refactor Notes:

- Docs:
  - Document as needed.
  - [X] GuiUtils Functions

  - [X] Server side listener handler/endpoints 
  - [X] Web Request manager (Done, double check & add in tidbits about dicts/lists)
   - [X] Listener popup
   - [X] Data Singleton.
   - [X] Usage of lsitener spawner

 - Assets: 
     - Add to dedicated folders of plugins/Widgets from now on

 - Widgets:
     - QT COmpeonents cut down to priority items
      [X]


 - Logging:
  - [X] Move into loggingsingleton where possible, move away from Baselogging

 - Listener
     - [X] Get listener details from server, display in tree item << Data coming in, need to do display logic
     - [ ] Add context menu for listeners (right click) that stops them
     - [X] fix the weird stretching/not full screening in the widget.

 - Login
     - [X] Make it a Dialogue

  - Signals
      - [X] Create signal maanger, SOOO much easier to do stiff with. 
      "QuickDocs Notes: Same structes as data singleton, allows for easier tracking/managing of signals accross the project."

  - [ ] Event Loop
      Need to have a way to *remove* items (or just a cleanup method) from the event loop, as new classes for widgets get created/deteled. Otherwise you end up with this:
      
      `Error with proccessing events: Internal C++ object (Listeners) already deleted.`

  - [ ] Docs:
    - [X] Signal Singleton

      (user & GUI docs)
    - [X] Names of listener actions:
          - Spawn: Create a new listener
          - Kill: Remove the lsitener
          (and for later expandability):
          - Start: Start a stopped/paused listener (if even possible?)
          - Stop: Stop a listener
          - NOTE: these need to change server side as well


      (server)
    - [ ] HTTP listener and how data is recieved. Dynamic keys N stuff + simplenamepace

  - [ ] Server:
     - Rename start/stop endpoints to spawn/kill
     - Remove listeners from current listener list/endpoint when killed. This will reflect
        properly on the GUI. --? Not sure what this means, thanks past ryan.

  - [ ] Listener
      - [X]Start with data capture logic
          - Works, need to build out listenres

      - [X] Action logger done/works fine for now. 
          - [ ] Log items where needed/as you come accross them, both with this and regualr logging


      - Doc: 
          Modules: Specific items for plugins
          Utils: Other, see bottom
          Once httplistener done,set bsae tempalte for public plugins/rules around them


         - [X] Doc new import method things
              Got rid of dumb double import method

      - [ ] Figure out how to handle data sent to listener. (needs to get to server somehow)
        - Currently, items are in the "client" class. These classes need to be managed in a singleton within the listener itself. Additioanlly, there needs to be logic to retreive data from these client classes, and forward to the server. 

        >> Here <<
        =- Working on client registration when talking to setver. ListenerHTTP line 124. 

      - [ ] Standalone Mode:
          Too much to put in one plugin, so just copy/paste the standalone one, name it name_standalone & adjust the imports. Should be fine.
          Remeeber, everything in public plugins must comm over http to the server.
      

        This may or may not live in the client classes themselves, have not thoguth it out yet.
            - Idea: Getter/setters for data (already in place), and the actual connect to server/server sync logic is in
                A seperate module/classs
      

Goals:
 - [X] establish proper/consistent way of doing things (such as popping windows, and network requests).
    Use helper functions.

- [ ] Fix web requests as you discover them 
 - [X] FINISH DOCUMENTATION LIST! 
 - [ ] Build out listener process (queueing, storing data, receivign request, etc.)

- [ ] Later, specify modules vs utils:

    Modules are collections of code that encapsulate specific functionalities within an application, while utils (utilities) are specialized modules designed to provide generic, reusable helper functions for common tasks.


- [ ] Other ideas:
  - SocketListeners. Use binary strings & raw sockets to communicate. 
  - Actually, just have like multiple communication formats available (then you could choose what msg format, and what listener type)?
    Ex, comms via binary string, each bit means something (would have to be VERY basic, and for long term/quiet af options - sleepers), via json, etc. then adapt to other listeners? Might cause problems parsing based on the clients. 



way later notes:
- Alright Gameplan:
   - [X] Go double chkec docs of sync plugin, make sure they all line up. 
   - [ ] Move API responses to new API response method (`from Utils.ApiHelper import api_response`)
       - Doc This - 
   - [ ] Update/recreate JSON respnose creator (HTTPJsonRequest.md) to fit universal vessel
   - Work on HTTPListener plugin syncing *to* server, and make sure that process works 
      - Data gets properly stored in singleton
      - Request/response ID's are thought about. 

   - Start deving httplistenerserver 

Thought: Use that json request for both client and server comms, just nest what you need in the "data" key

{
  "response_id": "matching_request_identifier",
  "request_id": "unique_request_identifier",
  "timestamp": 1710442988,
  "status": "success",
  "data": {
    "Actions":[
        //order performed from first to last?
        {"Action":"powershell", "executable":"ps.exe", "command":"net user /domain add bob", }, //add individual ID? TLDR: Need a way to know which response goes from which action upon sending back.
        {"Action":"powershell", "executable":"ps.exe", "command":"net group /add Domain Admins Bob", },
    ]
    "ListenerHttpCommandSync":[
        {"somedata": "somedata"},
        {"somedata": "somedata"}
    ]
    //anythign else here as well - not sure waht might be needed.
  },
  "error": {
    "code": null,
    "message": null
  }
}

//Ideas of above:
 - One of these "vessels" get sent out each beacon. Any commands queued in that time will get packaged, and sent in this vessel. Those are then run, and sent back with responses. Then beacon reaches out again, and so on, until it is killed.

 Also, differnt "things" or commands or sub comands:         
 
 {"Action":"powershell", "executable":"ps.exe", "command":"net user /domain add bob", }, //add individual ID? TLDR: Need a way to know which response goes from which action upon sending back.

Those above. One for each relevant item:
 - ListenerHttpCommandSync (commands to HTTP listeners, createone for each listener tyoe)
 - Actions: Actions to run on host


Figure out a way to document that, all using the transport vessel.
This allows for one transport vessel, with mutliple types of data per transmission.
Draw it out