## Holds clietn object code.
from collections import deque #double ended queue. NOT thread safe, use queue.Queue if needed

class Client:
    def __init__(self, name):
        self.name = name
        self.command_queue = deque() #None


    def enqueue_command(self, command = "sleep"):
        '''
        Adds command to client command queue
        
        '''
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
            command = "sleep"
        
        return command
    
    def print_queue(self):
        '''
        prints all contents of queue
        '''
        ## thank you python for making this easy. 
        for command in self.command_queue:
            print(command)