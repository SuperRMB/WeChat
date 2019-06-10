from django.urls import path
from login.views import mobileVerification,login

urlpatterns = [
    path('',login),
    path('mobile_verification/', mobileVerification),
]
