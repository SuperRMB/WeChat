from django.shortcuts import render,HttpResponse

# Create your views here.



def login(request):
    '''
    登录注册页面
    :param request:
    :return:
    '''

    return render(request,'login.html')

def mobileVerification(request):
    '''
    验证手机号
    验证手机号是否合法
    验证手机号是否注册
    :param request:
    :return:
    '''

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        print("用户名："+username +" 密码；"+password)


        return HttpResponse("用户名："+username +" 密码；"+password)


