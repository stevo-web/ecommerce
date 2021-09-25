from django.shortcuts import redirect, render
from main.models import Product, SubCategory, Category
from .models import Shop
from main.models import SubCategory
from django.contrib.auth.decorators import login_required
from main.models import Order
from Kenya.counties import counties
from .forms import AddProductForm
from cart.cart import Cart
import time


location = [f'{county["name"]}' for county in counties]


@login_required(login_url='login')
def sell(request):
    context = {}
    context["industry"] = SubCategory.objects.all()
    context["cart"] = Cart(request)
    context["location"] = location

    user = request.user
    if request.POST:
        name = request.POST["name"]
        _location = request.POST["_location"]
        industry = request.POST["industry"]
        link = request.POST["link"]
        mpesa = request.POST["mpesa"]

        shop = Shop.objects.create(owner_id=user.id, name=name, location=_location,  industry=industry, shop_link=link, mpesa_till=mpesa)
        user.has_shop = True
        user.save()
        shop.save()
        time.sleep(2)
        return redirect('shop-dashboard')

    context["location"] = location
    context["industries"] = Category.objects.all()
    return render(request, 'sell.html', context)


def shop_orders(request):
    context = {}
    user = request.user
    shop_id = Shop.objects.get(owner_id=user.id).id
    _shop_orders = Order.objects.filter(order_item__product__shop_id=shop_id)

    context["shop_orders"] = _shop_orders
    return render(request, 'shop/orders.html', context)


@login_required(login_url='login')
def dashboard(request):
    context = {}
    user = request.user
    shop = Shop.objects.get(owner_id=user.id)
    _shop_orders = Order.objects.filter(order_item__product__shop_id=shop.id)
    shop_products = Product.objects.filter(shop_id=shop.id)

    context["products"] = shop_products
    context["orders"] = _shop_orders
    context["shop"] = shop
    context["owner"] = user

    return render(request, 'shop/index.html', context)


def add_product(request):
    context = {}
    categories = SubCategory.objects.all()
    context['categories'] = categories
    shop = Shop.objects.get(owner_id=request.user.id)
    form = AddProductForm()
    context["form"] = form

    if request.POST:
        form = AddProductForm(request.POST, request.FILES)
        if form.is_valid():
            prod = form.save(commit=False)
            prod.shop = shop
            prod.save()

            return redirect('shop-dashboard')

    return render(request, 'shop/add-product.html', context)


def delete_product(request, pk):
    product = Product.objects.get(pk=pk)
    product.delete()

    return redirect('shop-dashboard')


def products(request):
    context = {}
    user = request.user
    shop = Shop.objects.get(owner_id=user.id)
    shop_products = Product.objects.filter(shop_id=shop.id)

    context["products"] = shop_products
    return render(request, 'shop/products.html', context)


def customers(request):

    return render(request, 'customers.html')
