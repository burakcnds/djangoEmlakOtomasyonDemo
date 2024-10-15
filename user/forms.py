# forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import *

class LoginForm(AuthenticationForm):
    class Meta:
        model = CustomUser  
        fields = ['username', 'password']

class SignUpForm(UserCreationForm):
    class Meta:
        model = CustomUser  
        fields = ['username', 'email', 'password1', 'password2']

