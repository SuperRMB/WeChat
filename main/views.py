from django.shortcuts import render
from .utils import UploadFileForm,handle_uploaded_file
# Create your views here.
AK = 'rEu02HvuEBBrpsc4Up3cO4IMHbN31rm5'

'''
http://api.map.baidu.com/geocoder/v2/?callback=renderReverse&location=35.658651,139.745415&output=json&pois=1&latest_admin=1&ak=您的ak //GET请求
http://api.map.baidu.com/place/v2/search?query=ATM机&tag=银行&region=北京&output=json&ak=您的ak //GET请求
'''

def main_page(request):
    if request.method == 'GET':
        return render(request,"main.html")
    elif request.method == 'POST':
        form = UploadFileForm(request.POST,request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'],request.POST['file'])
        return render(request, "main.html")