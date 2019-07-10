from django import forms


class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()


def handle_uploaded_file(upload_file, f):
    with open(upload_file, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
