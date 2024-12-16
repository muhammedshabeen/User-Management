# forms.py
from django import forms
from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

# Form to handle user registration
class RegistrationForm(UserCreationForm):
    class Meta:
        # Use the custom user model
        model = CustomUser
        # Fields to be displayed in the registration form
        fields = ['username', 'password1', 'password2', 'email', 'address', 'phone_number','name']

    def __init__(self, *args, **kwargs):
        # Initialize the form and apply custom styling to fields
        super(RegistrationForm, self).__init__(*args, **kwargs)
        for name in self.fields.keys():
            self.fields[name].widget.attrs.update({'class':'form-control'})
            
    def clean_phone_number(self):
        # Validate the phone number field
        phone_number = self.cleaned_data.get('phone_number')
        if not phone_number.isdigit() or len(phone_number) != 10:
            raise ValidationError("Enter a valid 10-digit phone number.")
        return phone_number

    def clean_email(self):
        # Validate the email field
        email = self.cleaned_data.get('email')
        if not email or "@" not in email:
            raise ValidationError("Enter a valid email address.")
        return email
    
    def clean(self):
        # Custom validation for the entire form
        cleaned_data = super().clean()
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords do not match.")
        return cleaned_data
    

# Form to handle user profile editing
class ProfileEditForm(forms.ModelForm):
    class Meta:
        # Use the custom user model
        model = CustomUser
        # Fields to be displayed in the profile edit form
        fields = ['username', 'email', 'address', 'phone_number','name']
    
    def __init__(self, *args, **kwargs):
        # Initialize the form and apply custom styling to fields
        super(ProfileEditForm, self).__init__(*args, **kwargs)
        for name in self.fields.keys():
            self.fields[name].widget.attrs.update({'class':'form-control'})
            
    def clean_phone_number(self):
        # Validate the phone number field
        phone_number = self.cleaned_data.get('phone_number')
        if not phone_number.isdigit() or len(phone_number) != 10:
            raise ValidationError("Enter a valid 10-digit phone number.")
        return phone_number
    
    def clean_email(self):
        # Validate the email field
        email = self.cleaned_data.get('email')
        if not email or "@" not in email:
            raise ValidationError("Enter a valid email address.")
        return email
