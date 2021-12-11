from django.db import models
from django.shortcuts import redirect, render
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
# Create your views here.

def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']

        user=auth.authenticate(request,username=username, password=password)

        if user is not None:
            print("auth is not none")
            auth.login(request,user)
            messages.success(request,'You are logged in successfully')
            redirect('https://google.com/')
            print("auth is not none2")
        else:
            print("invalid credentials")
            messages.warning(request,'Invalid Credentials')
            redirect('login')


    return render(request,'accounts/login.html')

def register(request):
    if request.method == 'POST':
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        confirm_password=request.POST['confirm_password']

        if password==confirm_password:
            if User.objects.filter(username=username).exists():
                messages.warning(request,'Username already exists')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.warning(request,'Email already exists') 
                    return redirect('register')
                else:
                    user=User.objects.create_user(
                                        first_name=firstname,
                                        last_name=lastname,
                                        username=username,
                                        email=email,
                                        password=password
                                        )
                    user.save()
                    messages.success(request,'Account created successfully')
                    return redirect('login')
                    
        else:
            messages.warning(request,'Password do not match')
            return redirect('register')        

    return render(request,'accounts/register.html')

def logout_user(request):
    logout(request)
    return redirect('home')

@login_required(login_url='login')
def dashboard(request):
    return render(request,'accounts/dashboard.html')