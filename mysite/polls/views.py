from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .forms import UploadFileForm

from .forms import handle_uploaded_file


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


def upload(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST,
                              request.Files)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'])
            return HttpResponse('success')
    else:
        form = UploadFileForm()
    return render(request, 'polls/upload.html', {'form': form})
