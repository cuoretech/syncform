import os
import binascii
import json
from webob import Response, exc
from cornice import Service
from pprint import pprint
from py2neo import neo4j

index = Service(name='index', path='/', description="simplest app")
auth = Service(name='auth', path='/auth', description="app for auth")
user = Service(name='user', path='/user', description="user")
person = Service(name='person', path='/person', description="person")
organization = Service(name='organization', path='/organization', description="organization")
_USERS = {}

@index.get()
def get_info(request):
    return {'hello': 'world'}

@user.get()
def get_info(request):
    data = {"users":[{"fname": "leo", "mname": "rue", "lname": "schultz", "gender": "male", "email": "schultz.leo@gmail.com", "phone": "7169690945", "dob": "02-12-1992", "street": "821 panelli place", "city": "santa clara", "state": "california"},{"fname": "kevin", "mname": "pycharmer", "lname": "aloysius", "gender": "male", "email": "kevinaloysius25@gmail.com", "phone": "4086502065", "dob": "11-08-1992", "street": "500 el camino real", "city": "santa clara", "state": "california"},{"fname": "thomas", "mname": "ethan", "lname": "hessler", "gender": "male", "email": "hessler.thomas93@gmail.com", "phone": "4083167651", "dob": "07-21-1993", "street": "821 panelli place", "city": "santa clara", "state": "california"},{"fname": "kevin", "mname": "rhino", "lname": "ryan", "gender": "male", "email": "kevincryan23@gmail.com", "phone": "7162009063", "dob": "09-23-1989", "street": "821 centeral ave", "city": "eden", "state": "new york"}]}
    return data

@person.get()
def get_info(request):
    data = {"persons":[{"fname": "leo", "mname": "rue", "lname": "schultz", "gender": "male", "email": "schultz.leo@gmail.com", "phone": "7169690945", "dob": "02-12-1992", "street": "821 panelli place", "city": "santa clara", "state": "california"},{"fname": "kevin", "mname": "pycharmer", "lname": "aloysius", "gender": "male", "email": "kevinaloysius25@gmail.com", "phone": "4086502065", "dob": "11-08-1992", "street": "500 el camino real", "city": "santa clara", "state": "california"},{"fname": "thomas", "mname": "ethan", "lname": "hessler", "gender": "male", "email": "hessler.thomas93@gmail.com", "phone": "4083167651", "dob": "07-21-1993", "street": "821 panelli place", "city": "santa clara", "state": "california"},{"fname": "kevin", "mname": "rhino", "lname": "ryan", "gender": "male", "email": "kevincryan23@gmail.com", "phone": "7162009063", "dob": "09-23-1989", "street": "821 centeral ave", "city": "eden", "state": "new york"}]}
    return data

@organization.get()
def get_info(request):
    data = {"organizations":[{"fname": "leo", "mname": "rue", "lname": "schultz", "gender": "male", "email": "schultz.leo@gmail.com", "phone": "7169690945", "dob": "02-12-1992", "street": "821 panelli place", "city": "santa clara", "state": "california"},{"fname": "kevin", "mname": "pycharmer", "lname": "aloysius", "gender": "male", "email": "kevinaloysius25@gmail.com", "phone": "4086502065", "dob": "11-08-1992", "street": "500 el camino real", "city": "santa clara", "state": "california"},{"fname": "thomas", "mname": "ethan", "lname": "hessler", "gender": "male", "email": "hessler.thomas93@gmail.com", "phone": "4083167651", "dob": "07-21-1993", "street": "821 panelli place", "city": "santa clara", "state": "california"},{"fname": "kevin", "mname": "rhino", "lname": "ryan", "gender": "male", "email": "kevincryan23@gmail.com", "phone": "7162009063", "dob": "09-23-1989", "street": "821 centeral ave", "city": "eden", "state": "new york"}]}
    return data

    json_data = open("user.json").read()
    data = json.loads(json_data)
    return data

def _create_token():
    return binascii.b2a_hex(os.urandom(20))

class _401(exc.HTTPError):
    def __init__(self, msg='Unauthorized'):
        body = {'status': 401, 'message': msg}
        Response.__init__(self, json.dumps(body))
        self.status = 401
        self.content_type = 'application/json'

def valid_token(request):
    header = 'X-Messaging-Token'
    token = request.headers.get(header)
    if token is None:
        raise _401()

    token = token.split('-')
    if len(token) != 2:
        raise _401()

    user, token = token

    valid = user in _USERS and _USERS[user] == token
    if not valid:
        raise _401()

    request.validated['user'] = user

def unique(request):
    name = request.body
    if name in _USERS:
        request.errors.add('url', 'name', 'This user exists!')
    else:
        user = {'name': name, 'token': _create_token()}
        request.validated['user'] = user

@auth.get(validators=valid_token)
def get_users(request):
    """Returns a list of all users."""
    return {'users': _USERS.keys()}


@auth.post(validators=unique)
def create_user(request):
    """Adds a new user."""
    user = request.validated['user']
    _USERS[user['name']] = user['token']
    return {'token': '%s-%s' % (user['name'], user['token'])}


@auth.delete(validators=valid_token)
def del_user(request):
    """Removes the user."""
    name = request.validated['user']
    del _USERS[name]
    return {'Goodbye': name}
