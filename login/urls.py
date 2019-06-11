from django.urls import path
from . import views

urlpatterns = [
    path('',views.login),
    path('legal/mobile/',views.mobile_legal),
    path('mobile_verification/', views.mobileVerification),
]
