from django.contrib import admin

from . models import Shop, Category, SubCategory, Product, OrderItem, Order

admin.site.site_header = "Elsoko Admin"
admin.site.site_title = "Elsoko Admin Portal"
admin.site.index_title = "Welcome to Elsoko Admin Portal"

admin.site.register(Shop)
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Product)
admin.site.register(OrderItem)
admin.site.register(Order)

