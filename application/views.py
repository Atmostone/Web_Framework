import os
import pathlib

from framework.templater import render


class TemplatePath:
    def __init__(self):
        self.path = os.path.join(pathlib.Path(__file__).parent.absolute(), 'templates')


class IndexView(TemplatePath):
    def __call__(self, request):
        return '200 OK', render('index.html', folder=self.path)


class AboutView(TemplatePath):
    def __call__(self, request):
        return '200 OK', render('about.html', folder=self.path)
