from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, logout, login as _login
from .models import User


def register(request):

    return render(request, 'register.html')


def login(request):
    context = {}

    return render(request, 'login.html', context)
