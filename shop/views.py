from django.shortcuts import redirect, render
from main.models import Product, SubCategory, Category
from .models import Shop
from Kenya.counties import counties

location = [f'{county["name"]}' for county in counties]


def sell(request):
    context = {}
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
        print('saved')
        return redirect('shop-dashboard')

    context["location"] = location
    context["industries"] = Category.objects.all()
    return render(request, 'sell.html', context)


def dashboard(request):
    context = {}
    user = request.user
    shop = Shop.objects.get(owner_id=user.id)
    context["shop"] = shop
    context["owner"] = user

    return render(request, 'shop/index.html', context)


def products(request):
    context = {}
    owner = request.user
    shop = Shop.objects.get(owner_id=owner.id)
    prods = Product.objects.filter(shop_id=shop.id)
    context["prods"] = prods

    return render(request, 'shop/products.html', context)


def add_product(request):
    context = {}
    categories = SubCategory.objects.all()
    context['categories'] = categories

    shop_id = Shop.objects.get(owner_id=request.user.id).id

    if request.POST:
        name = request.POST['name']
        category = request.POST['category']
        price = request.POST['price']
        discount = request.POST['discount']
        desc_title = request.POST['desc-title']
        description = request.POST['description']
        image = request.FILES['image']

        image3 = request.FILES['image3']
        image2 = request.FILES['image2']
        image4 = request.FILES['image4']

        product = Product.objects.create(
            shop_id=shop_id,
            category_id=category,
            name=name,
            price=price,
            image=image,
            discount=discount,
            description=description,
            description_title=desc_title,
            image2=image2,
            image3=image3,
            image4=image4
        )
        product.save()
    return render(request, 'shop/add-product.html', context)


def delete_product(request, pk):
    product = Product.objects.get(pk=pk)
    product.delete()

    return redirect('products')