from django.shortcuts import redirect, render
from main.models import Product, SubCategory, Category
from django.contrib.auth import get_user_model
from .models import Shop
from main.models import SubCategory
from django.contrib.auth.decorators import login_required
from main.models import Order, OrderItem
from Kenya.counties import counties
from .forms import AddProductForm, OrderForm
from cart.cart import Cart
import time

location = ['{county["name"]}' for county in counties]


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
    shop = Shop.objects.get(owner_id=user.id)
    items, _shop_orders = OrderItem.objects.filter(product__shop_id=shop.id), [item.order for item in OrderItem.objects.filter(product__shop_id=shop.id)]
    shop_products = Product.objects.filter(shop_id=shop.id)
    _customers = list(set([order.customer for order in _shop_orders]))

    context["orders_count"] = len(_shop_orders)
    context["customers_count"] = len(_customers)
    context["products"] = shop_products
    context["orders"] = _shop_orders
    context["customers"] = _customers
    context["shop"] = shop
    context["owner"] = user
    return render(request, 'shop/orders.html', context)


@login_required(login_url='login')
def dashboard(request):
    context = {}
    user = request.user
    shop = Shop.objects.get(owner_id=user.id)
    items, _shop_orders = OrderItem.objects.filter(product__shop_id=shop.id), [item.order for item in OrderItem.objects.filter(product__shop_id=shop.id)]
    shop_products = Product.objects.filter(shop_id=shop.id)
    _customers = list(set([order.customer for order in _shop_orders]))

    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

    data = []

    for month_no, month in enumerate(months, start=1):
        month_order_count = 0
        for order in _shop_orders:
            if order.made_on.month == month_no:
                month_order_count += 1
        data.append(month_order_count)

    context["months"] = months
    context["data"] = data

    context["orders_count"] = len(_shop_orders)
    context["customers_count"] = len(_customers)
    context["products"] = shop_products
    context["customers"] = _customers
    context["orders"] = _shop_orders
    context["shop"] = shop
    context["owner"] = user

    return render(request, 'shop/index.html', context)


def add_product(request):
    context = {}
    categories = SubCategory.objects.all()
    user = request.user
    shop = Shop.objects.get(owner_id=user.id)
    items, _shop_orders = OrderItem.objects.filter(product__shop_id=shop.id), [item.order for item in OrderItem.objects.filter(product__shop_id=shop.id)]
    shop_products = Product.objects.filter(shop_id=shop.id)
    _customers = list(set([order.customer for order in _shop_orders]))

    context["orders_count"] = len(_shop_orders)
    context["customers_count"] = len(_customers)
    context["products"] = shop_products
    context["customers"] = _customers
    context["orders"] = _shop_orders
    context["shop"] = shop
    context["owner"] = user
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
    items, _shop_orders = OrderItem.objects.filter(product__shop_id=shop.id), [item.order for item in OrderItem.objects.filter(product__shop_id=shop.id)]
    shop_products = Product.objects.filter(shop_id=shop.id)
    _customers = list(set([order.customer for order in _shop_orders]))

    context["orders_count"] = len(_shop_orders)
    context["customers_count"] = len(_customers)
    context["products"] = shop_products
    context["customers"] = _customers
    context["orders"] = _shop_orders
    context["shop"] = shop
    context["owner"] = user
    context["products"] = shop_products
    return render(request, 'shop/products.html', context)


def customers(request):
    context = {}
    user = request.user
    shop = Shop.objects.get(owner_id=user.id)
    items, _shop_orders = OrderItem.objects.filter(product__shop_id=shop.id), [item.order for item in OrderItem.objects.filter(product__shop_id=shop.id)]
    shop_products = Product.objects.filter(shop_id=shop.id)
    _customers = list(set([order.customer for order in _shop_orders]))

    context["orders_count"] = len(_shop_orders)
    context["customers_count"] = len(_customers)
    context["customers"] = _customers
    context["products"] = shop_products
    context["orders"] = _shop_orders
    context["shop"] = shop
    context["owner"] = user

    return render(request, 'shop/customers.html', context)


def order_detail(request, pk):
    context = {}
    user = request.user
    shop = Shop.objects.get(owner_id=user.id)
    items, _shop_orders = OrderItem.objects.filter(product__shop_id=shop.id), [item.order for item in OrderItem.objects.filter(product__shop_id=shop.id)]
    shop_products = Product.objects.filter(shop_id=shop.id)
    _customers = list(set([order.customer for order in _shop_orders]))

    order = Order.objects.get(pk=pk)
    order_items = OrderItem.objects.filter(order_id=pk)

    #form
    form = OrderForm()
    if request.POST:
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()

    context["form"] = form
    context["order"] = order
    context["order_items"] = order_items

    context["orders_count"] = len(_shop_orders)
    context["customers_count"] = len(_customers)
    context["customers"] = _customers
    context["products"] = shop_products
    context["orders"] = _shop_orders
    context["shop"] = shop
    context["owner"] = user
    return render(request, 'shop/order-detail.html', context)