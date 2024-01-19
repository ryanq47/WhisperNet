from neo4j import GraphDatabase
from dotenv import load_dotenv
import os
from Utils.LoggingBaseClass import BaseLogging
import inspect
from neo4j.exceptions import Neo4jError

## trying to follow pep8 a bit closer on this one 

class Neo4jConnection(BaseLogging):
    def __init__(self):
        BaseLogging.__init__(self)  

        self.__driver = None
        self.__uri = None
        self.__user = None
        self.__password = None

        self.load_env()
        self.connect()
        self.create_constraints()

    def load_env(self):
        '''
        Loads data form the .env file
        '''
        self.logger.debug(f"{inspect.stack()[0][3]}")

        try:
            self.logger.debug(f"Attempting to load .env")

            load_dotenv()  # Load environment variables from .env file
            self.__uri = os.getenv("NEO4J_URI")
            self.__user = os.getenv("NEO4J_USER")
            self.__password = os.getenv("NEO4J_PASSWORD")
        except Exception as e:
            self.logger.error(f"Error loading from .env file: {e}")
            return False
        
    def test(self) -> bool:
        '''
        Tests neo4j conn. Returns True on success
        '''
        self.logger.debug(f"{inspect.stack()[0][3]}")

        try:
            self.connect()
            self.close()
            self.logger.info("Successfully connected to neo4j db")
            return True

        except Exception as e:
            self.logger.error(f"Error connecting to Neo4j DB {e}")
            return False

    def connect(self):
        self.logger.debug(f"{inspect.stack()[0][3]}")
        self.logger.info(f"Attempting to connect to Neo4j @ {self.__uri}")

        if not self.__driver:
            try:
                # Establish a connection to the database
                self.__driver = GraphDatabase.driver(self.__uri, auth=(self.__user, self.__password))
                self.logger.info("Neo4j connection established.")
            except Exception as e:
                self.logger.error(f"Failed to create the driver: {e}")

    def close(self):
        self.logger.debug(f"{inspect.stack()[0][3]}")
        self.logger.info(f"Attempting to close connection to Neo4j @ {self.__uri}")
        # Close the connection if it's open
        if self.__driver:
            self.__driver.close()
            self.logger.info("Neo4j connection closed.")

    ######## Queries
    def custom_query(self, query, parameters=None, db=None):
        self.logger.debug(f"{inspect.stack()[0][3]}")
        self.logger.info(f"Running custom query on Neo4j: {query}")

        session = None
        response = None

        try:
            ## if a db name is given, connect to that db, otherwise use the default one
            session = self.__driver.session(database=db) if db else self.__driver.session() 
            response = list(session.run(query, parameters))
        except Exception as e:
            self.logger.error("Query failed:", e)
        finally:
            if session:
                session.close()
        return response
    
    ## Netowrk Queries
    #-[x]
    def get_network_nodes(self)-> list:
        '''
        A custom query to get all network nodes

        returns: A list of Dicts:
        [{'os': 'Windows 10', 'ip': '10.0.0.1/24'}, {'os': 'Windows 10', 'ip': '10.0.0.3/24'}]
        '''

        query = "MATCH (n: Network) RETURN n"
        try:
            with self.__driver.session() as session:
                results = session.run(query)
                return [dict(record['n']) for record in results]
        except Exception as e:
            self.logger.error("Query failed:", e)
            return []

    #-[x]
    def add_network_node(self, cidr, nickname)->list:
        '''
        Adds a network node to the DB. 

        cidr: Primary key, str of network id address
            ex: 10.0.0.0/24

        Cypher Notes: Using CREATE, instead of MERGE. This creates a new node, and then 
        will fail if the n.nickname already exists as it is constrained/our pirmary key
            
        Query: CREATE (n: Network{cidr:$cidr}) SET n.nickname = $nickname RETURN n

        '''
        query = '''
            CREATE (n: Network{cidr:$cidr}) SET n.nickname = $nickname RETURN n
        '''
        #MERGE (n: Network{cidr:$cidr}) SET n.nickname = $nickname RETURN n


        #query = "MATCH (h: Host) RETURN h" # all hosts
        try:
            with self.__driver.session() as session:
                results = session.run(query, cidr=cidr, nickname=nickname)
                self.logger.info(f"Created Network Node '{nickname}':'{cidr}'")
                return [dict(record['n']) for record in results]
        except Neo4jError as e:
            self.logger.warning(f"Neo4j Error: {e}")
            return

        except Exception as e:
            self.logger.error(f"Query failed: {e}")
            return []
    def remove_network_node(self, nickname)->list:
        '''
        Adds a network node to the DB. 

        cidr: Primary key, str of network id address
            ex: 10.0.0.0/24

        '''
        query = '''
        MATCH (n: Network{nickname:$nickname})
        DETACH DELETE n
        '''
        #query = "MATCH (h: Host) RETURN h" # all hosts
        try:
            with self.__driver.session() as session:
                results = session.run(query, nickname=nickname)
                self.logger.info(f"Removed Network Node '{nickname}'")
                return [dict(record['n']) for record in results]
        except Exception as e:
            self.logger.error("Query failed:", e)
            return []
    def get_network_node_properties(self, nickname):
        '''
        Gets ALL properties of the network node

        nickname: Primary key, str of network id address
            ex: "Dc01-org01"

        '''
        query = '''
        MATCH (n: Network{nickname:$nickname})
        return n
        '''
        #query = "MATCH (h: Host) RETURN h" # all hosts
        try:
            with self.__driver.session() as session:
                results = session.run(query, nickname=nickname)
                self.logger.info(f"Retrieved properties for Network Node '{nickname}'")
                return [dict(record['n']) for record in results]
        except Exception as e:
            self.logger.error("Query failed:", e)
            return []
        
    def add_or_update_network_node_property(self, nickname, property_name, value):
        '''
        Update a property of a client node. 

        Allowed Properties: {"cidr", "nickname", "misc"} - limited for injection & management purposes.

        nickname: nickname of client (str)
        property_name: name of property. See Allowed Properties

        value: Value of the property. Protected by injection via paramaterization
        
        '''
        allowed_properties = {"cidr", "nickname", "misc"}

        if property_name not in allowed_properties:
            self.logger.error(f"Invalid property name: {property_name}")
            return []

        query = f'MERGE (h:Network {{nickname: $nickname}}) SET h.{property_name} = $value RETURN h'

        try:
            with self.__driver.session() as session:
                results = session.run(query, nickname=nickname, value=value)
                self.logger.info(f"Updated '{property_name}' to '{value}' on Network Node {nickname} ")

                return [dict(record['h']) for record in results]
        except Exception as e:
            self.logger.error(f"Query failed: {e}")
            return []

    ## Client Queries
    def get_client_nodes(self) -> list:
        '''
        Get ALL client nodes in the DB.

        returns: A list of Dicts:
        [{'os': 'Windows 10', 'ip': '10.0.0.1/24'}, {'os': 'Windows 10', 'ip': '10.0.0.3/24'}]        
        '''
        query = "MATCH (h: Client) RETURN h" # all clients
        try:
            with self.__driver.session() as session:
                results = session.run(query)
                return [dict(record['h']) for record in results]
        except Exception as e:
            self.logger.error("Query failed:", e)
            return []

    def get_client_node_by_ip(self, ip) -> list:
        '''
        Get Nodes from their IP. Should *theoretically* only return 1 client

        returns: A list of Dicts:
        [{'os': 'Windows 10', 'ip': '10.0.0.1/24'}, {'os': 'Windows 10', 'ip': '10.0.0.3/24'}]
        '''
        query = "MATCH (h: Client) WHERE h.ip = $ip RETURN h"
        #query = "MATCH (h: Host) RETURN h" # all hosts
        try:
            with self.__driver.session() as session:
                results = session.run(query, ip=ip)
                return [dict(record['h']) for record in results]
        except Exception as e:
            self.logger.error("Query failed:", e)
            return []

    #-[x]
    def add_client_node(self, nickname):
        '''
        Adds a client node to the DB. 

        ip: Primary key, str of IP address

        Cypher Notes: Using CREATE, instead of MERGE. This creates a new node, and then 
        will fail if the h.nickname already exists as it is constrained/our pirmary key

        query = 'CREATE (h: Client{nickname:$nickname})  RETURN h'

        '''
        #query = 'MERGE (h: Client{nickname:$nickname})  RETURN h'
        query = 'CREATE (h: Client{nickname:$nickname})  RETURN h'

        #self.logger.critical("test123")

        #query = "MATCH (h: Host) RETURN h" # all hosts
        try:
            with self.__driver.session() as session:
                results = session.run(query, nickname=nickname)
                self.logger.info(f"Created Client Node '{nickname}'")
                return [dict(record['h']) for record in results]
        except Neo4jError as e:
            self.logger.warning(f"Neo4j Error: {e}")
            return

        except Exception as e:
            self.logger.error(f"Query failed: {e}")
            return []

    def remove_client_node(self, nickname):
        '''
        Remove a Client node from the DB. 

        ip: Primary key, str of IP address

        '''
        query = '''
        MATCH (h: Client{nickname:$nickname})  
        DETACH DELETE h
        '''
        try:
            with self.__driver.session() as session:
                results = session.run(query, nickname=nickname)
                self.logger.info(f"Removed Client Node '{nickname}'")
                return [dict(record['h']) for record in results]
        except Exception as e:
            self.logger.error("Query failed:", e)
            return []

    #- [x]
    def get_client_node_properties(self, nickname):
        '''
        Gets ALL properties of the network node

        nickname: Primary key, str of network id address
            ex: "Dc01-org01"

        '''
        query = '''
        MATCH (n: Client{nickname:$nickname})
        return n
        '''
        #query = "MATCH (h: Host) RETURN h" # all hosts
        try:
            with self.__driver.session() as session:
                results = session.run(query, nickname=nickname)
                self.logger.info(f"Retrieved properties for Network Node '{nickname}'")
                return [dict(record['n']) for record in results]
        except Exception as e:
            self.logger.error("Query failed:", e)
            return []

    #-[x]
    def add_or_update_client_node_property(self, nickname, property_name, value):
        '''
        Update a property of a client node. 

        Allowed Properties: {"os", "name", "misc"} - limited for injection & management purposes.

        ip: Ip of client (str)
        property_name: name of property. See Allowed Properties

        value: Value of the property. Protected by injection via paramaterization
        
        '''
        allowed_properties = {"os", "name", "misc", "ip"}

        if property_name not in allowed_properties:
            self.logger.error(f"Invalid property name: {property_name}")
            return []

        query = f'MERGE (h:Client {{nickname: $nickname}}) SET h.{property_name} = $value RETURN h'

        try:
            with self.__driver.session() as session:
                results = session.run(query, nickname=nickname, value=value)
                self.logger.info(f"Updated '{property_name}' to '{value}' on Client Node {nickname} ")

                return [dict(record['h']) for record in results]
        except Exception as e:
            self.logger.error(f"Query failed: {e}")
            return []

    ## Relationship Queries
    #-[x]
    def join_client_to_network(self, cidr, ip):
        ''' ## CHANGE ME TO USE NICKNAME
        Join a client to a network

        cidr: Network cidr of the network to join

        ip: ip of the client

        Using merge statements, so it theoretically shuold not matter if these nodes exist or not
        '''

        
        #query = '''
        #MERGE (h:Host{ip:"192.168.1.1"})
        #MERGE (n:Network{ip:"192.168.69.40/24"})
        #MERGE (n)<-[r:PART_OF]-(h)
        #return h,n,r
        #'''

        query = '''
        MERGE (h:Client{ip:$ip})
        MERGE (n:Network{cidr:$cidr})
        MERGE (n)<-[r:PART_OF]-(h)
        return h,n,r
        '''

        try:
            with self.__driver.session() as session:
                results = session.run(query, ip=ip, cidr=cidr)
                ## NEed to think about if we need a return on this, or a true/false
                return [dict(record['h']) for record in results]
        except Exception as e:
            self.logger.error(f"Query failed: {e}")
            return []


    def print_response(self, response = None):
        for record in response:
            node = record["h"]
            print("Node ID:", node.id)
            print("Labels:", list(node.labels))  # Convert labels to a list for easy viewing
            print("Properties:", dict(node))  # Convert node properties to a dictionary
            print()  # Just for a newline for better readability

    def create_constraints(self):
        '''
        Creates constraints for the Network and Client nodes, if they do not already exist.
        '''
        # Query to fetch all constraints
        fetch_constraints_query = "SHOW CONSTRAINTS"

        # Queries to create constraints
        create_network_constraint_query = "CREATE CONSTRAINT FOR (n:Network) REQUIRE n.nickname IS UNIQUE"
        create_client_constraint_query = "CREATE CONSTRAINT FOR (c:Client) REQUIRE c.nickname IS UNIQUE"

        try:
            with self.__driver.session() as session:
                # Fetch all existing constraints
                existing_constraints = session.run(fetch_constraints_query).data()

                # Check and create Network constraint
                if not any('Network' in constraint['labelsOrTypes'] and 'nickname' in constraint['properties'] for constraint in existing_constraints):
                    session.run(create_network_constraint_query)
                    self.logger.info("Created Network constraint")

                # Check and create Client constraint
                if not any('Client' in constraint['labelsOrTypes'] and 'nickname' in constraint['properties'] for constraint in existing_constraints):
                    session.run(create_client_constraint_query)
                    self.logger.info("Created Client constraint")

            self.logger.info("Constraint creation process completed")
            return True

        except Exception as e:
            self.logger.error(f"Query failed: {e}")
            return False




class Neo4jParse(BaseLogging):
    def __init__(self):
        BaseLogging.__init__(self)  

    '''
    Custom parser for neo4j data. Each functino takes a "node", which is just what the DB returns

    Might not be needed
    '''

    @staticmethod
    def get_properties(node):
        '''
        Gets properties of a node
        '''
        print(node)
        properties = dict(node)

        print(properties)

        return properties
    
    @staticmethod
    def get_labels(node):
        '''
        Gets labels of a node
        '''
        return list(node.labels)
    
    @staticmethod
    def get_cidr_from_network_node(node):
        '''
        Gets CIDR from network node
        '''
        properties = Neo4jParse.get_properties(node)
        return properties.get('cidr')
    
    @staticmethod
    def get_ip_from_host_node(node):
        '''
        Gets CIDR from network node
        '''
        properties = Neo4jParse.get_properties(node)
        print(properties)
        return properties.get('ip')
