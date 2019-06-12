from django.db import models
from login.models import LoginInfo
# Create your models here.

class UserInfo(models.Model):
    models.ForeignKey(LoginInfo,on_delete=models.CASCADE)
