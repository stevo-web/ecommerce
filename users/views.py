from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, logout as _logout, login as _login
from django.contrib import messages
from cart.cart import Cart
from Kenya.counties import counties
from .models import User
from main.models import Order, OrderItem

county_list = [county["name"] for county in counties]


def register(request):
    context = {}
    cart = Cart(request)
    context["counties"] = county_list
    context["cart"] = cart

    if request.POST:
        email = request.POST["email"]
        firstname = request.POST["firstname"]
        lastname = request.POST["lastname"]
        phone = request.POST["phone"]
        _location = request.POST["location"]
        password = request.POST["password"]
        password1 = request.POST["password1"]

        if password != password1:
            messages.error(request, 'password did not match')
        else:
            user = User.objects.create_user(email, password, firstname=firstname, lastname=lastname, phone=phone, location=_location)
            user.save()
            return redirect('login')

    return render(request, 'register.html', context)


def login(request):
    context = {}
    cart = Cart(request)
    context["cart"] = cart
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
            messages.error(request, 'invalid credentials')
    return render(request, 'login.html', context)


def dashboard(request):
    context = {}
    user = request.user
    context["orders"] = Order.objects.filter(customer_id=user.id).order_by('-made_on')
    context["order_items"] = OrderItem.objects.filter(order__customer_id=user.id)
    return render(request, 'customer-dashboard.html', context)


def order_detail(request, pk):
    context = {}
    order = Order.objects.get(pk=pk)
    order_items = OrderItem.objects.filter(order_id=order.id)
    context["order"] = order
    context["order_items"] = order_items
    return render(request, 'cus-order-detail.html', context)


def logout(request):
    _logout(request)
    return redirect('home')
