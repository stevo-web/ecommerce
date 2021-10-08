from django.db import models
from django.contrib.auth import get_user_model
from shop.models import Shop
from users.models import User


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class SubCategory(models.Model):
    category = models.ForeignKey(Category, blank=True, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=40)
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    category = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    new = models.BooleanField(default=True)
    price = models.FloatField()
    discount = models.FloatField(default=0)
    image = models.ImageField(upload_to='product images')
    description = models.TextField()
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    customer = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    address = models.CharField(max_length=60)
    location = models.CharField(max_length=60)
    payment = models.CharField(max_length=20)
    transport = models.CharField(max_length=20, blank=True, null=True)
    status = models.CharField(max_length=20, choices=(
        ('pending', 'pending'),
        ('in Transit', 'in Transit'),
        ('delivered', 'delivered')
    ))
    paid = models.BooleanField(default=False)
    total = models.FloatField(blank=True, null=True)
    made_on = models.DateTimeField(auto_now_add=True)
    estimated = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f'{self.id}'


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, blank=True, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    unit_price = models.FloatField()

    def __str__(self):
        return f'{self.product.name} order-item'
