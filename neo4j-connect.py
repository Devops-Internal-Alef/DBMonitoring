import sys

import yaml
# Install neo4j driver
from neo4j.v1 import GraphDatabase

try:
    with open("neo4j-auth.yaml") as yamlfile:
        neo4j_auth = yaml.load(yamlfile)
    driver = GraphDatabase.driver(neo4j_auth['uri'],
                                  auth=(neo4j_auth['user'], neo4j_auth['password']))
    print("Connection to Neo4j is sucessful")
    driver.close()
    sys.exit(0)
except Exception as e:
    print("Connection to Neo4j failed", e)
    sys.exit(2)
