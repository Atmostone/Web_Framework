class IndexView:
    def __call__(self, request):
        print(request)
        return '200 OK', [b'<h1>Hello world!</h1>']


class AboutView:
    def __call__(self, request):
        print(request)
        return '200 OK', [b'<h2>It is my own framework!</h2>']
