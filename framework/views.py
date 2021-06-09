from framework.templater import render


class Error404:
    def __call__(self, request):
        print(request)
        return '404 Not found', [render('templates/error.html', code='404').encode('utf-8')]
