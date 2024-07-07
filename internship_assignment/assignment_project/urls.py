from django.contrib import admin
from django.urls import path
from .views import *
urlpatterns = [
    path('login/',login,name="login") ,
    path('signup/',signup,name="signup") ,
    path('change_pass/',change_pass,name="change_pass") ,
    path('dashboard/',dashboard,name="dashboard") ,
    path('profile/',profile,name="profile") ,
    path('forgot_pass/',forgot_pass,name="forgot_pass") ,
    path('new_pass/<token>',new_pass,name="new_pass") ,
    path('logout/',logout,name="logout") ,
]