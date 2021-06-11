from wsgiref.util import setup_testing_defaults

from framework.parsers import parse_data
from framework.views import Error404


class Application:
    """
    Main class of framework
    """

    def __init__(self, urls, middleware):
        self.urls = urls
        self.middleware = middleware

    def __call__(self, environ, start_response):
        """
        :param environ:
        :param start_response:
        :return:
        """
        setup_testing_defaults(environ)
        request = {}

        path = environ['PATH_INFO']
        request_method = environ['REQUEST_METHOD']
        print('method:', request_method)

        if request_method == 'GET':
            # parse and output GET params
            params = parse_data(environ['QUERY_STRING'])
            print('GET params:', params)
        elif request_method == 'POST':
            # parse and output POST params
            content_length_data = environ.get('CONTENT_LENGTH')
            content_length = int(content_length_data) if content_length_data else 0
            data = environ['wsgi.input'].read(content_length) if content_length > 0 else b''
            params = parse_data(data.decode('UTF-8'))
            print('POST params:', params)

        # support requests without "/"
        if not path.endswith('/'):
            path += '/'

        # choose view, based on url path
        if path in self.urls:
            view = self.urls[path]
        else:
            view = Error404()

        # add middleware
        for controller in self.middleware:
            controller(request)

        # start view
        code, body = view(request)
        start_response(code, [('Content-Type', 'text/html')])
        return [body.encode('utf-8')]
