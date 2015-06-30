from py2neo import neo4j
from py2neo import Graph
from py2neo import Node
from py2neo.ext.ogm import Store
import json

class User():

    def __init__(self, fname=None, mname=None, lname=None, email=None, phone=None, dob=None, street=None, city=None, state=None, string=None):
        self.fname = fname
        self.mname = mname
        self.lname = lname
        self.email = email
        self.phone = phone
        self.dob = dob
        self.street = street
        self.city = city
        self.state = state
        graph = Graph()
        store = Store(graph)

    def saveUser(self):
        store.save_unique("Users", "email", self.email, self)
    def saveRel (self):
        store.save(self)
    def updateName(self):
        graph = Graph()
        graph.cypher.execute("MATCH (n { lname: 'Doug' }) SET n.fname = {self} RETURN n")
    def deleteUser(self):
        graph.cypher.execute("MATCH (n { fname: 'self' }) DELETE n")

graph = Graph()
store = Store(graph)
userlist = []
for record in graph.cypher.execute("START n=node(*) RETURN [n.fname, n.mname, n.lname, n.email, n.phone, n.dob, n.street, n.city, n.state]"):
    userlist.append(record[0])
# print (userlist)

single_user = []
for record in graph.cypher.execute("START n=node(347) RETURN [n.fname, n.mname, n.lname, n.email, n.phone, n.dob, n.street, n.city, n.state]"):
    single_user.append(record[0])

single_user_param = []
for record in graph.cypher.execute("START n=node(355) RETURN [n.fname, n.mname, n.lname]"):
    single_user_param.append(record[0])

# print (single_user)


