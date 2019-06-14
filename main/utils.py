from django import forms
import os

class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()



def handle_uploaded_file(uploadFile,name):
    path = os.path.join('upload',name)
    f = open(path, 'wb')
    for chunk in uploadFile.chunks():
        f.write(chunk)
    f.close()