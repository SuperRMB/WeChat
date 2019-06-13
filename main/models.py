from django.db import models
from login.models import LoginInfo
# Create your models here.

class UserInfo(models.Model):
    loginInfo = models.ForeignKey(LoginInfo,on_delete=models.CASCADE)
    avatar = models.CharField(max_length=100)
    nickname = models.CharField(max_length=20)
    wechat_id = models.CharField(max_length=20)

    def __str__(self):
        return self.nickname+"<=>"+self.wechat_id
