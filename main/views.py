from django.shortcuts import render
from .models import Product
import random


def index(request):
    context = {}
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
    product = Product.objects.get(pk=prod_id)
    similar_products = Product.objects.filter(category__name=product.category.name)
    context['similar_products'] = similar_products
    context['product'] = product
    return render(request, 'product.html', context)
