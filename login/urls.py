from django.urls import path
from . import views

app_name = 'login'
urlpatterns = [
    path('',views.login,name='login_page'),
    path('legal/mobile/',views.mobile_legal,name='mobile_legal'),
    path('mobile_verification/', views.mobileVerification,name='verification'),
]
