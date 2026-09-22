from django.shortcuts import render, redirect

# Create your views here.
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        if User.objects.filter(username=username).exists():
            messages.error(
                request, 'Username Already Exists!'
            )

            return redirect('register')
        User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        messages.success(
            request,
             'Account Succesfully Created!' )
        
        return redirect('login')
    
    return render(
        request, 
        'accounts/register.html'
    )


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(
            request, 
            username=username,
            password=password
        )
        if user is not None:
            login(request, user)
            return redirect('predict')
        else:
            messages.error(
                request,
                'Invalid Credentials'
            )
    return render(
        request, 
        'accounts/login.html'
    )

def user_logout(request):
    logout(request)
    return redirect('/')