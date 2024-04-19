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

        >> Here <<
      - [X] Action logger done/works fine for now. 
          - [ ] Log items where needed/as you come accross them, both with this and regualr logging

      - [ ] Figure out how to handle data sent to listener. (needs to get to server somehow)
        - Currently, items are in the "client" class. These classes need to be managed in a singleton within the listener itself. Additioanlly, there needs to be logic to retreive data from these client classes, and forward to the server. 

        This may or may not live in the client classes themselves, have not thoguth it out yet.
            - Idea: Getter/setters for data (already in place), and the actual connect to server/server sync logic is in
                A seperate module/classs
      

Goals:
 - [X] establish proper/consistent way of doing things (such as popping windows, and network requests).
    Use helper functions.

- [ ] Fix web requests as you discover them 
 - [X] FINISH DOCUMENTATION LIST! 
 - [ ] Build out listener process (queueing, storing data, receivign request, etc.)


- [ ] Other ideas:
  - SocketListeners. Use binary strings & raw sockets to communicate. 
  - Actually, just have like multiple communication formats available (then you could choose what msg format, and what listener type)?
    Ex, comms via binary string, each bit means something (would have to be VERY basic, and for long term/quiet af options - sleepers), via json, etc. then adapt to other listeners? Might cause problems parsing based on the clients. 
