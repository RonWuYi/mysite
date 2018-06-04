from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def root(request):
    return HttpResponse("This is root page")
