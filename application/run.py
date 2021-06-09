from wsgiref.simple_server import make_server

from application import middleware, urls
from framework.main import Application

application = Application(urls.routes, middleware.controllers)

with make_server('', 8000, application) as httpd:
    print("Serving on port 8000...")
    httpd.serve_forever()
