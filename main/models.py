from django.db import models
from django.db.models import base

from users.models import User


class Shop(models.Model):
    name = models.CharField(max_length=100)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=100)
    contact = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class SubCategory(models.Model):
    category = models.ForeignKey(Category, blank=True, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class SearchTags(models.Model):
    tag = models.CharField(max_length=100)

    def __str__(self):
        return self.tag


class Product(models.Model):
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    category = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    tag = models.ManyToManyField(SearchTags)
    price = models.FloatField()
    discount = models.FloatField(default=0)
    image = models.ImageField(upload_to='product images')
    description = models.TextField()

    def __str__(self):
        return self.name


class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    buyer = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.product.name} order-item'


class Order(models.Model):
    order_item = models.ManyToManyField(OrderItem)
    paid = models.BooleanField(default=False)
    total = models.FloatField()

    def __str__(self):
        return self.order_item.product.name + 'order'
