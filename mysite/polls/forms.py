from django import forms
from .models import Document

class UploadFileForm(forms.Form):
    # class Meta:
    title = forms.CharField(max_length=50)
    file = forms.FileField()

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = {'description', 'document', }

def handle_uploaded_file(upload_file, f):
    with open(upload_file, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
