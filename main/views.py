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


def category(request, cat_id):
    context = {}
    sub_category = SubCategory.objects.get(pk=cat_id)
    products = Product.objects.filter(category_id=cat_id)
    context["products"] = products
    context["category"] = sub_category

    return render(request, 'category.html', context)


def search(request):
    context = {}
    products = []
    found = {}
    if request.POST:
        search_key = request.POST["search"]
        _cat = Product.objects.filter(category__category__name__contains=search_key)
        _sub = Product.objects.filter(category__name__contains=search_key)
        _prod = Product.objects.filter(name__contains=search_key)
        _desc_title = Product.objects.filter(description_title__contains=search_key)
        _desc = Product.objects.filter(description__contains=search_key)
        _tag = Product.objects.filter(tag__tag__contains=search_key)

        for product in _tag:
            if product.id in found:
                pass
            else:
                found[product.id] = True
                products.append(product)

        for product in _desc:
            if product.id in found:
                pass
            else:
                found[product.id] = True
                products.append(product)

        for product in _desc_title:
            if product.id in found:
                pass
            else:
                found[product.id] = True
                products.append(product)

        for product in _prod:
            if product.id in found:
                pass
            else:
                found[product.id] = True
                products.append(product)

        for product in _cat:
            if product.id in found:
                pass
            else:
                found[product.id] = True
                products.append(product)

        for product in _sub:
            if product.id in found:
                pass
            else:
                found[product.id] = True
                products.append(product)


        if not products:
            context["nothing"] = True

        context["search_key"] = search_key
        context["products"] = products
        return render(request, 'search.html', context)
    else:
        return render(request, 'search.html', context)


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
