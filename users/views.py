from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, logout as _logout, login as _login
from .models import User


def register(request):

    return render(request, 'register.html')


def login(request):
    context = {}
    user = request.user
    if user.is_authenticated:
        return redirect('home')
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]

        user = authenticate(
            email=email,
            password=password
        )
        if user is not None:
            _login(request, user)
            return redirect('home')
        else:
            context["err"] = 'invalid username or password'
    return render(request, 'login.html', context)


def logout(request):
    _logout(request)
    return redirect('home')
