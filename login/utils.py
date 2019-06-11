'''
手机号登录注册常用工具
'''

def is_legal_mobile(mobile):
    '''
    验证手机号是否合法
    :param mobile:
    :return:
    '''
    m = str(mobile)
    if len(m) == 11 and m.startswith("1"):
        return True
    else:
        return False