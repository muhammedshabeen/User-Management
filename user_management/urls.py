from django.urls import path
from .views import *

urlpatterns = [
    
    path('',user_login,name='user_login'),
    path('register',register,name='register'),
    path('dashboard',dashboard,name='dashboard'),
    path('signout',signout,name='signout'),
    path('profile',profile,name='profile'),
]