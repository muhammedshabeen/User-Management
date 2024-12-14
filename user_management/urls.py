from django.urls import path
from .views import *

urlpatterns = [
    
    path('register',register,name='register'),
    path('user-login',user_login,name='user_login'),
    path('dashboard',dashboard,name='dashboard'),
    path('signout',signout,name='signout'),
    path('profile',profile,name='profile'),
]