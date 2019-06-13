from django import forms

class UploadFileForm(forms.Form):
    file_name = forms.CharField(max_length=50)
    file = forms.FileField()



def handle_uploaded_file(f,name):
    with open('static/img/'+name, 'wb') as destination:
        for chunk in f.chunks():
            destination.write(chunk)