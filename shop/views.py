from django.shortcuts import redirect, render
from .forms import CreateShop
from .models import Shop
from django.http.response import HttpResponse

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
    return HttpResponse('got here good')