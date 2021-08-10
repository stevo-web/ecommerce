from django.shortcuts import render
from django.contrib.auth import authenticate, logout, login as _login


def register(request):
    context = {}

    return render(request, 'register.html', context)


def login(request):
    context = {}

    return render(request, 'login.html', context)
