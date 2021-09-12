from django.db import models
from django.contrib.auth import get_user_model


class Shop(models.Model):
    owner = models.OneToOneField(get_user_model(), on_delete=models.CASCADE, unique=True, related_name="owner")
    name = models.CharField(max_length=50)
    industry = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    mpesa_till = models.CharField(max_length=20)
    shop_link = models.CharField(max_length=20, blank=True, null=True)
    shop_key = models.CharField(max_length=20, blank=True, null=True)
    shop_logo = models.ImageField(upload_to="shop_logos", blank=True)

    def __str__(self):
        return self.name
