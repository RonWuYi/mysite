from django.conf import settings
from django.http import HttpResponse
from django.conf.urls import url

setting = {
    'DEBUG':True,
    'ROOT_URLCONF':__name__
}

settings.configure(**setting)

# def home(request):
#     return HttpResponse('Hello world!')

def home(request):
    with open('index.html','rb') as f:
        html = f.read()
    return HttpResponse(html)

urlpatterns = [url('^$',home,name='home')]

if __name__ == '__main__':
    import sys
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)