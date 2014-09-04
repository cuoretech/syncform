from pyramid.view import view_config
from py2neo import neo4j, ogm
from database_config import db_config
from syncform.Model.User import *
from syncform.lib.session import *
from mako.template import Template
from pyramid.response import Response

graph_db = neo4j.GraphDatabaseService(db_config['uri'])
store = ogm.Store(graph_db)

@view_config(route_name='home', renderer='syncform:templates/index.mako')
def make_view(request):
    template = Template(filename='syncform:templates/index.mako')
    result = template.render(name=request.params['name'])
    response = Response(result)
    return response

# from pyramid.view import view_config
# @view_config(route_name='home', renderer='templates/mytemplate.pt')
# def my_view(request):
#     return {'project': 'SyncForm'}