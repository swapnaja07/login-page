from django.contrib import admin
from django.urls import path

from .views import home,register,login_user,logout_user,patient_dashboard,doctor_dashboard

urlpatterns = [
    path('', home,name="home"),
    path('register', register,name="register"),
    path("login_user",login_user, name="login_user"),
    path("logout_user",logout_user, name="logout_user"),
    path('patient_dashboard', patient_dashboard, name='patient_dashboard'),
    path('doctor_dashboard', doctor_dashboard, name='doctor_dashboard'),
    
]
