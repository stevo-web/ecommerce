from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, logout, login as _login
from .models import User


def register(request):
    if request.POST:
        firstname = request.POST["firstname"]
        lastname = request.POST["lastname"]
        email = request.POST["email"]
        phone = request.POST["phone"]
        image = request.FILES["image"]
        password = request.POST["password"]
        password1 = request.POST["password1"]

        if password == password1:
            user = User.objects.create_user(email=email, password=password1, firstname=firstname, lastname=lastname, phone=phone, image=image)
            user.save()
            return redirect('login')
        else:
            return ''

    return render(request, 'register.html')


def login(request):
    context = {}

    return render(request, 'login.html', context)
