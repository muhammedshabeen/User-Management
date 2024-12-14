# forms.py
from django import forms
from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

class RegistrationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'password1', 'password2', 'email', 'address', 'phone_number','name']

    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        for name in self.fields.keys():
            self.fields[name].widget.attrs.update({'class':'form-control'})
            
    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        if not phone_number.isdigit() or len(phone_number) != 10:
            raise ValidationError("Enter a valid 10-digit phone number.")
        return phone_number

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email or "@" not in email:
            raise ValidationError("Enter a valid email address.")
        return email
    
    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')
        username = cleaned_data.get('username')
        address = cleaned_data.get('address')
        name = cleaned_data.get('name')

        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords do not match.")
        if not username:
            raise ValidationError("Username is required")
        if not address:
            raise ValidationError("Address is required")
        if not name:
            raise ValidationError("Name is required")

        return cleaned_data
    
    
class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'address', 'phone_number','name']
    
    def __init__(self, *args, **kwargs):
        super(ProfileEditForm, self).__init__(*args, **kwargs)
        for name in self.fields.keys():
            self.fields[name].widget.attrs.update({'class':'form-control'})
            
    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        if not phone_number.isdigit() or len(phone_number) != 10:
            raise ValidationError("Enter a valid 10-digit phone number.")
        return phone_number
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email or "@" not in email:
            raise ValidationError("Enter a valid email address.")
        return email
    
    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        address = cleaned_data.get('address')
        name = cleaned_data.get('name')
        if not username:
            raise ValidationError("Username is required")
        if not address:
            raise ValidationError("Address is required")
        if not name:
            raise ValidationError("Name is required")

        return cleaned_data
