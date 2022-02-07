from django.shortcuts import redirect, render
from django.contrib.auth import logout

from django.contrib.auth.models import User
from django.contrib import messages , auth

# Importing decorator for the applications 
from django.contrib.auth.decorators import login_required

# Create your views here.
def login(request):
    if request.method == 'POST':
        user = request.POST['username']
        paswd = request.POST['password']


        user =auth.authenticate(username=user , password=paswd )
        if user is not None :
            auth.login(request , user)
            messages.success(request , 'You are logged in')
            return redirect('dashboard')
        else:
            messages.warning(request , 'Invalid credential')
            return redirect('login')


    return render(request , 'accounts/login.html' )

def logout_user(request):
    logout(request)
    return redirect('home')

def register(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        
        if password ==confirm_password :
            if User.objects.filter(username = username).exists() :
                messages.warning(request , 'Same user is already there')
                return redirect('register')
            elif User.objects.filter(email=email).exists() :
                messages.warning(request , 'Email already exits')
                return redirect('register')
            else:
                user =User.objects.create_user(first_name = firstname , last_name=lastname , username=username , email=email , password = password )
                user.save()
                messages.success(request ,'account created successfully' )
                return redirect('login')

        else:
            messages.warning(request , 'Password do not match')
            return redirect('register')


        

    return render(request , 'accounts/register.html' )


@login_required(login_url='login')
def dashboard(request):
    return render(request , 'accounts/dashboard.html' )
