from django.http import HttpResponse


def index(request):
    if request.method == 'GET':
        return HttpResponse("this is GET request")
    elif request.method == 'PUT':
        return HttpResponse("this is PUT request")
    elif request.method == 'POST':
        return HttpResponse("this is POST request")
    else:
        return HttpResponse("we do not know which request it is")


def root(request):
    return HttpResponse("root page")