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
    - [ ] Signal Singleton
    - [ ] Names of listener actions:
          - Spawn: Create a new listener
          - Kill: Remove the lsitener
          (and for later expandability):
          - Start: Start a stopped/paused listener (if even possible?)
          - Stop: Stop a listener
          - NOTE: these need to change server side as well

  - [ ] Server:
     - Rename start/stop endpoints to spawn/kill
     - Remove listeners from current listener list/endpoint when killed. This will reflect
        properly on the GUI.

Goals:
 - [X] establish proper/consistent way of doing things (such as popping windows, and network requests).
    Use helper functions.

- [ ] Fix web requests as you discover them 


