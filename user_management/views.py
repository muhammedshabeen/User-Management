from django.shortcuts import render, redirect
from .forms import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Registration successfully")
            return redirect('login')
        else:
            for field_name, errors in form.errors.items():
                for error in errors:
                    field_label = form.fields[field_name].label or field_name.replace('_', ' ').capitalize()
                    messages.error(request, f"{field_label}: {error}")
    context = {
        "form" : RegistrationForm()
    }
    return render(request,'register.html',context)



def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username,password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request,"Logined successfully")
            return redirect("dashboard")
        else:
            messages.error(request,"Incorrect username or password")
    return render(request,'login.html')


@login_required
def dashboard(request):
    return render(request,'dashboard.html')

@login_required
def profile(request):
    user = request.user
    if request.method == 'POST':
        form = ProfileEditForm(request.POST,instance=user)
        if form.is_valid():
            form.save()
            messages.success(request,"Profile Updated")
            return redirect('profile')
        else:
            for field_name, errors in form.errors.items():
                for error in errors:
                    field_label = form.fields[field_name].label or field_name.replace('_', ' ').capitalize()
                    messages.error(request, f"{field_label}: {error}")
    context = {
        "form" : ProfileEditForm(instance=user)
    }
    return render(request,'profile.html',context)



@login_required
def signout(request):
    request.session.flush()
    messages.success(request,"Logout successfully")
    return redirect('user_login')


def custom_404(request, exception):
    return render(request, '404.html',status=404)