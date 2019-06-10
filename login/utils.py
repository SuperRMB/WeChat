'''
手机号登录注册常用工具
'''

def is_legal_mobile(mobile):
    '''
    验证手机号是否合法
    :param mobile:
    :return:
    '''

    if len(mobile) == 11 and mobile.startswith("1"):
        return True
    else:
        return False