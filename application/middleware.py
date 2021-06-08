import datetime


def current_time(request):
    request['time'] = datetime.datetime.now()


controllers = [current_time]
