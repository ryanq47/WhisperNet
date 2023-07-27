class QueueHandler():
    """Handles the queue.

        Queue Object: <CLASSOBJ>.queue

        Print this instance to show the current contents of the Queue, or use the .show() method

    """ 
    def __init__(self):
        ## using a list for the queue, it's pretty flexible
        self.queue = list()

    def __str__(self):
        print(self.queue)

    def enqueue(self, item_to_add=None):
        """Adds item to queue. 

        Args:
            item_to_add (any, reqiured): The item to add to the queue. Defaults to None.
        """
        if item_to_add == None:
            print("Warning, item_to_add == None")

        
        try:
            self.queue.append(item_to_add)

        except Exception as e:
            print(f"Error enqueuing: {e}")



    def dequeue(self):
        """Returns, and removes the next item in the queue.

        Returns:
            Item (type unkown): The next item in the queue. 

            On failure, returns False

        """
        if self.queue == []:
            print(f"Queue is empty")

        try:
            ## .pop removes element from list, and returns it
            item_to_dequeue = self.queue.pop(0)
            return item_to_dequeue
        
        except Exception as e:
            print(f"Error dequeueing: {e}")
            return False



    def peek(self):
        """Returns the next item in he queue. Does NOT remove it from the queue

        Returns:
            Item (type unkown): The next item in the queue. 

            On failure, returns False
        """
        try:
            ## .pop removes element from list, and returns it
            item_to_dequeue = self.queue[0]
            return item_to_dequeue

        except Exception as e:
            print(f"Error dequeueing: {e}")
            return False


    def show(self):
        """Prints all items in the queue. Can also be achieved by printing the class object itself
        """
        print(self.queue)


    
q = QueueHandler()

q.enqueue(item_to_add="Item1")
q.enqueue(item_to_add="Item2")
q.enqueue(item_to_add="Item3")

print(q.queue)

while q.queue != []:
    print(q.dequeue())
