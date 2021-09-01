from django.shortcuts import redirect, render
from main.models import Product, SubCategory
from .forms import CreateShop
from .models import Shop


def sell(request):
    context = {}
    form = CreateShop(request.POST)
    if request.method == "POST":
        if form.is_valid():
            name = form.cleaned_data["name"]
            location = form.cleaned_data["location"]
            sale = form.cleaned_data["sale"]
            mpesa_till = form.cleaned_data['mpesa_till']

            user = request.user
            new_shop = Shop.objects.create(name=name, location=location, sale=sale, mpesa_till=mpesa_till, owner=user)
            new_shop.save()
            user.has_shop = True
            return redirect('shop-dashboard')
    context["form"] = form
    return render(request, 'sell.html', context)


def dashboard(request):
    context = {}
    return render(request, 'shop/index.html')


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