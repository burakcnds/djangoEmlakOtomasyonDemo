from django.shortcuts import render,redirect
from django.contrib.auth import login, authenticate,logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import *
from emlakapp.views import *


# Create your views here.

def index(request):
    if request.user.is_authenticated:
        return render(request,'main.html')
    login_form = LoginForm()  
    register_form = SignUpForm()
    if request.method == 'POST':
        if 'signup' in request.POST:
            register_form = SignUpForm(request.POST)
            if register_form.is_valid():
                user = register_form.save()
                login(request,user)
                return redirect('main')
        elif 'login' in request.POST:
            login_form = LoginForm(request, request.POST)
            if login_form.is_valid():
                user = login_form.get_user()
                login(request,user)
                return redirect('main')
    else:
        pass

    return render(request,'index.html',{ 'login_form': login_form,'register_form': register_form})



def anasayfa(request):
    return render(request,'main.html')


def userLogout(request):
    logout(request)
    return redirect('index')