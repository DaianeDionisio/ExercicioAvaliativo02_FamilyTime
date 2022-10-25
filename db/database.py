from neo4j import GraphDatabase
import re

class Graph:
    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self.driver.close()

    def execute_query(self, query, parameters=None):
        with self.driver.session() as session:
            results = session.run(query, parameters)
            for record in results:
                stringRecord = repr(record)
                stringRecord = re.sub("<.*=","", stringRecord)
                stringRecord = re.sub(">.*", "", stringRecord)
                print (stringRecord)