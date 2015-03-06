from py2neo import neo4j
from cornice import Service
import _userController
import user_model

user = Service(name='user', path='/user', description="user")
@user.get()
def get_info(request):
    return {'User'}
