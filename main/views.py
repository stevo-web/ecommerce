import random
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import CheckoutForm

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

    page = request.GET.get('page', 1)
    paginator = Paginator(products, 8)
    try:
        _products = paginator.page(page)
    except PageNotAnInteger:
        _products = paginator.page(1)
    except EmptyPage:
        _products = paginator.page(paginator.num_pages)

    sub_categories = SubCategory.objects.filter(category_id=1)
    latest = Product.objects.all()
    context["latest"] = latest
    context["sub_cats"] = sub_categories
    context["products"] = _products

    return render(request, "index.html", context)


def product_detail(request, prod_id):
    context = {}
    cart = Cart(request)
    context["cart"] = cart

    product = Product.objects.get(pk=prod_id)
    similar_products = Product.objects.filter(category__name=product.category.name)
    context['similar_products'] = similar_products
    context['product'] = product
    return render(request, 'product-page.html', context)


def category(request, cat_id):
    context = {}
    cart = Cart(request)
    context['cart'] = cart
    sub_category = SubCategory.objects.get(pk=cat_id)
    products = Product.objects.filter(category_id=cat_id)
    context["products"] = products
    context["category"] = sub_category

    return render(request, 'category.html', context)


def search(request):
    context = {}
    cart = Cart(request)
    context['cart'] = cart
    products = []
    found = {}
    if request.POST:
        search_key = request.POST["search"]
        _cat = Product.objects.filter(category__category__name__contains=search_key)
        _sub = Product.objects.filter(category__name__contains=search_key)
        _prod = Product.objects.filter(name__contains=search_key)
        _desc_title = Product.objects.filter(description_title__contains=search_key)
        _desc = Product.objects.filter(description__contains=search_key)
        # _tag = Product.objects.filter(tag__tag__contains=search_key)

        # for product in _tag:
        #     if product.id in found:
        #         pass
        #     else:
        #         found[product.id] = True
        #         products.append(product)

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



def cart_list(request):
    context = {}
    cart = Cart(request)
    context["cart"] = cart
    return render(request, 'cart.html', context)



def checkout(request):
    context = {}
    cart = Cart(request)
    context['cart'] = cart

    form = CheckoutForm()
    if request.method == 'POST':
        form = CheckoutForm(request.POST)
        if form.is_valid():
            address = form.cleaned_data['address']
            location = form.cleaned_data['location']
            payment = form.cleaned_data['payment']

            print(f'{ address } , {location} , {payment}')
    context["form"] = form
    return render(request, 'checkout.html', context)


def add_cart(request, prod_id, quantity):
    cart = Cart(request)
    prod = Product.objects.get(pk=prod_id)
    cart.add(prod, prod.price, quantity)
    messages.info(request, f'{prod.name} was added to cart')
    return redirect('home')


def update(request, prod_id, quantity):
    cart = Cart(request)
    prod = Product.objects.get(pk=prod_id)
    cart.update(prod, quantity, prod.price)
    messages.info(request, 'cart was updated')
    return redirect('cart')


def remove(request, prod_id):
    cart = Cart(request)
    prod = Product.objects.get(pk=prod_id)
    cart.remove(prod)
    messages.info(request, f'{prod.name} was removed from cart')
    return redirect('cart')
