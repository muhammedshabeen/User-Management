from django.urls import path
from .views import *

urlpatterns = [
    
    # Route for the login page (default route)
    path('',user_login,name='user_login'),
    
    # Route for the registration page
    path('register',register,name='register'),
    
    # Route for the dashboard page
    path('dashboard',dashboard,name='dashboard'),
    
    # Route for logging out
    path('signout',signout,name='signout'),
    
    # Route for the profile page
    path('profile',profile,name='profile'),
]