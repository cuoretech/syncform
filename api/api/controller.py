from api.user_model import *

class UserController():
	def print_user(self):
		print (self)
	def post_user(self):
		User.saveUser(self)
	def update_fname(self):
		User.updateName(self)
	def delete_user(self):
		User.deleteUser(self)

leo = User("Leo", "Rue", "Schultz", "schultz.leo@gmail.com", "7169690945", "02-12-1992", "659 Robles Ave", "Menlo Park", "California")
UserController.print_user(leo)
User.saveUser(leo)
thomas = User("Thomas", "Michael", "Hessler", "hessler.thomas93@gmail.com", "4083167651", "07-27-1993", "19 Arlington Place", "Buffalo", "New York")
User.saveUser(thomas)
kevina = User("Kevin", "Pycharmer", "Aloysius", "kevinaloysius25@gmail.com", "4086502065", "11-08-1992", "500 El Camino Real", "Santa Clara", "California")
User.saveUser(kevina)
kevinr = User("Kevin", "Cody", "Ryan", "kevincryan23@gmail.com", "7162009063", "09-23-1989", "821 Central Ave", "Eden", "New York")
User.saveUser(kevinr)
newuser = User("Doug", "Michael", "Stamper", "dstamper@whitehouse.gov", "2029092495", "08-01-1969", "100 Washington Ave", "Washington", "District of Columbia")
store.relate(leo, "LIKES", thomas)  # these relationships are not saved
store.relate(leo, "LIKES", kevina)  
store.relate(leo, "LIKES", kevinr)  # until `leo` is saved
User.saveRel(leo)
store.relate(thomas, "IS", newuser)
User.saveRel(thomas)




