from django.shortcuts import render,HttpResponse,HttpResponseRedirect,reverse
from .models import LoginInfo
from .utils import is_legal_mobile
import json

# Create your views here.


def login(request):
    '''
    登录注册页面
    :param request:
    :return:
    '''
    error = {}
    if request.method == 'GET':
        error['mobile_error'] = ''
        error['pwd_error'] = ''
        return render(request,'login.html')
    elif request.method == 'POST':
        mobile = request.POST.get('mobile')
        pwd = request.POST.get('pwd')
        isLegal = is_legal_mobile(mobile)
        if isLegal:
            info = LoginInfo.objects.filter(mobile=mobile)
            if info:  # 登录
                info = LoginInfo.objects.get(mobile=mobile)
                if info.pwd == pwd:
                    return HttpResponseRedirect(reverse('main:main_page'))
                else:
                    error.clear()
                    error['pwd_error'] = '密码错误'
                    return render(request, 'login.html', context=error)
            else:  # 注册
                info = LoginInfo(mobile=mobile, pwd=pwd)
                info.save()
                return HttpResponseRedirect(reverse('main:main_page'))
        else:
            error.clear()
            error['mobile_error'] = '请输入正确的手机号'
            return render(request, 'login.html', context=error)



def mobile_legal(requst):
    '''
    检验手机号
    :param requst:
    :return:
    '''
    tip = {}
    if requst.method == 'GET':
        mobile = requst.GET.get('mobile')
        isLegal = is_legal_mobile(mobile)
        if isLegal:
            tip['msg'] = ''
        else:
            tip['msg'] = '手机号不合法'
        return HttpResponse(json.dumps(tip))


