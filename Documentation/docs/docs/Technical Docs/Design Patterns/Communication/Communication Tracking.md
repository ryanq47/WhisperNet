## Communication Tracking & ID's


To effectively manage and track all communications, Message IDs are employed. These Message IDs are generated using UUID4, which ensures random and unique identification for each message. This method guarantees that each communication can be distinctly identified and referenced, facilitating organized and efficient message tracking.

## Types of ID's:

- RID (Request ID): The ID associated with a request. Used accross the stack. 

- LID (Listener ID): The ID associated with a listener. Each Listener has a unique LID associated with it. 

- AID (Action ID): The ID associated with the Action sync key. These are used to track actions for clients as they are forwarded, and executed. 

- LPID (Listener Process ID): Used exclusively on the Server for tracking local listener process instances. 

## Implementation:

All UUID's are generated in Utils.MessageBuilder, using the MessageHelper.generate_unique_id() method.

```
import uuid

class MessageHelper:
    @staticmethod
    def generate_unique_id() -> str:
        """
        Generate a unique message ID using UUIDv4.

        Returns:
            str: A unique UUIDv4 string.
        """
        return str(uuid.uuid4())
```