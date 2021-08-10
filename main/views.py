import random
import json
from django.shortcuts import render
from django.http.response import HttpResponse
from django.template import context

from cart.cart import Cart
from .models import *


def index(request):
    context = {}
    cart = Cart(request)
    context["cart"] = cart

    products = []
    for product in Product.objects.all():
        products.append(product)
    random.shuffle(products)

    latest = Product.objects.all()
    context["latest"] = latest
    context["products"] = products[:30]

    return render(request, "index.html", context)


def product_detail(request, prod_id):
    context = {}
    cart = Cart(request)
    context["cart"] = cart

    product = Product.objects.get(pk=prod_id)
    similar_products = Product.objects.filter(category__name=product.category.name)
    context['similar_products'] = similar_products
    context['product'] = product
    return render(request, 'product.html', context)


# Cart Views
def cart_list(request):
    context = {}

    return render(request, 'cart.html', context)


def cart_api(request):
    cart = Cart(request)
    context = {
        "count": cart.count(),
        "summary": cart.summary()
    }

    return HttpResponse(f'{context["count"]} {context["summary"]}')


def add_to_cart(request, prod_id, quantity):
    context = {}
    cart = Cart(request)
    product = Product.objects.get(pk=prod_id)
    cart.add(product, product.price, quantity)
    return HttpResponse("successful")
