from framework.templater import render


class Error404:
    def __call__(self, request):
        return '404 Not found', render('error.html', code='404')
