from py2neo import neo4j
from py2neo import Graph
from py2neo import Node, Relationship
db_graph = Graph()
alice = Node("Person", name="Alice")
bob = Node("Person", name="Bob")
alice_knows_bob = Relationship(alice, "KNOWS", bob)

Graph().create(alice_knows_bob)