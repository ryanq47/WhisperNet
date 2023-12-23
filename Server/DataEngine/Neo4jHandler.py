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

    def connect(self):
        if not self.driver:
            try:
                # Establish a connection to the database
                self.driver = GraphDatabase.driver(self.uri, auth=(self.user, self.password))
                print("Neo4j connection established.")
            except Exception as e:
                print(f"Failed to create the driver: {e}")

    def close(self):
        # Close the connection if it's open
        if self.driver:
            self.driver.close()
            print("Neo4j connection closed.")