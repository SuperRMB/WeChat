from django.test import TestCase
from urllib import request
import json
import random
# Create your tests here.

host_name = "https://api.shunliandongli.com/v2/front/"#正式域名
login_url = "member/login/index"
token=''
gid = ''


def login():
    params = {"username":'15068713363','password':'123456',"type":"username"}
    s = json.dumps(params)
    r = request.urlopen(url=host_name + login_url, data=s.encode(encoding='utf-8'))
    data = r.read()
    source_data = data.decode()
    try:
        info = json.loads(source_data)
        if info.get('code') == 1000:
            data_info = info.get('data')
            print("登录成功：" + data_info.get('nickname'))
            global token
            token = data_info.get('token')
    except:
        return False


def get_gid():
    headers = {'token':token}
    url="https://api.shunliandongli.com/v2/front/promotionfree/home"
    re = request.Request(url=url,headers=headers)
    r = request.urlopen(re)
    d = r.read().decode()
    print(d)
    data = json.loads(d)
    if data.get('code') == 1000:
        datas = data.get('data')
        goods = datas.get('goods')
        for g in goods:
            if g.get('is_join') == '1':
                global gid
                gid = g.get('gid')
                print("gid="+gid)
                break


def get_goods():
    url = 'https://api.shunliandongli.com/v2/front/promotionfree/checkReceiveGoods?gid='+gid
    headers = {'token': token}
    re = request.Request(url=url, headers=headers)
    r = request.urlopen(re)
    d = r.read().decode()
    print(d)


def getOrder():
    '''
    180
    shop_goods = [{'store_id':'2078','goods_items':[{'goods_id':'569618','sku_id':'6097122'}]}]
    sg = json.dumps(shop_goods)
    params = {'address_id':'6241312','paytype':'wechat','gid':'618_84','shop_goods':sg}


    159
    shop_goods = [{'store_id':'1800','goods_items':[{'goods_id':'278293','sku_id':'2705045'}]}]
    sg = json.dumps(shop_goods)
    params = {'address_id':'5619953','paytype':'wechat','gid':'618_80','shop_goods':sg}
    :return:
    '''
    url = 'https://api.shunliandongli.com/v2/front/plusfree/checkoutOrder'
    headers = {'token': token}
    proxy_list = [

        {"http": "61.135.217.7:80"},

        {"http": "111.155.116.245:8123"},

        {"http": "122.114.31.177:808"},

    ]
    proxy = random.choice(proxy_list)
    print(proxy)
    #180
    # shop_goods = [{'store_id':'4794','goods_items':[{'goods_id':'698946','sku_id':'7740997'}]}]
    # sg = json.dumps(shop_goods)
    # params = {'address_id':'2213963','paytype':'wechat','gid':'618_107','shop_goods':sg}

    #159
    shop_goods = [{'store_id': '5101', 'goods_items': [{'goods_id': '672784', 'sku_id': '7415570'}]}]
    sg = json.dumps(shop_goods)
    params = {'address_id': '5619953', 'paytype': 'wechat', 'gid': '618_106', 'shop_goods': sg}

    httpproxy_handler = request.ProxyHandler(proxy)
    opener = request.build_opener(httpproxy_handler)
    re = request.Request(url=url,headers=headers,data=json.dumps(params).encode("utf-8"))
    r = opener.open(re)
    # r = request.urlopen(re)
    data = r.read().decode()
    print(data)



def localLogin():
    url = 'http://127.0.0.1:8000/login/'
    r = request.urlopen(url=url)
    # print(help(r))
    # print(r.getheaders())
    headers = r.getheaders()
    cookie = None
    for h in headers:
        if h[0] == 'Set-Cookie':
            cookie = h
    print(cookie)

    # data = r.read().decode()
    # print(data)


    cs = cookie[1].split(';')[0].split('=')
    print(cs)
    headers = {'X-CSRFToken':cs[1]+';Path=/'}
    print(headers)
    params = {'mobile':'13007562706','pwd':'123456','csrfmiddlewaretoken':cs[1]}
    # httpproxy_handler = request.ProxyHandler({"http": "54.39.24.46:3128"})
    # opener = request.build_opener(httpproxy_handler)
    re = request.Request(url=url,headers= headers,data=json.dumps(params).encode('utf-8'),method='POST')
    # r = opener.open(re)
    # print(request._parse_proxy(httpproxy_handler))
    r = request.urlopen(re)
    data = r.read().decode()
    print(data)



# localLogin()
login()
# get_gid()
# get_goods()
getOrder()