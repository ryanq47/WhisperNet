## Client class, one per client joined. Basically a working in mem db.
# For perf issues... should probably dump this data to a real DB or something :| ask chatgpt
# Don't want it running for like 2momths then slowing down cause out of mem from all the
# reqeusts

#Takes app as a ref to the flask app to add url's N stuff -- WTF does this mean?


import collections
import time

class Client:
    def __init__(self, app, action_logger):
        self.app = app
        self.responses = {}
        self.command_queue = collections.deque()
        ## STUPID reason for this, init gets passed the action logger at init because
        #I don't ahve a way to tell if the calling plugin is running in standalone mode or not
        # So, the parent gets to import it, as it knows what mode it's in, and then passes it here. WHATEVER
        self.action_logger = action_logger
        self.nickname = "Nickname"

    # Response Handling

    def set_response(self, response):
        """
        Stores the response in the dictionary.
        The response should be a dictionary formatted as specified.
        
        Example:
            client.set_response({
                "response_id": "123",
                "request_id": "001",
                "timestamp": client.current_timestamp(),
                "status": "success",
                "result": {"data": "Example result data"},
                "error": {"code": None, "message": None}
            })
        """

        # potential problem, client is the one that sends back the response id. Could be tampered with. Need
        # to add check for this to make sure request & response match up?
        response_id = response.get("response_id")
        if response_id:
            self.responses[response_id] = response

        self.action_logger.log(
            response = response,
            action = "Recieved response",
            client = self.nickname,
            response_id = response_id
        )

    def get_response(self, response_id):
        """
        Retrieves a response by response_id.
        
        Example:
            response = client.get_response("123")
        """

        return self.responses.get(response_id)
        

    def set_response_subkey(self, response_id, key, value):
        """
        Sets a subkey for a specific response. If the response or subkey doesn't exist, it handles gracefully.
        
        Example:
            client.set_response_subkey("123", "status", "failed")
        """
        if response_id in self.responses:
            self.responses[response_id][key] = value

    def get_response_subkey(self, response_id, key):
        """
        Gets a subkey value from a specific response. Returns None if the key doesn't exist.
        
        Example:
            status = client.get_response_subkey("123", "status")
        """
        if response_id in self.responses:
            return self.responses[response_id].get(key)
        return None

    # Command Queue Handling

    def enqueue_command(self, command):
        """
        Adds a command to the queue.
        
        Example:
            client.enqueue_command(JSON_Command)
        """
        self.action_logger.log(
            request = command,
            action = "Queue command",
            client = self.nickname
        )

        self.command_queue.append(command)

    def dequeue_command(self):
        """
        Removes and returns the first command in the queue. Returns None if the queue is empty.
        
        Example:
            next_command = client.dequeue_command()
        """
        if self.command_queue:
            return self.command_queue.popleft()
        return None

    def peek_next_command(self):
        """
        Returns the first command in the queue without removing it. Returns None if the queue is empty.
        
        Example:
            next_command = client.peek_next_command()
        """
        if self.command_queue:
            return self.command_queue[0]
        return None

    def queue_size(self):
        """
        Returns the current size of the command queue.
        
        Example:
            queue_size = client.queue_size()
        """
        return len(self.command_queue)

    # Utility Functions

    def current_timestamp(self):
        """
        Returns the current timestamp.
        
        Example:
            timestamp = client.current_timestamp()
        """
        return int(time.time())

