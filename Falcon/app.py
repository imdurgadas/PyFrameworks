from CustomerResource import CustomerResource
import falcon
from paste import httpserver

wsgi_app = api = falcon.API()
customer = CustomerResource()
api.add_route('/customers', customer)
httpserver.serve(wsgi_app, host='127.0.0.1', port=8080)