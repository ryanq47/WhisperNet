## Holds clietn object code.
from collections import deque #double ended queue. NOT thread safe, use queue.Queue if needed

class Client:
    '''
    I'm trying to make this more traditional OOP... so getters & setters yay. Makes stuff a bit more clean/easier to use.
    
    '''
    def __init__(self, name):
        self.name = name
        self.command_queue = deque() #None
        self.callback = None


    def enqueue_command(self, command = ""):
        '''
        Adds command to client command queue
        

        Commands are storn as python dict objects. They are converted to JSON at reqeuest
        '''


        if command == "" or command == None:
            command = {"action":"sleep", "arguments":"none"}

        #print(command)

        self.command_queue.append(command)
        ...

    def reload_command_queue(self):
        '''
        reloads command queue from saved state, used if node crashes
        '''

        ...

    def save_command_queue(self):
        '''
        saves commmand queue to file/db incase node crashes
        '''

    def dequeue_command(self) -> str:
        '''
        Gets next cmomand in command queue. If none, returns sleep
        '''
        #...
        try:
            command = self.command_queue.popleft()

        except Exception as e:
            command = {"action":"sleep", "arguments":"none"}
        
        print(command)
        return command
    
    def print_queue(self):
        '''
        prints all contents of queue
        '''
        ## thank you python for making this easy. 
        for command in self.command_queue:
            print(command)

    def set_callback(self, callback=60):
        '''
        Sets the callback time for the client

        callback: int
        '''
        self.callback = callback

    def get_callback(self):
        '''
        Get callback time
        callback: int
        '''
        return self.callback

    def get_id(self):
        '''
        Getter for client name
        '''

        return self.name

