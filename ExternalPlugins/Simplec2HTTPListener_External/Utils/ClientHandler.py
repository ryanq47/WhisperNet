## Holds clietn object code.


class Client:
    def __init__(self, name):
        self.name = name
        self.command_queue = None


    def add_to_command_queue(self):
        '''
        Adds command to client command queue
        
        '''
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
        return "sleep"