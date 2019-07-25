from django.http import HttpResponse

def root_index(request):
    return HttpResponse("this is root index page")
    
def index(request):
    return HttpResponse("hello")