from wsgiref.util import setup_testing_defaults

from framework.views import not_found_404_view


class Application:
    def __init__(self, urls, middleware):
        self.urls = urls
        self.middleware = middleware

    def __call__(self, environ, start_response):
        setup_testing_defaults(environ)
        print('work')
        path = environ['PATH_INFO']

        if not path.endswith('/'):
            path += '/'

        if path in self.urls:
            view = self.urls[path]
        else:
            view = not_found_404_view
        request = {}
        for controller in self.middleware:
            controller(request)
        code, body = view(request)
        start_response(code, [('Content-Type', 'text/html')])
        return body
