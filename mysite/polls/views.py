import os

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from .forms import DocumentForm, UploadFileForm
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
    if request.method == 'POST' and request.FILES['myfile']:

        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        upload_file_url = fs.url(filename)
        form = UploadFileForm(request.POST,
                              request.Files)
        return render(request, 'polls/upload.html', {
            'uploaded_file_url': upload_file_url
        })
    #     if form.is_valid():
    #         for i in request.Files:
    #             handle_uploaded_file(os.path.join('C:\\Work\\test project\\github\\mysite\\up', i.filename), i)
    #         return HttpResponse('success')
    # else:
    #     form = UploadFileForm()
    return render(request, 'polls/upload.html')

def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = DocumentForm()
    return render(request, 'polls/upload1.html', {
        'form': form
    })

