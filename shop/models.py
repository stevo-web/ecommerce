from django.db import models
from django.contrib.auth import get_user_model


class Shop(models.Model):
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    sale = models.CharField(max_length=10, choices=(
        ('services', 'services'),
        ('products', 'products'),
        ('events', 'events')
    ))
    location = models.CharField(max_length=100)
    mpesa_till = models.CharField(max_length=20)

    def __str__(self):
        return self.name