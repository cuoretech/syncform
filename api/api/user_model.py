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
        #user_array.all = fname, mname, lname, email, phone, dob, street, city, state

graph = Graph()
store = Store(graph)
# leo = User()
# leo.fname = "Leo"
# leo.mname = "Rue"
# leo.lname = "Schultz"
# leo.email = "schultz.leo@gmail.com"
# leo.phone = "7169690945"
# leo.dob = "02-12-1992"
# leo.street = "659 Robles Ave"
# leo.city = "Menlo Park"
# leo.state = "California"
leo = User("Leo", "Rue", "Schultz", "schultz.leo@gmail.com", "7169690945", "02-12-1992", "659 Robles Ave", "Menlo Park", "California")
store.save_unique("Users", "email", leo.email, leo)
thomas = User("Thomas", "Michael", "Hessler", "hessler.thomas93@gmail.com", "4083167651", "07-27-1993", "19 Arlington Place", "Buffalo", "New York")
store.save_unique("Users", "email", thomas.email, thomas)
kevina = User("Kevin", "Pycharmer", "Aloysius", "kevinaloysius25@gmail.com", "4086502065", "11-08-1992", "500 El Camino Real", "Santa Clara", "California")
store.save_unique("Users", "email", kevina.email, kevina)
kevinr = User("Kevin", "Cody", "Ryan", "kevincryan23@gmail.com", "7162009063", "09-23-1989", "821 Central Ave", "Eden", "New York")
store.save_unique("Users", "email", kevinr.email, kevinr)
store.relate(leo, "LIKES", thomas)  # these relationships are not saved
store.relate(leo, "LIKES", kevina)  
store.relate(leo, "LIKES", kevinr)  # until `leo` is saved
store.save(leo)

userlist = []
results = graph.cypher.execute("START n=node(*)RETURN 'fname', n.fname, 'mname', n.mname, 'lname', n.lname, 'email', n.email,'phone', n.phone, 'dob', n.dob, 'street', n.street, 'city', n.city, 'state', n.state;")
for key in range(0, len(results)):
    userlist.append({'fname' : results[key].fname,'mname':results[key].mname,'lname':results[key].lname,'email':results[key].email,'phone':results[key].phone})



single_result = graph.cypher.execute("START n=node(301)RETURN 'fname', n.fname;")
single_result2 = graph.cypher.execute("START n=node(301)RETURN 'mname', n.mname;")
single_result3 = graph.cypher.execute("START n=node(301)RETURN 'lname', n.lname;")
single_result4 = graph.cypher.execute("START n=node(301)RETURN 'email', n.email;")
single_result5 = graph.cypher.execute("START n=node(301)RETURN 'phone', n.phone;")
single_result6 = graph.cypher.execute("START n=node(301)RETURN 'dob', n.dob;")
single_result7 = graph.cypher.execute("START n=node(301)RETURN 'street', n.street;")
single_result8 = graph.cypher.execute("START n=node(301)RETURN 'city', n.city;")
single_result9 = graph.cypher.execute("START n=node(301)RETURN 'state', n.state;")
#print (single_result)

#user_array.all = [{"fname": "leo", "mname": "rue", "lname": "schultz", "gender": "male", "email": "schultz.leo@gmail.com", "phone": "7169690945", "dob": "02-12-1992", "street": "821 panelli place", "city": "santa clara", "state": "california"},{"fname": "kevin", "mname": "pycharmer", "lname": "aloysius", "gender": "male", "email": "kevinaloysius25@gmail.com", "phone": "4086502065", "dob": "11-08-1992", "street": "500 el camino real", "city": "santa clara", "state": "california"},{"fname": "thomas", "mname": "ethan", "lname": "hessler", "gender": "male", "email": "hessler.thomas93@gmail.com", "phone": "4083167651", "dob": "07-21-1993", "street": "821 panelli place", "city": "santa clara", "state": "california"},{"fname": "kevin", "mname": "rhino", "lname": "ryan", "gender": "male", "email": "kevincryan23@gmail.com", "phone": "7162009063", "dob": "09-23-1989", "street": "821 centeral ave", "city": "eden", "state": "new york"}]

#leo.test()
    
