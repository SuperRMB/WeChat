from django.db import models

# Create your models here.
class LoginInfo(models.Model):
    mobile = models.CharField(max_length=11,primary_key=True)
    pwd = models.CharField(max_length=16)

    def __str__(self):
        return "手机号："+self.mobile