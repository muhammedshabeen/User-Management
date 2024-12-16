from django.shortcuts import render, redirect
from .forms import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login


# Handles user registration
def register(request):
    # Check if the request method is POST (form submission)
    if request.method == 'POST':
        # Instantiate the registration form with the submitted data
        form = RegistrationForm(request.POST)
        # Validate the form
        if form.is_valid():
            # Save the form data to create a new user
            form.save()
            # Display a success message
            messages.success(request,"Registration successfully")
            # Redirect the user to the login page
            return redirect('user_login')
        else:
            # If the form is invalid, iterate over errors and display them
            for field_name, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field_name}: {error}")
    # Provide an empty form instance for the GET request
    context = {
        "form" : RegistrationForm()
    }
    # Render the registration template with the form
    return render(request,'register.html',context)


# Handles user login
def user_login(request):
    # Check if the request method is POST (form submission)
    if request.method == 'POST':
        
        # Retrieve the username and password from the submitted form
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # Authenticate the user using Django's authentication system
        user = authenticate(request,username=username,password=password)
        
        if user is not None:
            # If authentication is successful, log the user in
            login(request, user)
            # Display a success message
            messages.success(request,"Logined successfully")
            # Redirect the user to the dashboard
            return redirect("dashboard")
        else:
            # Display an error message if authentication fails
            messages.error(request,"Incorrect username or password")
    # Render the login template for GET requests or failed POST attempts
    return render(request,'login.html')


# Displays the dashboard page (only accessible to logged-in users)
@login_required
def dashboard(request):
    # Render the dashboard template
    return render(request,'dashboard.html')


# Allows users to view and update their profile (only accessible to logged-in users)
@login_required
def profile(request):
    # Get the current logged-in user
    user = request.user
    
     # Check if the request method is POST (form submission)
    if request.method == 'POST':
        # Bind the profile edit form with the submitted data and the current user instance
        form = ProfileEditForm(request.POST,instance=user)
        
        # Validate the form
        if form.is_valid():
            # Save the form data to update the user's profile
            form.save()
            # Display a success message
            messages.success(request,"Profile Updated")
            # Redirect the user to the profile page
            return redirect('profile')
        else:
            # If the form is invalid, iterate over errors and display them
            for field_name, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field_name}: {error}")
    # Provide the profile edit form instance for the GET request
    context = {
        "form" : ProfileEditForm(instance=user)
    }
    # Render the profile template with the form
    return render(request,'profile.html',context)


# Logs out the user and clears the session (only accessible to logged-in users)
@login_required
def signout(request):
    # Clear the session data to log the user out
    request.session.flush()
    # Display a success message
    messages.success(request,"Logout successfully")
    # Redirect the user to the login page
    return redirect('user_login')
