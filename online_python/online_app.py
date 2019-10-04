from django.conf import settings
from django.http import HttpResponse
from django.conf.urls import url
from django.views.decorators.http import require_POST
from django.http import JsonResponse

setting = {
    'DEBUG':True,
    'ROOT_URLCONF':__name__
}

settings.configure(**setting)

@require_POST
def api(request):
    code = request.POST.get('code')
    output = run_code(code)

def home(request):
    with open('index.html', 'rb') as f:
        html = f.read()
    return HttpResponse(html)

urlpatterns = [url('^$',home,name='home')]

if __name__ == '__main__':
    import sys
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)