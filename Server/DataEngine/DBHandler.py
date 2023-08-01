import sqlite3
import logging

## temp sleep string
sleep_string = '''{"general": {"action": "sleep", "client_id": "", "client_type": "", "password": ""}, "conn": {"client_ip": "", "client_port": ""}, "msg": {"msg_to": "", "msg_content": "", "msg_command": "sleep", "msg_value": "", "msg_length": "", "msg_hash": ""}, "stats": {"latest_checkin": "", "device_hostname": "", "device_username": ""}, "security": {"client_hash": "", "server_hash": ""}}'''
## Needs sanitation?

## probably should be static
class SQLDBHandler:

    def __init__(self, db_name):
        self.dbconn = None
        self.cursor = None
        self.connect_to_db(db_name)


    def connect_to_db(self, db_name):
        try:
            self.dbconn = sqlite3.connect(db_name)
            self.cursor = self.dbconn.cursor()
            logging.debug(f"[DBHandler.connect_to_db()] Successful connection to: {db_name}")

        except Exception as e:
            logging.debug(f"[DBHandler.connect_to_db()] Error: {e}")

    
    def create_mclient_table(self, client_name = "TestClient"):
        self.cursor.execute(f'''
        CREATE TABLE IF NOT EXISTS {client_name} (
        id INTEGER,
        msg BLOB,
        response BLOB,
        requester BLOB
        )
        ''')
        self.dbconn.commit()

    def create_mclient_queuetrack_table(self):
        """Creates queue tracking tbale. this is handy for if the server crashes
        """
        self.cursor.execute(f'''
        CREATE TABLE IF NOT EXISTS client_queue_tracker (
        current_queue_number INTEGER,
        client_name BLOB,
        next_queue_number BLOB
        )
        ''')
        self.dbconn.commit()

    def create_mclient_queuetrack_row(self, client_name = "TestClient"):
        """Creates a row for the client (if it does not exist - working on that part)

        Args:
            client_name (str, optional): Name of client 
        """
        check_query = f'SELECT client_name FROM client_queue_tracker WHERE client_name = ?'
        self.cursor.execute(check_query, (client_name,))
        existing_row = self.cursor.fetchone()
        if existing_row:
            ## maybe recurse with id + 1 until it gets it right? 
            print(f"ID {client_name} already exists in the client_queue_tracker table.")
            return


        insert_query = f'INSERT INTO client_queue_tracker (current_queue_number, client_name, next_queue_number) VALUES (?, ?, ?)'
        #print("insert into client_queue_tracker")
        values = (0, client_name, 1)
        self.cursor.execute(insert_query, values)
        self.dbconn.commit()


    def enqueue_mclient_row(self, client_name="TestClient", id=None, msg="empty", response="empty", requester="empty"):
        """Enqueues a command to the queue

        Args:
            client_name (str, optional): The name of the client (which is used for the table)
            id (_type_, optional): The id of the message. increments by 1 upwards to track the queue
            msg (str, optional): the JSON message going TO the client
            response (str, optional): the JSON response FROM the client. 
            requester (str, optional): Which Fclient requested this action.
        """
        try:
            # Check if the ID already exists in the table
            check_query = f'SELECT id FROM {client_name} WHERE id = ?'
            self.cursor.execute(check_query, (id,))
            existing_row = self.cursor.fetchone()
            if existing_row:
                ## maybe recurse with id + 1 until it gets it right? 
                print(f"ID {id} already exists in the {client_name} table.")
                return

            # If the ID is unique, add to queue
            insert_query = f'INSERT INTO {client_name} (id, msg, response, requester) VALUES (?, ?, ?, ?)'
            values = (id, msg, response, requester)
            self.cursor.execute(insert_query, values)
            self.dbconn.commit()

        except Exception as e:
            logging.debug(f"[DBHandler.enqueue_mclient_row()] Error: {e}")

    def dequeue_mclient_row(self, client_name):
        ''' This is kinda ugly
        Steps:

        gets next queue number from DB.
        With said number, retrieves the MSG from that row
        returns message.
        increments current queue and next queue by 1 in DB
        
        Errors:
            If this tries to access beyond the messages in queued message, it errors out.

        Failrue handling: 
            Returns a sleep string if something fails
        '''
        try:
        ## NExt queue num
            self.cursor.execute(f'select next_queue_number from client_queue_tracker where client_name = "{client_name}"')
            ## [0] is needed, as this returns (1,)
            next_queue_number = self.cursor.fetchone()#[0]

            if next_queue_number == None:
                raise TypeError

            next_queue_number = next_queue_number[0]

        ## Current queue num
            self.cursor.execute(f'select current_queue_number from client_queue_tracker where client_name = "{client_name}"')
            ## [0] is needed, as this returns (2,)
            current_queue_number = self.cursor.fetchone()#[0]

            if current_queue_number == None:
                raise TypeError
        
            current_queue_number = current_queue_number[0]

        ## select next up cmd
            self.cursor.execute(f'select msg from {client_name} where id = "{next_queue_number}"')
            ## [0] is needed, as this returns (MSG,)
            msg = self.cursor.fetchone()#[0]

            if msg == None:
                raise TypeError
            
            msg = msg[0]

            print(f"Current Queue #: {current_queue_number}\nNext Queue Num: {next_queue_number}")
        
        ## update item
            # Update the client_queue_tracker table with the new values
            update_query    = f'UPDATE client_queue_tracker SET current_queue_number = ?, next_queue_number = ? WHERE client_name = ?'
            values          = (current_queue_number + 1, next_queue_number + 1, client_name)
            
            self.cursor.execute(update_query, values)
            self.dbconn.commit()

        except TypeError as te:
            logging.debug(f"[DBHandler.update_queue_tracker()] Queue is empty. Sending sleep: {te}")
            return sleep_string
        
        except ValueError as ve:
            #print(e)
            logging.debug(f"[DBHandler.update_queue_tracker()] Value error, the DB may have tried to access a message that didn't exist: {ve}")
            return sleep_string

        except Exception as e:
            #print(e)
            logging.debug(f"[DBHandler.update_queue_tracker()] Error: {e}")
            return sleep_string

        return msg


    def add_response_mclient_row(self, id=None, response="None", client_name="TestClient"):
        try:
            sql_query   = f'UPDATE {client_name} SET response = ? WHERE id = ?'
            values      = (response, id,)
            
            self.cursor.execute(sql_query, values)
            self.dbconn.commit()

        except Exception as e:
            #print(e)
            logging.debug(f"[DBHandler.add_response_mclient_row()] Error: {e}")



'''
s = SQLDBHandler(db_name="DevDB.db")
s.connect_to_db("DevDB.db")

s.create_mclient_table(client_name="testclient1")
s.create_mclient_queuetrack_table()

#addint client to queue track
s.create_mclient_queuetrack_row(client_name="testclient1")

## cmd being added... (really only done on the Fclient side)
s.enqueue_mclient_row(client_name="testclient1", id=2, msg="MSG")
## response being updated...
s.add_response_mclient_row(client_name="testclient1", id=1, response="BALLS")

#dequeing
print(s.dequeue_mclient_row(client_name="testclient1"))'''

'''
## shuold work as long as it's called correctly lol. worst case scenario the sleep command is retunred

Other notes, when queue fails out (or tries to reach a higher number than there are rows) it stays on that number. So
theoretically, the next item added to the queue will get sent to the client.

Otherwise it returns a sleep message on all errors

'''
