from neo4j import GraphDatabase
from dotenv import load_dotenv
import os
from Utils.LoggingBaseClass import BaseLogging
import inspect

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

    def get_host_nodes(self) -> list:
        '''
        Get ALL host nodes

        returns: A list of Dicts:
        [{'os': 'Windows 10', 'ip': '10.0.0.1/24'}, {'os': 'Windows 10', 'ip': '10.0.0.3/24'}]        
        '''
        query = "MATCH (h: Host) RETURN h" # all hosts
        try:
            with self.__driver.session() as session:
                results = session.run(query)
                return [dict(record['h']) for record in results]
        except Exception as e:
            self.logger.error("Query failed:", e)
            return []


    def get_host_node_by_ip(self, ip) -> list:
        '''
        Get Nodes from their IP. Should *theoretically* only return 1 host

        returns: A list of Dicts:
        [{'os': 'Windows 10', 'ip': '10.0.0.1/24'}, {'os': 'Windows 10', 'ip': '10.0.0.3/24'}]
        '''
        query = "MATCH (h: Host) WHERE h.ip = $ip RETURN h"
        #query = "MATCH (h: Host) RETURN h" # all hosts
        try:
            with self.__driver.session() as session:
                results = session.run(query, ip=ip)
                return [dict(record['h']) for record in results]
        except Exception as e:
            self.logger.error("Query failed:", e)
            return []

    def print_response(self, response = None):
        for record in response:
            node = record["h"]
            print("Node ID:", node.id)
            print("Labels:", list(node.labels))  # Convert labels to a list for easy viewing
            print("Properties:", dict(node))  # Convert node properties to a dictionary
            print()  # Just for a newline for better readability

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
