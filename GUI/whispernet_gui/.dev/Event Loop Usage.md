## Event Loop usage

#### What is it:
A (singleton) event loop for items that happen in the program, technically tied into the QT event loop.

#### When does it trigger:
Every second, post successful login

#### How to use:

```python

## init the Event loop class.

from Utils.EventLoop import Event

    def __init__(self)
        self.event_loop = Event()

## Adding items (functions) to the event loop:

    self.event_loop.add_to_event_loop(self.get_client_data)
    
## Optional args, and kwargs for those functions
    self.event_loop.add_to_event_loop(self.get_client_data, myarg="argument", myarg2="5768")

## You can add an event to the loop at any time, but I tend to call this code (aka queue up the events) when the plugin loads in (aka add items on __init__).
## once a successful login happens, the event loop will start, and your code will be called. All error handling is done within the event loop.

## getting data from these events: No idea, haven't figured that out yet. Probably slots & signals. 

```
