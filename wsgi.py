from pyramid.config import Configurator
from pyramid.response import Response
from pyramid.paster import get_app

def hello(request):
    return Response('Hello!')

config = Configurator()
config.add_route('hello', '/')
config.add_view('home', route_name='hello')

app = config.make_wsgi_app()

# Or from an .ini file:
# app = get_app('api.ini', 'syncform')