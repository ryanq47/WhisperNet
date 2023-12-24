from neo4j import GraphDatabase
from dotenv import load_dotenv
import os
from Utils.LoggingBaseClass import BaseLogging


class Neo4jConnection(BaseLogging):
    def init(self):
        BaseLogging.__init__(self)  

        load_dotenv()  # Load environment variables from .env file
        self.uri = os.getenv("NEO4J_URI")
        self.user = os.getenv("NEO4J_USER")
        self.password = os.getenv("NEO4J_PASSWORD")
        self.driver = None
        self.connect()

    def test(self) -> bool:
        '''
        Tests neo4j conn. Returns True on success
        '''
        try:
            self.connect()
            self.close()
            self.logger.info("Successfully connected to neo4j db")
            return True

        except Exception as e:
            self.logger.error(f"Error connecting to Neo4j DB {e}")
            return False


    def connect(self):
        if not self.driver:
            try:
                # Establish a connection to the database
                self.driver = GraphDatabase.driver(self.uri, auth=(self.user, self.password))
                self.logger.info("Neo4j connection established.")
            except Exception as e:
                self.logger.error(f"Failed to create the driver: {e}")

    def close(self):
        # Close the connection if it's open
        if self.driver:
            self.driver.close()
            self.logger.info("Neo4j connection closed.")