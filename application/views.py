import os
import pathlib

from framework.templater import render


class IndexView:
    def __call__(self, request):
        path = os.path.join(pathlib.Path(__file__).parent.absolute(), 'templates/index.html')
        return '200 OK', [render(path).encode('utf-8')]


class AboutView:
    def __call__(self, request):
        path = os.path.join(pathlib.Path(__file__).parent.absolute(), 'templates/about.html')
        return '200 OK', [render(path).encode('utf-8')]
