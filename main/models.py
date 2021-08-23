from django.db import models
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


class SearchTags(models.Model):
    tag = models.CharField(max_length=100)

    def __str__(self):
        return self.tag


class Product(models.Model):
    name = models.CharField(max_length=40)
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    category = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    tag = models.ManyToManyField(SearchTags)
    price = models.FloatField()
    discount = models.FloatField(default=0)
    image = models.ImageField(upload_to='product images')
    image2 = models.ImageField(upload_to="product images", blank=True, null=True)
    image3 = models.ImageField(upload_to="product images", blank=True, null=True)
    image4 = models.ImageField(upload_to="product images", blank=True, null=True)
    description_title = models.TextField(blank=True, null=True)
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
