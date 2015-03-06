from py2neo import neo4j
from py2neo import Graph
from py2neo.ext.ogm import Store

@resource(path='/user')
class User(object):

    def __init__(self, fname=None, mname=None, lname=None, email=None, phone=None, dob=None, street=None, city=None, state=None):
        self.fname = fname
        self.mname = mname
        self.lname = lname
        self.email = email
        self.phone = phone
        self.dob = dob
        self.street = street
        self.city = city
        self.state = state


    def __str__(self):
        return self.fname, self.mname, self.lname, self.email, self.phone, self.dob, self.street, self.city, self.state

graph = Graph()
store = Store(graph)

leo = User("Leo", "Rue", "Schultz", "schultz.leo@gmail.com", "7169690945", "02-12-1992", "659 Robles Ave", "Menlo Park", "California")
store.save_unique("Users", "email", leo.email, leo)
thomas = User("Thomas", "Michael", "Hessler", "hesler.thomas93@gmail.com", "4083167651", "07-27-1993", "19 Arlington Place", "Buffalo", "New York")
store.save_unique("Users", "email", thomas.email, thomas)
kevina = User("Kevin", "Pycharmer", "Aloysius", "kevinaloysius25@gmail.com", "4086502065", "11-08-1992", "500 El Camino Real", "Santa Clara", "California")
store.save_unique("Users", "email", kevina.email, kevina)
kevinr = User("Kevin", "Cody", "Ryan", "kevincryan23@gmail.com", "7162009063", "09-23-1989", "821 Central Ave", "Eden", "New York")
store.save_unique("Users", "email", kevinr.email, kevinr)
store.relate(leo, "LIKES", thomas)     # these relationships are not saved
store.relate(leo, "LIKES", kevina)  
store.relate(leo, "LIKES", kevinr)  # until `leo` is saved
store.save(leo)
